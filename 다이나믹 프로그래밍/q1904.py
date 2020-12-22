# N: 수열의 크기
memo = [0, 1, 2]
N = int(input())
if N == 1:
    print('1')
elif N == 2:
    print('2')
else:
    for i in range(3, N+1):
        tmp = memo[i - 1] + memo[i - 2]
        memo.append(tmp % 15746)
    print(memo[N])
