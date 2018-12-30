arr = [[0, 0, 1],
       [0, 0, 1],
       [1, 0, 0]]
paths = [[0 for x in range(3)] for x in range(3)]
m, n = 3, 3
desc = [[]]
for j in range(3):
    if arr[0][j] == 1:
        paths[0][j] = 0
    else:
        paths[0][j] = 1

for i in range(3):
    if arr[i][0] == 1:
        paths[i][0] = 0
    else:
        paths[i][0] = 1


def findPaths(arr, r, c):
    global paths
    # print(paths)
    for i in range(1, 3):
        for j in range(1, 3):
            if arr[i][j] == 1:
                continue
            else:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]


findPaths(arr, 3, 3)
print(paths[2][2])
