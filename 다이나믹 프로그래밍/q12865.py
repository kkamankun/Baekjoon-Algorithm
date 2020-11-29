# 0-1 Knapsack Problem
import sys
# import pprint


def knapsack(B, wt, val, n):
    memo = [[0] * (B + 1) for _ in range(n + 1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n + 1):
        for w in range(B + 1):  # 각 칸을 돌면서
            if i == 0 or w == 0:  # 0번째 행/열은 0으로 세팅
                memo[i][w] = 0
            elif wt[i - 1] <= w and w - wt[i - 1] >= 0:  # 점화식을 그대로 프로그램으로
                memo[i][w] = max(val[i - 1] + memo[i - 1][w - wt[i - 1]], memo[i - 1][w])  # max 함수 사용하여 큰 것 선택
            else:
                memo[i][w] = memo[i - 1][w]
    # pprint.pprint(memo)
    return memo[-1][-1]


weight = []
value = []
N, K = map(int, sys.stdin.readline().strip().split())  # 물품의 수 N, 배낭의 무게한도 K
for _ in range(N):
    W, V = map(int, sys.stdin.readline().strip().split())  # 각 물건의 무게 W, 해당 물건의 가치 V
    weight.append(W)
    value.append(V)
print(knapsack(K, weight, value, N))
