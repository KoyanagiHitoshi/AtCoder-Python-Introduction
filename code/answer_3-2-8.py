A, B = map(int, input().split())
count, outlet = 0, 1
while outlet < B:
    outlet = outlet-1
    outlet = outlet+A
    count = count+1
print(count)
