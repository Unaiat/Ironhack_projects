import numpy as np


def drop_nan(data):
    """
    This function deletes the rows with NaN values. 
    Arg: Name of the dataframe
    Returns: No return, it deletes the rows automatically. 
    """
    return data.dropna(how = 'any', axis = 0, inplace = True)

def replace(df, column, pattern1, pattern2):
    """
    This function replaces a character from a string in a dataframe
    Args: Name of the dataframe, name of the column, the character to be replaced and the replacement. 
    Returns: The series with the replacement. 
    """
    replacement = df[column] = df[column].str.replace(pattern1, pattern2)
    return replacement

def create_index(df):
    """
    This function creates an index starting from one until the end of the dataframe.
    This is done to have a primary key when inserting the data into SQL.  
    Args: Name of the dataframe
    Returns: The dataframe with the index as a column called ID. 
    """
    df.index = np.arange(1, len(df) + 1)
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index':'id'})
    return df



