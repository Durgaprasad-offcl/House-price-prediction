import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df=pd.read_csv("data/house_price.csv")
X=df[["HouseSize"]]
Y=df["Price"]
model=LinearRegression()
model.fit(X,Y)

predicted_price=model.predict(X)
plt.scatter(X,Y,label="Actual Data")
plt.plot(X,predicted_price,label="Regression Line")
plt.title("house price prediction")
plt.xlabel("house size")
plt.ylabel("price")
plt.legend()
plt.show()