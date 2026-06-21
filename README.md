# FIFA World Cup Analytics & Match Prediction

## Overview

FIFA World Cup Analytics & Match Prediction is a Data Science project that analyzes FIFA World Cup history from 1930 to 2022 and uses Machine Learning to predict match outcomes based on FIFA team rankings.

The project combines Exploratory Data Analysis (EDA), data visualization, feature engineering, machine learning, and a Streamlit web application.

---

## Features

### Historical World Cup Analysis

* World Cup winners analysis
* Attendance analysis
* Match result distribution
* Top-performing nations
* Team win percentage analysis

### Machine Learning Model

* Predicts match outcomes:

  * Home Win
  * Away Win
  * Draw
* Uses FIFA Rankings as predictive features
* Built using Random Forest Classifier

### Streamlit Web App

* Interactive team selection
* Match outcome prediction
* Prediction confidence scores
* Simple and user-friendly interface

---

## Dataset

The project uses:

* FIFA World Cup tournament dataset (1930–2022)
* FIFA World Cup match dataset
* FIFA team rankings dataset

---

## Exploratory Data Analysis

Key insights obtained from the analysis:

* Brazil is the most successful World Cup nation.
* The 1994 FIFA World Cup recorded the highest attendance.
* Home wins occur more frequently than away wins.
* Traditional football powers such as Brazil, Germany, Argentina, France, and Italy have the highest historical win percentages.

---

## Machine Learning Results

### Baseline Model

Features:

* Team Names

Accuracy:

* 45%

### Improved Model

Features:

* Home Team Rank
* Away Team Rank
* Rank Difference

Accuracy:

* 51%

The addition of FIFA ranking features improved model performance significantly compared to the baseline model.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Streamlit
* Jupyter Notebook

---

## Project Structure

```text
FIFA-WorldCup-Analytics/
│
├── data/
├── images/
├── notebooks/
│   └── fifa_worldcup_analysis.ipynb
│
├── model.pkl
├── result_encoder.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Historical FIFA rankings by year
* Advanced feature engineering
* XGBoost and CatBoost models
* Match prediction probabilities
* Deployment to Streamlit Cloud

---

## Author

**Tanmay M K**

B.Tech Data Science Student

Passionate about Data Science, Machine Learning, Sports Analytics, and AI.
