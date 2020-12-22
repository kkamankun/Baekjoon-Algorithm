# T: 테스트 케이스의 개수
# N: 40보다 작거나 같은 자연수 또는 0


def fibonacci(n, matrix):
    if n == 0:
        return matrix[0]
    elif n == 1:
        return matrix[1]
    else:  # n >= 2
        if matrix[n] != -1:  # 이전에 계산한 값이 있다면
            return matrix[n]  # 값을 사용하여 계산
        else:  # 이전에 계산한 값이 없다면
            matrix[n] = fibonacci(n-1, matrix) + fibonacci(n-2, matrix)  # 계산하여 저장
            return matrix[n]


memo = [0, 1]
T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print('1 0')
    elif N == 1:
        print('0 1')
    else:
        for i in range(N-1):
            memo.append(-1)
        print(fibonacci(N-1, memo), fibonacci(N, memo))
