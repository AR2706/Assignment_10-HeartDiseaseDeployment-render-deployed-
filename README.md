# Assignment_10-HeartDiseaseDeployment-render-deployed-


## 🚀 Live Demo

The machine learning application is deployed and live on Render! You can access it here:
👉 **[Heart Disease Prediction App](https://assignment-10-heartdiseasedeployment-4yzm.onrender.com/)**

## Project Overview
This repository contains the end-to-end deployment of a machine learning model designed to predict whether a patient is at risk of heart disease based on clinical parameters[cite: 1]. The project encompasses data preprocessing, model development, REST API creation using Flask, and live cloud deployment via Render[cite: 1].

**Live Render Deployment URL:** `[Insert your live Render URL here]`[cite: 1]

---

## Repository Structure
Based on the repository contents, the project structure is as follows:

* **`templates/`**: Contains the frontend HTML files for the user interface.
* **`README.md`**: Project documentation.
* **`app.py`**: The Flask REST API application that serves the model.
* **`heart.csv`**: The downloaded Heart Disease dataset used for training.
* **`model.pkl`**: The serialized, trained machine learning model saved using Joblib[cite: 1].
* **`requirements.txt`**: Python dependencies required for GitHub and Render deployment[cite: 1].
* **`train_model.ipynb`**: Jupyter notebook documenting the model training and evaluation process.
* **`train_model.py`**: Python script used for automated data preprocessing and model training.

---

## Observations & Model Performance
* **Dataset:** The project utilizes the Heart Disease Prediction Dataset sourced directly from Kaggle (`johnsmith88/heart-disease-dataset`)[cite: 1].
* **Data Preprocessing:** The dataset was loaded using Pandas, checked for missing values (none found), and split into 80% for training and 20% for testing[cite: 1, 2].
* **Model Training:** A Random Forest Classifier algorithm was selected and trained on the dataset[cite: 2].
* **Accuracy:** During evaluation on the testing set, the Random Forest model achieved a highly accurate prediction score of **0.9854 (98.54%)**[cite: 2].
* **API Functionality:** The Flask API successfully loads the trained model, accepts patient clinical parameters as JSON input, and dynamically returns the disease prediction[cite: 1].

---

## Conclusion
The Random Forest classification model demonstrated exceptional predictive capability, achieving a high accuracy score of 98.54% on the test data[cite: 2]. This robust performance indicates the model effectively captures the underlying patterns within the clinical parameters to accurately assess heart disease risk[cite: 1]. During the deployment phase on Render, the primary challenges involved ensuring seamless dependency management within the `requirements.txt` file and properly configuring the Gunicorn WSGI server to host the Flask application in a live cloud environment[cite: 1]. Overcoming these deployment hurdles highlights the crucial importance of MLOps in modern machine learning projects[cite: 1]. MLOps practices successfully bridge the gap between building an isolated, serialized model (`model.pkl`) and serving it as a scalable, publicly accessible web service[cite: 1]. By incorporating version control through GitHub and continuous deployment via Render, MLOps ensures that predictive healthcare models remain practical, reliable, and dynamically accessible for end-users[cite: 1].
