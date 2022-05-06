#Subscribe to channel = https://bit.ly/3F4Jxnd
for i in range(int(input())):
    X,Y = map(int,input().split())
    fast = (107/100)*X
    if Y<=fast:
        print("YES")
    else:
        print("NO")
