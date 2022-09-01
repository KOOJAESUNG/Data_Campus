### 1. 회귀분석
- 데이터 : [11개 자치구 정규화 데이터](https://github.com/jyoung19/Project/blob/main/Modeling/11%EA%B0%9C%20%EC%9E%90%EC%B9%98%EA%B5%AC%20%EC%A0%95%EA%B7%9C%ED%99%94%20%EB%8D%B0%EC%9D%B4%ED%84%B0.zip)
  - 1인당 자가용 수
  - 대졸 이상 비율
  - 만명당 공무원 수
  - 만명당 재정수입
  - 면적
  - 국민기초생활보장 수급자 비율
  - 인구 수
  - 재산세
  - 총 사업체 수
  - 투표율
  - 행정동 수
  
- 코드 : [입지선정 변수 선정 - 회귀분석](https://github.com/jyoung19/Project/blob/main/Modeling/%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D.ipynb)


### 2. k-means clustering
- 데이터 : [동별 정규화한 인구수, 생활보호대상자 비율 데이터](https://github.com/jyoung19/Project/blob/main/Modeling/11%EA%B0%9C%20%EC%9E%90%EC%B9%98%EA%B5%AC%20%EB%8F%99%EB%B3%84%20%EC%A0%95%EA%B7%9C%ED%99%94%ED%95%9C%20%EC%9D%B8%EA%B5%AC%EC%88%98%2C%20%EC%83%9D%ED%99%9C%EB%B3%B4%ED%98%B8%EB%8C%80%EC%83%81%EC%9E%90%20%EB%B9%84%EC%9C%A8%20%EB%8D%B0%EC%9D%B4%ED%84%B0.zip)
  - 수요보다 더 적게 지어진 11개 자치구
  
- 코드 : [11개 자치구 클러스터링, 입지선정](https://github.com/jyoung19/Project/blob/main/Modeling/11%EA%B0%9C%20%EC%9E%90%EC%B9%98%EA%B5%AC%20%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81%2C%20%EC%9E%85%EC%A7%80%EC%84%A0%EC%A0%95.ipynb)


### 3. 모델 성능 평가 (클러스터링, 입지선정)
- 데이터 : [동별 정규화한 인구수, 생활보호대상자 비율 데이터](https://github.com/jyoung19/Project/blob/main/Modeling/14%EA%B0%9C%20%EC%9E%90%EC%B9%98%EA%B5%AC%20%EB%8F%99%EB%B3%84%20%EC%A0%95%EA%B7%9C%ED%99%94%ED%95%9C%20%EC%9D%B8%EA%B5%AC%EC%88%98%2C%20%EC%83%9D%ED%99%9C%EB%B3%B4%ED%98%B8%EB%8C%80%EC%83%81%EC%9E%90%20%EB%B9%84%EC%9C%A8%20%EB%8D%B0%EC%9D%B4%ED%84%B0.zip)
  - 수요보다 더 많이 지어진 13개 자치구 + 수요만큼 지어진 1개 자치구
  
- 코드 : [모델 성능 평가](https://github.com/jyoung19/Project/blob/main/Modeling/%EB%AA%A8%EB%8D%B8%20%EC%84%B1%EB%8A%A5%20%ED%8F%89%EA%B0%80.ipynb)
