#課題データフレームからグラフ表示と基本統計量を求めよう

#必要なライブラリのインポート
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

#CSVファイルの読込（データフレーム）
df = pd.read_csv("sample_pandas_6.csv")

#カテゴリーCSVをマージ
category_df = pd.read_csv('category.csv')
df = pd.merge(df,category_df[['商品番号','カテゴリー']],how='inner',on='商品番号')

#＊＊1．カテゴリー列の要素の出現頻度をカウント＊＊
category_df = df['カテゴリー'].value_counts()
print(category_df)

#棒グラフの作成
plot = category_df.plot.bar(
    x='カテゴリー',
    y='注文数',
    title='カテゴリーごとの数量',
    xlabel='カテゴリー',
    ylabel='注文数',
    rot = 45 #x軸のラベルを45度回転させる(見やすいようにするため)
)

plt.show()

#＊＊2．商品番号列の商品番号ごとに基本統計量を求める＊＊
#商品番号ごとに注文数の統計量をだす
stats_by_product = df.groupby(['商品番号'])['注文数'].describe()
#Pandas groupby: groupby_obj['列名']　→　列名でデータを抽出
#上記の為、商品番号という箱（obj）から注文数のデータを取り出せている。

print(stats_by_product)