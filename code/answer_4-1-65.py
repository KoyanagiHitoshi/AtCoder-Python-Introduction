W, H = map(int, input().split())
if W*H % 144 == 0:
    print("16:9")
else:
    print("4:3")
