#from simpsons_api import phrases
from config.configuration import engine
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer

def all_names():
    """
    This function makes a query to the characters table in The_simpsons database. 
    Args: None.
    Returns: All the names and ids of the relevant characters. 
    """
    query = f"""
    SELECT * 
    FROM The_simpsons.characters; 
    """
    data = pd.read_sql_query(query,engine)
    return data.to_dict(orient="records")

def get_name(character):
    """
    This function makes a query to the characters table in The_simpsons database. 
    Args: Name of the character.
    Returns: The selected name and the corresponding id. 
    """
    query = f"""
    SELECT * 
    FROM The_simpsons.characters
    WHERE name = "{character}";
    """
    data = pd.read_sql_query(query,engine)
    return data.to_dict(orient="records")

def get__all_phrases():
    """
    This function makes a query to the phrases table in The_simpsons database.
    Args: None.
    Returns: All the phrases in the database. 
    """
    query = f"""
    SELECT phrases.character_id, phrases.phrase, characters.name
    FROM phrases
    JOIN characters 
    ON phrases.character_id = characters.character_id;  
    """
    data = pd.read_sql_query(query,engine)
    return data.to_dict(orient="records")


def get_phrase(name):
    """
    This function makes a query to the phrases table in The_simpsons database.
    Args: Name of the character.
    Returns: The phrases of the character. 
    """
    query = f"""
    SELECT phrases.character_id, phrases.phrase, characters.name
    FROM phrases
    JOIN characters 
    ON phrases.character_id = characters.character_id
    HAVING characters.name = "{name}";
    """
        
    data = pd.read_sql_query(query,engine)
    return data.to_dict(orient="records")

def all_episodes():
    """
    This function makes a query to the phrases table in The_simpsons database. 
    Args: The number of the episode.
    Returns: The available episodes.
    """
    query = f"""
    SELECT episode_id
    FROM The_simpsons.phrases
    GROUP BY episode_id;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_dict(orient="records")

def get_episode(num):
    """
    This function makes a query to the phrases table in The_simpsons database. 
    Args: The number of the episode.
    Returns: The phrases of that episode.
    """
    query = f"""
    SELECT phrases.episode_id, characters.name, phrases.phrase
    FROM phrases
    JOIN characters
    ON phrases.character_id = characters.character_id
    HAVING episode_id = {num};
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_dict(orient="records")

def last_id():
    """
    This function makes a query to the characters table in The:simpsons database. 
    Args: None
    Returns: The last ID, so the user can insert the next one. 
    """
    query = f"""
    SELECT MAX(characters.character_id)
    FROM characters;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_dict(orient="records")

def tokenize (string):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(string)
    return tokens

def sentimentAnalysis(sentence):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(sentence)
    pol = polarity['compound']
    return pol