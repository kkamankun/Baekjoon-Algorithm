# T: 테스트 케이스의 개수
# N: 수열의 크기
T = int(input())
for _ in range(T):
    memo = [0, 1, 1, 1]
    N = int(input())
    if N == 1 or N == 2 or N == 3:
        print('1')
    else:
        for i in range(4, N+1):
            tmp = memo[i - 2] + memo[i - 3]
            memo.append(tmp)
        print(memo[N])
