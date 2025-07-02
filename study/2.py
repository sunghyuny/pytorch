import numpy as np

# 1. 3x3 난수 배열 생성
arr = np.random.rand(3, 3)
print("원본 배열:\n", arr)

# 2. 평균이 0.5 이상인 값만 출력
print("0.5 이상:\n", arr[arr >= 0.5])

# 3. 각 행의 합계와 평균
row_sum = arr.sum()
row_mean = arr.mean(axis=1)
row_min = arr.min(axis=1)
row_max = arr.max()
row_gps = arr.argmax(axis=1)
print("행별 최대값:", row_max)
print("행별 최소값:", row_min)
print("행별 합계:", row_sum)
print("행별 평균:", row_mean)
print("행별 최대값 인덱스:", row_gps)

# 4. 1차원으로 평탄화 & 오름차순 정렬
flattened = arr.flatten()
sorted_arr = np.sort(flattened)
print("정렬된 배열:", sorted_arr)
