from django.shortcuts import render
import joblib
import pandas as pd
import json
from sklearn.preprocessing import PolynomialFeatures

# Return the home html page when requested. There are no parameters that need to be passed as context.
def home(request):
    return render(request, "home.html")

# Return the linear model selection html page when requested. There are no parameters that need to be passed as context.
def linearChoice(request):
    return render(request, "linearChoice.html")

# Return the simple linear regression page with the test data as context.
def linregress(request):
    test = pd.read_csv("ModelFiles/Linear_test.csv")
    X_test = test[["livingAreaSqFt"]]
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    
    context = {'d': data}
    return render(request, "linregress.html", context)

# Return the simple linear regression results html page, using the results of our model prediction as the context parameter.
def linearResults(request):
    linear_model = joblib.load("ModelFiles/LinearModel.sav")
    test = pd.read_csv("ModelFiles/Linear_test.csv")
    y_test = test[["latestPrice"]]
    
    sqft = request.GET["SQFT"]
    index = int(request.GET["INDEX"])
    y_true = y_test.at[index, 'latestPrice']

    yPredicted = linear_model.predict([[sqft]])
    return render(request, "linearResults.html", {'yPredicted': int(yPredicted[0]), 'y_true': y_true, 'x': sqft, 'index': index})

# Return the multiple linear regression page with the test data as context.
def multiregress(request):
    test = pd.read_csv("ModelFiles/Multi_test.csv")
    X_test = test[['livingAreaSqFt','numOfBathrooms', 'avgSchoolRating', 'numOfBedrooms', 'numOfHighSchools', 'MedianStudentsPerTeacher']]
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    
    context = {'d': data}
    return render(request, "multiregress.html", context)

# Return the multiple linear regression results html page, using the results of our model prediction as the context parameter.
def multiResults(request):
    linear_model = joblib.load("ModelFiles/multi_lin_model.sav")
    test = pd.read_csv("ModelFiles/Multi_test.csv")
    y_test = test[["latestPrice"]]
    
    index = int(request.GET["INDEX"])
    sqft = request.GET["SQFT"]
    bathrooms = request.GET["BATHROOMS"]
    schoolRating = request.GET["SCHOOLRATING"]
    bedrooms = request.GET["BEDROOMS"]
    highSchools = request.GET["HIGHSCHOOLS"]
    teachers = request.GET["TEACHERS"]

    xData = [sqft, bathrooms, schoolRating, bedrooms, highSchools, teachers]

    y_true = y_test.at[index, 'latestPrice']

    yPredicted = linear_model.predict([xData])
    return render(request, "multiResults.html", {'yPredicted': int(yPredicted[0]), 'y_true': y_true, 'x': xData, 'index': index})

# Return the polynomial regression page with the test data as context.
def polyregress(request):
    test = pd.read_csv("ModelFiles/Poly_test.csv")
    X_test = test[['livingAreaSqFt', 'numOfBathrooms', 'avgSchoolRating', 'numOfBedrooms', 'numOfHighSchools', 'MedianStudentsPerTeacher']]
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    
    context = {'d': data}
    return render(request, "polyregress.html", context)

# Return the polynomial regression results html page, using the results of our model prediction as the context parameter.
def polyResults(request):
    degree = request.GET["DEGREE"]
    poly_model = joblib.load("ModelFiles/PolyModel" + degree + ".sav")
    test = pd.read_csv("ModelFiles/Poly_test.csv")
    y_test = test[["latestPrice"]]
    range = y_test.latestPrice.max() - y_test.latestPrice.min()

    index = int(request.GET["INDEX"])
    sqFt = int(request.GET["SQFT"])
    bathrooms = request.GET["BATHROOMS"]
    schoolRating = request.GET["SCHOOLRATING"]
    bedrooms = request.GET["BEDROOMS"]
    highSchools = request.GET["HIGHSCHOOLS"]
    teachers = request.GET["TEACHERS"]

    xData = [sqFt, bathrooms, schoolRating, bedrooms, highSchools, teachers]

    poly = PolynomialFeatures(int(degree))
    xDataPoly = poly.fit_transform([xData])
    yPredicted = poly_model.predict(xDataPoly)
    yPredicted = yPredicted * range
    y_true = y_test.at[index, "latestPrice"]

    return render(request, "polyResults.html", {'yPredicted': int(yPredicted[0]), "y_true": y_true, "x": xData, "index": index})

def neuraln(request):
    return render(request, "neuraln.html")