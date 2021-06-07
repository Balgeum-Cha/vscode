#%%
import numpy as np
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
list2 = [1,2,'test']
array2 = np.array(list2)
print(array2, array2.dtpye)
# %%
pip install pycaret-nightly
# %%
