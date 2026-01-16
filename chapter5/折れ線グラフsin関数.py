#折れ線グラフ②　sin関数

import matplotlib.pyplot as plt
import numpy as np

#データを作成

x = np.linspace(0,10,100) 
#linspaceメソッド→（スタート、ストップ、分割数）
#今回の場合だと、0から10までの幅で配列を100個作成

y = 2 + 2 * np.sin(2*x)

#プロット
fig, ax = plt.subplots() #これから絵を描くためのキャンバス（fig)と画用紙（ax)を用意

ax.plot(x, y, linewidth=2.0)
#100個の（x,y)の点を繋いで線にする

ax.set(xlim = (0,10),xticks=np.arange(0,10),
       ylim = (-1,5),yticks=np.arange(-1,6))
#ax.set() →　画用紙のどの範囲を映すか決める
#xlim = (0,10) →　横軸は0から10まで見えるようにする
#xticks= np.arange(0,10) →　横軸のメモリを0，1，2と1ずつ増やす

#arange()　と　linespace()の違い

#＊＊　np.linespace(0,10,100) ＊＊
#0から10の間を100個に等分して！という命令
#分割数は決まっているので、間隔は中途半端になる

# ** np.arange(0,10)**
#0から始めて10になるまで1ずつ増やして！という命令
#分割数が何個かになるよりも、「キリよく1ずつ増やす」という間隔を優先

plt.show()