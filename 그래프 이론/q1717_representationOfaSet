"""
경로 압축법(Path Compression)을 통해 더욱 빠르게 작동하는
서로소 집합 알고리즘: Union-Find
두 서브트리를 계속 합치며 공통원소 파악
시간 복잡도: O(V + M(1 + log_2-M/V V)) -> V는 vertex 개수, M 은 union & find 연산의 개수
아무튼 시간 복잡도가 O(V*M) 보다는 작다.
"""
import sys
sys.setrecursionlimit(10**5)


# find 연산: 특정 원소가 속한 집합을 찾기 - 경로 압축법(Path Compression)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union 연산: 두 원소가 속한 집합을 합치기, 두 서브 트리 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (n + 1)      # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, sys.stdin.readline().rstrip().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
