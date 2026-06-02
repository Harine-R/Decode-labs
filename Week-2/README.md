# Data Classification Using AI

## Project Overview

This project demonstrates a basic AI classification model using the Iris Flower Dataset.

The objective is to:
- Load and understand a dataset
- Split data into training and testing sets
- Train a classification model
- Evaluate model accuracy
- Save the trained model

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- Joblib

## Dataset

The Iris Dataset contains flower measurements and class labels for three species:
- Setosa
- Versicolor
- Virginica

## Algorithm

Random Forest Classifier

## Project Structure

Week-2/
├── dataset_info.py
├── train_model.py
├── requirements.txt
├── README.md
└── model.pkl

## How to Run

Install dependencies:

pip install -r requirements.txt

Run dataset information:

python dataset_info.py

Train model:

python train_model.py

## Output

The model trains successfully and prints classification accuracy.

The trained model is saved as:

model.pkl