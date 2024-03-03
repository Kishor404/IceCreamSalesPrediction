import pandas as pd
from sklearn.linear_model import LinearRegression

# y=b0+(b1*x)

data=pd.read_csv("IceCreamSales.csv")

x=data["Temperature"].values.reshape(-1,1)
y=data["Profits"]

model=LinearRegression()

model.fit(x,y)

b0=model.intercept_
b1=model.coef_

x1=int(input("Enter Temperature (Fahrenheit) : "))

y1=model.predict([[x1]])

print("Predicted Profit : $",y1[0])