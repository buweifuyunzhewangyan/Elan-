# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:26:21 2018

@author: Elane
"""

import pandas as pd
from tqdm import tqdm
import numpy as np


f1 = pd.read_csv('yuanshuju//shaixuanwancheng_1129.csv')
f2 = pd.read_csv('yuanshuju//zhongjian.csv',encoding='gbk')
ATB_B = f1['voy_ATB_B']
f1_len = len(f1['ais_MMSI'])
l1=[]
l2=[]
l3=[]
index1 = []
ATA_B1 = f1['voy_ATA_B']
mmsi1 = f1['ais_MMSI']
ATA_B2 = f2['voy_ATA_B']
mmsi2 = f2['ais_MMSI']
ATA_A2 = f2['VoyATA_A']
for i in range(len(f1['ais_MMSI'])):
#    print(ATD_B.iloc[i])
    l1.append(str(ATA_B1.iloc[i])+str(mmsi1.iloc[i]))

for i in range(len(f2['ais_MMSI'])):
#    print(ATD_B.iloc[i])
    l2.append(str(ATA_A2.iloc[i])+str(mmsi2.iloc[i]))
    l3.append(str(ATA_B2.iloc[i])+str(mmsi2.iloc[i]))
for i in tqdm(range(len(l1))):
    if(pd.isnull(ATB_B.iloc[i])):
        index1.append(i)
#print(index1)
for i in tqdm(index1):
    for j in range(len(l2)):
        if(l1[i]==l3[j]):
            f1.loc[i,'voy_PortID_B':'AnchorageName_B']=f2.loc[j,'voy_PortID_C':'AnchorageName_C']
            f1.loc[i,'voy_ArrivalDraft_B']=f2.loc[j,'voy_ArrivalDraft_C']
            f1.loc[i,'voy_ATA_B']=f2.loc[j,'voy_ATA_C']
            f1.loc[i,'voy_ATB_B':'voy_ATD_B']=f2.loc[j,'voy_ATB_C':'voy_ATD_C']
            f1.loc[i,'voy_StayInPort_B':'voy_AnchorageTime_B']=f2.loc[j,'voy_StayInPort_C':'voy_AnchorageTime_C']
        elif(l1[i]==l2[j]):
            f1.loc[i,'voy_PortID_B':'AnchorageName_B']=f2.loc[j,'voy_PortID_B':'AnchorageName_B']
            f1.loc[i,'voy_ArrivalDraft_B']=f2.loc[j,'voy_ArrivalDraft_B']
            f1.loc[i,'voy_ATA_B']=f2.loc[j,'voy_ATA_B']
            f1.loc[i,'voy_ATB_B':'voy_ATD_B']=f2.loc[j,'voy_ATB_B':'voy_ATD_B']
            f1.loc[i,'voy_StayInPort_B':'voy_AnchorageTime_B']=f2.loc[j,'voy_StayInPort_B':'voy_AnchorageTime_B']

f1.to_csv('jieguo//完成_1129.csv',index=False,encoding="utf_8_sig")
print('全部完毕')


























