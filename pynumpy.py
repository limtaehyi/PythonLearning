import numpy as np

# 배열 생성
a = np.array([1, 2, 3]) # 1차원 배열
b = np.array([(1, 2, 3), (4, , 6)]) # 2차원 배열
c = np.zeros((2, 3)) # 모든 원소가 0인 2x3 배열
d = np.full((2, 3), 7) # 모든 원소가 7인 2x3 배열

# 배열덱싱
print(b[1, 2]) # 6
print(a[:2]) # [1 2]

# 배열 변경
e = b.reshape(3,2) # 3x2 배열로 변경
print(e)

# 배열 연산
f = np.array([(1, 2), (3, 4)])
g = np.array([(5, 6), (7, 8)])

print(np.add(f, g)) # 배열 원소 간 덧셈
print(np.subtract, g)) # 배열 원소 간 뺄셈
print(np.multiply(f, g)) # 배열 원소 간 곱셈
print(np.divide(f, g)) # 배열 원소 간 나눗셈

# 배열 통계
h = np.array([(1, 2), (3, 4), (5, 6)])
print(np.min(h)) # 최소값
print(np.max(h)) # 최대값
print(np.mean(h)) # 평균값
print(np.median(h)) # 중간값
print(np.sum(h)) # 전체 원소 합

# 배열 슬라이싱
i = np.array([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])
print(i[:, 1:3]) # 2~3열만 추출
