# n: 포도주 잔의 개수
# 포도주 잔에 들어 있는 포도주의 양 입력
# 최대로 마실 수 있는 포도주의 양 출력
# dp: 각 잔의 순서에 따른 최대로 마실 수 있는 포도주의 양
amount = [0]  # 포도주 잔에 들어 있는 포도주의 양
N = int(input())
for i in range(N):
    amount.append(int(input()))
dp = [0, amount[1]]
if N > 1:
    dp.append(amount[1] + amount[2])
for i in range(3, N+1):
    dp.append(max(dp[i-1], dp[i-2] + amount[i], dp[i-3] + amount[i-1] + amount[i]))
print(dp[-1])
