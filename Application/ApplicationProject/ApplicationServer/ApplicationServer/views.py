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
    # reads test data from file
    test = pd.read_csv("ModelFiles/Linear_test.csv")
    X_test = test[["livingAreaSqFt"]]
    #gets sample of test data to display
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    #adds data to context and sends to render
    context = {'d': data}
    return render(request, "linregress.html", context)

# Return the simple linear regression results html page, using the results of our model prediction as the context parameter.
def linearResults(request):
    # reads linear model from file
    linear_model = joblib.load("ModelFiles/LinearModel.sav")
    #reads test data from file
    test = pd.read_csv("ModelFiles/Linear_test.csv")
    y_test = test[["latestPrice"]]
    
    #gets x variables from request
    sqft = request.GET["SQFT"]
    index = int(request.GET["INDEX"])
    y_true = y_test.at[index, 'latestPrice']

    # predicts the cost
    yPredicted = linear_model.predict([[sqft]])
    #sends prediction along with the true result, x values, and index value to render
    return render(request, "linearResults.html", {'yPredicted': int(yPredicted[0]), 'y_true': y_true, 'x': sqft, 'index': index})

# Return the multiple linear regression page with the test data as context.
def multiregress(request):
    # reads test data from file
    test = pd.read_csv("ModelFiles/Multi_test.csv")
    X_test = test[['livingAreaSqFt','numOfBathrooms', 'avgSchoolRating', 'numOfBedrooms', 'numOfHighSchools', 'MedianStudentsPerTeacher']]
    #gets sample of test data to display
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    #adds data to context and sends to render
    context = {'d': data}
    return render(request, "multiregress.html", context)

# Return the multiple linear regression results html page, using the results of our model prediction as the context parameter.
def multiResults(request):
    # reads multiple linear model from file
    linear_model = joblib.load("ModelFiles/multi_lin_model.sav")
    #reads test data from file
    test = pd.read_csv("ModelFiles/Multi_test.csv")
    y_test = test[["latestPrice"]]
    
    #gets x variables from request
    index = int(request.GET["INDEX"])
    sqft = request.GET["SQFT"]
    bathrooms = request.GET["BATHROOMS"]
    schoolRating = request.GET["SCHOOLRATING"]
    bedrooms = request.GET["BEDROOMS"]
    highSchools = request.GET["HIGHSCHOOLS"]
    teachers = request.GET["TEACHERS"]

    xData = [sqft, bathrooms, schoolRating, bedrooms, highSchools, teachers]

    y_true = y_test.at[index, 'latestPrice']

    # predicts the cost
    yPredicted = linear_model.predict([xData])
    #sends prediction along with the true result, x values, and index value to render
    return render(request, "multiResults.html", {'yPredicted': int(yPredicted[0]), 'y_true': y_true, 'x': xData, 'index': index})

# Return the polynomial regression page with the test data as context.
def polyregress(request):
    # reads test data from file
    test = pd.read_csv("ModelFiles/Poly_test.csv")
    X_test = test[['livingAreaSqFt', 'numOfBathrooms', 'avgSchoolRating', 'numOfBedrooms', 'numOfHighSchools', 'MedianStudentsPerTeacher']]
    #gets sample of test data to display
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    #adds data to context and sends to render
    context = {'d': data}
    return render(request, "polyregress.html", context)

# Return the polynomial regression results html page, using the results of our model prediction as the context parameter.
def polyResults(request):
    # gets degree from request and reads the correct polynomial model from the file
    degree = request.GET["DEGREE"]
    poly_model = joblib.load("ModelFiles/PolyModel" + degree + ".sav")
    #reads test data from file
    test = pd.read_csv("ModelFiles/Poly_test.csv")
    y_test = test[["latestPrice"]]
    range = y_test.latestPrice.max() - y_test.latestPrice.min()

    #gets x variables from request
    index = int(request.GET["INDEX"])
    sqFt = int(request.GET["SQFT"])
    bathrooms = request.GET["BATHROOMS"]
    schoolRating = request.GET["SCHOOLRATING"]
    bedrooms = request.GET["BEDROOMS"]
    highSchools = request.GET["HIGHSCHOOLS"]
    teachers = request.GET["TEACHERS"]

    xData = [sqFt, bathrooms, schoolRating, bedrooms, highSchools, teachers]
    
    # transforms the data and predicts the cost using the model
    poly = PolynomialFeatures(int(degree))
    xDataPoly = poly.fit_transform([xData])
    yPredicted = poly_model.predict(xDataPoly)
    yPredicted = yPredicted * range
    y_true = y_test.at[index, "latestPrice"]
    #sends prediction along with the true result, x values, and index value to render
    return render(request, "polyResults.html", {'yPredicted': int(yPredicted[0]), "y_true": y_true, "x": xData, "index": index})

