import pickle
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
def predict_price(feature_list):
    regressor = pickle.load(open("regressor.pkl","rb"))
    oneHotEncoder = pickle.load(open("OneHotEncoder.pkl","rb"))
    feature_list = oneHotEncoder.transform(np.array(feature_list).reshape(1,-1)).toarray()
    predicted = regressor.predict(feature_list)
    clasifier = pickle.load(open("classifier.pkl","rb"))
    pred2 = clasifier.predict(np.array(predicted).reshape(1,-1)).toarray()
    return pred2[0]
