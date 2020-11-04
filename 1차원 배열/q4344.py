c = int(input())
for i in range(c):
    mean = 0
    s = 0
    cnt = 0
    A = list(map(int, input().split()))
    for j in range(1, len(A)):
        s += A[j]
    mean = s / A[0]
    # print("sum: ", mean)
    for k in range(1, len(A)):
        if mean < A[k]:
            cnt += 1
    # print("cnt: ", cnt)
    print("%.3f%%" % (round(cnt / (len(A) - 1), 5) * 100))
