R, X = map(int, input().split())
if (X == 1 and 1600 <= R <= 2999) or (X == 2 and 1200 <= R <= 2399):
    print("Yes")
else:
    print("No")
