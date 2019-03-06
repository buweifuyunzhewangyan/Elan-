# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:16:22 2018

@author: Elane
"""

import pandas as pd 
f1 = pd.read_csv('yuanshuju//shengfen4.csv',encoding='gbk')
shapename = f1['shipname']
shengfen = []
for name in shapename:
    name = str(name)
    if 'LIAO' == name[0:4]:
        shengfen.append('辽宁')
    elif 'LU' == name[0:2]:
        shengfen.append('山东')
    elif 'JIN' == name[0:3]:
        shengfen.append('天津')
    elif ('JI' == name[0:2] and 'JIN' != name[0:3]):
        shengfen.append('河北')
    elif 'SU' == name[0:2]:
        shengfen.append('江苏')
    elif 'HU' == name[0:2]:
        shengfen.append('上海')
    elif 'ZHE' == name[0:3]:
        shengfen.append('浙江')
    elif 'MIN' == name[0:3]:
        shengfen.append('福建')
    elif 'YUE' == name[0:3]:
        shengfen.append('广东')
    elif 'GUI' == name[0:3]:
        shengfen.append('广西')
    elif 'QIONG' == name[0:5]:
        shengfen.append('海南')
    else:
        shengfen.append(' ')
print(shengfen[0:100])
df = pd.DataFrame()
df['省份'] = shengfen
df.to_csv('jieguo//省份4.csv',index=False,encoding="utf_8_sig")