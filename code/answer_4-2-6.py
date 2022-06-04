X, Y = input().split(".")
print(X+"-" if 0 <= int(Y) <= 2 else X if 3 <= int(Y) <= 6 else X+"+")
