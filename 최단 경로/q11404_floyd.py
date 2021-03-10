'''
플로이드 워셜 알고리즘
All Source - All Destination
시간 복잡도: O(N^3)
'''
import sys

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
node_num = int(sys.stdin.readline().rstrip())
edge_num = int(sys.stdin.readline().rstrip())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
# (노드의 개수 + 1)의 크기로 할당하여, 노드의 번호를 인덱스로 하여 바로 리스트에 접근할 수 있도록 함
graph = [[INF] * (node_num + 1) for _ in range(node_num + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 (대각 행렬 0으로 초기화)
for i in range(1, node_num + 1):
    for j in range(1, node_num + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(edge_num):
    # src에서 des로 가는 비용은 weight라고 설정
    src, des, weight = map(int, sys.stdin.readline().rstrip().split())
    graph[src][des] = min(graph[src][des], weight)
    # 양방향일 경우 아래 한 줄 추가
    # graph[des][src] = weight

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, node_num + 1):
    for i in range(1, node_num + 1):
        for j in range(1, node_num + 1):
            # k를 지나치는 경로와, 직접 가는 경로중 더 짧은 경로로 업데이트
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행된 결과를 출력
for i in range(1, node_num + 1):
    for j in range(1, node_num + 1):
        # 도달할 수 없는 경우, 0 출력
        if graph[i][j] == INF:
            print(0, end=' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[i][j], end=' ')
    print()
