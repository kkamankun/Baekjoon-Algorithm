# N: 계단의 개수 (N은 300이하의 자연수)
# dp[]: N번째 계단에서 얻을 수 있는 총 점수의 최댓값을 저장
# score[]: 입력 값을 배열 형태로 저장
dp = [0]
score = [0]
N = int(input())
for i in range(1, N+1):
    score.append(int(input()))
    if i == 1 or i == 2:
        dp.append(dp[i-1] + score[i])  # 1번째, 2번째 계단에서 얻을 수 있는 총 점수의 최댓값
    else:
        dp.append(max(dp[i-2], dp[i-3] + score[i-1]) + score[i])  # N번째 계단에서 얻을 수 있는 총 점수의 최댓값
print(dp[N])  # N번째 계단에서 얻을 수 있는 총 점수의 최댓값
