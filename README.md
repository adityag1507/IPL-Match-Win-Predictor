# 🏏 IPL Match Win Predictor
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A machine learning-powered web application that predicts the winning probability of the chasing team in an IPL match using the current match situation.

The application combines a trained Scikit-Learn model with a Flask backend to deliver real-time predictions through a responsive and modern web interface.

---

## Live Demo

> Coming Soon (Render)

---

## Overview

Predicting the outcome of a T20 cricket match is a challenging problem because the probability changes dynamically after every ball.

This project estimates the winning probability of the chasing team using historical IPL match data and important match-state features such as current score, wickets remaining, overs completed, current run rate, and required run rate.

The model is integrated into a Flask application that allows users to interactively enter match details and receive instant probability predictions.

---

## Features

- Machine Learning-based IPL win probability prediction
- Supports all IPL 2025 franchises
- Responsive web interface for desktop and mobile devices
- Real-time prediction using a trained Scikit-Learn model
- Match summary including:
  - Runs Needed
  - Balls Left
  - Wickets Remaining
  - Current Run Rate (CRR)
  - Required Run Rate (RRR)
- Team logos
- Input validation for invalid match scenarios
- Modern black and red user interface

---

## Machine Learning Pipeline

The prediction model follows the following workflow:

1. Historical IPL match data preprocessing
2. Feature engineering
3. Model training using Scikit-Learn
4. Model serialization using Pickle
5. Flask-based deployment for real-time inference

---

## Model Input Features

The model predicts match outcome using:

- Batting Team
- Bowling Team
- Venue
- Target Score
- Current Score
- Overs Completed
- Wickets Lost
- Runs Left
- Balls Left
- Current Run Rate (CRR)
- Required Run Rate (RRR)

---

## Technology Stack

### Backend

- Python
- Flask

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Pickle

### Frontend

- HTML5
- CSS3

### Development

- Jupyter Notebook
- PyCharm

---

## Project Structure

```text
IPL_Match_Predictor/
│
├── app.py
├── pipe.pkl
├── Match.csv
├── Delivery.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── favicon.png
│   └── logos/
│
└── screenshots/
    ├── home.png
    ├── prediction.png
    └── mobile.png
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/adityag1507/IPL-Match-Win-Predictor.git
```

Move into the project directory

```bash
cd IPL-Match-Win-Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Screenshots

### Home Page

![Home](screenshots/home.png)

---

### Prediction Result

![Prediction](screenshots/prediction.png)

---

### Mobile View

<img src="screenshots/mobile.png" width="350">

---

## Future Enhancements

- Live IPL match integration
- Interactive probability visualizations
- Player statistics integration
- Advanced analytics dashboard
- Historical match comparison

---

## Author

**Aditya Goyal**

GitHub: https://github.com/adityag1507

LinkedIn: https://www.linkedin.com/in/aditya-goyal-14161b402

---
