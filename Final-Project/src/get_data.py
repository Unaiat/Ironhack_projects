from config.configuration import engine
import pandas as pd 

def get_phrases():
    """
    """
    query = f"""
    SELECT *
    FROM programs;    
    """
    data = pd.read_sql_query(query,engine)
    return data

def verba_phrases():
    """
    """
    query = f"""
    SELECT *
    FROM elections.verba;    
    """
    data = pd.read_sql_query(query,engine)
    return data

def phrases(party):
    """
    """
    query = f"""
    SELECT pa.name, p.phrases  
    FROM programs p
    JOIN parties pa
    ON p.party_id = pa.id
    HAVING pa.name = '{party}';    

    """
    data = pd.read_sql_query(query,engine)
    return data

def verba_candidate(candidate_id):
    """
    """
    query = f"""
    SELECT CONCAT(c.name, " ", c.surname) AS name, v.phrase
    FROM verba v
    JOIN candidates c
    ON c.id = v.candidate_id
    WHERE v.candidate_id = {candidate_id};   
    """
    data = pd.read_sql_query(query,engine)
    return data