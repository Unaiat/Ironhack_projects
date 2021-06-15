import requests
import json
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
from pymongo import MongoClient
client = MongoClient("localhost:27017")


tok1= os.getenv("tok1")
tok2= os.getenv("tok2")

url_query = 'https://api.foursquare.com/v2/venues/explore'

def make_call(company, query):
    """
    This function makes a call to the foursquare API and returns the result in a json. 
    Args: Name of the company, the category to search for. 
    Returns: The response in a json format.
    """
    parameters = {
    "client_id": tok1,
    "client_secret": tok2,
    "v": "20180323",
    "ll": f"{company.get('coordinates')[0]},{company.get('coordinates')[1]}",
    "query": query, 
    "limit": 100    
}
    return requests.get(url= url_query, params = parameters).json()

def make_df(response):
    """
    This function creates a dataframe with the response of the query done to the foursquare API. 
    Args: Name given to the response of the call to the API. 
    Returns: A DataFrame that can be saved as json and imported to the MongoDB database. 
    """
    list_with_dicts = []
    data = response.get("response").get("groups")[0].get("items")
    name = []
    latitude = []
    longitude = []
    for d in data:
        for_list = {}
        for_list["name"] = d.get("venue").get("name")
        for_list["latitude"] = d.get("venue").get("location").get("lat")
        for_list["longitude"] = d.get("venue").get("location").get("lng")
        list_with_dicts.append(for_list)
                                               
    documents = []
    for dictionary in list_with_dicts:
        temporal = {
            "name": dictionary.get("name"),
            "location": {"type": "Point", "coordinates": [dictionary.get("longitude"), dictionary.get("latitude")]}

        }
        documents.append(temporal)


    df = pd.DataFrame(documents)
    df.head()
 
    return df

def check_near(database, name_collection, lon, lat, metres):
    """
    This function checks the if the selected venues are in a given range, calculated from a specific location. 
    Args: Name of the collection to check the venues, longitude and latitude of the place to check and the range in meters.
    Returns: A dataframe with the venues inside the range (if any). 
    """
    lon_lat = lon, lat
    db = client.get_database(database)
    collection = db.get_collection(name_collection)
    collection_point = {"type": "Point",  "coordinates": lon_lat}
    query = {"location": {"$near": {"$geometry": collection_point, "$maxDistance": metres}}}
    query_final = collection.find(query)
    df = pd.DataFrame(list(query_final))
    return df

