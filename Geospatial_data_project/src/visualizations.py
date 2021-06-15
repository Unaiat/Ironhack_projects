import seaborn as sns
import matplotlib.pyplot as plt

def histogram(figsize, source, column, title):
    """
    This function makes histograms with given information. 
    Args: Size of the graph, the dataframe to create it (the one from which it will take the points column) and a title. 
    Returns: The graph with the selected information. 
    """
    y, x = plt.subplots(figsize = (figsize))
    sns.countplot(x = source[column], palette="Set2")    
    x.set_title(title, size = 15)
    plt.xticks(size = 15, rotation=90)
    plt.show()
    
    
