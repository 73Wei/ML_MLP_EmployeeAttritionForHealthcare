#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "WCH"

import pandas as pd
import numpy as np
import myfun_healthcare
import itertools
from pandas import ExcelWriter  # 匯入 excel writer

# 參考資料 https://www.kaggle.com/datasets/jpmiller/employee-attrition-for-healthcare

df1 = pd.read_excel("watson_healthcare_modified.xlsx")
print(df1.columns)                              # 全部欄位名稱

# 找尋是否有空的資料並且刪掉
myfun_healthcare.pandas_nan_col_刪掉表單內空值(df1)

# 替代內容 Administrative(行政的) = Admin(行政)
#df1=myfun_healthcare.pandas_替換(df1,"Administrative","Admin")
#print(df1["JobRole"][350:])

# 先看各欄位資料型態
print(df1.dtypes,df1.shape)
# 把欄位轉成數字
###  指定轉換內容
df1['Attrition'] = [1 if each == 'Yes' else 0 for each in df1['Attrition']]
df1['Gender'] = [1 if each == 'Male' else 0 for each in df1['Gender']]
df1['OverTime'] = [1 if each == 'Yes' else 0 for each in df1['OverTime']]

### 把其他文字型態的欄位列成表單
listobject=["BusinessTravel","Department","EducationField","JobRole","MaritalStatus"]


###  透過迴圈轉換成數字
#df["Category2"] = pandas_col_StingToInt(df,"Category")
n=0
for i in range(len(listobject)):
    df1[""+listobject[n]+""]=myfun_healthcare.pandas_col_StingToInt(df1,""+listobject[n]+"")
    n=n+1

###  印出每一行的質和數量
n=0
for i in range(len(listobject)):
    r=print(df1[""+listobject[n]+""].max())

print(df1.head())

## 按照年齡排好
#df1=df1.sort_values(by="Age")

## 寫入Excel
writer = ExcelWriter('healthcare_資料清洗後.xlsx', engine='xlsxwriter')      # 另存為資料清洗後
df1.to_excel(writer, sheet_name='healthcare_資料清洗後',index=False,header=1)   # 分頁欄位的名稱 header=1 要印表頭
writer.save()




