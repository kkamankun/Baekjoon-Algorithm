# T: 테스트 케이스의 개수
# 입력으로 반복 횟수 R, 문자열 S가 주어짐
# 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력
T = int(input())
for _ in range(T):
    R, S = input().split()
    for i in range(len(S)):
        print(S[i] * int(R), end='')
    print()
