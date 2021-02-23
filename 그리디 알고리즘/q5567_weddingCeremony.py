n = int(input())  # 상근이의 동기의 수 n 입력받기
m = int(input())  # 리스트의 길이 m 입력받기
friend_list = []
for _ in range(m):
    friend_list.append(list(map(int, input().split())))

# 상근이 친구 초대
firstInv_list = []
for i in range(m):
    if friend_list[i][0] == 1:
        firstInv_list.append(friend_list[i][1])
    elif friend_list[i][1] == 1:
        firstInv_list.append(friend_list[i][0])
    else:
        pass

# 상근이 친구의 친구 초대
secondInv_list = []
for e in firstInv_list:
    for i in range(m):
        if friend_list[i][0] == e and friend_list[i][0] != 1:
            secondInv_list.append(friend_list[i][1])
        elif friend_list[i][1] == e and friend_list[i][0] != 1:
            secondInv_list.append(friend_list[i][0])
        else:
            pass


# print(firstInv_list)
# print(secondInv_list)
print(len(set(firstInv_list+secondInv_list)))
