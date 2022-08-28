import pandas as pd

#서울 구별 대졸자 수를 구한다
univ=pd.read_excel("./교육정도별+인구(6세+이상)_계.xlsx",index_col='자치구별(2)')
univ.drop(columns=['자치구별(1)','교육정도별(1)','연령별(1)'],inplace=True)
univ
univ=univ.loc['종로구':,'2020':]
univ.index.name='2020'
univ
univ_sum=[]
#대학,대학교,대학원 졸업자 수를 합산한다.
for i in range(2,univ['2020'].count(),3):
    univ_sum.append(int(univ.iloc[i,]+univ.iloc[i-1,]+univ.iloc[i-2,]))
len(univ_sum)

#인덱스에서 nan을 제외하고 gu 리스트에 넣는다.
gu=[]
for i in list(univ.index):
    if type(i)==str:
        gu.append(i)
#서울 구별 대졸이상인구수 데이터프레임을 만든다.
univ_gu=pd.DataFrame(univ_sum,gu)
univ_gu.columns=['대졸이상비율']#데이터프레임끼리 계산을 위해 컬럼명 변경
univ_gu.index.name='2020'
univ_gu

#서울 구별 주민등록인구를 추출한다.
people=pd.read_excel("./주민등록인구(연령별_동별)_20220816173236.xlsx",index_col='동별(2)')
people.drop(index=['동별(2)','소계'],columns=['동별(1)','항목'],inplace=True)
people.index.name='2020'
people.columns=['대졸이상비율'] #데이터프레임끼리 계산을 위해 컬럼명 변경
people_gu=people.astype(int)

#서울 구별 대졸자 비율을 구한다.
univ_per_people=univ_gu/people_gu

#서울 구별 대졸자 비율을 정규화한다.
univ_per_people['정규화']=(univ_per_people-univ_per_people.min())/(univ_per_people.max()-univ_per_people.min())
univ_per_people.to_excel("./대졸이상비율.xlsx")