#%%
# Normalize
movie = {'naver': [2,4,6,8,10],
        'netflix':[1,2,3,4,5]
}
# %%
movie = pd.DataFrame(data=movie)
movie
# %%
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
min_max_movie = min_max_scaler.fit_transform(movie)
# %%
pd.DataFrame(min_max_movie, columns = ['naver','netflix'])
# %%
# Standard Scaling
# 평균과 표준편차가 1이 되도록 변환
from sklearn.preprocessing import StandardScaler
standard_scaler = StandardScaler()

x = np.arange(10)
print(x)
# outlier 추가
x[9] = 1000
print(x)
# %%
x.mean(), x.std()
# %%
scaled = standard_scaler.fit_transform(x.reshape(-1,1))
# %%
x.mean(), x.std()
# %%
scaled.mean(), scaled.std()
# %%
round(scaled.mean(),2), scaled.std()

# %%i
"""5/26"""a
# %%
