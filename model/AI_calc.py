import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier #決定機のインポート

#CSVデータの読み込み
CSV_data=pd.read_csv('./file.CSV')
#データの（行数、列数）
print(CSV_data.shape)
#データの先頭10行表示
print(CSV_data.head(10))
#統計量の確認
print(CSV_data.describe())

#説明変数X と 目的変数yへの分割
#説明変数X=すべての行(:),1列目と2列目([0,1])
X=CSV_data.iloc[:,[0,1]]
print(X)
#目的変数y=すべての行(:),3列目(2)
y=CSV_data.values[:,2]
print(y)

#学習データとテストデータへの分割
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

#識別機=決定木
classifier=DecisionTreeClassifier()
#学習！
classifier.fit(X_train,y_train)
#モデルを使った推論
print(X_test)
print("↓")
print("推論",classifier.predict(X_test))
#正答率の計算
print("回答",y_test)
print("結果",classifier.score(X_test,y_test))