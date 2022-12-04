abc = list(map(int, input().split()))
total = 0
for dice in abc:
    total = total+(7-dice)
print(total)
