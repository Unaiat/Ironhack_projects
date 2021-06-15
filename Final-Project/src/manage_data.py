import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import plotly.express as px
import pandas as pd
import random

parties_count = {
    "PSOE": "./data/programs/csv-s/psoe_phrases_count.csv", 
    "PP": "./data/programs/csv-s/pp_phrases_count.csv", 
    "Ciudadanos": "./data/programs/csv-s/ciudadanos_phrases_count.csv", 
    "Unidas Podemos": "./data/programs/csv-s/unidas_podemos_phrases_count.csv",
    "Más Madrid": "./data/programs/csv-s/mas_madrid_phrases_count.csv",
    "Vox": "./data/programs/csv-s/vox_phrases_count.csv"
}

word_clouds = {
    "PSOE": ["./images/cloud_psoe.png", "./images/cloud_verb_psoe.png", "./images/cloud_noun_psoe.png", "./images/cloud_gabilondo.png"], 
    "PP": ["./images/cloud_pp.png", "./images/cloud_verb_pp.png", "./images/cloud_noun_pp.png", "./images/cloud_ayuso.png"], 
    "Ciudadanos": ["./images/cloud_ciudadanos.png", "./images/cloud_verb_ciudadanos.png", "./images/cloud_noun_ciudadanos.png", "./images/cloud_bal.png"], 
    "Unidas Podemos": ["./images/cloud_unidas_podemos.png", "./images/cloud_verb_unidas_podemos.png", "./images/cloud_noun_unidas_podemos.png", "./images/cloud_iglesias.png"],
    "Más Madrid": ["./images/cloud_mas_madrid.png", "./images/cloud_verb_mas_madrid.png", "./images/cloud_noun_mas_madrid.png", "./images/cloud_garcia.png"],
    "Vox": ["./images/cloud_vox.png", "./images/cloud_verb_vox.png", "./images/cloud_noun_vox.png", "./images/cloud_monasterio.png"]
}

verba = {
    "PSOE": "./data/verba_results/verba_candidates/gabilondo_verba.csv", 
    "PP": "./data/verba_results/verba_candidates/ayuso_verba.csv",  
    "Ciudadanos": "./data/verba_results/verba_candidates/bal_verba.csv",  
    "Unidas Podemos": "./data/verba_results/verba_candidates/iglesias_verba.csv", 
    "Más Madrid": "./data/verba_results/verba_candidates/garcia_verba.csv", 
    "Vox": "./data/verba_results/verba_candidates/monasterio_verba.csv"
}

phrases = {
    "PSOE": "./data/programs/csv-s/psoe.csv", 
    "PP": "./data/programs/csv-s/pp.csv",  
    "Ciudadanos": "./data/programs/csv-s/ciudadanos.csv",  
    "Unidas Podemos": "./data/programs/csv-s/unidas_podemos.csv", 
    "Más Madrid": "./data/programs/csv-s/mas_madrid.csv", 
    "Vox": "./data/programs/csv-s/vox.csv"
}

def party_list():
    data = pd.read_csv("./data/programs/csv-s/parties_table.csv")
    data = data['name']
    return data

def select_party(party):
    df = pd.read_csv(parties_count[party])
    df = df.set_index("Word", drop = True)
    return df    

def select_verba(party):
    df = pd.read_csv(verba[party])
    df = df.set_index("Word", drop = True)
    return df

def select_wordcloud_verba(party):
    last = Image.open(word_clouds[party][3])
    return last

def get_program_part(party, palabra):
    data = pd.read_csv(phrases[party])
    data = data.drop(columns = 'id')
    data = data.dropna(axis = 0, how = 'any')
    data = data[data['phrases'].str.contains(palabra, case = False)]
    return data

