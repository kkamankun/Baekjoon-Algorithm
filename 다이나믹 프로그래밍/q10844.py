# N: 수의 길이
# dp: 다이나믹 프로그래밍을 위한 2차원 리스트
# 행은 수의 길이, 열은 마지막 자리의 수를 의미, 각 요소는 수의 길이가 N이고 끝 마지막 자리가 j인 계단 수의 개수
mod = 1000000000
N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N + 1)]
for j in range(1, 10):
    dp[1][j] = 1
for i in range(2, N+1):
    for j in range(0, 10):
        if j == 0:
            dp[i][0] = dp[i-1][1] % mod
        elif j == 9:
            dp[i][9] = dp[i-1][8] % mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod

result = 0
for i in range(10):
    result += dp[N][i]
print(result % mod)

# 다른 풀이
N = int(input())
dp = [[0] * 12 for _ in range(0, N)]

for i in range(2, 11):
    dp[0][i] = 1

for r in range(1, N):
    for c in range(1, 11):
        dp[r][c] = (dp[r-1][c-1] + dp[r-1][c+1]) % 1000000000

print(sum(dp[N-1]) % 1000000000)
