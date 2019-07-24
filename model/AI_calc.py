import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier #����@�̃C���|�[�g

#CSV�f�[�^�̓ǂݍ���
CSV_data=pd.read_csv('./file.CSV')
#�f�[�^�́i�s���A�񐔁j
print(CSV_data.shape)
#�f�[�^�̐擪10�s�\��
print(CSV_data.head(10))
#���v�ʂ̊m�F
print(CSV_data.describe())

#�����ϐ�X �� �ړI�ϐ�y�ւ̕���
#�����ϐ�X=���ׂĂ̍s(:),1��ڂ�2���([0,1])
X=CSV_data.iloc[:,[0,1]]
print(X)
#�ړI�ϐ�y=���ׂĂ̍s(:),3���(2)
y=CSV_data.values[:,2]
print(y)

#�w�K�f�[�^�ƃe�X�g�f�[�^�ւ̕���
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

#���ʋ@=�����
classifier=DecisionTreeClassifier()
#�w�K�I
classifier.fit(X_train,y_train)
#���f�����g�������_
print(X_test)
print("��")
print("���_",classifier.predict(X_test))
#�������̌v�Z
print("��",y_test)
print("����",classifier.score(X_test,y_test))