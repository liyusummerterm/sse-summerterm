# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:06:49 2020

@author: Zhusq

"""
import os
import numpy as np
import pandas as pd
from hyperparams import hp
from PyEMD import EMD
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import ModelCheckpoint
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

class EmdLstmModel():
    
    def __init__(self,hp,series,task):
        
        
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
        # 对x,y进行归一化
        self.X = self.scaler_emd.fit_transform(self.X)
        
        self.y = self.series.reshape(-1, 1)
        self.y = self.scaler_series.fit_transform(self.y)
        self.y = self.y.flatten()
        

        self.lstm_input_shape = (hp.look_back,hp.emd_len)
        
        if task == "tmax":
            self.save_path = 'model/tmax_lstm.h5'
        else:
            self.save_path = 'model/tmin_lstm.h5'
    
        if os.path.exists(self.save_path):
            self.model = load_model(self.save_path)
        else:
            self.model = self.train_model()
            
    '''EMD 因式分解'''
    def get_emd_result(self,series):
        emd=EMD()
        emd.emd(series)
        imfs, res = emd.get_imfs_and_residue()
        res = res.reshape(1,-1)
        return np.concatenate([imfs, res]).T

    '''创建lstm模型'''
    def create_model(self):
        model = Sequential()
        model.add(LSTM(self.rnn_hedden_size, 
                       input_shape=self.lstm_input_shape, 
                       return_sequences=True))
        model.add(LSTM(self.rnn_hedden_size))
        model.add(Dense(self.forward_days))
        model.compile(loss='mean_squared_error',
                      optimizer='adam',
                      metrics=['mse','mae'])
        print("模型结构：\n")
        model.summary() 
        return model
    
    def sample_to_data(self,x,y,jump=1):
        '''
        拼接训练数据，以look_back的数据去预测后forward_days的数据
        '''
        X = []
        Y = []
        for i in range(0, len(x) - self.look_back - self.forward_days + 1, jump):
            X.append(x[i:(i + self.look_back)])
            Y.append(y[(i + self.look_back):(i + self.look_back + self.forward_days)])
        return np.array(X), np.array(Y)
    
    '''训练lstm模型'''
    def train_model(self):

        # 组成训练数据
        trian_X, train_y = self.sample_to_data(self.X,self.y)
        # 拿出一部分不去训练。用来季检验算法性能
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
    
    def model_predict(self):
        # 组成测试数据
        X_test = [[self.X[-self.look_back:]]]
        y_predict = self.model.predict(X_test)
        y_predict = self.scaler_series.inverse_transform(y_predict.reshape(-1,1)).ravel()
        return y_predict
