# 🏥 Doctor Appointment Scheduler with No-Show Risk Predictor

## 📋 Overview
A full-stack web application that predicts patient no-show risk using Machine Learning (Logistic Regression with 94% accuracy).

## ✨ Features
- Patient registration and authentication
- Real-time no-show risk prediction at booking
- Interactive dashboard for patients
- Power BI analytics dashboard
- Risk level indicators (Low/Medium/High/Very High)

## 🛠️ Tech Stack
- **Backend**: Django 6.0, SQLite
- **ML Model**: Scikit-learn (Logistic Regression)
- **Frontend**: Bootstrap 5, HTML/CSS
- **Visualization**: Power BI

## 📊 Model Performance
- Accuracy: 94%
- Precision: 96%
- Recall: 96%
- F1-Score: 96%
- ROC-AUC: 0.94

## 🚀 Installation

```bash
# Clone repository
git clone https://github.com/Vigneshwararaj-M/doctor-appointment-scheduler.git
cd doctor-appointment-scheduler

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django pandas numpy scikit-learn xgboost

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
