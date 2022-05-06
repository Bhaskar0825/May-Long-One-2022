#Subscribe to channel = https://bit.ly/3F4Jxnd
for i in range(int(input())):
    X = int(input())
    Sugarcane = (20/100)*(X*50)
    Salt = (20/100)*(X*50)
    Rent = (30/100)*(X*50)
    print(int((X*50)-(Sugarcane+Salt+Rent)))
