# -*- coding: utf-8 -*-

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

def get_predict(filename):
    # 选择训练的数据
    path = "data/" + filename + ".csv"
    tasks = ['TMAX', 'TMIN', 'TAVG', 'PRCP']
    for task in tasks :
        # 获取数据
        series = get_data(path, task)

        # emd lstm 建模
        tmax_EmdLstmModel = EmdLstmModel(hp, series, task, filename)

        # 打印预测七天的结果
        print("打印" + task + "预测七天的结果")
        predict = tmax_EmdLstmModel.model_predict()
        print(predict)
        np.savetxt('predict_max.csv', predict, delimiter=',')

