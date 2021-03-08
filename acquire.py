# establishing environment
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

def get_hearth():
    """
    No argument needed. Acquires data and returns as DFs, 5 in total.
    DFs will be returned in the following order:
    cards, classes, mtypes, ctypes, keywords
    """

    # reading in card data and saving as DF
    cards = pd.read_csv('hearthstone_standard_cards.csv')

    # reading in card classes and saving as DF
    classes = pd.read_csv('classes.csv')

    # reading in minion types data and saving as DF
    mtypes = pd.read_csv('minionTypes.csv')

    # reading in types data and saving as DF
    ctypes = pd.read_csv('types.csv')

    # reading in keywords data and saving as DF
    keywords = pd.read_csv('keywords.csv')

    return cards, classes, mtypes, ctypes, keywords

