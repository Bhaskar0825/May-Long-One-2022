#Subscribe to channel = https://bit.ly/3F4Jxnd
for i in range(int(input())):
    X,Y = map(int,input().split())
    if (X + Y)>0:
        if X==Y:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
