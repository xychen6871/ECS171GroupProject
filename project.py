import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler 
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('austinHousingData.csv')
labelsToRemove = ['city', 'streetAddress', 'description', 'hasGarage', 'numPriceChanges', 'latest_saledate', 'latest_salemonth', 'latest_saleyear', 'latestPriceSource', 'numOfPhotos', 'homeImage']
df.drop(labelsToRemove, axis = 1, inplace=True)
print(df)
