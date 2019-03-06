# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:05:34 2018

@author: Elane
"""

import pandas as pd
from tqdm import tqdm
f1 = pd.read_csv('yuanshuju//shaixuan_1128.csv')
ATA_B = f1['voy_ATD_B']
mmsi = f1['ais_MMSI']
l1 = []
l2 = []
delet_index1 = []
for i in range(len(ATA_B)):
#    print(ATD_B.iloc[i])
    l1.append(str(ATA_B.iloc[i])+str(mmsi.iloc[i]))

for i in tqdm(range(len(f1['ais_MMSI']))):
    if((f1['voy_CountryNameEN_A'][i]=='China'or f1['voy_CountryNameEN_A'][i]=='Hong Kong, China')):
        delet_index1.append(i)
#    if not l1[i] in l2:
#        l2.append(l1[i])
#    else:
#        delet_index1.append(i)
    
f1 = f1.drop(delet_index1) 
print(len(f1['ais_MMSI']))
f1.to_csv('jieguo//筛选完成_1129.csv',index=False,encoding="utf_8_sig")
print('筛选完毕')