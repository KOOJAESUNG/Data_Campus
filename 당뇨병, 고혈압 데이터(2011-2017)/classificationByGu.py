import pandas as pd

file=[]
for i in range(2011,2018):
    file.append(pd.read_csv("당뇨병, 고혈압 데이터(2011-2017)/diseases_"+str(i)+".csv",index_col="자치구"))
file[0]
qqq=pd.DataFrame()
www=pd.DataFrame()
for k in file[0].index:
    a = []
    b=[]
    for i in range(0,7):
        a.append(file[i].loc[k,"당뇨병 이상"])
        b.append(file[i].loc[k,"고혈압 이상"])
    qqq[k]=a
    www[k]=b

qqq.index=[2011,2012,2013,2014,2015,2016,2017]
www.index=[2011,2012,2013,2014,2015,2016,2017]

qqq.to_excel("당뇨병, 고혈압 데이터(2011-2017)/class_by_gu_dang.xlsx")
www.to_excel("당뇨병, 고혈압 데이터(2011-2017)/class_by_gu_go.xlsx")







