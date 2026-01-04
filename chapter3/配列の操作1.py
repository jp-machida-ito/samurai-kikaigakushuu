#配列の操作

import numpy as np
random_multi_array = np.random.randint(1, 10, (2,5))
random_multi_array #array([[3, 1, 7, 6, 2],
                            #[6, 1, 5, 2, 9]])
                            
#最大値
random_multi_array.max() #9

#最小値
random_multi_array.min() #1

#スライシング（ある位置からある位置までの配列を取得）
#1．まず一次元配列を作成
random_array = np.random.randint(1, 10, (10,))
random_array #array([2, 7, 9, 9, 4, 5, 8, 9, 9, 2])

random_array[0:3] #array([2,7,9])　先頭から3つの要素を取得

#配列の結合
a = np.array([1,2,3])#一次元
b = np.array([4,5,6])#一次元
np.concatenate((a,b)) #array([1,2,3,4,5,6])

a = np.array([[1,2,3]])#多次元
b = np.array([[4,5,6]])#多次元
np.concatenate((a,b),axis=0) #array([[1, 2, 3],
                                    #[4, 5, 6]])
