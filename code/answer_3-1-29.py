A, B, C = map(int, input().split())
water = C-(A-B)
print(water if water > 0 else 0)
