# -*- coding: utf-8 -*-
"""Logistic_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/107S_xKPrV8ZOtvzheawqc3VQOXgWvpcf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df=pd.read_csv("iris.csv")

df.head(5)

df.info()

df["variety"].value_counts()

final_df=df[df["variety"]!="Virginica"]

final_df["variety"].value_counts()

final_df=final_df.replace({"variety":{"Setosa":1, "Versicolor":0}})

X=final_df.iloc[:,:-1]
Y=final_df.iloc[:,-1]

new_line="\n"
print(f"Features values: {new_line}{X.head(5)}")
print(f"{new_line} Label: {new_line}{Y.head(5)}")

x_train,x_test, y_train, y_test=train_test_split(X,Y, test_size=0.2, random_state=151)

print("train size x: ",x_train. shape)
print("train size y : ",y_train.shape)
print("test size x : ", x_test.shape)
print("test size y : ",y_test.shape)

from sklearn.linear_model import LogisticRegression
modelLogistic = LogisticRegression()
modelLogistic.fit(x_train,y_train)
print ("The intercept bO= ", modelLogistic.intercept_)
print ("The coefficient b1=", modelLogistic.coef_)
y_test_pred=modelLogistic.predict(x_test)

from sklearn.metrics import confusion_matrix
ConfusionMatrix=confusion_matrix(y_test, y_test_pred)
print(ConfusionMatrix)

ax=sns.heatmap(ConfusionMatrix, annot=True, cmap="BuPu")
ax.set_title('Confusion Matrix for Iris dataset')
ax.set_xlabel('Prediction for type of FLOWERS')
ax.set_ylabel('Actual type of FLOWERS')
ax.xaxis.set_ticklabels(['Not Setosa', 'Setosa'])
ax.yaxis.set_ticklabels([ 'Versicolor', 'Not Versicolor'])
plt.show()

#Accuracy
TP=ConfusionMatrix[1,1]
TN=ConfusionMatrix[0,0]
Total=len(y_test)
print("Accuracy from the confusion matrix is ",(TN+TP)/Total)
