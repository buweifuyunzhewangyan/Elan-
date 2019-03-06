# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:16:29 2019

@author: Elane
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:17:28 2019

@author: Elane
"""

from tkinter import *
import tkinter.filedialog
import pandas as pd
from tqdm import tqdm
import numpy as np
import time
import threading
import six
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements
import datetime

root = Tk()
root.title('泊位匹配')
#root.geometry('800x500+290+100')
root.resizable(False, False)

def f1():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        lb1.config(text = filename);
    else:
        lb1.config(text = "您没有选择任何文件");
        
def f2():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        lb2.config(text = filename);
    else:
        lb2.config(text = "您没有选择任何文件");




def pipei():
    f1 = open(lb1["text"],encoding='UTF-8')
    f2 = open(lb2["text"],'rb')
    f1 = pd.read_csv(f1)
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
    
    result.to_excel(lb4["text"],index=False,encoding="utf_8_sig")
    lb5.config(text = '泊位匹配完成');



lb1 = Label(root,text = '')
lb1.pack()
btn1 = Button(root,text="拼接完成的文件",command=f1)
btn1.pack()

lb2 = Label(root,text = '')
lb2.pack()
btn2 = Button(root,text="berthid",command=f2)
btn2.pack()


now_time = datetime.datetime.now().strftime('%Y-%m-%d')
lb4 = Label(root,text = 'C://Users//Elane053//Desktop//泊位匹配完成_'+now_time+'.csv')
lb4.pack()

btn4 = Button(root,text="开始匹配",command=pipei, fg='#F5F5F5', bg='#7A7A7A', height=1, width=15,
              relief=GROOVE, bd=2, activebackground='#F5F5F5', activeforeground='#535353')
btn4.pack()

lb5 = Label(root,text = '')
lb5.pack() 

root.mainloop()
