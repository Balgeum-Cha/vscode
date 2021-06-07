#%%
from typing import Sequence
import numpy as np
import pandas as pd
array1 = np.array([1,2,3])
print('array1 type;',type(array1))
print('array1 type 형태 :', array1.shape)
array2 = np.array([[1,2,3],[2,3,4]])
print('array2 type:',type(array2))
print('array2 type 형태 :', array2.shape)
array3 = np.array([[1,2,3]])
print('array3 type:',type(array3))
print('array3 type 형태 :', array3.shape)

# array1은 1차원 , array2, array3 은 2차원임을 확인할 수 있음. [] 은 1차원 [[]]은 2차원임.
# %%
import numpy as np
list1 = [1,2,'test']
array4 = np.array(list1)
print(array4)
# 데이터 타입이 더 큰 데이터 타입으로 변환됨
# %%
# %%
# 특정 크기와 차원을 가진 ndarray를 연속값이나, 0, 1 로 초기화해 쉽게 생성해야할 경우,
# arrang(),, zeros(), ones()를 이용해 쉽게 ndarray 생성가능 
sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)
# %%
# 0 생성
zero_array = np.zeros((3,2),dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)
# %%
one_array = np.ones((3,2))
print(one_array)
print(one_array.dtype, one_array.shape)
# %%
