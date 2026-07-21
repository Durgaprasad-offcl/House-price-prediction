import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from math import sqrt
#Load dataset
df=pd.read_csv("data/house_price.csv")
print(df)
print(df.head())
#select features and target
X=df[["HouseSize"]]
Y=df["Price"]
print(X)
print(Y)
#train the model
model=LinearRegression()
model.fit(X,Y)
#predict new house price
new_house=pd.DataFrame({"HouseSize":[2500]})
prediction=model.predict(new_house)
print(prediction)
print("model trained suceessfully!")
predictions=model.predict(X)
mae=mean_absolute_error(Y,predictions)
mse=mean_squared_error(Y,predictions)
r2=r2_score(Y,predictions)
print("MAE:",mae)
print("MSE:",mse)
print("R2score:",r2)
import pandas as pd
import joblib
joblib.dump(model,"models/house_price_model.pkl")

rmse=sqrt(mse)
print("RMSE:",rmse)
