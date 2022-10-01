ABC = [int(input()) for i in range(3)]
sorted_ABC = sorted(ABC)[::-1]
for idx in ABC:
    print(sorted_ABC.index(idx)+1)
