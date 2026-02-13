#scikit-learn
#お手軽機械学習ライブラリ。データセットの取得、前処理、モデルの構築、評価などが簡単に行える。
#データセットモジュールが多数あり、自身でCSVを用意しなくても、サンプルデータを簡単に取得できる。

# ＊＊1．サンプルデータの取得＊＊
from sklearn.datasets import load_wine 
dataset = load_wine()
#print(dataset.feature_names) #特徴量の名前を表示

#データを見やすくするために、pandasのDataFrameに変換
import pandas as pd
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

df['category'] = dataset.target #ワインの種別はdataset.targetに格納されている。これをDataFrameの新しい列として追加

#print(df.head()) #データの先頭5行を表示
#print(df.shape) #データの行数と列数を表示

# ＊＊2．サンプルデータの分割＊＊
X = dataset.data #説明変数（ワインの成分）
Y = dataset.target #目的変数（ワインの種別）

from sklearn.model_selection import train_test_split #データ分割用の関数をインポート

train_test_split(X,Y,test_size=0.3,random_state=5) #データを訓練用とテスト用に分割。
#test_size=0.3はデータの30%をテスト用に使用することを指定。random_state=5は乱数のシード値を設定し、結果の再現性を確保。

#説明変数Xの学習データ、説明変数Xのテストデータ、目的変数Yの学習データ、目的変数Yのテストデータをそれぞれ取得
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=5)

#print(X.shape,X_train.shape,X_test.shape) #データの形状を表示
#print(Y.shape,Y_train.shape,Y_test.shape) #データの形状を表示

# ＊＊3．予測モデルのインスタンス化＊＊
#今回は予測モデルとして、決定木（Decision Tree）を使用
from sklearn.tree import DecisionTreeClassifier #決定木の分類器をインポート
model = DecisionTreeClassifier(random_state=5) #モデルのインスタンスを作成。random_state=5で乱数のシード値を設定

# ＊＊4．モデルの学習＊＊
model.fit(X_train,Y_train) #学習データを使ってモデルを学習

# ＊＊5．モデルの予測＊＊
#説明変数ｘ（ワインの成分）のテストデータに基づいてワインの種別を予測した値と
#目的変数Y（ワインの種別）のテストデータがどれだけマッチしているかを確認

#まず、説明変数Xのテストデータからワインの種別を予測
Y_pred = model.predict(X_test)
#print(Y_pred) #予測結果を表示
#print(Y_test) #実際のワインの種別を表示

#モデルの評価
from sklearn.metrics import accuracy_score #精度評価用の関数をインポート
accuracy_score(Y_test,Y_pred) #予測結果と実際の値を比較して精度を計算

#　＊＊6．予測＊＊
#新しいデータに基づいてワインの種別を予測！種別不明のワインについて成分データから、種別の予測を行う。
import numpy as np
X_new = np.array([
    [13,1.6,220,100,2.5,2.6,0.3,1.5,5,1.04,3.4,0.9,750],
    [12,2.0,180,90,2.0,2.0,0.2,1.2,4,0.99,2.5,0.6,680],
    [14,1.5,250,110,3.0,3.0,0.4,1.8,6,1.10,4.0,1.0,800]
])

print(model.predict(X_new)) #新しいデータに基づいてワインの種別を予測