import pandas as pd 
import joblib
model=joblib.load("models/house_price_model.pkl")
new_house=pd.DataFrame({"HouseSize":[2500]})
prediction=model.predict(new_house)
print(f"predicted house price:{prediction[0]:.2f} lakshs")