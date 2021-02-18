# 그리디 알고리즘이 통하는 활동 선택 문제
# N: 회의의 수
# 회의의 시작시간과 끝나는 시간을 입력받아 최대 사용할 수 있는 회의의 최대 개수를 출력
# '가장 먼저 끝나는 회의' 부터 선택
def q1931(inputArr):
    cnt = 0
    endTime = 0
    for i in range(len(inputArr)):
        if endTime <= inputArr[i][0]:  # 이전 회의의 끝나는 시간이 다음 회의의 시작시간 이전이라면
            endTime = inputArr[i][1]  # 다음 회의 시간 검토
            cnt += 1  # 진행 가능한 회의
    return cnt


N = int(input())
activity = []
for _ in range(N):
    si, fi = map(int, input().split())
    activity.append((si, fi))

activity.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간으로 먼저 정렬 (끝나는 시간이 같다면, 시작시간 기준으로 오름차순 정렬)
print(q1931(activity))
