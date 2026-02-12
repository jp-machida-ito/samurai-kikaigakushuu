#pandasをつかいこなそう！

import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample_pandas_6.csv")
#read_csv()メソッド：CSVファイルを読み込むPandas専用の機能

#①先頭から5行目までを表示
print(df.head())
#head()メソッド：最初の5行だけを表示させるPandas専用機能
#最初の10行を表示したいなら、head(10)になる

#②先頭から2番目にある「Z4WOOIYV」という商品番号の行のみ取得
print(df.query('商品番号 == "Z4WOOIYV"')) #クォーテーションで囲む必要あるので、外と中で種類を分けましょう

#③600円の行のみ抽出
print(df.query('単価 == 600'))

#④在庫数が5個以下の行を取得
print(df.query('在庫 <= 5'))

#⑤在庫が5個以下　且つ　「8T7D5DQA」という商品番号を取得
print(df.query('在庫 <=5 and 商品番号 == "8T7D5DQA"'))