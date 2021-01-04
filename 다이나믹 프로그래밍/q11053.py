# N: 수열 A의 크기
# 수열 A의 요소를 입력받고 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력
# dp: 각 원소가 포함된 수열의 가장 긴 증가하는 부분 수열의 길이
N = int(input())
A = list(map(int, input().split()))
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
