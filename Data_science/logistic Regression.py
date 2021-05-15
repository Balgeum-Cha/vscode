#%%
# Logistic Regression
# 독립 변수의 선형 결합을 이용하여 사건의 발생가능성을 예측하는데 사용되는 통계 기법
# Logistic Regression, 서포트벡터 머신과 같은 알고리즘은 이진 분류만 가능함(2개의 클래스 판별만 가능함)
# 3개 이상의 클래스에 대한 판별 진행은 아래와 같은 전략으로 판별
# one vs rest (O v R): K개의 클래스가 존재할 때, 1개의 클래스를 제외한 다른 클래서 K개 만들어, 각각의 이진 분류에 대한 확률을 구하고, 총합을 통해 최종 클래스를 판별
# one vs one(O v O ) : 4개의 계절을 구분하는 클래스가 존재한다고 가정했을 떄, 0vs1, 0vs2, 0vs3, ...2vs3 까지 가장 많이 양성으로 선택된 클래스 판별
# 대부분 O v R 전략을 사용
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression


# %%
# 모델 선언
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris = load_iris()
data = iris['data']
feature_names = iris['feature_names']
target = iris['target']
df_iris = pd.DataFrame(data, columns = feature_names)
df_iris['target'] = target
from sklearn.model_selection import train_test_split
x_train, x_valid, y_train, y_valid  = train_test_split(df_iris.drop('target',1),df_iris['target'],stratify=df_iris['target'])
sns.countplot(y_train)

model= LogisticRegression()
# %%
# 모델 학습
model.fit(x_train, y_train)
# %%
prediction = model.predict(x_valid)
# %%
prediction[:5]
# %%
(prediction == y_valid).mean()
# %%
