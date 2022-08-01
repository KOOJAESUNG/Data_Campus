import pandas as pd

rawdata = []
for i in range(1,8):
    new = pd.read_excel("raw/당뇨고혈압_201"+str(i)+".xlsx")
    new.fillna("0",inplace=True)
    rawdata.append(new)

for k in range(0,7):
    rawdata[k].iloc[2:, 3:] = rawdata[k].iloc[2:, 3:].replace("-", "0").astype(int)
    rawdata[k] = rawdata[k].loc[(rawdata[k]["성별(1)"] == "합계") | (rawdata[k]["성별(1)"] == "성별(1)")]
    rawdata[k].reset_index(inplace=True)
    rawdata[k] = rawdata[k][:29]
    rawdata[k] = rawdata[k][['시군구별(2)', '201'+str(k+1)+'.1', '201'+str(k+1)+'.2','201'+str(k+1)+'.3','201'+str(k+1)+'.5','201'+str(k+1)+'.6','201'+str(k+1)+'.7']]
    rawdata[k].columns = list(rawdata[k].iloc[1, :])
    rawdata[k].drop(index=[0, 1, 2, 3], inplace=True)
    rawdata[k].index = rawdata[k]["시군구별(2)"]
    rawdata[k].drop(columns="시군구별(2)", inplace=True)
    rawdata[k].index.name = 2011+k
    dang = rawdata[k].iloc[:,:3]
    go=rawdata[k].iloc[:,3:]
    dang.to_excel("당뇨병_연도별/dang_by_year_"+str(2011+k)+".xlsx")
    go.to_excel("고혈압_연도별/go_by_year_"+str(2011+k)+".xlsx")

