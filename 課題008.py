#課題_008

#サンプルデータの取得
from sklearn.datasets import load_wine
dataset = load_wine()

import pandas as pd 
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

df['category'] = dataset.target

#サンプルデータの分割
X = dataset.data
Y = dataset.target

from sklearn.model_selection import train_test_split
train_test_split(X,Y,test_size=0.2,random_state=5)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=5)

#予測モデルのインスタンス化(ランダムフォレスト)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=5)

#モデルの学習
model.fit(X_train, Y_train)

#モデルの予測
Y_pred = model.predict(X_test)

#モデルの評価
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y_test, Y_pred)

print(accuracy)