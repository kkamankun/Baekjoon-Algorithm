# 그리디 알고리즘이 통하는 분할 가능 배낭 문제
# N: 사람의 수
# 각각의 사람에게 인사를 할 때, 잃는 체력과 얻는 체력을 입력받아
# 얻을 수 있는 최대 기쁨을 출력
# dp[n][he]는 n번째 사람에게 인사를 할 때, 체력이 he 만큼 남아있을 때의 기쁨
# N = 3
res = 0
# health = [0, 1, 21, 79]
# pleasure = [0, 20, 30, 25]
N = int(input())
health = [0] + list(map(int, input().split()))
pleasure = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(101)] for _ in range(N+1)]
dp[1][100-health[1]] = pleasure[1]
for i in range(2, N+1):
    dp[i][100-health[i]] = pleasure[i]
    for j in range(100, 0, -1):
        if j + health[i] <= 100 and dp[i-1][j+health[i]] != 0:  # i번째 사람에게 인사하는 경우
            # max(dp[i-1][(남은 체력) + (i번째 인사함으로써 소모되는 체력)], dp[i-1][남은 체력])
            dp[i][j] = max(dp[i-1][j+health[i]] + pleasure[i], dp[i-1][j])
        else:  # i번째 사람에게 인사를 안하는 경우
            dp[i][j] = max(dp[i][j], dp[i-1][j])
for k in range(100, 0, -1):
    res = max(dp[N][k], res)
print(res)
