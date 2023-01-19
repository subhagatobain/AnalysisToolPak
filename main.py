# This is a sample Python script.
import pandas as pd
import library as lb
#import numpy as np
from sklearn import linear_model
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
salesdict = {'sales':[1,2,3,4,5,6,7,8,9],'price':[0.1,0.1,0.1,0.2,0.2,0.2,0.1,0.1,0.1],'wd':[99,99,99,100,100,100,100,100,99]}

salesdict_dt =pd.DataFrame(salesdict)
print(salesdict_dt)

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



print("new coeff")
reg = lb.Linreg()
print(reg.summary_(salesdict_dt[['price','wd']],salesdict_dt['sales']))
#reg.fit(salesdict_dt[['price','wd']],salesdict_dt['sales'])
#print(reg.summary_(salesdict_dt[['price','wd']],salesdict_dt['sales']))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
