import pandas as pd

for i in range(2012,2021):
    rawdata = pd.read_excel("서울시공체시설통계_변환_2/raw/서울시_공공체육시설_통계_"+str(i)+"년.xlsx")
    rawdata.columns = list(rawdata.iloc[0, :])
    rawdata.index = rawdata["자치구별(2)"]
    rawdata = rawdata[["육상경기장", "축구장", "테니스장", "간이운동장(동네체육시설)", '구기체육관', '수영장', '롤러스케이트장', '골프연습장']]
    rawdata = rawdata.transpose()
    rawdata = rawdata[rawdata.iloc[:, 2] == "개소 (개소)"].transpose()
    rawdata.columns = ['육상경기장', '축구장', '테니스장', '간이운동장(동네체육시설)', '구기체육관', '투기체육관', '생활체육관',
                       '전천후 게이트볼장', '수영장', '롤러스케이트장', '골프연습장']
    rawdata.drop(index="자치구별(2)", inplace=True)
    rawdata.replace("-", 0, inplace=True)
    rawdata = rawdata.astype(int)
    rawdata.drop(index='소계', inplace=True)
    rawdata.index.name=str(i)
    rawdata.to_excel("서울시공체시설통계_변환_2/data/data_"+str(i)+".xlsx")

