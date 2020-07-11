# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os
from hyperparams import hp
from model import EmdLstmModel

def get_data(path,task):
    data = pd.read_csv(path)
    data = data.dropna(how = 'all')
    series = data[task].dropna(how = 'all')
    series=series.values.astype('float64')
    series = np.reshape(series,(series.shape[0]))
    return series

def get_predict(city, date):
    # 选择训练的数据
    path = "data/" + city + ".csv"
    tasks = ['TMAX', 'TMIN', 'TAVG', 'PRCP']
    for task in tasks :
        # 获取数据
        series = get_data(path, task)

        # emd lstm 建模
        tmax_EmdLstmModel = EmdLstmModel(hp, series, task, city)

        # 打印预测七天的结果
        print("打印" + task + "预测七天的结果")
        predict = tmax_EmdLstmModel.model_predict(date)
        print(predict)

path = 'data/'
pathlist = os.listdir(path)
for filename in pathlist:
    print(filename[:-4])
    get_predict(filename[:-4], '2020-3-6')