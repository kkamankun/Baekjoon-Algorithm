# 캐릭터의 개수(N)와 올릴 수 있는 레벨 총합(K)을 입력받기
n, k = list(map(int, input().split(' ')))
# 각 캐릭터의 개별 레벨 정보를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 올린 레벨의 총합 계산
        if mid > x:
            total += mid - x
    # 레벨의 총합이 최대 총합(K)보다 큰 경우 레벨을 덜 올리기(왼쪽 부분 탐색)
    if total > k:
        end = mid - 1
    # 레벨의 총합이 최대 총합(K)보다 작은 경우 레벨을 더 많이 올리기(오른쪽 부분 탐색)
    else:
        result = mid  # 조건을 만족할 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)
