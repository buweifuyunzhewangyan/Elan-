# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:12:13 2019

@author: Elane
"""

import pandas as pd
from tqdm import tqdm
import os

#oslist = os.listdir('C://Users//Elane053//Desktop//lys实习工作//2017年数据')
#for one_os in tqdm(oslist[0:1]):
#    a = one_os
#    b = a[15:25]+'_'
    
    
a = 'C://Users//Elane053//Desktop//lys实习工作//2017年数据//20190103132413_区域2数据2017年.csv'
b = a[15:25]+'_' 
f=open(a)
df1 = pd.read_csv(f)
df2 = df1.drop(i for i in range(len(df1['MMSI'])) if (df1.loc[i,'ShipTypeCN']!='货船')and (df1.loc[i,'ShipTypeCN']!='捕捞'))
df2=df2.reset_index(drop=True)
df2 = df2.drop(i for i in range(len(df2['MMSI'])) if int(df2.loc[i,'MMSI'])<10000 and df2.loc[i,'ShipTypeCN']=='货船')
#    print(len(df2['MMSI']))
df2=df2.reset_index(drop=True)
df2.to_csv('C://Users//Elane053//Desktop//lys实习工作//2017年数据//'+b+'渔船货船.csv',encoding='utf_8_sig',index=False)
huo_mmsi=[]
yu_mmsi=[]
non_mmsi=[]
for i in range(len(df1['MMSI'])):
    if (df1.loc[i,'ShipTypeCN']=='货船' and int(df1.loc[i,'MMSI'])>9999):
        huo_mmsi.append(int(df1.loc[i,'MMSI']))
    if df1.loc[i,'ShipTypeCN']=='捕捞':
        yu_mmsi.append(int(df1.loc[i,'MMSI']))
    if pd.isnull(df1.loc[i,'ShipTypeCN']):
        non_mmsi.append(int(df1.loc[i,'MMSI']))
        
    #huo_mmsi.append(int(df1.loc[i,'MMSI']) for i in tqdm(range(len(df1['MMSI']))) if (df1.loc[i,'ShipTypeCN']=='货船'))
    #yu_mmsi.append(int(df1.loc[i,'MMSI']) for i in range(len(df1['MMSI'])) if df1.loc[i,'ShipTypeCN']=='捕捞')
    #non_mmsi.append(int(df1.loc[i,'MMSI']) for i in range(len(df1['MMSI'])) if pd.isnull(df1.loc[i,'ShipTypeCN']))
huo_mmsi=list(set(huo_mmsi))
yu_mmsi=list(set(yu_mmsi))
non_mmsi=list(set(non_mmsi))
ais_num = len(df1['MMSI'])
huo_num = len(huo_mmsi)
yu_num = len(yu_mmsi)
all_list = list(set(list(df1['MMSI'])))
all_num = len(all_list)
max_value=max(len(huo_mmsi),len(yu_mmsi),len(non_mmsi))
for i in range(max_value-len(huo_mmsi)):
    huo_mmsi.append('')
for i in range(max_value-len(yu_mmsi)):
    yu_mmsi.append('')
for i in range(max_value-len(non_mmsi)):
    non_mmsi.append('')
mmsi = pd.DataFrame()
mmsi['货船MMSI'] = huo_mmsi
mmsi['渔船MMSI'] = yu_mmsi
mmsi['无静态信息的MMSI'] = non_mmsi
mmsi.to_excel('C://Users//Elane053//Desktop//lys实习工作//2017年数据//'+b+'MMSI列表.xlsx',encoding='utf_8_sig',index=False)
tongji = pd.DataFrame()
tongji['船舶总数'] = [all_num]
tongji['渔船数量'] = [yu_num]
tongji['货船数量'] = [huo_num]
tongji['AIS轨迹点数'] = [ais_num]
tongji.to_excel('C://Users//Elane053//Desktop//lys实习工作//2017年数据//'+b+'统计数据.xlsx',encoding='utf_8_sig',index=False)