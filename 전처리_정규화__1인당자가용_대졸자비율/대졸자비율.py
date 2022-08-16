import pandas as pd

univ=pd.read_excel("전처리_정규화__1인당자가용_대졸자비율/교육정도별+인구(6세+이상)_계.xlsx",index_col='자치구별(2)')
univ.drop(columns=['자치구별(1)','교육정도별(1)','연령별(1)'],inplace=True)
univ
univ=univ.loc['종로구':,'2020':]
univ.index.name='2020'
univ
univ_sum=[]
for i in range(2,univ['2020'].count(),3):
    univ_sum.append(int(univ.iloc[i,]+univ.iloc[i-1,]+univ.iloc[i-2,]))
len(univ_sum)

gu=[]
for i in list(univ.index):
    if type(i)==str:
        gu.append(i)
univ_gu=pd.DataFrame(univ_sum,gu)
univ_gu.columns=['대졸이상비율']
univ_gu.index.name='2020'
univ_gu

people=pd.read_excel("전처리_정규화__1인당자가용_대졸자비율/주민등록인구(연령별_동별)_20220816173236.xlsx",index_col='동별(2)')
people.drop(index=['동별(2)','소계'],columns=['동별(1)','항목'],inplace=True)
people.index.name='2020'
people.columns=['대졸이상비율']
people_gu=people.astype(int)

univ_per_people=univ_gu/people_gu
univ_per_people['정규화']=(univ_per_people-univ_per_people.min())/(univ_per_people.max()-univ_per_people.min())
univ_per_people.to_excel("전처리_정규화__1인당자가용_대졸자비율/대졸이상비율.xlsx")
univ_per_people.sort_values('정규화')