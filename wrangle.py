import os
import pandas as pd
import numpy as np
#from env import host, username, password
from scipy import stats
from sklearn.model_selection import train_test_split

#--------------------------------------------------------------------

def get_connection(db, user=username, host=host, password=password):
    
    '''
    This function is to connect to the Codeup MySQL server, and by itself won't do anything. It works in conjunction with 
    the  other functions within this .py file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#--------------------------------------------------------------------

def get_laptop_data():
    '''
    Basic function to full laptop data from the csv file.
    '''
    df = pd.read_csv('Cleaned_Laptop_data.csv')
    
    return df

#--------------------------------------------------------------------



#--------------------------------------------------------------------



#--------------------------------------------------------------------

def df_splits(df, col, val='Yes', strat='Yes', seed=42):
    '''
    This function takes in a dataframe and a taget column, as well as several optional arguments. You can decide if you want a validate set and if you want to stratify. 
    By leaving those two variables alone you will stratify on the target column and get a validate subset. If you change them to anything when calling the function,
    you will not get a validate or stratification. There is also an argument for the seed, which is set to 42 by default.
    '''
    # If val is left alone at 'Yes', the function will run this loop and return a validate subset.
    if val == 'Yes':
        # If strat is left alone at 'Yes', the function will stratify by the column named when calling the function.
        if strat == 'Yes':
            # Train, validate, and test subsets created.
            train, val_test = train_test_split(df, train_size=.6, random_state=seed, stratify=df[col])
            validate, test = train_test_split(val_test, train_size=.6, random_state=seed, stratify=val_test[col])
            # Printing the shapes of each subset 
            print(train.shape, validate.shape, test.shape)
            return train, validate, test
        # If the strat argument is changed at all, it will default to not doing it and not stratify when splitting.
        else:
            #Splitting the data into train, validate, and test.
            train, val_test = train_test_split(df, train_size=.6, random_state=seed)
            validate, test = train_test_split(val_test, train_size=.6, random_state=seed)
            # Again, printing the subset
            print(train.shape, validate.shape, test.shape)
            return train, validate, test
    # This part of the loop is for if you changed the val argument to something other than 'Yes', which will make it not create a validate subset. 
    else:
        # If strat is left at 'Yes', the function will stratify on the column named when calling the function
        if strat == 'Yes':
            # Splitting the data into train and test subsets
            train, test = train_test_split(df, train_size=.8, random_state=seed, stratify=df[col])
            # Printing the shapes
            print(train.shape, test.shape)
            return train, test

        else:
            # Splitting the data into train and test
            train, test = train_test_split(df, train_size=.8, random_state=seed)
            # Printing the shapes
            print(train.shape, test.shape)
            return train, test

#--------------------------------------------------------------------



#--------------------------------------------------------------------



#--------------------------------------------------------------------
