def factorial(N):
    if N == 0:
        return 1
    else:
        return N*factorial(N-1)


print(factorial(4))
