#円グラフ

import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib 

#円グラフを描画

x = np.array([30,40,30])
#npの配列にしておけば、倍数計算とか楽！！単なるリストだと要素を繰り返すだけ！！

label = ["いぬ","ねこ","とり"]
plt.title("好きな動物")

plt.pie(x,labels=label)
#①plt.pie()メソッドが、裏側で％計算をしてくれる
#②左側のlabelsは、pieメソッドが持っている設定項目の名前。右側のlabelは変数

plt.show()