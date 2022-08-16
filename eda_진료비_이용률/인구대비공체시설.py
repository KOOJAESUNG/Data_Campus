import pandas as pd
#import os
#os.chdir(r'사용할 파일 디렉토리')

# 인구수 데이터 전처리
data = pd.read_excel('eda_진료비_이용률/행정구역_시군구_별__성별_인구수_2009-2019.xlsx')
people = pd.DataFrame()
people['지역'] = data['행정구역(시군구)별']
for i in range(2009, 2020):
  people[str(i)] = data[str(i)]
people = people.drop([0, 1], axis = 0).reset_index(drop = True) # 이렇게 만들어진 people은 wide form 데이터
# 다루기 쉬운 narrow form 데이터로 바꿔주기 위해 데이터 melt 이거 for문으로 구현가능한 사람.. 변수명에 i 들어가서 잘 안 됨..
people_2009 = people.melt(id_vars = '지역', value_vars = '2009')
people_2010 = people.melt(id_vars = '지역', value_vars = '2010')
people_2011 = people.melt(id_vars = '지역', value_vars = '2011')
people_2012 = people.melt(id_vars = '지역', value_vars = '2012')
people_2013 = people.melt(id_vars = '지역', value_vars = '2013')
people_2014 = people.melt(id_vars = '지역', value_vars = '2014')
people_2015 = people.melt(id_vars = '지역', value_vars = '2015')
people_2016 = people.melt(id_vars = '지역', value_vars = '2016')
people_2017 = people.melt(id_vars = '지역', value_vars = '2017')
people_2018 = people.melt(id_vars = '지역', value_vars = '2018')
people_2019 = people.melt(id_vars = '지역', value_vars = '2019')
people_final = pd.concat([people_2009, people_2010, people_2011, people_2012, people_2013, people_2014, people_2015, people_2016, people_2017, people_2018, people_2019]).reset_index(drop = True)
people_final.columns = ['지역', 'year', 'people']

# 지역별 면적 데이터 전처리
data = pd.read_excel('eda_진료비_이용률/지역별_면적_20220804110648.xlsx')
df_prep = data.iloc[16:, :].reset_index(drop = True)
ground = pd.DataFrame()
ground['지역'] = people_final['지역']
for i in range(2009, 2020):
  ground[str(i)] = df_prep[str(i)]
ground_2009 = ground.melt(id_vars = '지역', value_vars = '2009')
ground_2010 = ground.melt(id_vars = '지역', value_vars = '2010')
ground_2011 = ground.melt(id_vars = '지역', value_vars = '2011')
ground_2012 = ground.melt(id_vars = '지역', value_vars = '2012')
ground_2013 = ground.melt(id_vars = '지역', value_vars = '2013')
ground_2014 = ground.melt(id_vars = '지역', value_vars = '2014')
ground_2015 = ground.melt(id_vars = '지역', value_vars = '2015')
ground_2016 = ground.melt(id_vars = '지역', value_vars = '2016')
ground_2017 = ground.melt(id_vars = '지역', value_vars = '2017')
ground_2018 = ground.melt(id_vars = '지역', value_vars = '2018')
ground_2019 = ground.melt(id_vars = '지역', value_vars = '2019')
df_ground = pd.concat([ground_2009, ground_2010, ground_2011, ground_2012, ground_2013, ground_2014, ground_2015, ground_2016, ground_2017, ground_2018, ground_2019]).reset_index(drop = True)
df_ground = df_ground.dropna(axis = 0).reset_index(drop = True)
df_ground.columns = ['지역', 'year', '면적'] # narrow form

# 공공체육시설 수 데이터 전처리
data_1 = pd.read_excel('eda_진료비_이용률/체육시설_2009_2015.xlsx')
data_2 = pd.read_excel('eda_진료비_이용률/체육시설_2016_2019.xlsx')
data = pd.merge(data_1, data_2)
data_plot = pd.DataFrame()
for i in range(2009, 2020):
  data_plot['지역'] = data['소재지(시군구)별(1)']
  data_plot[str(i)] = data[str(i)]
data_plot = data_plot.dropna(axis = 0).drop([0, 1, 2, 3, 4], axis = 0).reset_index(drop = True) # wide form
df_2009 = data_plot.melt(id_vars = '지역', value_vars = '2009')
df_2010 = data_plot.melt(id_vars = '지역', value_vars = '2010')
df_2011 = data_plot.melt(id_vars = '지역', value_vars = '2011')
df_2012 = data_plot.melt(id_vars = '지역', value_vars = '2012')
df_2013 = data_plot.melt(id_vars = '지역', value_vars = '2013')
df_2014 = data_plot.melt(id_vars = '지역', value_vars = '2014')
df_2015 = data_plot.melt(id_vars = '지역', value_vars = '2015')
df_2016 = data_plot.melt(id_vars = '지역', value_vars = '2016')
df_2017 = data_plot.melt(id_vars = '지역', value_vars = '2017')
df_2018 = data_plot.melt(id_vars = '지역', value_vars = '2018')
df_2019 = data_plot.melt(id_vars = '지역', value_vars = '2019')
df = pd.concat([df_2009, df_2010, df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019]).reset_index(drop = True)
df.columns = ['지역', 'year', 'value'] # narrow form

# 공원 수의 경우 필요 연도의 데이터 모두 불러온 후, 위의 data_1, data_2 합친 것과 같은 방식 이용해서 합쳐주면 될 거 같아요!
# 하고 전처리 과정 모두 동일하게 진행하고 df_park 정도의 이름으로 narrow form 데이터 만들어주고 밑의 df_final에 합쳐주기!

# 인구 대비 공체시설
df_temp = pd.merge(df, people_final, on = ['지역', 'year'])
df_final = pd.merge(df_temp, df_ground, on = ['지역', 'year'])
df_final['ratio'] = df_final['value'].copy()
for i in range(len(df_final)):
    try:
        df_final['ratio'][i] = int(df_final['value'][i])/int(df_final['people'][i])
    except:
        df_final['ratio'][i] = 0

df_final[df_final['지역']=='서울특별시']

df_final[df_final['지역']=='서울특별시'].reset_index().drop(columns='index').to_excel("eda_진료비_이용률/인구대비공체시설_서울.xlsx")