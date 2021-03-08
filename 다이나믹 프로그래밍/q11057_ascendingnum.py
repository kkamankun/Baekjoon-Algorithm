"""
행은 수의 길이, 열은 마지막 자리의 수를 의미
각 요소는 수의 길이가 N이고 끝 마지막 자리가
j인 오르막 수의 개수
"""
mod = 10007

# 정수 N을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [[0 for _ in range(10)] for _ in range(n + 1)]

# 다이나믹 프로그래밍(Dynamic programming) 진행 (보텀업)
for i in range(0, 10):
  d[1][i] = 1
for i in range(2, n + 1):
  for j in range(0, 10):
      for k in range(0, j+1):
        d[i][j] += d[i-1][k]
        d[i][j] %= mod

result = 0
for i in range(10):
  result += d[n][i]
print(result % mod)
  
