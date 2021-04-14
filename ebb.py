# ebb.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as md

try:
    csv_name = str(input('請輸入要繪製成布林帶的CSV文件名稱：'))
    ema_days = int(input('請輸入指數加權移動平均線的天數：'))
    stds_n = float(input('請輸入均線上下？個標準差：'))

    df = pd.read_csv(os.path.join('./csvFile', csv_name+'.csv'))
    df['date'] = pd.to_datetime(df['date'])
    # print(df.dtypes)
        
    weights = np.exp(np.linspace(-1, 0, ema_days))
    weights /= weights.sum()
    medios = np.convolve(df['close_price'][::-1], weights[::-1], 'valid')
    stds = np.zeros(medios.size)
    for i in range(stds.size):
        stds[i] = df['close_price'][::-1][i:i+ema_days].std()
    lowers = medios - stds*stds_n
    uppers = medios + stds*stds_n
    
    mp.figure(csv_name + ' ' + 'Exponential Moving Average Bollinger Bands', facecolor='lightgray')
    mp.title(csv_name + '\n' + 'Exponential Moving Average Bollinger Bands', fontsize=20)
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
    mp.plot(df['date'][::-1][ema_days-1:], medios, c='dodgerblue', label='Medio'+'(EMA'+str(ema_days)+')')
    mp.plot(df['date'][::-1][ema_days-1:], lowers, c='limegreen', label='Lower')
    mp.plot(df['date'][::-1][ema_days-1:], uppers, c='orangered', label='Upper')
    mp.legend()
    mp.gcf().autofmt_xdate()
    mp.show()
except OSError:
    print('找不到此CSV文件')
except ValueError:
    print('請輸入正確的數字')