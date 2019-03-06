# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 13:52:58 2018

@author: Elane
"""

import pandas as pd
from tqdm import tqdm
import numpy as np

f1 = pd.read_csv('yuanshuju//liangcheng.csv',encoding='gbk')
f2 = pd.read_csv('yuanshuju//sancheng.csv',encoding='gbk')
f3 = pd.read_csv('yuanshuju//sicheng.csv',encoding='gbk')
delet_index1=[]
delet_index2=[]
delet_index3=[]
#去除目的地是五港而且目的地不是中国的数据
#for i in tqdm(range(len(f1['ais_MMSI']))):
#    if((f1['voy_CountryNameEN_A'][i]=='China'
#       or f1['voy_CountryNameEN_A'][i]=='Hong Kong, China')):
#        delet_index1.append(i)
#f1 = f1.drop(delet_index1) 
f1_len = len(f1['ais_MMSI'])
print(len(f1['ais_MMSI']))
for i in tqdm(range(len(f2['ais_MMSI']))):
    if((f2['voy_CountryNameEN_B'][i]!='China'and f2['voy_CountryNameEN_B'][i]!='Hong Kong, China')):
        f1.loc[f1_len+1+i,'ship_ShipName':'ais_NavArea']=f2.loc[i,'ship_ShipName':'ais_NavArea']
        f1.loc[f1_len+1+i,'voy_PortID_A':'AnchorageName_A']=f2.loc[i,'voy_PortID_B':'AnchorageName_B']
        f1.loc[f1_len+1+i,'VoyArrivalDraft_A']=f2.loc[i,'voy_ArrivalDraft_B']
        f1.loc[f1_len+1+i,'VoyATA_A']=f2.loc[i,'voy_ATA_B']
        f1.loc[f1_len+1+i,'VoyATB_A':'voy_ATD_A']=f2.loc[i,'voy_ATB_B':'voy_ATD_B']
        f1.loc[f1_len+1+i,'VoyStayInPort_A':'VoyAnchorageTime_A']=f2.loc[i,'voy_StayInPort_B':'voy_AnchorageTime_B']
        #C 放到 B 上
        f1.loc[f1_len+1+i,'voy_PortID_B':'AnchorageName_B']=f2.loc[i,'voy_PortID_C':'AnchorageName_C']
        f1.loc[f1_len+1+i,'voy_ArrivalDraft_B']=f2.loc[i,'voy_ArrivalDraft_C']
        f1.loc[f1_len+1+i,'voy_ATA_B']=f2.loc[i,'voy_ATA_C']
        f1.loc[f1_len+1+i,'voy_ATB_B':'voy_ATD_B']=f2.loc[i,'voy_ATB_C':'voy_ATD_C']
        f1.loc[f1_len+1+i,'voy_StayInPort_B':'voy_AnchorageTime_B']=f2.loc[i,'voy_StayInPort_C':'voy_AnchorageTime_C']
        
    elif((f2['voy_CountryNameEN_A'][i]!='China'and f2['voy_CountryNameEN_A'][i]!='Hong Kong, China')):
        f1.loc[f1_len+1+i,'ship_ShipName':'ais_NavArea']=f2.loc[i,'ship_ShipName':'ais_NavArea']
        f1.loc[f1_len+1+i,'voy_PortID_A':'AnchorageName_A']=f2.loc[i,'voy_PortID_A':'AnchorageName_A']
        f1.loc[f1_len+1+i,'VoyArrivalDraft_A']=f2.loc[i,'VoyArrivalDraft_A']
        f1.loc[f1_len+1+i,'VoyATA_A']=f2.loc[i,'VoyATA_A']
        f1.loc[f1_len+1+i,'VoyATB_A':'voy_ATD_A']=f2.loc[i,'VoyATB_A':'voy_ATD_A']
        f1.loc[f1_len+1+i,'VoyStayInPort_A':'VoyAnchorageTime_A']=f2.loc[i,'VoyStayInPort_A':'VoyAnchorageTime_A']
        #C 放到 B 上
        f1.loc[f1_len+1+i,'voy_PortID_B':'AnchorageName_B']=f2.loc[i,'voy_PortID_C':'AnchorageName_C']
        f1.loc[f1_len+1+i,'voy_ArrivalDraft_B']=f2.loc[i,'voy_ArrivalDraft_C']
        f1.loc[f1_len+1+i,'voy_ATA_B']=f2.loc[i,'voy_ATA_C']
        f1.loc[f1_len+1+i,'voy_ATB_B':'voy_ATD_B']=f2.loc[i,'voy_ATB_C':'voy_ATD_C']
        f1.loc[f1_len+1+i,'voy_StayInPort_B':'voy_AnchorageTime_B']=f2.loc[i,'voy_StayInPort_C':'voy_AnchorageTime_C']
print(len(f1['ais_MMSI']))

for i in tqdm(range(len(f3['ais_MMSI']))):
    if((f3['voy_CountryNameEN_C'][i]!='China'and f3['voy_CountryNameEN_C'][i]!='Hong Kong, China')):
        f1.loc[f1_len+1+i,'ship_ShipName':'ais_NavArea']=f3.loc[i,'ship_ShipName':'ais_NavArea']
        f1.loc[f1_len+1+i,'voy_PortID_A':'AnchorageName_A']=f3.loc[i,'voy_PortID_C':'AnchorageName_C']
        f1.loc[f1_len+1+i,'VoyArrivalDraft_A']=f3.loc[i,'voy_ArrivalDraft_C']
        f1.loc[f1_len+1+i,'VoyATA_A']=f3.loc[i,'voy_ATA_C']
        f1.loc[f1_len+1+i,'VoyATB_A':'voy_ATD_A']=f3.loc[i,'voy_ATB_C':'voy_ATD_C']
        f1.loc[f1_len+1+i,'VoyStayInPort_A':'VoyAnchorageTime_A']=f3.loc[i,'voy_StayInPort_C':'voy_AnchorageTime_C']
        #D 放到 B 上
        f1.loc[f1_len+1+i,'voy_PortID_B':'AnchorageName_B']=f3.loc[i,'voy_PortID_D':'AnchorageName_D']
        f1.loc[f1_len+1+i,'voy_ArrivalDraft_B']=f3.loc[i,'voy_ArrivalDraft_D']
        f1.loc[f1_len+1+i,'voy_ATA_B']=f3.loc[i,'voy_ATA_D']
        f1.loc[f1_len+1+i,'voy_ATB_B':'voy_ATD_B']=f3.loc[i,'voy_ATB_D':'voy_ATD_D']
        f1.loc[f1_len+1+i,'voy_StayInPort_B':'voy_AnchorageTime_B']=f3.loc[i,'voy_StayInPort_D':'voy_AnchorageTime_D']
    
    elif((f3['voy_CountryNameEN_B'][i]!='China'and f3['voy_CountryNameEN_B'][i]!='Hong Kong, China')):
        f1.loc[f1_len+1+i,'ship_ShipName':'ais_NavArea']=f3.loc[i,'ship_ShipName':'ais_NavArea']
        f1.loc[f1_len+1+i,'voy_PortID_A':'AnchorageName_A']=f3.loc[i,'voy_PortID_B':'AnchorageName_B']
        f1.loc[f1_len+1+i,'VoyArrivalDraft_A']=f3.loc[i,'voy_ArrivalDraft_B']
        f1.loc[f1_len+1+i,'VoyATA_A']=f3.loc[i,'voy_ATA_B']
        f1.loc[f1_len+1+i,'VoyATB_A':'voy_ATD_A']=f3.loc[i,'voy_ATB_B':'voy_ATD_B']
        f1.loc[f1_len+1+i,'VoyStayInPort_A':'VoyAnchorageTime_A']=f3.loc[i,'voy_StayInPort_B':'voy_AnchorageTime_B']
        #D 放到 B 上
        f1.loc[f1_len+1+i,'voy_PortID_B':'AnchorageName_B']=f3.loc[i,'voy_PortID_D':'AnchorageName_D']
        f1.loc[f1_len+1+i,'voy_ArrivalDraft_B']=f3.loc[i,'voy_ArrivalDraft_D']
        f1.loc[f1_len+1+i,'voy_ATA_B']=f3.loc[i,'voy_ATA_D']
        f1.loc[f1_len+1+i,'voy_ATB_B':'voy_ATD_B']=f3.loc[i,'voy_ATB_D':'voy_ATD_D']
        f1.loc[f1_len+1+i,'voy_StayInPort_B':'voy_AnchorageTime_B']=f3.loc[i,'voy_StayInPort_D':'voy_AnchorageTime_D']
        
    elif((f3['voy_CountryNameEN_A'][i]!='China'and f3['voy_CountryNameEN_A'][i]!='Hong Kong, China')):
        f1.loc[f1_len+1+i,'ship_ShipName':'ais_NavArea']=f3.loc[i,'ship_ShipName':'ais_NavArea']
        f1.loc[f1_len+1+i,'voy_PortID_A':'AnchorageName_A']=f3.loc[i,'voy_PortID_A':'AnchorageName_A']
        f1.loc[f1_len+1+i,'VoyArrivalDraft_A']=f3.loc[i,'VoyArrivalDraft_A']
        f1.loc[f1_len+1+i,'VoyATA_A']=f3.loc[i,'VoyATA_A']
        f1.loc[f1_len+1+i,'VoyATB_A':'voy_ATD_A']=f3.loc[i,'VoyATB_A':'voy_ATD_A']
        f1.loc[f1_len+1+i,'VoyStayInPort_A':'VoyAnchorageTime_A']=f3.loc[i,'VoyStayInPort_A':'VoyAnchorageTime_A']
        #D 放到 B 上
        f1.loc[f1_len+1+i,'voy_PortID_B':'AnchorageName_B']=f3.loc[i,'voy_PortID_D':'AnchorageName_D']
        f1.loc[f1_len+1+i,'voy_ArrivalDraft_B']=f3.loc[i,'voy_ArrivalDraft_D']
        f1.loc[f1_len+1+i,'voy_ATA_B']=f3.loc[i,'voy_ATA_D']
        f1.loc[f1_len+1+i,'voy_ATB_B':'voy_ATD_B']=f3.loc[i,'voy_ATB_D':'voy_ATD_D']
        f1.loc[f1_len+1+i,'voy_StayInPort_B':'voy_AnchorageTime_B']=f3.loc[i,'voy_StayInPort_D':'voy_AnchorageTime_D']

print(len(f1['ais_MMSI']))

f1.to_csv('yuanshuju//shaixuan_1128.csv',index=False,encoding="utf_8_sig")

print('筛选完毕')











