#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "WCH"

import pandas as pd
import numpy as np
import myfun_healthcare
from sklearn.preprocessing import MinMaxScaler
from pandas import ExcelWriter  # 匯入 excel writer
myfun_healthcare.matplot_中文字()

df = pd.read_excel('healthcare_資料清洗後.xlsx',0)
print(df.shape)

listAge=myfun_healthcare.pandas_取得裡面的種類(df,"Age")                 # 年齡
#listAge.sort()                                                         # 由小到大排好
listGender=myfun_healthcare.pandas_取得裡面的種類(df,"Gender")            # 性別  男生是 1  女生是2
listSatisfy=myfun_healthcare.pandas_取得裡面的種類(df,"JobSatisfaction")  # 工作滿意度
listJobRole=myfun_healthcare.pandas_取得裡面的種類(df,"JobRole")          # 工作角色

# 計算數量

#t1=df[df["JobSatisfaction"] == "phD"]["Education"].value_counts()

print("============= 年齡 =============")

#print(df["Age"].value_counts().sort_values)

y=[]
x=[]
for Age in listAge:
    total = df[df['Age'] == Age]
    print("年齡(Age)是",Age," 的有",total.shape[0]," 位")
    y.append(float(total.shape[0]))
    x.append(str(Age))

# 平均
print("年齡平均:",df["Age"].mean().round(2),"歲")


print("============= 性別 =============")
#print(df["Gender"].value_counts())
print("女生是2,男生是 1")

y=[]
x=[]

for Gender in listGender:
    total = df[df['Gender'] == Gender]
    y.append(float(total.shape[0]))
    x.append(str(Gender))
    print("性別(Gender)是",Gender," 的有",total.shape[0]," 位")

# 總共
#print("總共:",df["Gender"].sum(),"位")     # 不知道為什麼會多加一次 678

print("=============工作滿意度=============")

#print(df["JobSatisfaction"].value_counts())
print("分數越高表示越滿意")
y=[]
x=[]
for Satisfy in listSatisfy:
    total = df[df["JobSatisfaction"] == Satisfy]
    print("對工作滿意程度(JobSatisfaction)是",Satisfy," 的有",total.shape[0]," 位")
    y.append(float(total.shape[0]))
    x.append(str(Satisfy))

# 平均
print("對工作滿意程度平均:",df["JobSatisfaction"].mean().round(2),"分")

print("=============工作角色=============")
#print(df["JobRole"].value_counts())
print("對照表:2:Nurse  3：Other  1:Therapist  4:Admin")
y=[]
x=[]
for JobRole in listJobRole:
    total = df[df["JobRole"] == JobRole]
    print("工作角色(JobRole)是",JobRole," 的有",total.shape[0]," 位")
    y.append(float(total.shape[0]))
    x.append(str(JobRole))

print("=============數據 標準化=============")
#   Pandas  x 轉 numpy
x=df.to_numpy()
print(x)

#  標準化 x
scaler = MinMaxScaler(feature_range=(0,1))      # 初始化 # 設定縮放的區間上下限
scaler.fit(x)                                   # 找標準化範圍
x= scaler.transform(x)                          # 把資料轉換
print("標準化:",x[:2])

# numpy 轉 Pandas
df = pd.DataFrame(x, columns=df.columns)

writer = ExcelWriter('資料清洗後標準化.xlsx', engine='xlsxwriter')      # 另存為資料清洗後
df.to_excel(writer, sheet_name='資料清洗後標準化',index=False,header=1)   # 分頁欄位的名稱 header=1 要印表頭
writer.save()





