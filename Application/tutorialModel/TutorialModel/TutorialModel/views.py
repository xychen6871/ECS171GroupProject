from django.http import HttpResponse
from django.shortcuts import render
import pandas
import json
import joblib

def home(request):
    test = pandas.read_csv("testData.csv")
    encoder = joblib.load("stateEncoder.sav")

    testEncoded = test.drop(['RD_Spend', 'Administration', 'Marketing_Spend', 'Profit'], axis=1)

    testEncoded = test.drop(['RD_Spend', 'Administration', 'Marketing_Spend', 'Profit', 'Unnamed: 0'], axis=1)

    testEncoded = encoder.inverse_transform(testEncoded)
    test.drop(['0', '1', '2'], axis=1, inplace=True)
    testData = pandas.merge(test.drop(['Unnamed: 0'], axis=1), pandas.DataFrame(testEncoded), right_index=True,left_index=True)
    testData["State"] = testData[0]
    testData.drop([0], axis=1, inplace=True)

    json_records = testData.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    context = {'d': data}
    return render(request, "home.html", context)

def result(request):
    regressor = joblib.load("regressor.sav")
    encoder = joblib.load("stateEncoder.sav")

    rd = request.GET['RD']
    admin = request.GET['Admin']
    market = request.GET['Market']
    state = request.GET['State']

    state = encoder.transform([[state]])

    xData = [rd, admin, market, state[0][0], state[0][1], state[0][2]]

    yPredicted = regressor.predict([xData])



    return render(request, "result.html", {'yPredicted': yPredicted})

