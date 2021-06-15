import numpy as np 
import pandas as pd
from collections import Counter
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import spacy
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def create_index(df):
    """
    This function creates an index starting from one until the end of the dataframe.
    This is done to have a primary key when inserting the data into SQL.  
    Args: Name of the dataframe
    Returns: The dataframe with the index as a column called ID. 
    """
    df.index = np.arange(1, len(df) + 1)
    df.reset_index(inplace = True)
    df = df.rename(columns = {'index':'id'})
    return df

def replace(df, column, pattern1, pattern2):
    """
    This function replaces a character from a string in a dataframe
    Args: Name of the dataframe, name of the column, the character to be replaced and the replacement. 
    Returns: The series with the replacement. 
    """
    replacement = df[column] = df[column].str.replace(pattern1, pattern2)
    return replacement

def drop_columns(df):
    """
    This function drops the columns that should not be included in the database
    Args: None (The columns are the same in all the dataframes)
    Returns: The clean dataframe
    """
    df = df.drop(['id', 'link', 'start_time', 'end_time', 'programme_id'], axis = 1)
    return df

def clean_verba(df, party_id, candidate_id, boolean):
    """
    This function prepares the dataframes to be inserted in the database. 
    Args: Name of the dataframe to clean, the party_id as integer, 
    the candidate_id as integer and the boolean to be filtered in the queries as integer". 
    Returns: The cleaned dataframe.
    """
    df = drop_columns(df) # Delete the unnecessary columns
    create_index(df) # Create an index for SQL
    df["date"] = df["programme_date"].apply(lambda x: x.split("T") [0]) #Create a column only with the date
    df.drop(columns = "programme_date", inplace = True) # Delete the programme_date column
    df['party_id'] = party_id # Create a column with the party_id
    df['p0_c1'] = boolean # Create a column with the boolean 0 = party, 1 = candidate
    df['candidate_id'] = candidate_id # Create a column with the candidate id
    column_names = ["index", "p0_c1", "party_id", "candidate_id", "content", "date"] # Variable to order columns
    df = df.reindex(columns = column_names) # Reorder columns
    df = df.rename(columns = {"index": "id", "content": "phrase"}) # Rename columns
    return df

def tokenize (string):
    """
    This function applies the tokenization to a string.
    Args: String to apply the tokenization.
    Returns: Tokenized string.
    """
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(string)
    return tokens

def stop_words(words):
    """
    This function selects the stopword from a text.
    Args: Text to create the stop words.
    returns: A string without the stop words.
    """
    stop_words = set(stopwords.words('spanish'))
    new_list = []
    for string in words:
        if string not in stop_words:
            new_list.append(string)
    return " ".join(new_list)

def translate_into_english(string):
    """
    This function translates a string into English. 
    Args: The string to translate. 
    Returns: The translation into English.
    """
    spanish_string = TextBlob(string)
    try:
        english_blob=spanish_string.translate(from_lang='es',to='en')
        return "".join(list(english_blob))
    except:
        return string

def sentiment_analysis(sentence):
    """
    This function applies the Sentiment Intensity Analyzer to a given sentende. 
    Args: Sentence to analyze. 
    Returns: A column with the compound sentiment analysis. 
    """
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(sentence)
    pol = polarity['compound']
    return pol   

def sentiment_calc(text):
    try:
        return TextBlob(text).sentiment
    except:
        return None

def count_values(df, column):
    """
    This function separates all the words in a selected column from a selected dataframe and makes a value count. 
    Args: Dataframe and column to apply the function
    Returns: A dataframe with the word and its frequency. 
    """
    word_count = df[column].str.split(expand = True).stack().value_counts() # Separate all strings in words
    df_new = pd.DataFrame(word_count) # Create a new dataframe with the separate words
    df_new.reset_index(inplace = True) # Add an index
    df_new.rename(columns = {'index': 'Word', 0: 'Frequency'}, inplace = True) # Rename the columns to Word and Frequency
    df_new['Word'] = df_new['Word'].str.capitalize() # Capitalize all words
    return df_new

def delete_extra_words(df, *args):
    """
    This function deletes the words that should not be included but were not detected as stop words. 
    Args: Dataframe to apply the function and the list of words to delete. 
    Returns: The dataframe without the words. 
    """
    to_delete = args
    for w in to_delete:
        df['Word'] = df['Word'].replace(w, None) # Iterates through words in a given list and turns them into None.
    df.dropna(inplace = True, how = 'any', axis = 0) # Deletes the None values.
    return df  

def for_streamlit(df):
    """
    This function prepares the dataframe to be read by streamlit and create a graph with it. 
    Args: Name of the dataframe. 
    Returns: The dataframe with the Word column as index and the frequency of each word. 
    """
    df = df.groupby(['Word']).sum()
    df = df.sort_values(by = ['Frequency'], ascending = False)
    return df[0:30]

nlp = spacy.load('es_core_news_sm')

def spacy_verb(df, column):
    """
    This function performs the analysys of the texts using the spacy es_core_news_sm library. 
    Args: Dataframe and column.
    Returns: A Dataframe with the verbs with the highest frequency. 
    """
    text = df[column].str.cat(sep=', ') # put the text of all the rows together
    doc = nlp(text)
    search = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    freq = Counter(search)
    most_common = freq.most_common(30)
    df_new = pd.DataFrame(most_common, columns = ['Word', 'Frequency'])
    df_new['Word'] = df_new['Word'].str.capitalize()
    df_new = df_new.set_index('Word')
    return df_new

def spacy_noun(df, column):
    """
    This function performs the analysys of the texts using the spacy es_core_news_sm library. 
    Args: Dataframe and column. 
    Returns: A Dataframe with the nouns with the highest frequency. 
    """
    text = df[column].str.cat(sep=', ') # put the text of all the rows together
    doc = nlp(text)
    search = [token.text for token in doc if token.pos_ == "NOUN"]
    freq = Counter(search)
    most_common = freq.most_common(30)
    df_new = pd.DataFrame(most_common, columns = ['Word', 'Frequency'])
    df_new['Word'] = df_new['Word'].str.capitalize()
    df_new = df_new.set_index('Word')
    return df_new

