# 0-1 배낭 문제 (0-1 knapsack problem)
# import pprint


# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
def knapsack(B, wt, val, n):
    memo = [[0] * (B + 1) for _ in range(n + 1)]  # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
    for i in range(n + 1):  # 왼쪽에서 오른쪽으로 요소를 계산하여 채워나가고
        for w in range(B + 1):  # 그 다음 행을 채워나감
            if i == 0 or w == 0:  # 첫 번째 행과 첫 번째 열은
                memo[i][w] = 0  # 0으로 초기화
            elif wt[i - 1] <= w and w - wt[i - 1] >= 0:  # 배낭의 무게한도보다 물건의 무게가 작거나 같으면
                # i번째 물건을 위해 i번째 물건의 무게를 비웠을 때의 최적해에 i번째 물건의 가치를 더한 값과
                # i-1개의 물건을 가지고 구한 전 단계의 최적해 중 큰 값 선택
                memo[i][w] = max(val[i - 1] + memo[i - 1][w - wt[i - 1]], memo[i - 1][w])
            else:  # 배낭의 무게한도보다 물건의 무게가 큰 경우 물건을 넣을 수 없으므로
                memo[i][w] = memo[i - 1][w]  # i번째 물건을 뺀 i-1개의 물건들을 가지고 구한 전 단계의 최적해의 가치 선택
    # pprint.pprint(memo)
    return memo[-1][-1]


weight = []  # 물건의 무게
value = []  # 물건의 가치
N, K = map(int, input('물품의 수와 배낭의 무게한도: ').split())  # 물품의 수 N, 배낭의 무게한도 K
print('각 물건의 무게와 해당 물건의 가치: ')
for _ in range(N):  # N개의 줄에 걸쳐 각 물건의 무게와 해당 물건의 가치를 입력받기
    W, V = map(int, input().split())  # 각 물건의 무게 W, 해당 물건의 가치 V
    weight.append(W)  # 원소 추가
    value.append(V)  # 원소 추가
# 결과 출력
print('배낭에 넣을 수 있는 물건들의 가치의 최댓값: ', knapsack(K, weight, value, N))  # 최적해의 가치 출력
