#%%
import numpy as np
import pandas as pd
train = pd.read_csv("train.csv")
# %%
train.head()
# %%
# 전처리: train / validation 세트 나누기
# 1. feature와 label을 정의
# 2. 적절한 비율로 train /validation set 나눈다.

feature =[
    'Pclass','Sex','Age','Fare'
]

label = [
    'Survived'
]

# %%
train[feature].head()
# %%
train[label].head()
# %%
from sklearn.model_selection import train_test_split
# %%
# return 받는 데이터 순서가 중요
x_train, x_valid, y_train, y_valid = train_test_split(train[feature], train[label], test_size=0.2, shuffle=True, random_state=30)
# %%
x_train.shape, y_train.shape
# %%
x_valid.shape, y_valid.shape
# %%

train.info()
# %%
#결측치 개수 확인
train.isnull().sum()
# %%
#개별 컬럼 결측치 확인
train['Age'].isnull().sum()
# %%
# 수치형 데이터에 대한 결측치 처리
# 0으로 넣기
train['Age'].fillna(0).describe()
# %%
# 수치형 데이터에 대한 결측치 처리
# 평균으로 넣기
train['Age'].fillna(train['Age'].mean()).describe()
# %%
# 한번에 fit & transform 해서 데이터 결측치 없애는 법
from sklearn.impute import SimpleImputer
train = pd.read_csv('train.csv')
imputer = SimpleImputer(strategy='median')
result = imputer.fit_transform(train[['Age','Pclass']])
train[['Age','Pclass']] = result
train[['Age','Pclass']].isnull().sum()
# %%

# %%
# 문자형 데이터에 대한 결측치 처리
imputer = SimpleImputer(strategy='most_frequent')
result = imputer.fit_transform(train[['Embarked','Cabin']])
train[['Embarked','Cabin']] = result
train[['Embarked','Cabin']].isnull().sum()

# %%
