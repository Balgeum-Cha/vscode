#%%
import warnings
warnings.filterwarnings('ignore')
import pandas as pd


# %%
from sklearn.datasets import load_iris
iris = load_iris()
print(iris['DESCR'])
# %%
data = iris['data']
data[:5]
# %%
feature_names = iris['feature_names']
feature_names
# %%
target = iris['target']
iris['target_names']
# %%
df_iris = pd.DataFrame(data, columns = feature_names)
df_iris.head()
# %%
df_iris['target'] = target
df_iris.head()
# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot('sepal width (cm)','sepal length (cm)',hue='target',palette='muted',data=df_iris)
plt.title('Sepal')
plt.show()
# %%
sns.scatterplot('petal width (cm)','petal length (cm)', hue ='target', palette='muted',data = df_iris)
plt.title('Petal')
plt.show()
# %%
# 3d 그래프 PCA (차원 축소 그래프)
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

fig = plt.figure(figsize=(8,6))
ax = Axes3D(fig, elev = -150, azim= 110)
X_reduced = PCA(n_components = 3).fit_transform(df_iris.drop('target',1))
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=df_iris['target'],
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("Iris 3D")
ax.set_xlabel("x")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("y")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("z")
ax.w_zaxis.set_ticklabels([])

plt.show()
# %%
from sklearn.model_selection import train_test_split
x_train, x_valid, y_train, y_valid  = train_test_split(df_iris.drop('target',1),df_iris['target'])
# %%
x_train.shape, y_train.shape
# %%
x_valid.shape, y_valid.shape
# %%
sns.countplot(y_train)
# %%
# stratify : 훈련/ 테스트 데이터들이 원래의 input dataset의 클래스의 비율과 같은 비율을 가지도록 할 것인지 지정한다.  
x_train, x_valid, y_train, y_valid  = train_test_split(df_iris.drop('target',1),df_iris['target'],stratify=df_iris['target'])
# %%
sns.countplot(y_train)
# %%
# %%
# 내일은 공부하기!