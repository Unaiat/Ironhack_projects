![portada](https://github.com/agalvezcorell/using_Kaggle-API/blob/main/images/portada_.jpg)

## You can download Kaggle datasets directly from the API!

### Kaggle? What’s that?

Kaggle is “an AirBnB for Data Scientists – this is where they spend their nights and weekends”. It’s a platform where you can find ANY dataset you need to develop your projects or to practice your data handling skills.

####  **Search datasets, list data files, and download data files**

### To get started you need to…

Get the Kaggle API token, which you can obtain from Account Tab -> ‘Create API token’ once you’ve logged in Kaggle website. This token will be downloaded as a file named kaggle.json.
Keep your token in a safe place! (Hide it copying in your .kaggle folder).
And then, using ‘!’in your ipynb to execute commands without using your shell, and this command:  
`!kaggle datasets download -d teajay/global-yourdatasetname' 
You can download and manage your dataset!


## Do I need something to manage this?
Yes, you have to run this command: “pip3 install kaggle” to use the kaggle command as shown in the examples below.

The command line tool supports the following dataset commands: {list, files, download, create, version, init}

#### Datasets
The API supports the following commands for Kaggle Datasets, among others:
{list,files,download,create,version,init,metadata, status}
- list      ----> List available datasets
- files     ----> List dataset files
- download  ----> Download dataset files
   
 

##### To list datasets:
usage: kaggle datasets list [-h] [--sort-by SORT_BY] [--size SIZE] [--file-type FILE_TYPE] [--license LICENSE_NAME] [--tags TaG_IDS] [-s SEARCH] [-m] [--user USER] [-p PAGE] [-v]

Example:
kaggle datasets list -s demographics
kaggle datasets list --sort-by votes

##### To download dataset files:
usage: kaggle datasets download [-h] [-f FILE_NAME] [-p PATH] [-w] [--unzip][-o] [-q][dataset]

Examples:
kaggle datasets download zillow/zecon
kaggle datasets download zillow/zecon -f State_time_series.csv
