import re
import pandas as pd

def selecting_millions(pattern, string):
    """
    This function
    Args: The pattern and the values in the column. 
    Return: A column with the selected values
    """
    try:
        num = re.search(pattern, string)
        return num.group()
    except:
        return("not found")
    
def score(df1, df2, df3, df4, df5, df6, df7, df8):
    """
    This function calculates a score based on the length of each dataframe made with the responses of the API queries.
    Args: Names of the dataframes considered in the calculation. 
    Returns: A score in a range from 0 to 10. 
    """
    
    score_starbucks = 0

    if len(df1) == 0:
        score_starbucks = 0
    elif len(df1) >= 0 and len(df1) < 10:
        score_starbucks = 0.5
    elif len(df1) >= 10 and len(df1) < 20:
        score_starbucks = 1    
    else:
        score_starbucks = 1.25

    score_schools = 0

    if len(df2) == 0:
        score_schools = 0
    elif len(df2) >= 0 and len(df2) < 6:
        score_schools = 0.90
    elif len(df2) > 6 and len(df2) < 12:
        score_schools = 1.80   
    else:
        score_schools = 2.25
             
    score_theater = 0
             
    if len(df3) == 0:
        score_theater = 0
    elif len(df3) >= 0 and len(df3) < 28:
        score_theater = 0.4
    elif len(df3) > 28 and len(df3) < 56:
        score_theater = 0.8   
    else:
        score_theater = 1

    score_basketball = 0

    if len(df4) == 0:
        score_basketball = 0
    else: 
        score_basketball = 0.5

    score_restaurants = 0

    if len(df5) == 0:
        score_restaurants = 0
    elif len(df5) >= 0 and len(df5) < 12:
        score_restaurants = 0.5
    elif len(df5) >= 12 and len(df5) < 24:
        score_restaurants = 1    
    else:
        score_restaurants = 1.25

    score_nightlife = 0

    if len(df6) == 0:
        score_nightlife = 0
    elif len(df6) >= 0 and len(df6) < 24:
        score_nightlife = 0.6
    elif len(df6) >= 24 and len(df6) < 48:
        score_nightlife = 1.2    
    else:
        score_nightlife = 1.5

    score_cinema = 0

    if len(df7) == 0:
        score_cinema = 0
    elif len(df7) >= 0 and len(df7) < 24:
        score_cinema = 0.6
    elif len(df7) >= 24 and len(df7) < 48:
        score_cinema = 1.2    
    else:
        score_cinema = 1.5

    score_gym = 0

    if len(df8) == 0:
        score_gym = 0
    elif len(df8) >= 0 and len(df8) < 20:
        score_gym = 0.5
    elif len(df8) >= 20 and len(df8) < 40:
        score_gym = 1
    else:
        score_gym = 1.25
    
    total_score = score_starbucks + score_schools + score_theater + score_basketball + score_restaurants + score_nightlife + score_cinema + score_gym
    return round(total_score, 2)