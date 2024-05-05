a = int(input())
b = int(input())
if a % b != 0:
    print(b-(a % b))
else:
    print(0)
