#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "WCH"

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn import tree
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.tree import export_graphviz
import pickle
from matplotlib.font_manager import FontProperties  # 中文字體
import pydot
import myfun_healthcare

###### 1.讀取檔案 轉numpy 標準化 分訓練xy ######

df = pd.read_excel("資料清洗後標準化.xlsx")  # 讀取 pandas資料
colX=df.columns[0:].tolist()
colX1=df.columns[2:].tolist()
print(colX,colX1)
#myfun_healthcare.ML_read_excel_標準化("資料清洗後.xlsx",listx,['Personality'],0.05)    # 單純呼叫函數
train_x, test_x, train_y, test_y=\
              myfun_healthcare.ML_read_excel("資料清洗後標準化.xlsx",colX,['Attrition'],0.2)  # 呼叫並帶出 train_x, test_x, train_y, test_y


###### 2.KNN 演算法 ######
model=myfun_healthcare.ML_分類_KNN(train_x, test_x, train_y, test_y)
pickle.dump(model, open("knn.model", 'wb'))

###### 3.Kmeans 演算法 ######
myfun_healthcare.ML_分類_kmeans(train_x, test_x, test_y)

###### 4.隨機森林 演算法 ######
myfun_healthcare.ML_分類_RandomForest_plt(colX,train_x, test_x, train_y, test_y)

###### 5.決策樹 演算法 沒設定 ######
myfun_healthcare.ML_分類_DecisionTree(train_x, test_x, train_y, test_y)

###### 5.決策樹 演算法 entropy ######
myfun_healthcare.ML_分類_DecisionTree_entropy_plt(colX,train_x, test_x, train_y, test_y)

###### 6.決策樹 演算法 gini ######
myfun_healthcare.ML_分類_DecisionTree_gini_plt(colX,train_x, test_x, train_y, test_y)

###### 7.Naive Bayes 演算法 ######
myfun_healthcare.ML_分類_Naive_Bayes(train_x, test_x, train_y, test_y)


