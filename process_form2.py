#Process Form2 data with Douglas Peucker algorithm: to use fewer points to represent a biking route in the documents 
import pandas as pd
import numpy as np
from itertools import groupby
import DouglasPeucker

df=pd.read_csv(r'2_mobike_track_2017-06-20.csv',sep=',')
newdata = pd.DataFrame(columns = ['Orderid','Userid','Bikeid','Time','Lng','Lat'])
newdata1 = pd.DataFrame(columns = ['Orderid','Userid','Bikeid','Time','Lng','Lat'])

OrderGroup = df.groupby(['Orderid'])

d=DouglasPeuker.DouglasPeucker()

for Orderid,group in OrderGroup:
    list1=[]
    newdata.drop(newdata.index, inplace=True)
    for index, row in group.iterrows():
        list0=[]
        list0.append(row['Lng'])
        list0.append(row['Lat'])
        list1.append(list0)
    d.main(list1)
    TransArr = d.qualify_list
    i=0
    j=0
    for index, row in group.iterrows():
        if(list1[j] in TransArr):
            newdata.loc[i]=row
            i+=1
        j+=1
    newdata1=pd.concat([newdata1,newdata])

newdata1["Orderid"]=newdata1["Orderid"].astype('int')
newdata1["Userid"]=newdata1["Userid"].astype('int')
newdata1["Bikeid"]=newdata1["Bikeid"].astype('int')
newdata1["Time"]=newdata1["Time"].astype('int')

newdata1.to_csv('newdata.csv',index=False,sep=",")











