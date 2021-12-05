# ECS 171 Group 2 Project Source Guide - TODO: FIX PLACEHOLDER VALUES ONCE THE REAL FILES HAVE BEEN DETERMINED

## Report

Our report can be found at [Report/Report.pdf](https://github.com/xychen26/ECS171GroupProject/blob/main/Report/report.pdf).

Parts of our report used data and code from the following sources:
- The correlation analysis used information gathered from [correlationAnalysis.ipynb](https://github.com/xychen26/ECS171GroupProject/blob/main/correlationAnalysis.ipynb)
- The simple linear regression model was developed in [Simple_LinearRegression_outlier_removed.ipynb](https://github.com/xychen26/ECS171GroupProject/blob/main/Simple_LinearRegression_outlier_removed.ipynb) and [Results for Linear Regression Models.ipynb](https://github.com/xychen26/ECS171GroupProject/blob/main/Results%20for%20Linear%20Regression%20Models.ipynb)
- The multiple linear regression model was developed in [Multivariate_LinearRegression_outlier_removed.ipynb]() and [Results for Linear Regression Models.ipynb](https://github.com/xychen26/ECS171GroupProject/blob/main/Results%20for%20Linear%20Regression%20Models.ipynb)
- The polynomial regression model was developed in [Polynomial Regression Data Analysis (with Outliers).ipynb](https://github.com/xychen26/ECS171GroupProject/blob/main/Polynomial%20Regression%20Data%20Analysis%20(with%20Outliers).ipynb) and [Polynomial Regression Data Analysis.ipynb](https://github.com/xychen26/ECS171GroupProject/blob/main/Polynomial%20Regression%20Data%20Analysis.ipynb)
- The neural network model was developed in [NN_Hyper_Parameter_Tuned_Filtered_v3_Jeehoon.ipynb](https://github.com/xychen26/ECS171GroupProject/blob/main/NN_Hyper_Parameter_Tuned_Filtered_v3_Jeehoon.ipynb)


## Application

Our application's main folder can be found at [Application/ApplicationProject/ApplicationServer/](https://github.com/xychen26/ECS171GroupProject/tree/main/Application/ApplicationProject/ApplicationServer)

To run it, please ensure that you have the following dependencies: 
- Anaconda
- Tensorflow/Keras
- Django

In the application's main folder, open the anaconda prompt and use the following command "_python manage.py runserver_". Then go to http://localhost:8000/ in an internet browser (or whichever port the server is running on) to see our models in action.

The models used for the application were stored in the [Application/ApplicationProject/ApplicationServer/ModelFiles](https://github.com/xychen26/ECS171GroupProject/tree/main/Application/ApplicationProject/ApplicationServer/ModelFiles) folder as well as the code used to generate the save files.
- [Simple Linear Regression Model Generation](https://github.com/xychen26/ECS171GroupProject/blob/main/Application/ApplicationProject/ApplicationServer/ModelFiles/GenerateLinearModel.ipynb)
- [Multiple Linear Regression Model Generation](https://github.com/xychen26/ECS171GroupProject/blob/main/Application/ApplicationProject/ApplicationServer/ModelFiles/GenereateMultiLinearModel.ipynb)
- [Polynomial Regression Model Generation](https://github.com/xychen26/ECS171GroupProject/blob/main/Application/ApplicationProject/ApplicationServer/ModelFiles/GeneratePolyModel.ipynb)
- [Neural Network Model Generation](https://github.com/xychen26/ECS171GroupProject/blob/main/Application/ApplicationProject/ApplicationServer/ModelFiles/GenerateNNmodel.ipynb)
- Model save files were named _NN_model.sav_, _LinearModel.sav_, _multi_lin_model.sav_, and _PolyModel**X**.sav_ where **X** is the degree of the polynomial model from 2 through 10.
- Scaler, X, and y test files are also included in the folder.

### Application Citations
- [Setting up a server with Django](https://www.youtube.com/watch?v=zcALUNZNBUk)
- [Bootstrap CDN](https://www.bootstrapcdn.com/)
- [Bootstrap Buttons](https://getbootstrap.com/docs/4.0/components/buttons/)
- [Bootstrap Grid Format](https://getbootstrap.com/docs/4.0/layout/grid/)
- [Hyperlinks in html](https://www.w3schools.com/html/html_links.asp)
- [Dataframe to html with Django](https://www.geeksforgeeks.org/rendering-data-frame-to-html-template-in-table-view-using-django-framework/)
- [Submitting table data to Django back-end](https://stackoverflow.com/questions/56863105/how-do-i-pass-table-data-from-a-template-over-to-django-on-a-button-submit-click)
- [Test Application startup data](https://www.kaggle.com/karthickveerakumar/startup-logistic-regression)
- [Creating readonly text fields](https://stackoverflow.com/questions/35659178/prevent-typing-in-text-field-input-even-though-field-is-not-disabled-read-only)
- [Saving and Loading Keras Objects](https://stackoverflow.com/questions/67661244/how-to-pickle-weakref-in-python-tensorflow-keras?noredirect=1)
