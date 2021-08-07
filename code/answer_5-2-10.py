ABC = [int(input()) for i in range(3)]
sort_ABC = sorted(ABC)[::-1]
for abc in ABC:
    print(sort_ABC.index(abc)+1)
