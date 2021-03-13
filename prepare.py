# establishing environment
import pandas as pd
import numpy as np

def prep_hearth(cards, classes, mtypes, ctypes, keywords):
    """
    Accepts the 5 hearthstone DFs created by get_hearth function. 
    Returns single, merged, fully prepared DF, ready for exploration. 
    The following is the order the DFs should be listed in as arguments: 
    cards, classes, mtypes, ctypes, keywords
    """
    # lowercasing cards DF columns
    cards.columns = cards.columns.str.lower()

    # lowercasing name and text column values
    cards.text = cards.text.str.lower()
    cards.name = cards.name.str.lower()

    # creating list of all DFs besides cards
    df_list = [classes, mtypes, ctypes, keywords]

    # iterating through DFs
    # lowercasing all column names, dropping original name column, renaming slug to name column
    for dtafrm in df_list:
        dtafrm.columns = dtafrm.columns.str.lower()
        dtafrm.drop(columns = 'name', inplace = True)
        dtafrm.rename(columns = {"slug": "name"}, inplace = True)

    # Merging DFs

    # removing brackets and commas from multiclassids column
    cards.multiclassids = cards.multiclassids.str.replace('\]|,|\[' , '')

    # creating column to hold primary class id 
    # if card is of one class, this will reflect its sole class
    # if card is dual, this will reflect the 1st of the two classes in the multiClassIds column
    # necessary since dual class cards erroneously hold the 'neutral' class value in their primary class id 
    cards['primeclassid'] = np.where((cards.multiclassids.str.contains(' ')), cards["multiclassids"].str.split(" ", expand = True)[0], cards.classid)

    # converting key columns to make all value data types match
    cards.primeclassid = cards.primeclassid.astype(str)
    classes.id = classes.id.astype(str)

    # merging 'classes' df with card df
    df = pd.merge(cards, classes[['id', 'name']], 
                left_on = 'primeclassid', right_on = 'id', how="left", 
                suffixes = (None, '_prime_hero_class'))

    # dropping columns I no longer need
    df.drop(columns = ['primeclassid', 'classid', 'duels'], inplace = True)

    # changing null values of minionTypeId for neutral minions to -1
    df['miniontypeid'] = np.where((df.miniontypeid.isnull() == True) & (df.cardtypeid == 4), -1, df.miniontypeid)

    # adding missing keyword data to 'keywords' df
    # -1 is for minions with no tribe
    mtypes.loc[len(mtypes.index)] = ['no_tribe', -1]

    # merging 'mtypes' df
    df = pd.merge(df, mtypes[['id', 'name']], 
                left_on = 'miniontypeid', right_on = 'id', how="left", 
                suffixes = (None, '_minion_type'))

    # dropping column I no longer need
    df.drop(columns = ['miniontypeid'], inplace = True)

    # dropping column I no longer need
    df.drop(columns = ['rarityid'], inplace = True)

    # dropping column I no longer need
    df.drop(columns = ['cardsetid'], inplace = True)

    # merging 'ctypes' df
    df = pd.merge(df, ctypes[['id', 'name']], 
                left_on = 'cardtypeid', right_on = 'id', how="left", 
                suffixes = (None, '_card_type'))

    # dropping column I no longer need
    df.drop(columns = ['cardtypeid'], inplace = True)

    # replacing dashes with underscores in names
    keywords.name = keywords.name.str.replace('-', '_')

    # adding missing keyword data to 'keywords' df
    keywords.loc[len(keywords.index)] = ['64', 'start_of_game', 
                                        'does something at the start of the game.', 
                                        'does something at the start of the game.']

    # removing brackets and commas from keyword id column
    df.keywordids = df.keywordids.str.replace('\]|,|\[' , '')

    # splitting keyword ids into separate columns for each card
    kwdf = df["keywordids"].str.split(" ", expand = True) 

    # renaming columns
    kwdf.columns = ['keywordid1', 'keywordid2', 'keywordid3', 'keywordid4', 'keywordid5']

    # concatenating split keyword id columns with main df
    df = pd.concat([df, kwdf], axis=1)

    # converting keywords id column to str type to enable merge
    keywords.id = keywords.id.astype(str)

    # creating loop to add a column for the text name of each keyword ability of each card
    # via merging with keywords DF
    for x in kwdf.columns:
        df = pd.merge(df, keywords[['id', 'name']], 
                left_on = x, right_on = 'id', how = "left",
                suffixes = (None, x + '_name'))

    # creating list of columns to drop
    columns_to_drop = ['id', 'slug', 'artistname', 'image', 'imagegold', 'flavortext', 'cropimage', 'collectible']

    # dropping columns
    df.drop(columns = columns_to_drop, inplace = True)

    # filling null text values with 'no effect'
    df["text"].fillna("no effect", inplace = True) 

    # converting nulls, aka non-minion cards to 'not a minion' type
    df['id_minion_tribe'] = np.where((df.id_minion_type.isnull() == True), 'not a minion', df.id_minion_type)
    df['name_minion_tribe'] = np.where((df.name_minion_type.isnull() == True), 'not a minion', df.name_minion_type)

    # dropping minionTypeId since id_minion_type suffices
    df.drop(columns = ['id_minion_type', 'name_minion_type'], inplace = True)

    # filling nulls with "no_childid"
    df.childids.fillna("no_childid", inplace = True) 

    # creating list of column names
    hada = ['health', 'attack']

    # iterating through columns filling nulls within each
    for att in hada:
        df[att].fillna(float('inf'), inplace = True)

    # Creating boolean columns

    # loop iterates through each keyword and creates a boolean column for it
    for kw in keywords.name:
        df['has_' + kw] = np.where(
        (df.namekeywordid1_name == kw) |
        (df.namekeywordid2_name == kw) |
        (df.namekeywordid3_name == kw) |
        (df.namekeywordid4_name == kw) |
        (df.namekeywordid5_name == kw), 1, 0)
        
    # creating column that holds all keyword names for each card
    df['allkws'] = df.namekeywordid1_name + ' ' + df.namekeywordid2_name + ' ' + df.namekeywordid3_name + ' ' + df.namekeywordid4_name + ' ' + df.namekeywordid5_name
    
    # creating empty list
    key_word_col_drop = []

    # iterating through columns in df and creating list of columns to drop
    for col in df.columns:
        if 'keywordid' in col:
            key_word_col_drop.append(col)
            
    # dropping columns
    df.drop(columns = key_word_col_drop, inplace = True)

    # removing brackets and commas from multiclassids column
    df.multiclassids = df.multiclassids.str.replace('\]|,|\[' , '')

    # creating column that holds secondary class separate from primary class
    df['id_second_hero_class'] = df["multiclassids"].str.split(" ", expand = True)[1]

    # converting column to str type to enable merge with newly created column 'id_second_hero_class'
    classes.id = classes.id.astype(str)

    # creating df containing columns for merge in order to rename before merge without altering original classes DF
    classes2 = classes[['id', 'name']]

    # renaming columns
    classes2.columns = ['id_second_hero_class', 'name_second_hero_class']

    # merging 'classes' on secondary hero class id to get secondary class names
    df = pd.merge(df, classes2[['id_second_hero_class', 'name_second_hero_class']], 
                on = 'id_second_hero_class', how = "left")

    # creating boolean columns for each hero class
    for c in classes.name:
        df['is_' + c] = np.where(
        (df.name_prime_hero_class == c) | (df.name_second_hero_class == c), 1, 0)

    # filling nulls in new columns
    df['name_second_hero_class'].fillna('monoclass', inplace = True)
    df['id_second_hero_class'].fillna('monoclass', inplace = True)

    # creating column where 1 = multiclass, 0 = monoclass)
    # contains ' ' will suffice since only cards with a space in this value are multiclass
    df['is_multiclass'] = np.where((df.multiclassids.str.contains(' ')), 1, 0)

    # dropping column I no longer need
    df.drop(columns = 'multiclassids', inplace = True)

    # creating column where 1 = card has childids, 0 = card has no childids)
    # contains ',' will suffice since only cards with a comma in this value have childids
    df['has_child_ids'] = np.where((df.childids.str.contains(',')), 1, 0)

    # dropping column I no longer need
    df.drop(columns = 'childids', inplace = True)

    # iterating through card types and creating a boolean column for each
    for ctype in ctypes.name:
        df['is_' + ctype] = np.where((df.name_card_type == ctype), 1, 0)

    # dropping column I no longer need
    df.drop(columns = 'id_card_type', inplace = True)

    # iterating through minion tribes and creating a boolean column for each
    for mtype in mtypes.name:
        df['is_' + mtype] = np.where((df.name_minion_tribe == mtype), 1, 0)

    # dropping column I no longer need
    df.drop(columns = 'id_minion_tribe', inplace = True)

    # Miscellaneous changes

    # creating list of index values for columns that only have 0 values
    all_0_cols = np.where(df.isin([0]).all() == True)

    # dropping columns based on index value
    df.drop(df.columns[all_0_cols], axis = 1, inplace = True)

    # making identical dfs of all dual class cards
    dcc = df[df.name_second_hero_class != 'monoclass']
    dcc2 = df[df.name_second_hero_class != 'monoclass']

    # swapping primary and secondary hero class values
    dcc2.name_prime_hero_class, dcc2.name_second_hero_class, dcc2.id_prime_hero_class, dcc2.id_second_hero_class = dcc.name_second_hero_class, dcc.name_prime_hero_class, dcc.id_second_hero_class, dcc.id_prime_hero_class

    # adding new rows to main df
    df = pd.concat([df, dcc2])

    # resetting index
    df.reset_index(drop = True, inplace = True)

    # counting words in card names and adding as variable
    df['name_word_count'] = df.name.apply(lambda x: len(str(x).split(' ')))

    # adjusting order of columns
    df = df[['manacost', 'name', 'name_word_count', 'text', 'has_child_ids', 'health', 'attack',
         'id_prime_hero_class', 'name_prime_hero_class', 
        'id_second_hero_class', 'name_second_hero_class', 'allkws', 'name_card_type',
        'name_minion_tribe', 'has_taunt', 'has_spellpower', 'has_divine_shield',
        'has_charge', 'has_secret', 'has_stealth', 'has_battlecry',
        'has_freeze', 'has_windfury', 'has_deathrattle', 'has_combo',
        'has_overload', 'has_silence', 'has_counter', 'has_immune',
        'has_discover', 'has_quest', 'has_poisonous', 'has_lifesteal',
        'has_rush', 'has_evilzug', 'has_twinspell', 'has_mega_windfury',
        'has_reborn', 'has_empower', 'has_outcast', 'has_spellburst',
        'has_sidequest', 'has_corrupt', 'has_start_of_game',
        'is_demonhunter', 'is_druid', 'is_hunter', 'is_mage', 'is_paladin', 'is_priest',
        'is_rogue', 'is_shaman', 'is_warlock', 'is_warrior', 'is_neutral',
        'is_multiclass', 'is_hero', 'is_minion', 'is_spell',
        'is_weapon', 'is_murloc', 'is_demon', 'is_mech', 'is_elemental',
        'is_beast', 'is_totem', 'is_pirate', 'is_dragon', 'is_all',
        'is_no_tribe']]

    return df