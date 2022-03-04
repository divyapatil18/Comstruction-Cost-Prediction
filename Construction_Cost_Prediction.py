# -*- coding: utf-8 -*-
"""ContractorCostPredictionFinal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TDueT839sL9hkgOvoo8_Phnso99FlLeB
"""

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

import pandas as pd

df=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/contractor_cost_prediction.csv")
 
X = df.iloc[:,0:7]
y = df.iloc[:, 7]

#Normalizing the data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 0)

#Dependencies
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU,PReLU,ELU
from keras.layers import Dropout
# Neural network
model = Sequential()
model.add(Dense(5,kernel_initializer = 'he_uniform', input_shape= (X_train[0].shape) )) #the input layer and the first hidden layer
model.add(Dense(2,kernel_initializer = 'he_uniform', activation='relu')) #the second hidden layer
model.add(Dense(2,kernel_initializer = 'he_uniform', activation='relu')) #the third hidden layer
model.add(Dense(1,kernel_initializer = 'glorot_uniform', activation='sigmoid')) #the output layer

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history=model.fit(X_train, y_train,validation_split=0.33,epochs=50, verbose=1 , batch_size=50) 
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

print(history.history.keys())

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Predicting the Test set results
y_pred = model(X_test)
y_pred = (y_pred > 0.3)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Calculate the Accuracy
from sklearn.metrics import accuracy_score
score=accuracy_score(y_pred,y_test)
