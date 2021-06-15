

def clean_dataset(dataset):
    """
    This function creates new columns with numerical data and deletes the ones that will not be used in the analysis.
    Args: Name of the dataset
    Returns: The clean dataset
    """
    dic_cut = { "Fair": 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}
    dataset["cut_n"] = dataset["cut"].map(dic_cut)
    
    dic_color = { "D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
    dataset['color_n'] = dataset["color"].map(dic_color)
    
    dic_clarity = { "I3": 1, "I2": 1.33, "I1": 1.66, "SI2": 2, "SI1": 2.5, "VS2": 3,
                   "VS1": 3.5, "VVS2": 4, "VVS1": 4.5, "IF": 5, "F": 6}
    dataset['clarity_n'] = dataset["clarity"].map(dic_clarity)
    
    dataset.drop(['cut', 'color', 'clarity', 'x', 'y', 'z', 'id'], axis = 1, inplace = True)
    
    return dataset

def prepare_prediction(df, model):
    """
    This function cleans the dataframe with the predictions and prepares is to be saved as csv.
    Args: Name of the dataframe.
    Returns: The cleaned dataframe. 
    """
    df.drop(['price'], axis = 1, inplace = True)
    y_predict = model.predict(df)
    df['price'] = y_predict
    df = df.drop(["carat","depth","table","cut_n","color_n","clarity_n"], axis = 1)
    df.reset_index(inplace = True)
    df.rename(columns = {'index': 'id'}, inplace = True)
    return df