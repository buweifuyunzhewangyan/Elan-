# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:21:14 2018

@author: Elane
"""
import pandas as pd
from tqdm import tqdm
import numpy as np

f1 = pd.read_csv('yuanshuju//yanjianggangkou.csv',encoding='gbk')
f2 = pd.read_csv('yuanshuju//all-changjiangkou.csv',encoding='gbk')

ATD_B = f1['voy_ATD_A']
mmsi_1 = f1['ais_MMSI']
ATD_A = f2['voy_ATD_B']
mmsi_2 = f2['ais_MMSI']
l1 = []
l2 = []
index1 = []
index2 = []
for i in range(len(ATD_B)):
#    print(ATD_B.iloc[i])
    l1.append(str(ATD_B.iloc[i])+str(mmsi_1.iloc[i]))
for i in range(len(ATD_A)):
    l2.append(str(ATD_A.iloc[i])+str(mmsi_2.iloc[i]))

for i in tqdm(range(len(ATD_B))):
    for j in range(len(ATD_A)):
        if(l1[i]==l2[j]):
            #记录需要拼接的行序号
            index1.append(i)
            index2.append(j)
            break

#数据拼接   
#print('拼接前：',f1.iloc[index1[0],42])
voy_Distance_1 = []
voy_Distance_2 = []
voy_SailingTime_1 = []
voy_SailingTime_2 = []
for i in tqdm(range(len(index1))):
    f1.loc[index1[i],'voy_PortID_A':'AnchorageName_A'] = f2.loc[index2[i],'voy_PortID_A':'AnchorageName_A']
    f1.loc[index1[i],'VoyArrivalDraft_A':'VoyDepartDraft_A'] = f2.loc[index2[i],'VoyArrivalDraft_A':'VoyDepartDraft_A']
    f1.loc[index1[i],'VoyStayInPort_A':'VoyAnchorageTime_A'] = f2.loc[index2[i],'VoyStayInPort_A':'VoyAnchorageTime_A']
    voy_Distance_1.append(f1.loc[index1[i],'voy_Distance'])
    voy_Distance_2.append(f2.loc[index2[i],'voy_Distance'])
    voy_SailingTime_1.append(f1.loc[index1[i],'voy_SailingTime'])
    voy_SailingTime_2.append(f2.loc[index2[i],'voy_SailingTime'])
distance=[]
time = []    
for i in tqdm(range(len(voy_Distance_1))):
    distance.append(float(voy_Distance_1[i])+float(voy_Distance_2[i]))
    time.append(float(voy_SailingTime_1[i])+float(voy_SailingTime_2[i]))
    
#for i in tqdm(range(len(index1))):
#    f1.loc[index1[i],69] = distance[i]
#    f1.loc[index1[i],70] = time[i]
f1.loc[index1,'voy_Distance'] = distance
f1.loc[index1,'voy_SailingTime'] = time
f1.loc[index1,'voy_AverageSpeed'] = np.array(distance)/np.array(time)
print("len_f1",len(f1['ais_MMSI']))


f1.to_csv('jieguo//反向拼接完成_12_27.csv',index=False,encoding="utf_8_sig")




