a, b = map(int, input().split())
graph = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8],
         [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14], [7, 15]]
if [a, b] in graph:
    print("Yes")
else:
    print("No")
