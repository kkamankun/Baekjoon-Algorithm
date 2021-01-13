# N: 수열의 길이
# 입력받은 수열의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력
# dp: 각 원소가 포함된 수열의 가장 긴 바이토닉 수열의 길이
# 접근 방식:
# 1. 배열의 첫 번째 인덱스부터 LIS 구하기
# 2. 배열의 맨 뒤부터 거꾸로 LIS 구하기
# 3. 두 방향에서 구한 LIS 값들을 인덱스별로 합쳐서 나온 가장 큰 값에서 1을 뺀 값이 정답
N = int(input())
A = list(map(int, input().split()))
dpR = [1]*N
dpL = [1]*N
ans = list()
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:  # Right
            dpR[i] = max(dpR[i], dpR[j]+1)
for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:  # Left
            dpL[i] = max(dpL[i], dpL[j]+1)
ans = [dpR[i] + dpL[i] for i in range(N)]
print(max(ans)-1)
