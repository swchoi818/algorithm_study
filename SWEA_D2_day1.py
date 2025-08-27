t = int(input())

for i in range(t):
    cnt = int(input())
    day_price = list(map(int,input().split()))
    day_price.reverse()
    result = 0
    sell_price = 0

    for j in range(len(day_price)):
        if day_price[j] > sell_price:
            sell_price = day_price[j]
        else:
            result += sell_price - day_price[j]
    print(f"#{i+1} {result}")
