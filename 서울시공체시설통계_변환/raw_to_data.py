import pandas as pd

for i in range(2010,2018):
    rawdata = pd.read_excel("raw/서울시_공공체육시설_통계_"+str(i)+"년.xls")
    rawdata.columns = list(rawdata.iloc[1, :])
    rawdata.index=rawdata["자치구"]
    rawdata = rawdata[["육상경기장", "축구장", "테니스장", "간이운동장(동네체육시설)", '구기체육관',
                       '투기체육관', '생활체육관', '수영장', '롤러스케이트장', '골프연습장']]
    rawdata = rawdata.transpose()
    rawdata = rawdata[rawdata.iloc[:,2]=="개소"].transpose()
    rawdata.drop(index="자치구",inplace=True)
    rawdata.index.name=str(i)
    rawdata.to_excel("data/data_"+str(i)+".xlsx")

