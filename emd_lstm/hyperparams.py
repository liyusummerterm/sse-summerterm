# -*- coding: utf-8 -*-

class hp:

    '''
    train_data = './data/maxmin.csv'
    '''

    # 选取多少百分比的数据做预测数据
    # 来评估算法性能
    test_size = 0.2
    
    # 通过后几天的数据来做预测
    look_back = 20
    # 预测几天的数据
    forward_days = 7
    
    epochs = 50
    batch_size = 512
    
    # emd 子序列长度
    emd_len = 7
    
    # lstm dim
    rnn_hedden_size = 200

'''
    # columns name
    first_task = "tmax"
    next_task = "tmin"
'''