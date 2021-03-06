from __future__ import print_function
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Embedding
from keras.layers import LSTM, SimpleRNN, GRU
from keras.datasets import imdb
from keras.utils.np_utils import to_categorical
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error)
from sklearn import metrics
from sklearn.preprocessing import Normalizer
import h5py
from keras import callbacks
from keras.callbacks import CSVLogger
import keras
import keras.preprocessing.text
import itertools
from keras.callbacks import CSVLogger
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, CSVLogger
from keras import callbacks

#trainlabels = pd.read_csv('dgcorrect/trainlabel.csv', header=None)

#trainlabel = trainlabels.iloc[:,0:1]

#testlabels = pd.read_csv('/home/spark/vinay/code1/dgcorrect/testlabel.csv', header=None)

#testlabel = testlabels.iloc[:,0:1]


#train = pd.read_csv('dgcorrect/train.txt', header=None)
#test = pd.read_csv('/home/spark/vinay/code1/dgcorrect/test1.txt', header=None)


#X = train.values.tolist()
#X = list(itertools.chain(*X))


#T = test.values.tolist()
#T = list(itertools.chain(*T))


import sys
da = sys.argv[1]

df = pd.DataFrame([x.split(';') for x in da.split('\n')])

T = df.values.tolist()
T = list(itertools.chain(*T))


#T = list(da)


 # Generate a dictionary of valid characters
#valid_chars = {x:idx+1 for idx, x in enumerate(set(''.join(X)))}

#max_features = len(valid_chars) + 1
#maxlen = np.max([len(x) for x in X])
#print(maxlen)
# Convert characters to int and pad
#X = [[valid_chars[y] for y in x] for x in X]


#X_train = sequence.pad_sequences(X, maxlen=maxlen)

max_len = 37
# Generate a dictionary of valid characters
valid_chars = {x:idx+1 for idx, x in enumerate(set(''.join(T)))}

max_features = 38
print(max_features)
maxlen = np.max([len(x) for x in T])
#print(maxlen)
# Convert characters to int and pad
T = [[valid_chars[y] for y in x] for x in T]


X_test = sequence.pad_sequences(T, maxlen=max_len)


#y_train = np.array(trainlabel)
#y_test = np.array(testlabel)

print(X_test)

embedding_vecor_length = 128

model = Sequential()
model.add(Embedding(max_features, embedding_vecor_length, input_length=max_len))
model.add(GRU(128))
model.add(Dropout(0.1))
model.add(Dense(1))
model.add(Activation('sigmoid'))

'''
model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
checkpointer = callbacks.ModelCheckpoint(filepath="logs/gru/checkpoint-{epoch:02d}.hdf5", verbose=1, save_best_only=True, monitor='val_acc',mode='max')
csv_logger = CSVLogger('logs/gru/training_set_gruanalysis.csv',separator=',', append=False)
model.fit(X_train, y_train, batch_size=32, nb_epoch=1000,validation_split=0.33, shuffle=True,callbacks=[checkpointer,csv_logger])


score, acc = model.evaluate(X_test, y_test, batch_size=128)
print('Test score:', score)
print('Test accuracy:', acc)
'''

# try using different optimizers and different optimizer configs
model.load_weights("logs/lstm/checkpoint-01.hdf5")


y_pred = model.predict_classes(X_test)
print(y_pred)

print(X_test.shape)


'''
y_pred = model.predict(X_test)
np.savetxt('res/gru.csv', y_pred)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred , average="binary")
precision = precision_score(y_test, y_pred , average="binary")
f1 = f1_score(y_test, y_pred, average="binary")

print("confusion matrix")
print("----------------------------------------------")
#print("accuracy")
#print("%.3f" %accuracy)
#print("racall")
#print("%.3f" %recall)
#print("precision")
#print("%.3f" %precision)
#print("f1score")
#print("%.3f" %f1)


cm = metrics.confusion_matrix(y_test, y_pred)
print("==============================================")
print(cm)
tp = cm[0][0]
fp = cm[0][1]
tn = cm[1][1]
fn = cm[1][0]
print("tp")
print(tp)
print("fp")
print(fp)
print("tn")
print(tn)
print("fn")
print(fn)

print("LSTM acc")
Acc = float(tp+tn)/float(tp+fp+tn+fn)
print(Acc)
print("precision")
prec = float(tp)/float(tp+fp)
print(prec)
print("recall")
rec = float(tp)/float(tp+fn)
print(rec)
print("F-score")
fs = float(2*tp)/float((2*tp)+fp+fn)
print(fs)

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
loss, accuracy = model.evaluate(X_test, y_test)
print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy*100))
'''



