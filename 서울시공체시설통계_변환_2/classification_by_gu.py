import pandas as pd

file=[]
for i in range(2013,2021):
    file.append(pd.read_excel("서울시공체시설통계_변환_2/result/"+str(i)+".xlsx",index_col=str(i)))
    file[0]
qqq=pd.DataFrame()
for k in file[0].index[0:]:
    a = []
    for i in range(0,8):
        a.append(file[i].loc[k,"합"])
    for j in range(1,8):
        a[j]+=a[j-1]
    qqq[k]=a
qqq.index=[2013,2014,2015,2016,2017,2018,2019,2020]

qqq.to_excel("서울시공체시설통계_변환_2/Cummulative_공체.xlsx")






