# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:51:16 2020

@author: Zhusq

"""
import pandas as pd
import numpy as np
from hyperparams import hp
from model import EmdLstmModel

def get_data(path,task):
    data = pd.read_csv(hp.train_data)
    data = data.dropna()
    series = data[task]
    series=series.values.astype('float64')
    series = np.reshape(series,(series.shape[0]))
    return series


# 选择训练的数据
path = "data/maxmin.csv"
task  = "tmax"

# 获取数据
series = get_data(path,task)

# emd lstm 建模
tmax_EmdLstmModel = EmdLstmModel(hp,series,task)

# 打印预测七天的结果
print("打印tmax预测七天的结果")
print(tmax_EmdLstmModel.model_predict())


task = "tmin"

# 获取数据
series = get_data(path,task)

# emd lstm 建模
tmin_EmdLstmModel = EmdLstmModel(hp,series,task)

# 打印预测七天的结果
print("打印tmin预测七天的结果")
print(tmin_EmdLstmModel.model_predict())
