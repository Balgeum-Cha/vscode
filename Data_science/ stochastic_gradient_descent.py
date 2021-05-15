#%%
# stochastic gradient descent = 확률적 경사하강법
from IPython.display import Image
from sklearn.linear_model import SGDClassifier
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
#모델선언
sgd = SGDClassifier()
#모델학습
sgd.fit(x_train,y_train)
#모델예측
prediction = sgd.predict(x_valid)
(prediction == y_valid).mean()
# %%
# %%