##pandasをつかいこなそう

import pandas as pd

#CSVファイルをデータフレームとして読み込む
df = pd.read_csv("sample_pandas_6.csv")

#先頭から5行目までを表示
print(df.head())

# **①任意の値を加工**
#消費税10%を加算する関数
def tax(x):
    return x * 1.10

print(df['単価'].apply(tax))
#applyメソッド: 列や行に関数を適用する

# **型の変更**
type(df['発注日'].loc[0]) #str型(文字列)
df['発注日'] = pd.to_datetime(df['発注日']) #datetime型（日付）に変換

## **データを結合**
#新たな列をデータフレームに挿入することを「結合」と呼ぶ
#「結合」に便利なメソッド：concat
#pd.concat([元のデータフレーム, 結合するデータフレーム], axis=0 or 1)
#axis=0:行（縦）方向に結合、axis=1:列(横）方向に結合

tax_series = df['単価'].apply(tax) #消費税10%を加算したシリーズを作成
tax_seriesname = "単価（税込み）"
pd.concat([df,tax_series],axis=1)

# **データをマージしよう！**
#マージ:複数のデータフレームを共通の列を基準に結合すること(特定の値を基準に紐づける)
#pandas.merge(分析対象のデータフレーム, マージしたいデータフレーム[['一致させる要素の列名', '付随する列の名前']], how='inner', on='一致させる要素の列名')

#商品番号を基準に、商品カテゴリーのデータフレームとマージする
category_df = pd.read_csv('category.csv')
print(category_df)
df = pd.merge(df,category_df[['商品番号','カテゴリー']],how='inner',on='商品番号')
print(df)