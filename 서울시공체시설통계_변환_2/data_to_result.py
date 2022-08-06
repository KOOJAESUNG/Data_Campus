import pandas as pd

data=[]
for i in range(2012,2021):
    data.append(pd.read_excel("서울시공체시설통계_변환_2/data/data_"+str(i)+".xlsx", index_col=str(i)))
    data[i-2013].replace("-", "0",inplace=True)
    data[i-2013]=data[i-2013].astype(int)

for k in range(1,9):
    new_data=data[k]-data[k-1]
    new_data.to_excel("서울시공체시설통계_변환_2/result/"+str(2012+k)+".xlsx")