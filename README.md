# Hearthstone Project

# About this Project

Hearthstone: Heroes of Warcraft is an online card game created by Blizzard, Inc. This dataset provides access to a subset of cards in the game, namely "standard" cards (as of March 21, 2021), which consist only of cards released within the past two years, as well as classic (i.e., original) cards.

- This project will focus on exploring cards that within the standard format of Hearthstone as of February 2021. 

- This project is currently on hold and will remain so until further notice.

# Goals

- Explore the data to gather insights about the characteristics of the game's different class types and their relationships with each other in the current format

# Purpose

- Practice visualizing data using a variety of different plot types


# Data Dictionary

allkws - All keyword names that the card possesses. 

armor - The armor of the card.

artistName (artistname)- Name of the artist who's art is displayed on the card.

attack - The attack of the card.

cardTypeId (cardtypid) - A number corresponding to the type of the card. More info in metadata/types.csv.

cardSetId (cardsetid) - A number corresponding to the set of cards that the card belongs to. More info in metadata/sets.csv.

childIds (childids) - A list of ids of cards that are related to the card in some way.

childid_count - The number of child ids that a card has.

classId (classid) - A number corresponding to the card's class type. More info in metadata/classes.csv.

collectible - Whether a card is collectible. A value of 1 indicates collectible cards; 0 indicates uncollectible cards.

cropImage (cropimage) - A link to a cropped version of image.

durability - The durability of a weapon card.

has_child_ids - Boolean column that represents if the card has child ids (0 == False, 1 == True).

health - The health of the card.

id - The card's unique ID.

image - A link to an image of the entire card.

imageGold (imagegold) - A link to a golden image of the entire card.

flavorText (flavortext) - Supplemental text of the card shown only outside of battle.

id_prime_hero_class - The id number of the card's primary class. 

id_second_hero_class - The name of the card's secondary class. 

is_multiclass - Boolean column that represents if the card has multiple classes (0 == False, 1 == True)

keywordIds (keywordids) - A list of numbers corresponding to any keywords related to the card. More info in metadata/keywords.csv.

manaCost (manacost) - The mana cost of the card.

minionTypeId (miniontypeid) - A number corresponding to the type of minion of the card. More info in metadata/minionTypes.csv.

multiClassIds (multiclassids) - A list of numbers corresponding to the card's class type if the card belongs to more than one class. More info in metadata/classes.csv.

name - The name of the card.

name_card_type - The name of the card's type (weapon, minion, etc)

name_minion_tribe - The name of the card's tribe, if any (murloc, demon, etc.). 

name_prime_hero_class - The name of the card's primary hero class.

name_second_hero_class - The name of the card's secondary hero class.

name_word_count - The number of words in the card's name.

rarityId (rarityid) - A number corresponding to the rarity of the card. More info in metadata/rarities.csv.

slug - The card's ID and name, concatenated with a -.

text - The text presented on the card.

has_taunt, has_spellpower, has_divine_shield, has_charge, has_secret, has_stealth, has_battlecry, has_freeze, has_windfury, has_deathrattle, has_combo, has_overload, has_silence, has_counter, has_immune, has_discover, has_quest, has_poisonous, has_lifesteal, has_rush, has_evilzug, has_twinspell, has_mega_windfury, has_reborn, has_empower, has_outcast, has_spellburst, has_sidequest, has_corrupt, has_start_of_game - Boolean columns that represent if a card has a certain keyword (0 == False, 1 == True)

is_demonhunter, is_druid, is_hunter, is_mage, is_paladin, is_priest, is_rogue, is_shaman, is_warlock, is_warrior, is_neutral - Boolean columns that reflect if a card is of a certain class (0 == False, 1 == True)

is_hero, is_minion, is_spell, is_weapon - Boolean columns that reflect a card's type (0 == False, 1 == True)

is_murloc, is_demon, is_mech, is_elemental, is_beast, is_totem, is_pirate, is_dragon, is_all, is_no_tribe - Boolean columns that reflect if a card is of a certain tribe (0 == False, 1 == True)

filtered_text - Column that holds values from 'text' column, with some changes made via lemmatization, tokenization, and regex.

# Project Plan

- Acquire
    - Download data as csv from Kaggle
    - Import data into Jupyter Notebook via pandas and save as data frame

- Prepare
    - Prepare data as needed for exploration including but not limited to
    - Dropping unneeded columns
    - Converting all string column values to lower case
    - Updating column names
    - Converting column names to all lower case
    - Change columnn name spaces to underscores
    - Update column name terms to make them easier to understand
    - Update data types as needed to facilitate expected operations
    - Handle null values via imputing or dropping
    - Convert dates (if any) to datetime format if appropriate for exepected operations
    - Split categorical column values into boolean columns

- Exploration
    - Explore each classes' cards to identify their unique characteristics
    - Make extensive use of plotting with a wide array of plot types

Conclusion
    - Summarize operations and findings from project

# How to Reproduce

Download data into your working directory.
- CSV data sourcefiles are located within this repostiory

Install acquire.py and prepare.py into your working directory.

Run the jupyter notebook.