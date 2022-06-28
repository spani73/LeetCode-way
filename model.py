import pandas as pd
import numpy as np
from joblib import dump, load
from sklearn.feature_extraction.text import TfidfVectorizer

clf = load('classifier.joblib') 

tfidf = load('tfidf.joblib') 


def ProcessData(data):
    X= data
    X_predict1 = tfidf.transform([X])
    New_predict1 = clf.predict(X_predict1)
    probability = np.max(clf.predict_proba(X_predict1))*100
    return New_predict1

print(ProcessData("https://www.udemy.com/course/building-real-time-rest-apis-with-spring-boot/?referralCode=6312172DF8B8C2C11F5E"))