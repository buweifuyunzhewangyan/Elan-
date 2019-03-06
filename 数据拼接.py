# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:47:15 2018

@author: Elane
"""

import pandas as pd
from tqdm import tqdm
import numpy as np

f1 = open('yuanshuju//1.csv')
f2 = open('yuanshuju//2.csv')
f3 = open('yuanshuju//3.csv')
f1 = pd.read_csv(f1)
f2 = pd.read_csv(f2)
f3 = pd.read_csv(f3)
delet_index1=[]
delet_index2=[]
delet_index3=[]
#去除目的地是五港而且目的地不是中国的数据
for i in tqdm(range(len(f1['ais_MMSI']))):
    if(f1['voy_PortName_B'][i]=='Caofeidian' or f1['voy_PortName_B'][i]=='Qinhuangdao'
       or f1['voy_PortName_B'][i]=='Tangshan' or f1['voy_PortName_B'][i]=='Tianjin'
       or f1['voy_PortName_B'][i]=='Huanghua' or (f1['voy_CountryNameEN_B'][i]!='China'
       and f1['voy_CountryNameEN_B'][i]!='Hong Kong, China')):
        delet_index1.append(i)
f1 = f1.drop(delet_index1) 

for i in tqdm(range(len(f2['ais_MMSI']))):
    if(f2['voy_PortName_B'][i]=='Caofeidian' or f2['voy_PortName_B'][i]=='Qinhuangdao'
       or f2['voy_PortName_B'][i]=='Tangshan' or f2['voy_PortName_B'][i]=='Tianjin'
       or f2['voy_PortName_B'][i]=='Huanghua' or (f2['voy_CountryNameEN_B'][i]!='China'
       and f2['voy_CountryNameEN_B'][i]!='Hong Kong, China')):
        delet_index2.append(i)
f2 = f2.drop(delet_index2) 
        
for i in tqdm(range(len(f3['ais_MMSI']))):
    if(f3['voy_PortName_B'][i]!='Changjiangkou' or f3['voy_PortName_C'][i]!='Changjiangkou'
       or f3['voy_PortName_D'][i]=='Caofeidian'or f3['voy_PortName_D'][i]=='Qinhuangdao'
       or f3['voy_PortName_D'][i]=='Tangshan' or f3['voy_PortName_D'][i]=='Tianjin'
       or f3['voy_PortName_D'][i]=='Huanghua' or (f3['voy_CountryNameEN_D'][i]!='China'
       and f3['voy_CountryNameEN_D'][i]!='Hong Kong, China')):
        delet_index3.append(i)
f3 = f3.drop(delet_index3)  

print("len_f1",len(f1['ais_MMSI']))

ATD_B = f1['voy_ATD_B']
mmsi_1 = f1['ais_MMSI']
ATD_A = f2['voy_ATD_A']
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

print(len(index1),len(index2))
#数据拼接   
#print('拼接前：',f1.iloc[index1[0],42])
voy_Distance_1 = []
voy_Distance_2 = []
voy_SailingTime_1 = []
voy_SailingTime_2 = []
for i in tqdm(range(len(index1))):
    f1.iloc[index1[i],42:52] = f2.iloc[index2[i],42:52]
    f1.iloc[index1[i],58:62] = f2.iloc[index2[i],58:62]
    f1.iloc[index1[i],66:68] = f2.iloc[index2[i],66:68]
    voy_Distance_1.append(f1.iloc[index1[i],69])
    voy_Distance_2.append(f2.iloc[index2[i],69])
    voy_SailingTime_1.append(f1.iloc[index1[i],70])
    voy_SailingTime_2.append(f2.iloc[index2[i],70])
distance=[]
time = []    
for i in tqdm(range(len(voy_Distance_1))):
    distance.append(float(voy_Distance_1[i])+float(voy_Distance_2[i]))
    time.append(float(voy_SailingTime_1[i])+float(voy_SailingTime_2[i]))
    
#for i in tqdm(range(len(index1))):
#    f1.iloc[index1[i],69] = distance[i]
#    f1.iloc[index1[i],70] = time[i]
f1.iloc[index1,69] = distance
f1.iloc[index1,70] = time
f1.iloc[index1,71] = np.array(distance)/np.array(time)
print("len_f1",len(f1['ais_MMSI']))
#print('拼接后：',f1.iloc[index1[0],42])
ATA_1 = f1['VoyATA_A']
ATA_2 = f3['VoyATA_A']
mmsi_1 = f1['ais_MMSI']
mmsi_2 = f3['ais_MMSI']
l3=[]
l4=[]
index3=[]
index4=[]
for i in range(len(ATA_1)):
    l3.append(str(ATA_1.iloc[i])+str(mmsi_1.iloc[i]))
for i in range(len(ATA_2)):
    l4.append(str(ATA_2.iloc[i])+str(mmsi_2.iloc[i]))

for i in tqdm(range(len(ATA_1))):
    for j in range(len(ATA_2)):
        if(l3[i]==l4[j]):
            #记录需要拼接的行序号
            index3.append(i)
            index4.append(j)
            break

print(len(index3),len(index4))

for i in tqdm(range(len(index3))):
    f1.iloc[index3[i],42:52] = f3.iloc[index4[i],87:97]
    f1.iloc[index3[i],57:61] = f3.iloc[index4[i],98:102]
    f1.iloc[index3[i],65:67] = f3.iloc[index4[i],103:105]

for i in tqdm(range(len(f1['ais_MMSI']))):
    if(np.isnan(f1.iloc[i,2])):
        f1.iloc[i,15] = f1.iloc[i,25]
        f1.iloc[i,16] = f1.iloc[i,26]
        f1.iloc[i,13] = f1.iloc[i,28]

f1.to_csv('jieguo//拼接完成_1_22.csv',index=False,encoding="utf_8_sig")
f1.to_csv('yuanshuju//pinjiewancheng_1_22.csv',index=False,encoding="utf_8_sig")
print('拼接完毕')
print ('\a'*7)


















