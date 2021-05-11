#%%
import numpy as np
import pandas as pd
train = pd.read_csv("train.csv")
# %%
train.info()
# %%
# 문자형 수치형으로 변환
def convert(data):
    if data == 'male':
        return 1
    elif data == 'female':
        return 0
# %%
train['Sex'].value_counts()
# %%
train['Sex'].apply(convert)
# %%
# Label encoder 이용 --> 문자형을 수치형으로 바꿔줌
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit_transform(train['Sex'])
train['Sex_num'] = le.fit_transform(train['Sex'])
# %%
train['Sex_num'].value_counts() 
# %%
le.classes_
# %%
le.inverse_transform([0,1,0,1,1])
# %%
# NAN 값이 포함되어 있으면, Label encoder가 정상동작하지 않음 결측치 제거해줘야함! 

# One hot encoding : 각 각의 값에 대해 독립성을 부여함/ 수치형 값의 관계를 끊어주어서 독립적인 형태로 바꿔줌
# 원핫인코딩은 카테고리(계절, 항구,...)의 특성을 가지는 column에 대해서 적용합니다.

# 결측치 처리
train['Embarked'].value_counts()
train['Embarked'] = train['Embarked'].fillna('S')
train['Embarked'].value_counts()
# %%
# le = LabelEncoder() 라벨 인코더를 사용하여 수치형으로 변환
train['Embarked_num'] = le.fit_transform(train['Embarked'])
train['Embarked_num'].value_counts()
# %%
# one hot encoding
one_hot = pd.get_dummies(train['Embarked_num'])
# %%
one_hot.columns = ['C','Q','S']
# %%
one_hot
# %%