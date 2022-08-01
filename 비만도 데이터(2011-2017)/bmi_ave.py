import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

aa=[]

for i in range(2011,2018):
    aa.append(pd.read_csv("비만도 데이터(2011-2017)/BMI_"+str(i)+".csv"))

ave=[]
for k in range(7):
    ave.append(aa[k]["이상"].mean())

average=pd.DataFrame(ave)
average=average.transpose()
list(average.columns)
average.columns=[2011,2012,2013,2014,2015,2016,2017]
average=average.transpose()
plt.plot(average[1:])
plt.xlabel('연도')
plt.ylabel('BMI')
plt.title("서울 BMI")
plt.savefig("비만도 데이터(2011-2017)/서울 BMI 추이.pdf")


plt.show()
qq=pd.read_excel("비만도 데이터(2011-2017)/전국 bmi 2012~.xls",index_col="Unnamed: 0")
qq=qq.transpose()

plt.plot(qq.loc[:"2017","전체"])
plt.xlabel('연도')
plt.ylabel('BMI')
plt.title("전국 BMI")
plt.savefig("비만도 데이터(2011-2017)/전국 BMI 추이.pdf")