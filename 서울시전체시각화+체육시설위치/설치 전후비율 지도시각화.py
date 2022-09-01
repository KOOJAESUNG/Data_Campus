import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium
import json

pd.set_option('display.max_columns', None)

#도봉구 설치 전후 비율 파일 불러오기
도봉_df = pd.read_csv('./동별 cluster파일/dobong_cluster.csv', index_col=0)

도봉_df = 도봉_df[['dong', 'cluster']]
도봉_df

#동대문구 설치 전후 비율 파일 불러오기
동대문_df = pd.read_csv('./동별 cluster파일/dongdaemun_cluster.csv', index_col=0)

동대문_df = 동대문_df[['dong', 'cluster']]
동대문_df

#동작구 설치 전후 비율 파일 불러오기
동작_df = pd.read_csv('./동별 cluster파일/dongjak_cluster.csv', index_col=0)

동작_df = 동작_df[['dong', 'cluster']]
동작_df


#강북구 설치 전후 비율 파일 불러오기
강북_df = pd.read_csv('./동별 cluster파일/gangbuk_cluster.csv', index_col=0)

강북_df = 강북_df[['dong', 'cluster']]
강북_df

#강동구 설치 전후 비율 파일 불러오기
강동_df = pd.read_csv('./동별 cluster파일/gangdong_cluster.csv', index_col=0)

강동_df = 강동_df[['dong', 'cluster']]
강동_df


#강서구 설치 전후 비율 파일 불러오기
강서_df = pd.read_csv('./동별 cluster파일/gangseo_cluster.csv', index_col=0)

강서_df = 강서_df[['dong', 'cluster']]
강서_df

#관악구 설치 전후 비율 파일 불러오기
관악_df = pd.read_csv('./동별 cluster파일/gwanak_cluster.csv', index_col=0)

관악_df = 관악_df[['dong', 'cluster']]
관악_df

#중랑구 설치 전후 비율 파일 불러오기
중랑_df = pd.read_csv('./동별 cluster파일/jungnang_cluster.csv', index_col=0)

중랑_df = 중랑_df[['dong', 'cluster']]
중랑_df

#중랑구 설치 전후 비율 파일 불러오기
#중랑_df['dong'] = 중랑_df['dong'].str.replace('.', '.', )
중랑_df

#노원구 설치 전후 비율 파일 불러오기
노원_df = pd.read_csv('./동별 cluster파일/nowon_cluster.csv', index_col=0)

노원_df = 노원_df[['dong', 'cluster']]
노원_df

#노원_df['dong'] = 노원_df['dong'].str.replace('.', '.', )
노원_df


#성북구 설치 전후 비율 파일 불러오기
성북_df = pd.read_csv('./동별 cluster파일/seongbuk_cluster.csv', index_col=0)

성북_df = 성북_df[['dong', 'cluster']]
성북_df


#성동구 설치 전후 비율 파일 불러오기
성동_df = pd.read_csv('./동별 cluster파일/seongdong_cluster.csv', index_col=0)

성동_df = 성동_df[['dong', 'cluster']]
성동_df

#성동_df['dong'] = 성동_df['dong'].str.replace('.', '.', )
성동_df



# 11개 자치구 (동, 클러스터) 데이터 합치기

df_merge = pd.concat([도봉_df, 동대문_df, 동작_df, 강북_df, 강동_df, 강서_df, 관악_df, 중랑_df, 노원_df, 성북_df, 성동_df], axis = 0)
df_merge

# 공공체육시설 설치 전(ratio_before)과 후(ratio_after)의 인구 만명당 공체시설 비율 데이터 불러오기

ratio_df = pd.read_excel('전후비율 모두 합침.xlsx', index_col=0)
ratio_df = ratio_df.rename(columns={'동':'dong'})
ratio_df

# 동별로 중심점의 위도, 경도 데이터 불러오기

ll_df = pd.read_csv('./서울 위도경도.csv', encoding='cp949', index_col=0)
ll_df = ll_df.rename(columns={'읍면동':'dong', '위도':'latitude', '경도':'longitude'})
ll_df


# 동을 기준으로 데이터프레임 합치기

