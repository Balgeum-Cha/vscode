#%%
import numpy as np
from sklearn.linear_model import LinearRegression

# %%
x = np.arange(10).reshape(-1,1)
y = (2*x + 1).reshape(-1,1)
# %%
x
# %%
y
# %%
# 모델 선언
model = LinearRegression()
# %%
model
# %%
# 학습
model.fit(x,y)
# %%
prediction = model.predict([[10]])
# %%
prediction
# %%
