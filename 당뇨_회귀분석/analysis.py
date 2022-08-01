import pandas as pd
from statsmodels.formula.api import ols

dang=pd.read_excel("당뇨_회귀분석/class_by_gu_dang.xlsx",index_col="Unnamed: 0")
public_sports=pd.read_excel("당뇨_회귀분석/Cummulative.xlsx",index_col="Unnamed: 0")

a=[]
b=[]
for i in range(7):
    for k in range(len(dang.columns)):
        a.append(dang.iloc[i,k])
        b.append(public_sports.iloc[i,k])
a
df=pd.DataFrame()
df["당"]=a
df["공체시설"]=b
df
res = ols("당 ~ 공체시설", data=df).fit()
res.summary()