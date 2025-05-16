import pickle
import numpy as np
import os

model = None
data_columns = None

def load_model():
    global model, data_columns
    print("Loading model from:", os.path.abspath("kmeans_model.pkl"))
    with open("kmeans_model.pkl", "rb") as f:
        model = pickle.load(f)

    # If you have a columns.json with features, load it too, otherwise just define features here
    data_columns = ['income', 'spending_score']

def predict_cluster(income, spending_score):
    global model
    try:
        # Prepare feature array with only income and spending_score
        x = np.array([income, spending_score]).reshape(1, -1)
        pred = model.predict(x)
        return int(pred[0])
    except Exception as e:
        print("Prediction error:", e)
        return "Error"
