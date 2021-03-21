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