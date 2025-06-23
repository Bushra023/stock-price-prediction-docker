# 📊 Stock Price Prediction API with Flask & Docker
This project demonstrates how to deploy a machine learning model using Flask and Docker, providing real-time stock price predictions based on historical market data.

# 🚀 Features
Trained a Linear Regression model to predict stock prices using historical features like:

open_price

prev_close (previous day's close)

ma_7 (7-day moving average)

REST API built with Flask

Containerized application using Docker

Easily deployable and accessible via http://localhost:5000

Supports JSON-based input/output for model predictions

# 🏗️ Tech Stack
Python

Flask

Scikit-Learn

Docker

# 📁 Project Structure
├── app.py                # Flask Application to serve ML model

├── Dockerfile            # Docker configuration

├── requirements.txt      # Project dependencies

├── model.pkl             # Trained ML model (Linear Regression)

├── README.md             # Project overview and instructions

├── .gitignore            # Ignoring unnecessary files


# ⚙️ Getting Started
Run the App with Docker
Ensure you have Docker installed. Then:

`docker build -t stock-prediction-app .`

`docker run -p 5000:5000 stock-prediction-app`

`Visit: http://localhost:5000`

# 📡 Example API Usage
Prediction Endpoint

`POST http://localhost:5000/predict`

Request Body:

`{
  "open_price": 123.45,
  "prev_close": 122.80,
  "ma_7": 124.00
}`

Example with cURL:

`curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"open_price": 123.45, "prev_close": 122.80, "ma_7": 124.00}'`
