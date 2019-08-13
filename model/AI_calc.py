import pandas as pd 
from sklearn.model_selection import train_test_split

#from sklearn.tree import DecisionTreeClassifier #決定機のインポート
from keras.models import Sequential
from keras.layers import Dense

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
print("説明変数")
X=CSV_data.iloc[:,[0,1]]
print(X)
#目的変数y=すべての行(:),3列目(2)
print("目的変数")
y=CSV_data.values[:,2]
print(y)

#学習データとテストデータへの分割
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

#ニューラルネット構築
print("構築")
model = Sequential()
model.add(Dense(3,activation='relu',input_dim=2))
model.add(Dense(3,activation='relu'))
print(model.get_weights())

#学習
print("学習")
model.compile(loss='binary_crossentropy',
             optimizer='sgd',
             metrics=['accuracy'])

hist = model.fit(X_train , y_train,
                 epochs=200,
                 batch_size=64)
#print(X_test)
#print("↓")
#print("推論",classifier.predict(X_test))
#正答率の計算
#print("回答",y_test)
#print("結果",classifier.score(X_test,y_test))
