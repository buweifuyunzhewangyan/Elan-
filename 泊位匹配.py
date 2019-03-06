# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 15:24:10 2018

@author: Elane
"""

import pandas as pd
from tqdm import tqdm
import numpy as np

f1 = open('yuanshuju//pinjiewancheng_1_22.csv',encoding='UTF-8')
f2 = open('yuanshuju//berthid1.1.xlsx','rb')
f1 = pd.read_csv(f1)
#zh = pd.read_excel('yuanshuju//berthid1.1.xlsx',sheetname='装货泊位',encoding='gbk')
#xh = pd.read_excel('yuanshuju//berthid1.1.xlsx',sheetname='卸货泊位',encoding='gbk')

zh = pd.read_excel(f2,sheetname='装货泊位')
xh = pd.read_excel(f2,sheetname='卸货泊位')

#print(zh['PortID'].index.tolist())
delet_index = []
delet_index2 = []


berthid_a = f1['voy_BerthID_A']
berthid_b = f1['voy_BerthID_B']
#terid_a = f1['voy_TerminalID_A']
#terid_b = f1['voy_TerminalID_B']
#tername_a = f1['voy_TerminalName_A']
#tername_b = f1['voy_TerminalName_B']
berthid_zh = zh['Berth_ID'].tolist()
berthid_xh = xh['Berth_ID'].tolist()
#去重
berthid_zh = list(set(berthid_zh))
berthid_xh = list(set(berthid_xh))

#terid_zh = zh['Terminal_ID'].tolist()
#terid_xh = xh['Terminal_ID'].tolist()
#terid_zh = list(set(terid_zh))
#terid_xh = list(set(terid_xh))

#====================码头匹配=======================
#for i in tqdm(range(len(f1['ais_MMSI']))):
#    if (terid_a[i] not in terid_zh) and (~pd.isnull(tername_a[i]) and (i not in delet_index)):
#        delet_index.append(i)
#    if (terid_b[i] not in terid_xh) and (~pd.isnull(tername_b[i]) and (i not in delet_index)):
#        delet_index.append(i)

for i in tqdm(range(len(f1['ais_MMSI']))):
    if (berthid_a[i] not in berthid_zh) and (i not in delet_index):
        delet_index.append(i)
    if (berthid_b[i] not in berthid_xh) and (i not in delet_index2):
        delet_index2.append(i)

f2 = f1.drop(delet_index)
f3 = f1.drop(delet_index2)
result = f2.append(f3)
#删除重复行
result = result.drop_duplicates().reset_index(drop=True)

berthid_a = result['voy_BerthID_A']
delet_index = []

for i in tqdm(range(len(result['ais_MMSI']))):
    if ((berthid_a[i] not in berthid_zh) and (~pd.isnull(berthid_a[i]))):
        delet_index.append(i)

result = result.drop(delet_index).reset_index(drop=True)

result = result.drop(i for i in tqdm(range(len(result['ais_MMSI']))) if ((((result['ship_LengthLOA'][i]<70)or 
                        (result['ship_LengthLOA'][i]>500))and pd.isnull(result['ship_ShipName'][i]))
                    or (((result['ship_DeadWeight'][i]>200000))and ~pd.isnull(result['ship_ShipName'][i]))
                    or result['voy_StayOnBerth_B'][i]<=1
                    or result['VoyStayOnBerth_A'][i]<=1))

result.to_excel('jieguo//泊位匹配完成_1_22.xlsx',index=False,encoding="utf_8_sig")
print ('\a'*7)


















