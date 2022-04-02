import pylab as plt

import pandas as pd

import seaborn as sns

def getGraphic(dataframe):
    
    plt.figure(figsize=(10, 6))

    return sns.heatmap(dataframe.isnull(), yticklabels=False, cmap='viridis', cbar=False)

def getDic(dataframe, column):

    return dict(dataframe[column].value_counts())