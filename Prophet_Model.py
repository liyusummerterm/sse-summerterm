# -*- coding: utf-8 -*-
# 首先导入我们需要的包，fbprophet没多少包依赖，pandas是为了读入数据的，pyplot是用来绘图的，fbprophet也支持直接绘图
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
import pystan
model_code = 'parameters {real y;} model {y ~ normal(0,1);}'
model = pystan.StanModel(model_code=model_code)  # this will take a minute
y = model.sampling(n_jobs=1).extract()['y']
y.mean()  # should be close to 0

data = pd.read_csv('maxmin.csv')
data = data.sort_values(by=['date'])
data = data.reset_index()

# 对数据做格式转化，prophet所需要的只有两列，分别是ds和y，这里我分别预测未来一个月的最小值和最大值。
dfmin = pd.DataFrame()
dfmin['ds'] = data['date']
dfmin['y'] = data['tmin']
dfmax = pd.DataFrame()
dfmax['ds'] = data['date']
dfmax['y'] = data['tmax']
dfmax.head(10)

# 分别预测未来一个月的最低温度和最高温度，所以需要分别训练minModel和maxModel两个模型
minModel = Prophet()
minModel.fit(dfmin)
maxModel = Prophet()
maxModel.fit(dfmax)

futuremin = minModel.make_future_dataframe(periods=30)
futuremax = maxModel.make_future_dataframe(periods=30)
futuremin.tail()

fcmin = minModel.predict(futuremin)
fcmax = maxModel.predict(futuremax)
fcmin[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
# 这几个数据分别是预测日期，预测结果值，预测结果上下界。

fig0 = minModel.plot(fcmin)
fig1 = minModel.plot_components(fcmin)

fig2 = maxModel.plot(fcmax)
fig3 = maxModel.plot_components(fcmin)

plt.plot(fcmin['ds'].tail(30), fcmin['yhat'].tail(30))
plt.plot(fcmax['ds'].tail(30), fcmax['yhat'].tail(30))

