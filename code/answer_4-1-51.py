A, B, C = map(int, input().split())
water = C-(A-B)
if water > 0:
    print(water)
else:
    print(0)
