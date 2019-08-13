import pandas as pd 
from sklearn.model_selection import train_test_split

#from sklearn.tree import DecisionTreeClassifier #決定機のインポート
from keras.models import Sequential
from keras.layers import Dense

##TesorBoard
#from datetime import datetime
#from tensorflow.keras.callbacks import Callback,TensorBoard
#logdir = "log/run-{}/".format(datetime.utcnow().strftime("%Y%m%d%H%M%S"))
#li_cb =[]
#li_cb.append(TensorBoard(log_dir=logdir,histogram_freq=1,write_graph=True,write_grads=True))

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
X=CSV_data.loc[:,['right','left']]
print(X)
#目的変数y=すべての行(:),3,4,5列目(2)
print("目的変数")
y=CSV_data.loc[:,['wa','sa','seki']]
print(y)

#学習データとテストデータへの分割
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

#ニューラルネット構築
print("構築")
model = Sequential()
model.add(Dense(6,input_dim=2,activation='relu'))
model.add(Dense(3,activation='relu'))
model.summary()
print(model.get_weights())

#学習
print("学習")
model.compile(loss='binary_crossentropy',
             optimizer='sgd',
             metrics=['accuracy'])

hist = model.fit(X_train , y_train,
                 epochs=200,
                 batch_size=64)
print("X_test:",X_test)
print("↓")
print("推論")
print(model.predict(X_test))
#正答率の計算
print("回答")
print("y_test:",y_test)
print("評価")
score=model.evaluate(X_test,y_test,verbose=0)
print("loss:",score[0])
print("acc :",score[1])
