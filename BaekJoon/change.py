# 5585
price = int(input())
change = 1000-price
coin = [500,100,50,10,5,1]
count = 0
for co in coin:
    while change >= co:
        change -= co
        count += 1
print(count)
