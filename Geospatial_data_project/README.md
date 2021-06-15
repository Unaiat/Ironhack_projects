# Geospatial_data_project

This is the third project I have done in the IronHack data analytics bootcamp. The task was to compare different locations and decide which one would be the best to open a company in the gaming industry. 

We had a [MongoDB](https://docs.mongodb.com/) database of companies around the world, storing information about their location (coordinates) and their type (among other data). 

To take the decision, we had to decide some requirements such has having schools nearby. Once we decide a list of conditions, we had to check them making requests to the [Foursquare API](https://developer.foursquare.com/docs/places-api/getting-started/#make-your-first-api-call) and geoqueries with MongoDB. 

- [requests](https://docs.python-requests.org/en/master/) to make the requests from the API 
- [pandas](https://pandas.pydata.org/docs/user_guide/index.html) to create the dataframes 
- [json](https://docs.python.org/3/library/json.html) to navigate through the information from the API 
- [os](https://docs.python.org/3/library/os.html) to use bash commands in python
- [seaborn](https://seaborn.pydata.org/index.html) and [matplotlib](https://matplotlib.org/stable/contents.html) to make the visualizations
- [folium](https://python-visualization.github.io/folium/quickstart.html#Getting-Started) to create the maps
- [pymongo](https://pymongo.readthedocs.io/en/stable/) to work with MongoDB 
- [dotenv] 

I carried out the analysis in three cities, London, Berlin and Paris, making a Jupyter Notebook for each one. 

<img width=1000 src="images/london_map.png">

The explanation of each step can be found in the Storytelling notebook. 

I would like to note that the result is influenced by the amount of information in the MongoDB database and Foursquare, and it doesn't take into account factor such as renting prices etc. 
