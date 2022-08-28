import pandas as pd

#서울 구별 자동차등록 수 데이터를 추출한다.
car=pd.read_excel("./자동차등록(월별_구별)_20220816172135.xlsx",index_col='자치구별(2)')
car=pd.DataFrame(car.iloc[:,1])
car.drop(index='자치구별(2)',inplace=True)
car.columns=['서울']
car.index.name='2020'
car=car.astype(int)

#서울 구별 주민등록인구수를 추출한다.
people=pd.read_excel("./주민등록인구(연령별_동별)_20220816173236.xlsx",index_col='동별(2)')
people.index
people.drop(index='동별(2)',columns=['동별(1)','항목'],inplace=True)
people.index.name='2020'
people.columns=['서울']
people=people.astype(int)

#서울 구별 1인당 자가용 수를 구한다.
car_per_people=car/people
car_per_people.columns=['1인당 자가용 수']
car_per_people.drop(index='소계',inplace=True)
car_per_people.describe()

#서울 구별 1인당 자가용 수를 정규화한다.
car_per_people['정규화']=(car_per_people-car_per_people.min())/(car_per_people.max()-car_per_people.min())
car_per_people.to_excel("./1인당 자가용 수.xlsx")
