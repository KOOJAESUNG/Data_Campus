import pandas as pd

file=[]
for i in range(2011,2018):
    file.append(pd.read_excel("서울시공체시설통계_변환/result/"+str(i)+".xlsx",index_col=str(i)))
qqq=pd.DataFrame()
for k in file[0].index[1:]:
    a = []
    for i in range(0,7):
        a.append(file[i].loc[k,"합"])
    for j in range(1,7):
        a[j]+=a[j-1]
    qqq[k]=a
qqq.index=[2011,2012,2013,2014,2015,2016,2017]

qqq.to_excel("서울시공체시설통계_변환/Cummulative.xlsx")






