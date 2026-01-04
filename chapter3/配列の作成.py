#NumPyを使用してみよう

#1．一次元配列の作成
import numpy as np
narray = np.array([0,1,2])
narray #narray([0,1,2])

type(narray) #numpy.ndarray 一次元配列の型
narray.size #3 サイズとは、配列の要素数のことを指す

nones = np.ones(10) #サイズが10の一次元配列を作成
nones #array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

#2.多次元配列の作成
multi_array = np.array([[0,1,2,],[3,4,5],[6,7,8,]])
multi_array #array([[0, 1, 2],
                    #[3, 4, 5],
                    #[6, 7, 8]]) 行列のようになる

