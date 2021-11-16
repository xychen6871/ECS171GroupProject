from django.shortcuts import render
import joblib
import pandas as pd
import json
from sklearn.preprocessing import PolynomialFeatures

def home(request):
    return render(request, "home.html")

def linearChoice(request):
    return render(request, "linearChoice.html")

def linregress(request):
    test = pd.read_csv("ModelFiles/Linear_test.csv")
    X_test = test[["livingAreaSqFt"]]
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    
    context = {'d': data}
    return render(request, "linregress.html", context)

def linearResults(request):
    linear_model = joblib.load("ModelFiles/LinearModel.sav")
    test = pd.read_csv("ModelFiles/Linear_test.csv")
    y_test = test[["latestPrice"]]
    
    sqft = request.GET["SQFT"]
    index = int(request.GET["INDEX"])
    y_true = y_test.at[index, 'latestPrice']

    yPredicted = linear_model.predict([[sqft]])
    return render(request, "linearResults.html", {'yPredicted': int(yPredicted[0]), 'y_true': y_true, 'x': sqft, 'index': index})

def multiregress(request):
    test = pd.read_csv("ModelFiles/Multi_test.csv")
    X_test = test[['livingAreaSqFt','numOfBathrooms', 'avgSchoolRating', 'numOfBedrooms', 'numOfHighSchools', 'MedianStudentsPerTeacher']]
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    
    context = {'d': data}
    return render(request, "multiregress.html", context)

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

def polyregress(request):
    test = pd.read_csv("ModelFiles/Poly_test.csv")
    X_test = test[['numOfBathrooms', 'avgSchoolRating', 'numOfBedrooms', 'numOfHighSchools', 'MedianStudentsPerTeacher']]
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    
    context = {'d': data}
    return render(request, "polyregress.html", context)

def polyResults(request):
    degree = request.GET["DEGREE"]
    poly_model = joblib.load("ModelFiles/PolyModel" + degree + ".sav")
    test = pd.read_csv("ModelFiles/Poly_test.csv")
    y_test = test[["latestPrice"]]
    range = y_test.latestPrice.max() - y_test.latestPrice.min()

    index = int(request.GET["INDEX"])
    bathrooms = request.GET["BATHROOMS"]
    schoolRating = request.GET["SCHOOLRATING"]
    bedrooms = request.GET["BEDROOMS"]
    highSchools = request.GET["HIGHSCHOOLS"]
    teachers = request.GET["TEACHERS"]

    xData = [bathrooms, schoolRating, bedrooms, highSchools, teachers]

    poly = PolynomialFeatures(int(degree))
    xDataPoly = poly.fit_transform([xData])
    yPredicted = poly_model.predict(xDataPoly)
    yPredicted = yPredicted * range
    y_true = y_test.at[index, "latestPrice"]

    return render(request, "polyResults.html", {'yPredicted': int(yPredicted[0]), "y_true": y_true, "x": xData, "index": index})

def neuraln(request):
    return render(request, "neuraln.html")