# Return the neural network page with the test data as context.
def neuraln(request):
    # reads the test data from file
    test = pd.read_csv("ModelFiles/neuralNet_test.csv")
    X_test = test[['livingAreaSqFt', 'numOfBathrooms', 'avgSchoolRating', 'numOfBedrooms', 'numOfHighSchools', 'MedianStudentsPerTeacher']]
    
    # get sample of test data to display
    X_test = X_test.sample(n=10)
    json_records = X_test.reset_index().to_json(orient='records')

    data = json.loads(json_records)
    
    # adds data to context and sends to render
    context = {'d': data}
    return render(request, "neuraln.html", context)

# Return the neural network results html page, using the results of our model prediction as the context parameter.
def neuralResults(request):
    # read linear model from file
    NN_model = tf.keras.models.load_model("ModelFiles/NN_model.sav")
    scaler = joblib.load("ModelFiles/scalerNN.sav")

    # read the test data from file
    test = pd.read_csv("ModelFiles/neuralNet_test.csv")
    y_test = test[["latestPrice"]]

    # get x variables from request
    index = int(request.GET["INDEX"])
    sqFt = int(request.GET["SQFT"])
    bathrooms = float(request.GET["BATHROOMS"])
    schoolRating = float(request.GET["SCHOOLRATING"])
    bedrooms = float(request.GET["BEDROOMS"])
    highSchools = float(request.GET["HIGHSCHOOLS"])
    teachers = float(request.GET["TEACHERS"])

    xData = scaler.transform([[sqFt, bathrooms, schoolRating, bedrooms, highSchools, teachers]])

    # predict the cost
    yPredicted = NN_model.predict(xData)
    y_true = y_test.at[index, "latestPrice"]

    # show the price bucket where the prediction fells to    
    maxP = 0
    aList = yPredicted[0]
    print(len(aList))
    for i in range(0, len(aList)):
        if aList[i] > aList[maxP]:
            maxP = i

    k = 50000
    fPrice = 0
    lPrice = 0
    for j in range(0, 22):
        if j < 11:
            if maxP == j:
                print("The prediction means that the cost is between $", k*j, " and $", k*(j+1))
                fPrice = k*j
                lPrice = k*(j+1)

        if j >= 12:
            if maxP == j:
                if maxP == 12:
                    print("The predicion means that the cost is from $600000 to $700000")
                    fPrice = 600000
                    lPrice = 700000
                if maxP == 13:
                    print("The predicion means that the cost is from $700000 to $800000")
                    fPrice = 700000
                    lPrice = 800000
                if maxP == 14:
                    print("The predicion means that the cost is from $800000 to $900000")
                    fPrice = 800000
                    lPrice = 900000
                if maxP == 15:
                    print("The predicion means that the cost is from $900000 to $1000000")
                    fPrice = 900000
                    lPrice = 1000000
                if maxP == 16:
                    print("The predicion means that the cost is from $1000000 to $1500000")
                    fPrice = 1000000
                    lPrice = 1500000
                if maxP == 17:
                    print("The predicion means that the cost is from $1500000 to $2000000")
                    fPrice = 1500000
                    lPrice = 2000000
                if maxP == 18:
                    print("The predicion means that the cost is from $2000000 to $3000000")
                    fPrice = 2000000
                    lPrice = 3000000
                if maxP == 19:
                    print("The predicion means that the cost is from $3000000 to $4000000")
                    fPrice = 3000000
                    lPrice = 4000000
                if maxP == 20:
                    print("The predicion means that the cost is from $4000000 to $5000000")
                    fPrice = 4000000
                    lPrice = 5000000
                if maxP == 21:
                    print("The predicion means that the cost is from $5000000 to $6000000")
                    fPrice = 5000000
                    lPrice = 6000000
                if maxP == 22:
                    print("The predicion means that the cost is from $6000000 to $7000000")
                    fPrice = 6000000
                    lPrice = 7000000
                if maxP == 23:
                    print("The predicion means that the cost is from $7000000 to $8000000")
                    fPrice = 7000000
                    lPrice = 8000000
                if maxP == 24:
                    print("The predicion means that the cost is from $8000000 to $9000000")
                    fPrice = 8000000
                    lPrice = 9000000
                if maxP == 25:
                    print("The predicion means that the cost is from $9000000 to $10000000")
                    fPrice = 9000000
                    lPrice = 10000000

    # send prediction to render
    return render(request, "neuralResults.html", {'yPredicted': yPredicted[0], 'y_true': y_true, 'x': xData, 'index': index, 'fPrice': fPrice, 'lPrice': lPrice})
