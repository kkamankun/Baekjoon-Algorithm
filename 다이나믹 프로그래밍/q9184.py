MAX = 21
dp = [[[0 for col in range(MAX)] for row in range(MAX)] for depth in range(MAX)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]


while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        exit()
    else:
        print('w(%d, %d, %d) = %d' % (x, y, z, w(x, y, z)))
