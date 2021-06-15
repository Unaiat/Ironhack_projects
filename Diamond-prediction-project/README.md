<img width=300 src=https://media.giphy.com/media/3oEjI4xcY0Ye5DX8Tm/giphy.gif>

# Diamond prediction project

This is part of a machine learning project we did in the seventh week of the Data Analytics bootcamp at IronHack. 

The objective is to try different models to predict the price of diamonds from this [Kaggle](https://www.kaggle.com/c/diamonds-datamad0321/data) dataset. 

In order to do so, first I analyzed the meaning of each of the columns and their correlation. 

There were three columns with strings representing values, that we had pass to numeric. So I decided to give them a punctuation depending on their potential influence in the evaluation and predicton. 

The cut of the diamond is categorized as bellow, and to each category I gave a number from 1 to 5. 

- Ideal cut = 5
- Premium = 4
- Very Good = 3
- Good = 2
- Fair = 1

I repeated the same operation with the color:

- D = 1
- E = 2
- F = 3
- G = 4
- H = 5
- I = 6
- J = 7

The third column was clarity, and in this case I divided the 11 categories into 6 groups:

- Group I: I3 = 1 | I2 = 1.33 | I1 = 1.66
- Group SI: SI2 = 2 | SI1 = 2.5
- Group VS: VS2 = 3 | VS1 = 3.5
- Group VVS: VVS 2 = 4 | VVS1 = 4.5
- Group IF = 5
- Group F = 6

To decide which columns leave for the training and prediction, I used this correlation matrix.

<img width=1000 src="./images/class_and_gender.svg">

I decided to delete the x, y, z columns, with give the size and are very correlated with the carat and the price. Table and depth also give the size of the diamond. 

The models I tested can be seen in the list bellow:

- Ridge = 0.12296497489885815
- Lasso = 0.12296497489885815
- Sgd = 8518389333027969.0
- Knn = 0.17156369503893218
- Gradient = 0.012208391143577328
- RandomForestRegressor = 0.01105387595279491
- MLPRegressor = 0.027630135819751555

The metric used to evaluate them was the Mean Squared Error (MSE), and I adjusted the parameters for four of them using Grid Search. 

Note = I also used a Linear Regression as a trial. 

### Libraries: 

- [Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)
- [Seaborn](https://seaborn.pydata.org/)
- [Sklearn](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)

### Files: 
- data = Folder with the tests.csv, train.csv, test_clean.csv, train.clean.csv files
- predictions = Folder with the predictions
- images = Folder with the heatmap
- Jupyter Notebook with the cleaning and the models
- src = Folder with a .py archive with functions to clean the data. 
