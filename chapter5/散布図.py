#散布図

import matplotlib.pyplot as plt
import numpy as np

#データを生成する
np.random.seed(3)
#seed()とは、乱数の再現ボタン。
#コンピューターでは、「完全なでたらめ」を作るのが苦手。
#代わりに、複雑な数式を使って、ランダムっぽく見える数字を順番に作っている

#seed(3)の意味は、
#「3番の台本を選ぶ」というイメージ。「3番の台本に従って、数字を出してね！」

x = 4 + np.random.normal(0,2,60) #平均が0、標準偏差5の標準正規分布から60個の乱数の生成
y = 4 + np.random.normal(0,2,len(x)) #平均が0、標準偏差5の標準正規分布からxと同じ数の乱数の生成

#np.random.normal(平均,標準偏差,個数)　←numpyのrandomという場所に所属しているメソッド
#指定した平均とバラツキ具合を持つランダムな数字の集まりを作る

#プロットする
plt.scatter(x,y)
plt.show()
