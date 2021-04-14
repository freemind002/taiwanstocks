# kdj.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md

try:
    csv_name = str(input('請輸入要繪製成KDJ線的CSV文件名稱：'))
    rsv_days = int(input('請輸入RSV的參數：'))

    df = pd.read_csv(os.path.join('./csvFile', csv_name+'.csv'))
    df['date'] = pd.to_datetime(df['date'])
    # print(df.dtypes)
    
    # 未成熟隨機值RSV
    rsvs = np.zeros(df['close_price'].size-(rsv_days-1))
    for i in range(rsvs.size):
        rsvs[i] = (df['close_price'][::-1][i+(rsv_days-1):i+rsv_days]-df['close_price'][::-1][i:i+rsv_days].min())\
                 /(df['close_price'][::-1][i:i+rsv_days].max()-df['close_price'][::-1][i:i+rsv_days].min())\
                 *100
    # print(rsvs.size)
    # K值
    ks = np.zeros(df['close_price'].size-(rsv_days-2))
    for i in range(ks.size):
        ks[i] = 50 if i == 0 else 2/3*ks[i-1] + 1/3*rsvs[i-1]
    # print(ks.size)
    # D值
    ds = np.zeros(df['close_price'].size-(rsv_days-2))
    for i in range(ds.size):
        ds[i] = 50 if i == 0 else 2/3*ds[i-1] + 1/3*ks[i]
    # print(ds.size)
    # J值
    js = np.zeros(df['close_price'].size-(rsv_days-2))
    for i in range(js.size):
        js[i] = 3*ds[i] - 2*ks[i]
    # print(ds.size)
    
    mp.figure(csv_name + ' ' + 'Stochastics　KDJ　Line', facecolor='lightgray')
    mp.title(csv_name + '\n' + 'Stochastics　KDJ　Line', fontsize=20)
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
    mp.plot(df['date'][::-1][rsv_days-2:], ks, c='orangered', label='K'+str(rsv_days))
    mp.plot(df['date'][::-1][rsv_days-2:], ds, c='limegreen', label='D'+str(rsv_days))
    mp.plot(df['date'][::-1][rsv_days-2:], js, c='dodgerblue', label='J'+str(rsv_days))
    mp.legend()
    mp.gcf().autofmt_xdate()
    mp.show()
except OSError:
    print('找不到此CSV文件')
except ValueError:
    print('請輸入正確的數字')