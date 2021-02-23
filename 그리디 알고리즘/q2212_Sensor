n = int(input())  # 센서의 개수 N 입력받기
k = int(input())  # 집중국의 개수 K 입력받기
location_list = list(map(int, input().split()))  # 센서의 좌표 N개 입력 받기
location_list.sort()  # 오름차순 정렬

interval = []
for i in range(1, n):  # K개의 구간 설정
    interval.append(location_list[i] - location_list[i-1])

interval.sort()
# 수신 가능 영역의 길이의 합 계산
answer = 0
for i in range(n-k):
    answer += interval[i]
print(answer)
