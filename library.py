import pandas as pd
#import numpy as n
from sklearn import linear_model
#import rpy2
#import rpy2.robjects as robjects


class Linreg(linear_model.LinearRegression):
        def __init__ (self):
            linear_model.LinearRegression.__init__(self)

        def summary_(self,x,y):
            reg = linear_model.LinearRegression()
            reg.fit(x,y)
            print("Coefficients:",reg.coef_)
            print("Intercept:", reg.intercept_)
            print("R_sq: ",reg.score(x,y))

from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant

def variance_inflation_factors(exog_df):
    '''
    Parameters
    ----------
    exog_df : dataframe, (nobs, k_vars)
        design matrix with all explanatory variables, as for example used in
        regression.

    Returns
    -------
    vif : Series
        variance inflation factors
    '''
    exog_df = add_constant(exog_df)
    vifs = pd.Series(
        [1 / (1. - OLS(exog_df[col].values,
                       exog_df.loc[:, exog_df.columns != col].values).fit().rsquared)
         for col in exog_df],
        index=exog_df.columns,
        name='VIF'
    )
    return vifs
