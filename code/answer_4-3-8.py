K = int(input())
if K < 60:
    if K < 10:
        print("21:0"+str(K))
    else:
        print("21:"+str(K))
else:
    if K-60 < 10:
        print("22:0"+str(K-60))
    else:
        print("22:"+str(K-60))
