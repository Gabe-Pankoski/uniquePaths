def uniquePaths(m: int, n: int) -> int:
    #1x1 input
    if m == 1 and n == 1:
        return 1
    #Otherwise
    layout = [ [0]*m for i in range(n) ]
    for i in range(1, m):
        layout[0][i] = 1
    for i in range(1, n):
        layout[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            layout[i][j] = layout[i-1][j] + layout[i][j-1]
    return layout[n-1][m-1]

out = uniquePaths(3, 7)
print(out)
