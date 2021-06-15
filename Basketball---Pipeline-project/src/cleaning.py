def get_id(response):
    """
    This function creates a dictionary with the names and ids of the teams. 
    Arg: The response of the previous request to the API. 
    Returns: The dictionary of names and ids of the teams. 
    """
    list_teams = response['data']
    team_names = [name['full_name'] for name in list_teams]
    team_ids = [name['id'] for name in list_teams]
    combined = zip(team_names, team_ids)
    id_team_name = dict(combined)
    return id_team_name

def append_missing(x):
    """
    This function inserts the missing game in the dataframe. 
    Arg: Name of the dataframe. 
    Returns: The dataframe with the value added. 
    """
    new_row = {'Home team':'Denver Nuggets', 'Home team score':114, 
               'Visitor team':'Los Angeles Lakers', 'Visitor team score':126, 'Date': '2020-09-18T00:00:00.000Z'}
    x = x.append(new_row, ignore_index = True)
    return x  

def get_year(x):
    x = x.split("-")
    return int(x[0])

def clean_date(x):
    x = x.split("T")
    return x[0]

