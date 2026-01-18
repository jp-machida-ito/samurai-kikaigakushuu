#箱ひげ図

import matplotlib.pyplot as plt
import japanize_matplotlib #日本語表示

#例）モーターの周波数の箱ひげ図を作る場合
hertz = [300,200,200,500,600,2000,1600,1800,1850,1700,1500,1500,1400,5000,6000,2000]

#箱ひげ図
plt.boxplot(hertz)

#日本語でタイトルを設定する
plt.title("モーター音の周波数")

#描画
plt.show()