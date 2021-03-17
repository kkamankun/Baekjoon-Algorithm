import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
  cmd = sys.stdin.readline().rstrip().split()
  if cmd[0] == 'push_front': queue.appendleft(int(cmd[1]))
  elif cmd[0] == 'push_back': queue.append(int(cmd[1]))
  elif cmd[0] == 'pop_front':
    if queue:
      print(queue[0])
      queue.popleft()
    else: print(-1)
  elif cmd[0] == 'pop_back':
    if queue:
      print(queue[-1])
      queue.pop()
    else: print(-1)
  elif cmd[0] == 'size':  print(len(queue))
  elif cmd[0] == 'empty':
    if not queue: print(1)
    else: print(0)
  elif cmd[0] == 'front':
    if queue: print(queue[0])
    else: print(-1)
  elif cmd[0] == 'back':
    if queue: print(queue[-1])
    else: print(-1)
  else: pass
