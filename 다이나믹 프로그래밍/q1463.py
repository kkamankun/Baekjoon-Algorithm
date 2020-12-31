# N: 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N
# dp: 1을 만들기 위해서 연산을 하는 횟수의 최솟값
N = int(input())
dp = [0, 0]
for i in range(2, N+1):
    dp.append(0)
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i - 1], dp[i // 3], dp[i // 2]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i-1], dp[i//3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    else:
        dp[i] = dp[i-1] + 1
print(dp[N])
