import pandas as pd


for i in range(2011,2018):
    file_=pd.read_excel("result/"+str(i)+".xlsx",index_col=str(i))
    file_[file_>5]=1
    file_[file_<0]=1
    file_["합"] = file_.sum(axis=1)
    file_.drop(index="기타(서울외)",inplace=True)
    file_.to_excel("result/"+str(i)+".xlsx")