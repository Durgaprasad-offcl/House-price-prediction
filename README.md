# 🏠 House Price Prediction using Linear Regression

A simple, beginner-friendly Machine Learning web application that predicts house prices based on house size, built with **Python**, **Scikit-learn**, and **Streamlit**.

## 📌 Overview

This project walks through a complete, minimal end-to-end Machine Learning workflow:

1. Load and explore a house price dataset
2. Train a **Linear Regression** model on house size vs. price
3. Save the trained model using **Joblib**
4. Serve real-time predictions through an interactive **Streamlit** web app

It's designed as a clean starting point for anyone learning how to take a model from training to deployment.

---

## 🚀 Features

- 📊 Instant house price predictions from a single input
- 🖥️ Clean, interactive Streamlit UI
- 🤖 Simple, interpretable Linear Regression model
- 💾 Model persistence with Joblib (train once, reuse anywhere)
- 🧩 Modular project structure (data / model / app / training script separated)
- 📈 Great for beginners exploring the ML → Web App pipeline

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Handling | Pandas, NumPy |
| Modeling | Scikit-learn |
| Persistence | Joblib |
| Web App | Streamlit |

---

## 📂 Project Structure

```
House-price-prediction/
│
├── app.py                     # Streamlit web application
├── README.md
├── requirements.txt
│
├── data/
│   └── house_data.csv         # Training dataset
│
├── models/
│   └── house_price_model.pkl  # Trained & saved model
│
└── src/
    └── train.py                # Model training script
```

---

## 📊 Dataset

| Feature | Description |
|---|---|
| `House Size` | Size of the house (in sq ft) |
| `Price` | House price (target variable) |

> Replace `data/house_data.csv` with your own dataset to retrain the model on real-world data.

---

## 🤖 Machine Learning Model

**Algorithm:** Linear Regression

The model learns a linear relationship between house size and price:

```
Price = m × (House Size) + c
```

Where `m` (slope) and `c` (intercept) are learned from the training data using `scikit-learn`'s `LinearRegression`.

---

## ▶️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Durgaprasad-offcl/House-price-prediction.git
cd House-price-prediction
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Retrain the model
```bash
python src/train.py
```
This will regenerate `models/house_price_model.pkl`.

### 5. Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🖥️ How to Use

1. Enter the **house size** (in sq ft) in the input field
2. Click **Predict Price**
3. View the **predicted price** displayed instantly

### Example

```
🏠 House Price Prediction

Enter House Size (sq ft): [ 1500 ]

[ Predict Price ]

💰 Predicted House Price: ₹1,25,00,000
```

---

## 📈 Roadmap / Future Improvements

- [ ] Support multiple features (location, bedrooms, bathrooms, etc.)
- [ ] Improve UI/UX with charts and layout enhancements
- [ ] Add CSV upload for batch predictions
- [ ] Add model evaluation metrics (R², RMSE) to the app
- [ ] Deploy on Streamlit Community Cloud
- [ ] Add unit tests for training and prediction pipeline

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](../../issues) or open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share it.

---

## 👨‍💻 Author

**Durga Prasad**
B.Tech Data Science Student
Python · SQL · Machine Learning · Streamlit

---

⭐ If you found this project useful, consider giving it a star — it helps a lot!