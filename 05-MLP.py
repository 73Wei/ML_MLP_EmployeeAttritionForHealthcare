#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "WCH"

import tensorflow as tf
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import random
import math
import time
from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
import datetime
import operator
import myfun_healthcare
plt.style.use('seaborn-poster')

df = pd.read_excel("資料清洗後標準化.xlsx")  # 讀取 pandas資料

col=df.columns[1:].tolist()
print(col)
#myfun_healthcare.ML_read_excel_標準化("資料清洗後.xlsx",listx,['Personality'],0.05)    # 單純呼叫函數
train_x, test_x, train_y, test_y=\
              myfun_healthcare.ML_read_excel("資料清洗後標準化.xlsx",col,['Attrition'],0.01)

print(df.shape)

#train_x, test_x, train_y, test_y,scaler=myfun.ML_read_dataframe_標準化("C肝.xlsx", col, col_target)
#print("外型大小",train_x.shape,test_x.shape,train_y.shape,test_y.shape)
#print("前面幾筆:",train_x)

category=2
dim=31
#### one hot encodeing 熱編碼
train_y2=tf.keras.utils.to_categorical(train_y,num_classes=(category))
test_y2=tf.keras.utils.to_categorical(test_y,num_classes=(category))

#print("train_x[:4]",train_x[:4])
#print("train_y[:4]",train_y[:4])
#print("train_y2[:4]",train_y2[:4])


# 建立模型
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=100,
    activation=tf.nn.relu,
    input_dim=dim))
model.add(tf.keras.layers.Dense(units=100,
    activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=100,
    activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=category,
    activation=tf.nn.softmax ))

#opti1=tf.keras.optimizers.Adadelta(learning_rate=0.0001)     # Adadelta

model.summary()                   # 顯示模型
#model.compile(optimizer=opti1,
model.compile(optimizer='adam',
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=['accuracy'])
model.fit(train_x, train_y2,
          epochs=300,
          batch_size=10,
          verbose=1, # 訓練時顯示的訊息的狀態，0 無顯示、1 進度、2 詳細
          #validation_split=0.1 # 如是 0.1，在訓練時會拿 10% 的數據自行驗證數據)
          )

#測試
score = model.evaluate(test_x, test_y2)
print("score:",score)

predict = model.predict(test_x)
print("Ans:",np.argmax(predict,axis=-1))






