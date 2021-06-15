import requests 
import pandas as pd
import json
import os
from pandas import json_normalize
from bs4 import BeautifulSoup
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import downloading_saving as dsa
import cleaning as cl
import visualizations as vi

def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle.
    Returns: a folder with the downloaded and unzipped csv.
    '''
    
    #Gets the name of the dataset.zip
    url = input("Introduce la url: ")
    
    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}; say -v Monica 'descargando'"
    decompress = f"tar -xzvf {endopint}.zip; say -v Monica 'descomprimiendo'"
    delete = f"rm -rf {endopint}.zip; say -v Monica 'borrando el zip'"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Move the csv to your data folder
    move_and_delete = f"mv *.csv data/dataset.csv; say -v Monica 'moviendo el dataset'"
    return os.system(move_and_delete)

def balldontlie_request(url):
    """ 
    This function makes requests to the balldontlie API. 
    Arg: Url with the request.
    Returns: The requested information.
    """
    response = requests.get(url).json()
    return response

def lakers_df(response2):
    """"
    This function creates a dataframe iterating through the json file got from the API. 
    Arg: The response of the API. 
    Returns: The dataframe.  
    """
    home_list = [game['home_team']['full_name'] for game in response2]
    home_score = [score['home_team_score'] for score in response2]
    visitor_list = [game['visitor_team']['full_name'] for game in response2]
    visitor_score = [score['visitor_team_score'] for score in response2]
    date_game = [date['date'] for date in response2]
    columns = ['Home team', 'Home team score', 'Visitor team', 'Visitor team score', 'Date']
    lakers_combined = zip(columns, (home_list, home_score, visitor_list, visitor_score, date_game))
    dict_combined = dict(lakers_combined)
    df_lakers = pd.DataFrame(dict_combined)
    return df_lakers

def save_graph(name, path):
    """
    This function saves the graphs.
    Arg: Name of the graph and path to save it.
    Return: None
    """
    name.figure.savefig(path)