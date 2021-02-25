# n, w, L 입력받기
# n: 트럭의 대수
# w: 다리의 길이
# L: 다리의 최대하중
n, w, L = map(int, input().split())

# 트럭의 무게 입력받기
truck_weight = list(map(int, input().split()))

bridge = [0] * w  # 다리의 길이만큼
time = 0  # 소요시간

while len(bridge) != 0:
    time += 1
    bridge.pop(0)
    if truck_weight:
        if sum(bridge) + truck_weight[0] <= L:  # 다리 위의 트럭의 무게와 대기중인 트럭의 무게의 합이 다리의 최대하중보다 작거나 같다면,
            bridge.append(truck_weight.pop(0))  # 다리 위에 트럭 추가
        else:  # 다리의 최대하중보다 크다면,
            bridge.append(0)  # 대기

print(time)  # 모든 트럭들이 다리를 건너는 소요시간

