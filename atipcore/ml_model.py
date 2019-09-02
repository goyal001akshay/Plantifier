import pickle
import math
from fuzzywuzzy import fuzz
from .cosine_similarity import calculate_keyword_match
from os import path
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
# from sklearn.linear_model import LogisticRegression

if not path.exists('.ml_engine.pickle'):
    print("Preparing ml_engine")
    testdata_set = pd.read_csv('.test_data.csv')
    dataframe = testdata_set[['sepal_length','sepal_width','petal_length', 'petal_width']]
    x = np.array(dataframe.values)
    yf = testdata_set[['id']]
    y = np.array(yf.values).ravel()
    clf = GaussianNB()    
    # clf = LogisticRegression()  
    clf.fit(x, y)

    with open('.ml_engine.pickle', 'wb') as f:
        pickle.dump(clf, f)


ml_engine = pickle.load(open('.ml_engine.pickle', 'rb'))


def predict_score(sepal_length,sepal_width,petal_length, petal_width):
    
    predicted = ml_engine.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    result = predicted
    return result


def _get_keyword_score(model_answer, answer):
    return calculate_keyword_match(model_answer, answer)
