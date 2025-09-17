# 🎓 Digital Credit Scoring System

A **machine learning system** that predicts students’ credit scores (300–850) and risk levels (Low / Medium / High) using academic, financial, and spending data.  
The goal is to provide an alternative credit scoring model for students who lack traditional credit history.

## 🚀 Features
- Credit score prediction on a **300–850 scale**  
- Risk categorization: **Low, Medium, High**  
- Interactive **Streamlit web app** for scoring  
- Explanation of top contributing factors for transparency  

## 🛠️ Tech Stack
- Python 3.10+  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  

## 📂 Project Structure
Digital-Credit-Scoring/
│── app.py                                                       # Streamlit web app
│── credit_model.pkl                                             # Trained ML model
│── features.pkl                                                 # Feature list used for training
│── processed_student_data.csv                                   # Clean dataset
│── credit_scoring.ipynb                                         # Colab notebook



✨Create a virtual environment:
- python -m venv venv
- venv\Scripts\activate

✔ Run the Streamlit app:
- streamlit run app.py






















