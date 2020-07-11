# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import tensorflow.keras.layers as layers
import datetime
from PyEMD import EMD
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential

class EmdLstmModel():
    
    def __init__(self, hp, series, task, filename):

        self.series = series # 输入的序列
        self.epochs = hp.epochs
        self.batch_size = hp.batch_size
        self.test_size = hp.test_size
        
        self.rnn_hedden_size = hp.rnn_hedden_size
        self.look_back = hp.look_back
        self.forward_days = hp.forward_days
        
        self.scaler_emd = MinMaxScaler(feature_range=(0,1))
        self.scaler_series = MinMaxScaler(feature_range=(0,1))
        
        self.X = self.get_emd_result(self.series)
        ''' 
        对x,y进行归一化 
        '''
        self.X = self.scaler_emd.fit_transform(self.X)
        
        self.y = self.series.reshape(-1, 1)
        self.y = self.scaler_series.fit_transform(self.y)
        self.y = self.y.flatten()
        

        self.lstm_input_shape = (hp.look_back,hp.emd_len)
        
        self.save_path = 'model/' + task + '/' + filename + '.h5'

        if os.path.exists(self.save_path):
            self.model = load_model(self.save_path)
        else:
            self.model = self.train_model()
            
    '''EMD 因式分解'''
    def get_emd_result(self, series):
        emd=EMD()
        emd.emd(series, None, 6)
        imfs, res = emd.get_imfs_and_residue()
        res = res.reshape(1,-1)
        return np.concatenate([imfs, res]).T

    '''创建lstm模型'''
    def create_model(self):
        model = Sequential([
            layers.LSTM(self.rnn_hedden_size,
                 input_shape=self.lstm_input_shape,
                 return_sequences=True),
            layers.LSTM(self.rnn_hedden_size),
            layers.Dense(self.forward_days)
        ])

        model.compile(loss='mean_squared_error',
                      optimizer='adam',
                      metrics=['mse','mae'])
        print("模型结构：\n")
        model.summary() 
        return model
    
    def sample_to_data(self, x, y, jump=1):

        # 拼接训练数据，以look_back的数据去预测后forward_days的数据
        X = []
        Y = []
        for i in range(0, len(x) - self.look_back - self.forward_days + 1, jump):
            X.append(x[i:(i + self.look_back)])
            Y.append(y[(i + self.look_back):(i + self.look_back + self.forward_days)])
        return np.array(X), np.array(Y)
    
    '''训练lstm模型'''
    def train_model(self):

        # 组成训练数据
        trian_X, train_y = self.sample_to_data(self.X, self.y)
        # 拿出一部分不去训练。用来检验算法性能
        X_train, X_validate, y_train, y_validate = train_test_split(trian_X,
                                                                    train_y,
                                                                  test_size=self.test_size)
        print("create train model")
        model = self.create_model()
        
        # keep the min loss model
        checkpoint = ModelCheckpoint(self.save_path,
                             monitor='val_loss',
                             verbose=0, 
                             save_best_only=True,
                             mode='min')

        print("fit and test model")
        model.fit(X_train, 
                    y_train,
                    epochs=self.epochs, 
                    validation_data=(X_validate, y_validate), 
                    callbacks=[checkpoint],
                    batch_size=self.batch_size)

        return model
    
    def model_predict(self, date):
        # 组成测试数据
        d1 = datetime.datetime.strptime('2020-7-7', '%Y-%m-%d')
        d2 = datetime.datetime.strptime(date, '%Y-%m-%d')

        d = d1 - d2

        X_test = self.X[-(self.look_back + d.days):(-d.days)]
        X_test = np.expand_dims(X_test, axis=0)
        y_predict = self.model.predict(X_test)
        y_predict = self.scaler_series.inverse_transform(y_predict.reshape(-1,1)).ravel()
        return y_predict
