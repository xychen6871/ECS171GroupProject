import numpy as np
import operator
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler 
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def min_max_normalization(x) :
    x_min = min(x)
    x_max = max(x)
    x = [(a - x_min)/(x_max - x_min) for a in x]
    return x

#Independent variables: numOfBathrooms, avgSchoolRating, numOfBedrooms, numOfHighSchools, and MedianStudentsPerTeacher
#Dependent varaibles: lateestPrice


df = pd.read_csv('austinHousingData.csv')
labelsToRemove = ['zpid', 'city', 'streetAddress', 'latitude', 'longitude', 'description', 'hasGarage', 'numPriceChanges', 'latest_saledate', 'latest_salemonth', 'latest_saleyear', 'latestPriceSource', 'numOfPhotos', 'homeImage']

df.drop(labelsToRemove, axis = 1, inplace=True)

X = df[['numOfBathrooms', 'avgSchoolRating', 'numOfBedrooms', 'numOfHighSchools', 'MedianStudentsPerTeacher']]
Y = df.latestPrice

#for col in X.columns:
#    X[col] = min_max_normalization(X[col])
Y = min_max_normalization(Y)
degree = 2
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X)

tSize = int(len(df)*0.1)
X_poly_train, X_poly_test, Y_train, Y_test = X_poly[:-tSize], X_poly[-tSize:], Y[:-tSize], Y[-tSize:]

model = LinearRegression()
model.fit(X_poly_train, Y_train)

Y_train_pred = model.predict(X_poly_train)
Y_test_pred = model.predict(X_poly_test)

mse_train = mean_squared_error(Y_train,Y_train_pred)
mse_test = mean_squared_error(Y_test,Y_test_pred)
print("Training MSE for degree", degree, "=", mse_train)
print("Testing MSE for degree", degree, "=", mse_test)
