# N: 삼각형의 크기

dp = []
N = int(input())
dp = [list(map(int, input().split()))]
for i in range(1, N):
    values = list(map(int, input().split()))  # 입력받는 값들
    tmp = []
    for j in range(i+1):
        if j == 0:
            tmp.append(dp[i-1][j] + values[j])
        elif j == i:
            tmp.append(dp[i-1][j-1] + values[j])
        else:
            tmp.append(max(dp[i-1][j-1] + values[j], dp[i-1][j] + values[j]))
    dp.append(tmp)

print(max(dp[N-1]))
