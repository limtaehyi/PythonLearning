import pandas as pd

# !! -- 필수파일 -- !!
# !! -- ./data.csv -- !!

# 데이터 세트를 CSV 파일에서 불러오기
df = pd.read_csv("data.csv")

# 처음 5행을 출력
print(df.head())

# 기본 통계정보 출력
print(df.describe())

# 결측값 확인
print(df.isnull().sum())

# 지정된 열의 결측치 삭제
df = df.dropna(subset=["name"])

# 특정 열 선택
selected_column = df["name"]

# 여러 열 선택
selected_columns = df[["name", "age"]]

# 각 열별 고유 값 개수 출력
print(df.nunique())

# 특정 열의 고유 값별 범주 개수 출력
print(df["name"].value_counts())

# 특정 조건에 따라 행 필터링
threshold_value = 10
filtered_df = df[df["age"] > threshold_value]

# 특정 열을 기준으로 데이터프레임 정렬
sorted_df = df.sort_values(by="age", ascending=False)

# 데이터프레임에 새로운 열 추가
def some_function(x):
    return x * 2

#df["new_column"] = some_function(df["existing_column"])

# 데이터프레임 열 이름 변경
df = df.rename(columns={"name": "uname"})

# 결과 확인
print(df.head())
