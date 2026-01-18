#ヒストグラム

import numpy as np
import matplotlib.pyplot as plt

#平均が15、標準偏差5の標準正規分布から2000個の乱数の生成
x = np.random .normal(15,5,2000)

#np.random.normal(平均,標準偏差,個数)　←numpyのrandomという場所に所属しているメソッド
#指定した平均とバラツキ具合を持つランダムな数字の集まりを作る

#ヒストグラムをプロット
plt.hist(x,bins=30)
#hist()メソッドでは、デフォルトで棒（bins）の数が10本
#細かい特徴を把握したい場合は、bins=30のように棒を増やしてあげるといい

plt.show()