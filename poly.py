# poly.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import pandas as pd
import numpy as np
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import matplotlib.dates as md

try:
    csv_name = str(input('請輸入要繪製成多項式線性迴歸線的CSV文件名稱：'))
    n = int(input("請輸入？次多項式迴歸："))

    df = pd.read_csv(os.path.join('./csvFile', csv_name+'.csv'))
    df['date'] = pd.to_datetime(df['date'])
    # print(df.dtypes)

    x = np.zeros(df['close_price'].size)
    for i in range(df['close_price'].size):
        x[i] = i
    x = x.reshape(x.size, 1)
    y = np.array([df['close_price'][::-1]])[-1]
    # print(x.shape,y.shape)

    model = pl.make_pipeline(sp.PolynomialFeatures(n), lm.LinearRegression())
    model.fit(x, y)
    pred_y = model.predict(x)
    print(n, '次多項式迴歸')
    print('R平方為：', sm.r2_score(y, pred_y))

    mp.figure(csv_name + ' ' + 'Polynomial Regression', facecolor='lightgray')
    mp.title(csv_name + '\n' + 'Polynomial Regression', fontsize=20)
    mp.rcParams['figure.figsize'] = (20.0, 10.0) 
    mp.xlabel('Date', fontsize=14)
    mp.ylabel('Close', fontsize=14)
    ax = mp.gca()
    # 設置水平坐標每三個月為主刻度
    ax.xaxis.set_major_locator(md.MonthLocator(range(1, 12, 3)))
    # 設置水平坐標每一個月為次刻度
    ax.xaxis.set_minor_locator(md.MonthLocator())
    # 設置水平坐標主刻度標籤格式
    ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
    mp.tick_params(labelsize=10)
    mp.grid(linestyle=':')
    mp.plot(df['date'], df['close_price'], c='lightgray', label='Close Price')
    mp.plot(df['date'][::-1], pred_y,  c='dodgerblue', label='Regression')
    mp.legend()
    mp.gcf().autofmt_xdate()
    mp.show()
except OSError:
    print('找不到此CSV文件')
except ValueError:
    print('請輸入正確的數字')