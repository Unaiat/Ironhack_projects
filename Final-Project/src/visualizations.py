import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def create_word_cloud(df, name):
    """
    This function creates a word cloud with the info of a dataframe with words as index and a column with their frequency. 
    Args: Dataframe with the info and name to save it as string. 
    Returns: A wordcloud and saves it as a png file. 
    """
    text = " ".join(w for w in df['Word'].astype(str)) # Creates a text string with all the words in the columns. 
    madrid_mask = np.array(Image.open("./images/madrid.png")) # Creates a mask for the wordcloud with the image

    # Create the wordcloud with certain parameters
    wordcloud = WordCloud(background_color="white",height=500, width=500, scale=10, 
                          prefer_horizontal=0.888, mask = madrid_mask).generate(text)

    
    plt.figure(figsize=[20, 15])
    plt.imshow(wordcloud)
    plt.axis("off")

    plt.show()
    wordcloud.to_file(f"./images/{name}.png")
    
def verba_cloud(df, name):  
    """
    This function creates a word cloud with the words from the results of the Verba searches
    Args: Name of the dataframe to take the info from and name to save it as string. 
    Returns: A word cloud and saves it as a png file.
    """
    text = " ".join(w for w in df['Word'].astype(str)) # Creates a text string with all the words in the columns. 
    
    #Create the wordcloud with certain parameters
    wordcloud = WordCloud(background_color="white").generate(text)

    plt.figure(figsize=[15, 15])
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis("off")

    plt.show()
    wordcloud.to_file(f"./images/{name}.png")
    
    