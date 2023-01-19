#import pandas as pd
#import numpy as n
from sklearn import linear_model


class Linreg(linear_model.LinearRegression):
        def __init__ (self):
            linear_model.LinearRegression.__init__(self)

        def summary_(self,x,y):
            reg = linear_model.LinearRegression()
            reg.fit(x,y)
            print("Coefficients:",reg.coef_)
            print("Intercept:", reg.intercept_)
            print("R_sq: ",reg.score(x,y))

