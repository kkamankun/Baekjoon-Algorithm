import sys

n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
  cmd = sys.stdin.readline().rstrip().split()
  if cmd[0] == 'push':
    stack.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if stack:
      print(stack[-1])
      stack.pop()
    else:
      print(-1)
  elif cmd[0] == 'size':
    print(len(stack))
  elif cmd[0] == 'empty':
    if not stack:
      print(1)
    else:
      print(0)
  elif cmd[0] == 'top':
    if stack:
      print(stack[-1])
    else:
      print(-1)
  else:
    pass