df_new = pd.merge(df_merge, ratio_df, on='dong')
df_new


# 동을 기준으로 데이터프레임 합치기

df_all = pd.merge(df_new, ll_df, on='dong')
df_all


with open('./skorea_submunicipalities_geo_simple.json', mode='rt', encoding='utf-8') as f:
   geo = json.loads(f.read())
   f.close()


# # 2. 마커 표시

# ## 2-1. 클러스터별로 설치 개수만큼 마커 표시


# ### 1. 노원구

# 노원구에서 공공체육시설의 추가 설치가 필요한 동

노원_lst = ['월계1동', '상계9동', '하계1동', '월계2동', '상계1동', '상계6.7동', '공릉1동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 노원_lst:
    print(df_all.loc[[i]].index)


노원_num = df_all.loc[[131, 132, 134, 136, 141, 145]]
노원_num


# 상계6.7동 (누락된 데이터 추가)
노원_num.loc[146] = ['상계6.7동', 2, 0.109697, 0.219394, 37.654843, 127.066965]
노원_num


# ### 2. 강북구

# 강북구에서 공공체육시설의 추가 설치가 필요한 동

강북_lst = ['수유2동', '송중동', '인수동', '삼각산동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 강북_lst:
    print(df_all.loc[[i]].index)

강북_num = df_all.loc[[47, 51, 53, 55]]
강북_num


# ### 3. 관악구
# 관악구에서 공공체육시설의 추가 설치가 필요한 동

관악_lst = ['난곡동', '삼성동', '청림동', '미성동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 관악_lst:
    print(df_all.loc[[i]].index)

관악_num = df_all.loc[[96, 113, 114, 115]]
관악_num


# ### 4. 도봉구
# 도봉구에서 공공체육시설의 추가 설치가 필요한 동

도봉_lst = ['방학2동', '창5동', '쌍문2동', '쌍문1동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 도봉_lst:
    print(df_all.loc[[i]].index)

도봉_num = df_all.loc[[0, 1, 5, 11]]
도봉_num


# ### 5. 강서구
# 강서구에서 공공체육시설의 추가 설치가 필요한 동

강서_lst = ['화곡4동', '방화1동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 강서_lst:
    print(df_all.loc[[i]].index)

강서_num = df_all.loc[[82, 90]]
강서_num


# ### 6. 강동구

# 강동구에서 공공체육시설의 추가 설치가 필요한 동

강동_lst = ['암사1동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 강동_lst:
    print(df_all.loc[[i]].index)

강동_num = df_all.loc[[61]]
강동_num


# ### 7. 동작구
# 동작구에서 공공체육시설의 추가 설치가 필요한 동

동작_lst = ['노량진1동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 동작_lst:
    print(df_all.loc[[i]].index)

동작_num = df_all.loc[[28]]
동작_num


# ### 8. 성동구
# 성동구에서 공공체육시설의 추가 설치가 필요한 동

성동_lst = ['금호2.3가동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 성동_lst:
    print(df_all.loc[[i]].index)

# 금호2.3가동 (누락된 데이터 추가)

성동_num = pd.DataFrame({'dong':['금호2.3가동'],
                       'cluster':2,
                       'ratio_before':0.159117,
                       'ratio_after':0.238675,
                       'latitude':37.553257,
                       'longitude':127.020896})
성동_num


# ### 9. 동대문구
# 동대문구에서 공공체육시설의 추가 설치가 필요한 동

동대문_lst = ['이문1동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 동대문_lst:
    print(df_all.loc[[i]].index)

동대문_num = df_all.loc[[23]]
동대문_num


# ### 10. 중랑구
# 중랑구에서 공공체육시설의 추가 설치가 필요한 동

중랑_lst = ['신내1동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 중랑_lst:
    print(df_all.loc[[i]].index)

중랑_num = df_all.loc[[127]]
중랑_num


# ### 11. 성북구
# 성북구에서 공공체육시설의 추가 설치가 필요한 동

성북_lst = ['장위1동', '월곡2동']

for i in range(len(df_all)):
  if df_all['dong'][i] in 성북_lst:
    print(df_all.loc[[i]].index)

성북_num = df_all.loc[[158, 159]]
성북_num


# ## 공공체육시설 위치 점찍기
import pandas as pd
import folium

coordinate_com = pd.DataFrame()#체육시설수가 충족된 구
coordinate_yet=pd.DataFrame()#체육시설수가 충족되지 않은 구
gu_complete = ['금천구',
               '광진구', '양천구', '구로구', '영등포구', '서초구', '강남구', '송파구','마포구','서대문구','용산구','은평구','종로구','중구']
gu_yet = ['강북구', '강서구', '동작구','관악구', '강동구', '성동구', '동대문구', '중랑구','성북구','도봉구','노원구']

#데이터 전처리
for i in gu_complete:
    exercise = pd.read_excel("./구별파일/" + i + ".xlsx", sheet_name='Sheet2')
    while 1:
        if '위도' in list(exercise.columns):
            break
        else:
            exercise.reset_index()
            exercise.columns = list(exercise.iloc[0, :])
            exercise = pd.DataFrame(exercise.iloc[1:, :])
    print(exercise)
    exercise.reset_index()
    exercise = exercise.loc[:, ['위도', '경도']]
    coordinate_com = pd.concat([coordinate_com, exercise], ignore_index=True)

for i in gu_yet:
    exercise = pd.read_excel("./구별파일/" + i + ".xlsx", sheet_name='Sheet2')
    while 1:
        if '위도' in list(exercise.columns):
            break
        else:
            exercise.reset_index()
            exercise.columns = list(exercise.iloc[0, :])
            exercise = pd.DataFrame(exercise.iloc[1:, :])
            print("ok")
    exercise.reset_index()
    exercise = exercise.loc[:, ['위도', '경도']]
    coordinate_yet = pd.concat([coordinate_yet, exercise], ignore_index=True)

#위도,경도가 뒤바뀐 구 수정
for k in range(len(coordinate_com)):
    if coordinate_com.iloc[k, 0] < 100:
        temp = coordinate_com.iloc[k, 0]
        coordinate_com.iloc[k, 0] = coordinate_com.iloc[k, 1]
        coordinate_com.iloc[k, 1] = temp

for k in range(len(coordinate_yet)):
    if coordinate_yet.iloc[k, 0] < 100:
        temp = coordinate_yet.iloc[k, 0]
        coordinate_yet.iloc[k, 0] = coordinate_yet.iloc[k, 1]
        coordinate_yet.iloc[k, 1] = temp

y_com = coordinate_com['위도']
x_com = coordinate_com['경도']
y_yet=coordinate_yet['위도']
x_yet=coordinate_yet['경도']

#위도,경도만 추출
coords_com = []
coords_yet=[]
for i in range(len(coordinate_com)):
    xx = x_com[i]
    yy = y_com[i]
    coords_com.append([xx, yy])
for i in range(len(coordinate_yet)):
    xx = x_yet[i]
    yy = y_yet[i]
    coords_yet.append([xx, yy])


# 자치구별 추가 공공체육시설 설치 전후의 인구수대비 체육시설 수 비율을 넣어둔 데이터 가져오기
kangbuk = pd.read_excel('./강북구 전후비율.xlsx')
kangseo = pd.read_excel('./강서구 전후비율.xlsx')
gwanak = pd.read_excel('./관악구 전후비율.xlsx')
dobong = pd.read_excel('./도봉구 전후비율.xlsx')
dongjak = pd.read_excel('./동작구 전후비율.xlsx')
seongbuk = pd.read_excel('./성북구 전후비율.xlsx')
kangdong = pd.read_excel('./강동구 전후비율.xlsx')
nowon = pd.read_excel('./노원구 전후비율.xlsx')
dongdaemun = pd.read_excel('./동대문구 전후비율.xlsx')
seongdong = pd.read_excel('./성동구 전후비율.xlsx')
jungnang = pd.read_excel('./중랑구 전후비율.xlsx')

# 데이터 모두 합치기
seoul_less = pd.concat([kangbuk, kangseo, gwanak, dobong, dongjak, seongbuk, kangdong, nowon, dongdaemun, seongdong, jungnang], axis = 0).reset_index(drop = True)
seoul_less

# 지도 시각화하는 데에 필요한 동과 색을 칠할 전/후 비율 데이터만을 가져오기
data = seoul_less[['동', 'ratio_before', 'ratio_after']]
data


# 행정동 별 boundary 그려놓은 지도 구축
seoul = folium.Map(location=[37.541, 126.986], zoom_start=12, tiles='cartodbpositron')

with open('./skorea_submunicipalities_geo_simple.json' , mode='rt', encoding='utf-8') as f:
   geo = json.loads(f.read())
   f.close()

folium.GeoJson(geo, name='korea_provinces').add_to(seoul)


# json파일과 동이름 맞추기
data['동'] = data['동'].str.replace('.', '·', )
data




##시각화
seoul = folium.Map(location=[37.541, 126.986], zoom_start=11.3, tiles='cartodbpositron') # 서울 지도



folium.Choropleth(
    geo_data = geo, # 행정동 별로
    data = data,    # 사용할 데이터
    columns = ['동', 'ratio_before'], # 사용할 열
    key_on = 'feature.properties.name', # 데이터와 매칭될 json파일의 속성
    legend_name = 'ratio_before',
    fill_color = 'OrRd',
    nan_fill_color = 'white',
    fill_opacity = 1,
    nan_fill_opacity=0.2
).add_to(seoul)



# marker_cluster = MarkerCluster().add_to(seoul)
#
# for i in range(len(coords_com)):
#     folium.Circle(
#         location=tuple(coords_com[i]),
#         radius=50,
#         color='blue',
#         fill='crimson',
#     ).add_to(marker_cluster)
# for i in range(len(coords_yet)):
#     folium.Circle(
#         location=tuple(coords_yet[i]),
#         radius=50,
#         color='red',
#         fill='crimson',
#     ).add_to(marker_cluster)
# for i in range(len(coords_com)):
#     folium.Circle(
#         location=tuple(coords_com[i]),
#         radius=50,
#         color='blue',
#         fill='crimson',
#     ).add_to(seoul)
for i in range(len(coords_yet)):
    folium.Circle(
        location=tuple(coords_yet[i]),
        radius=50,
        color='green',
        fill='crimson',
    ).add_to(seoul)
#seoul.save("체육시설위치+입지선정.html")


#seoul = folium.Map(location=[37.651461111, 127.05833333], zoom_start=12, tiles='cartodbpositron')

# folium.Choropleth(
#     geo_data=geo,
#     data=df_all,
#     columns=['dong', 'ratio_after'],
#     key_on='properties.name',
#     # fill_color = 'OrRd',
#     # nan_fill_color = 'white',
#     # fill_opacity = 1,
#     legend_name='공공체육시설 설치 이후 인구 만명당 체육시설 수(비율)'
# ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 노원_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='orange'),
        tooltip=dong + " (노원구 : 7개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 강북_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='blue'),
        tooltip=dong + " (강북구 : 4개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 관악_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='green'),
        tooltip=dong + " (관악구 : 4개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 도봉_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='purple'),
        tooltip=dong + " (도봉구 : 4개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 강서_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='red'),
        tooltip=dong + " (강서구 : 2개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 강동_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='darkred'),
        tooltip=dong + " (강동구 : 1개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 동작_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='lightred'),
        tooltip=dong + " (동작구 : 1개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 성동_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='gray'),
        tooltip=dong + " (성동구 : 1개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 동대문_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='lightblue'),
        tooltip=dong + " (동대문구 : 1개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 중랑_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='pink'),
        tooltip=dong + " (중랑구 : 1개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)

for index, dong, cluster, ratio_before, ratio_after, latitude, longitude in 성북_num.itertuples():
    folium.map.Marker(
        [latitude, longitude],
        popup=dong,  # 마커 클릭시 표현될 문구
        icon=folium.Icon(color='darkpurple'),
        tooltip=dong + " (성북구 : 2개)"  # 마커에 마우스를 올릴시 표현될 문구
    ).add_to(seoul)


seoul.save("./서울시전체시각화+현재공체시설위치.html")