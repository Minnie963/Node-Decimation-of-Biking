#This program simplifies the route in CSV file that has been process by 'ConvertComma.py'

import pandas as pd
import numpy as np
import DouglasPeucker
import datetime

time_stamp = datetime.datetime.now()
print("Start importing data  "+"Time:" + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))

rawdata=pd.read_csv(r'track_sample_comma.csv',sep=',')
time_stamp = datetime.datetime.now()

leftdata=rawdata.drop(labels=['endpositiony/track'],axis=1)
newdata = pd.DataFrame(columns = ['orderid','endpositiony','track'])

time_stamp = datetime.datetime.now()
print("Start processing data  "+"Time:" + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))

i=0
for index,row in rawdata.iterrows():
    #When there is data to be preocessed
    newdata.loc[i,['orderid']]=row['orderid']
    newStr=''
    start=row['endpositiony/track'].find('#')
    if(start>=0):
        #Use data after '/' as a new substring separated by '|'
        AllStr=row['endpositiony/track'][start+1:].replace(';','|')
        newdata.loc[i,['endpositiony']]=row['endpositiony/track'][0:start-1]

        #Seperate the string into 3-array(latitude,longitude, time) with '#'
        AllArrs=AllStr.split('#')
        for index, value in enumerate(AllArrs):
            AllArrs[index]=AllArrs[index].split('|')
            for index0,value0 in enumerate(AllArrs[index]):
                AllArrs[index][index0]=float(AllArrs[index][index0])

        #Douglas Peucker Algorithm
        d=DouglasPeucker.DouglasPeuker()
        d.main(AllArrs)

        #Concat dataframes, replace English comma with Chinese comma
        TransArr=d.qualify_list
        # newStr+=row['endpositiony/track'][start+1:]
        for Arr in TransArr:
            newStr+='#'
            j=0
            for index in Arr:
                if(j==0):
                    newStr+=str(index)
                    newStr+=','#Can be replaced with other symbols
                if(j==1):
                    newStr+=str(index)
                    newStr+=';'
                if(j==2):
                    newStr+=str(int(index))
                j+=1
        newStr.lstrip('"')
        newStr.rstrip('"')
        newdata.loc[i,["track"]]=newStr
    else:
        newStr+=row['endpositiony/track']
        newStr=newStr.rstrip('/')
        newdata.loc[i,["endpositiony"]]=newStr
    i+=1
    if(row['orderid']%1000==0):
        time_stamp = datetime.datetime.now()
        print("Process"+str(row['orderid'])+'data  '+"Time:" + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))

time_stamp = datetime.datetime.now()
print("Complete processing data  "+"Time:" + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))

#Concat dataframes into original form
time_stamp = datetime.datetime.now()
expecteddata=pd.merge(leftdata,newdata)

time_stamp = datetime.datetime.now()
print("Saving into CSV file...  "+"Time:" + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
expecteddata.to_csv('FinalData.csv',index=False,sep=',')
time_stamp = datetime.datetime.now()
print("Work completed"+"Time:" + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))