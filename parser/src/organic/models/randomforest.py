import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import RFE
import joblib
import os


class RandomForest:

    def __init__(self):

        self.pipe = joblib.load('organic/models/saved/randomforest.joblib')


    def predict(self, X_pred):
        pipe = joblib.load('organic/models/saved/randomforest.joblib')
        return self.predict(X_pred)
