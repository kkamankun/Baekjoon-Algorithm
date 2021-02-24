from collections import deque
import itertools
import copy

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph_ori = []
for i in range(n):
    graph_ori.append(list(map(int, input().split())))
graph_test = copy.deepcopy(graph_ori)

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2차원 리스트에서 값이 0인 요소들의 위치 찾기
list_0 = [[i, j] for i in range(n) for j in range(m) if graph_ori[i][j] == 0]

# 2차원 리스트에서 값이 2인 요소들의 위치 찾기
list_2 = [[i, j] for i in range(n) for j in range(m) if graph_ori[i][j] == 2]


# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 연구소를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph_test[nx][ny] == 1:
                continue
            # 바이러스가 퍼진 영역으로 기록
            if graph_test[nx][ny] == 0:
                graph_test[nx][ny] = 2
                queue.append((nx, ny))
    return


# 벽 3개를 세울 수 있는 조합
answer = 0
for x in itertools.combinations(list_0, 3):

    graph_test[x[0][0]][x[0][1]] = 1  # 벽 세우기1
    graph_test[x[1][0]][x[1][1]] = 1  # 벽 세우기2
    graph_test[x[2][0]][x[2][1]] = 1  # 벽 세우기3

    # 바이러스 퍼트리기(BFS)
    for y in list_2:
        bfs(y[0], y[1])

    # 안전 영역의 크기 구하기
    size = 0
    for i in range(n):
        for j in range(m):
            if graph_test[i][j] == 0:
                size += 1

    if answer < size:
        answer = size

    graph_test = copy.deepcopy(graph_ori)

print(answer)
