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

def subset_graphs(figsize, source, column, title):
    """
    This function makes histograms with the average points scored by all NBA players on a selected season. 
    Args: Size of the graph, the dataframe to create it (the one from which it will take the points column) and a title. 
    Returns: The graph with the selected information. 
    """
    fig, ax = plt.subplots(figsize = (figsize))
    sns.histplot(x = source[column], kde = True)
    ax.set_title(title)
    plt.show()

def combined_graph():
    """
    This function combines all the dataframes to create a line chart comparing the scoring average of the selected players. 
    Args: None
    Returns: The graph with the selected information. 
    """
    plt.figure(figsize=(15,11))

    plt.title('Career average points of players with highest salaries in the NBA (2019-2020)', fontdict={'fontname':'arial', 'fontsize':20})

    plt.plot(df_curry['year'], df_curry['pts'], linestyle = 'solid', marker = '.', color = 'blue')
    plt.plot(df_westbrook['year'], df_westbrook['pts'], linestyle = 'solid', marker = ".", color = 'green')
    plt.plot(df_paul['year'], df_paul['pts'], linestyle = 'solid', marker = ".", color = 'red') 
    plt.plot(df_harden['year'], df_harden['pts'], linestyle = 'solid', marker = ".", color = 'orange')
    plt.plot(df_durant['year'], df_durant['pts'], linestyle = 'solid', marker = ".", color = 'purple')
    plt.plot(df_wall['year'], df_wall['pts'], linestyle = 'solid', marker = ".", color = 'brown') 
    plt.plot(df_james['year'], df_james['pts'], linestyle = 'solid', marker = ".", color = 'pink')
    plt.plot(df_lowry['year'], df_lowry['pts'], linestyle = 'solid', marker = ".", color = 'gray')
    plt.plot(df_griffin['year'], df_griffin['pts'], linestyle = 'solid', marker = ".", color = 'olive')
    plt.plot(df_harris['year'], df_harris['pts'], linestyle = 'solid', marker = ".", color = 'cyan')

    plt.xticks(df_james['year'][::1])

    plt.xlabel('Year', fontdict={'fontname':'arial', 'fontsize':15})
    plt.ylabel('Point average', fontdict={'fontname':'arial', 'fontsize':15})

    plt.legend(['Stephen Curry', 'Russell Westbrook', 'Chris Paul', 'James Harden', 'Kevin Durant', 
                'John Wall', 'LeBron James', 'Kyle Lowry', 'Blake Griffin', 'Tobias Harris'])

    plt.show()

    plt.savefig('mygraph.png', dpi=300) 

    