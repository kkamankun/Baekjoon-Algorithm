afrom collections import Counter
import sys

t = 0
s = sys.stdin.readline().rstrip()
s = s.lower()
counter = Counter(s)

for key, value in counter.items():
    if 119 <= ord(key) <= 122:
        t += value * 9
    elif 116 <= ord(key) <= 118:
        t += value * 8
    elif 112 <= ord(key) <= 115:
        t += value * 7
    elif 109 <= ord(key) <= 111:
        t += value * 6
    elif 106 <= ord(key) <= 108:
        t += value * 5
    elif 103 <= ord(key) <= 105:
        t += value * 4
    elif 100 <= ord(key) <= 102:
        t += value * 3
    elif 97 <= ord(key) <= 99:
        t += value * 2

print(t + len(s))
