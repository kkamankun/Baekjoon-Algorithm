# N: 집의 수
# c1: 집을 빨강으로 칠하는 비용
# c2: 집을 초록으로 칠하는 내용
# c3: 집을 파랑으로 칠하는 비용
memo = []
N = int(input())
for _ in range(N):  # 초기화
    c1, c2, c3 = map(int, input().split())
    memo.append([c1, c2, c3])

for i in range(1, N):
    memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + memo[i][0]
    memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + memo[i][1]
    memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + memo[i][2]

print(min(memo[N-1][0], memo[N-1][1], memo[N-1][2]))
