import pandas as pd
import matplotlib.pyplot as plt

cummulative_fitness = pd.read_excel("공체시설_내과환자수_상관관계_분석/Cummulative_공체.xlsx",index_col="Unnamed: 0")
cummulative_fitness_sum=cummulative_fitness.loc[:,'종로구':'강동구'].sum(axis=1)


hospital_expense = pd.DataFrame()
hospital_expense.index=['환자수','요양급여비용총액','보험자부담금']
for i in range(2013,2021):
    hospital = pd.read_csv("공체시설_내과환자수_상관관계_분석/진료과목별 데이터/건강보험심사평가원_병원급이상 진료과목별 시도별 진료비 통계 "+str(i)+".csv", encoding='cp949')
    hospital=hospital.iloc[3,:]
    hospital=hospital[['환자수','요양급여비용총액','보험자부담금']]
    hospital[[1,2]]=hospital[[1,2]]/hospital[0]
    hospital_expense[i]=hospital

hospital_expense=hospital_expense.transpose()
plt.plot(cummulative_fitness_sum.loc[2013:2017,],hospital_expense.loc[2013:2017,'보험자부담금'])
plt.show()