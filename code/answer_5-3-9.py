N = int(input())
if N <= 9:
    print("AGC00"+str(N))
elif N <= 41:
    print("AGC0"+str(N))
else:
    print("AGC0"+str(N+1))
