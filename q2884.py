h, m = map(int, input().split())
if(m < 45) :
    if(h-1 < 0):
        h = 24
    print(h-1, (m+60)-45)
else :
    print(h, m-45)
