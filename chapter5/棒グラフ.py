#棒グラフ

import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

x = np.array([1,2,3,4,5])
y = np.array([100,120,150,200,160])

label = (["昆布","梅","鮭","ツナマヨ","すじこ"])
plt.title("おにぎりの具ごとの値段")

plt.bar(x,y,tick_label=label)
#tick_labelは、plt.bar()メソッドの設定項目。目盛りの名札を意味する

plt.show()