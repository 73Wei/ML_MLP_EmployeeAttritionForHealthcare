#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "WCH"

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from pandas import ExcelWriter  # 匯入 excel writer
import myfun_healthcare
myfun_healthcare.matplot_中文字()
import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("TKAgg")
"""
資料來源　https://reurl.cc/rRo5ob
參考資料 https://reurl.cc/kEkX99
"""
df = pd.read_excel('watson_healthcare_modified.xlsx',0)
print(df.columns)                              # 全部欄位名稱
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

########
plt.figure(figsize=(10,8))
sns.countplot(x='Age',hue='Attrition',data=df)
plt.xlabel("Age")
plt.ylabel("Attrition")
plt.title("Age & Attrition")
plt.savefig("Age_Attrition.png")
plt.show()


sns.violinplot(data=df, x="Gender", y='Age', hue='Attrition')
plt.savefig("violinplot.png")
plt.show()

print("============= 性別 =============")
#print(df["Gender"].value_counts())

y=[]
x=[]

for Gender in listGender:
    total = df[df["Gender"] == Gender]
    y.append(float(total.shape[0]))
    x.append(str(Gender))
    print("性別(Gender)是",Gender," 的有",total.shape[0]," 位")

########
sns.displot(data=df, x="Gender", hue="MaritalStatus", multiple="stack")
plt.title("Gender & MaritalStatus")
plt.subplots_adjust(left=0.146, bottom=None, right=None, top=0.9, wspace=None, hspace=None)  #  調整上面的 出血邊
plt.savefig("Gender_MaritalStatus.png")
plt.show()

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

y=[]
x=[]
for JobRole in listJobRole:
    total = df[df["JobRole"] == JobRole]
    print("工作角色(JobRole)是",JobRole," 的有",total.shape[0]," 位")
    y.append(float(total.shape[0]))
    x.append(str(JobRole))

############
sns.relplot(data=df, x="DistanceFromHome", y="MonthlyIncome", hue="JobRole",col="Gender")
plt.xlabel("Distance From Home")
plt.ylabel("Monthly Income")
#plt.title("DistanceFromHome & MonthlyIncome")
plt.subplots_adjust(left=0.1, bottom=None, right=None, top=0.9, wspace=None, hspace=None)  #  調整上面的 出血邊
plt.savefig("DistanceFromHome_MonthlyIncome.png")
plt.show()


############
sns.relplot(
    data=df, x="TotalWorkingYears", y="PercentSalaryHike", col="Department",
    hue="Gender", kind="line")
plt.savefig("PercentSalaryHike.png")
plt.show()

############
sns.pairplot(df, hue="Attrition")
plt.savefig("pairplot.png")
plt.show()