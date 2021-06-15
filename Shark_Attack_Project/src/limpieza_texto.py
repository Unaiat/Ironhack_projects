
def clean_fatal(x):
    """
    This function cleans the entries in the Fatal (Y/N) column. 
    It replaces the lowercase 'y' with an uppercase 'Y', and 
    Arg: String
    Returns: The string replaced by "Y", "N" or "UNKNOWN"
    """
    if x == "y":
        return "Y"
    elif x == "Y":
        return "Y"
    elif x == " N" or x == "N":
        return "N"
    elif x == "M" or x == "2017":
        return "UNKNOWN"
    else:
        return "UNKNOWN"
    
def drop_nan(data):
    """
    This function deletes the rows where all the values are NaN. 
    Arg: Name of the dataframe
    Returns: No return, it deletes the rows automatically. 
    """
    data.dropna(how = 'all', axis = 0, inplace = True)
    

def searching(pattern, string):
    """
    This function selects the strings that fit a regex pattern.
    Arg: The pattern and the column to look for it
    Return: The word that fits the pattern, or "not found" if there is no match.  
    """
    try:
        return re.search(pattern, string).group().capitalize()
    except:
        return("not found")
    
def get_age(pattern, num):
    """
    This function selects the strings that fit a regex pattern. 
    As in some cases there were more than one, it takes the first case.
    Arg: The pattern and the column to look for it.
    Return: The first element that fits the pattern. 
    """
    try:
        return re.findall(pattern, x), age [0]
    except:
        pass