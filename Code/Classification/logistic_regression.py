# -*- coding: utf-8 -*-
"""Logistic Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wojzQcVLLBYi7SYputyHXdhhL5QPtPlO
"""

import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
import seaborn as sbn
from sklearn.linear_model import LogisticRegression

data=pd.read_csv('cnn files/train.csv',low_memory=False)
data.head()

test=pd.read_csv('cnn files/test.csv',low_memory=False)
test.head()

x=data.iloc[:,0:180]
y=data.iloc[:,-1]

le=LabelEncoder()
y=le.fit_transform(y)

x_test=test.iloc[:,0:180]
y_test=test.iloc[:,-1]

y_test=le.fit_transform(y_test)

lr=LogisticRegression(max_iter=100000)

x.head()

x_test.head()

lr.fit(x,y)

y_pred=lr.predict(x_test)

print(metrics.accuracy_score(y_test,y_pred))

print(classification_report(y_test,y_pred))

from sklearn.metrics import confusion_matrix
c_m=confusion_matrix(y_test,y_pred)

import seaborn as sbn
df_cm=pd.DataFrame(c_m)

plt.figure(figsize=(20,17))
plt.title("Confusion Matrix for Gaussian Naive Bayes")
sbn.heatmap(df_cm,annot=True)

