import pandas as pd

data=[]
for i in range(2010,2018):
    data.append(pd.read_excel("data/data_"+str(i)+".xlsx", index_col=str(i)))
    data[i-2010].replace("-", "0",inplace=True)
    data[i-2010]=data[i-2010].astype(int)


for k in range(1,8):
    new_data=data[k]-data[k-1]
    new_data.to_excel("result/"+str(2010+k)+".xlsx")