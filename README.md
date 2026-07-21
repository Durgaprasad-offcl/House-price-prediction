# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview
This machine learning project predicts house prices based on house size using the Linear Regression algorithm. It demonstrates the complete machine learning workflow from data loading to model evaluation and visualization.

---

---

## 📊 Dataset
The dataset contains two columns:
- **HouseSize** (sq.ft)
- **Price** (Lakhs)

Example:

| House Size | Price |
|-----------:|------:|
| 500        | 25    |
| 700        | 35    |
| 900        | 45    |

---

## 📈 Regression Graph

The graph shows:
- 🔵 Blue dots → Actual house prices
- 📏 Straight line → Linear Regression best-fit line

---

## 🤖 Prediction Example

**Input:**
```text
House Size = 2500 sq.ft
```

**Output:**
```text
Predicted House Price: 125.00 Lakhs
```

---

## 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

## 📌 Features
- Load CSV dataset
- Train Linear Regression model
- Predict house prices
- Evaluate using:
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - RMSE (Root Mean Squared Error)
  - R² Score
- Save model using Joblib
- Load model for prediction
- Data visualization

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model**
   ```bash
   python src/train.py
   ```

3. **Make predictions**
   ```bash
   python src/predict.py
   ```

4. **Visualize results**
   ```bash
   python src/visualize.py
   ```

---

## 📚 What I Learned
- Data preprocessing
- Feature and target selection
- Linear Regression
- Model training
- Model prediction
- Model evaluation
- Data visualization
- Saving and loading ML models
- Organizing a professional ML project

---

## 👨‍💻 Author
**Durga Prasad**
B.Tech – Data Science
Machine Learning Enthusiast