n,m = map(int,input().split())
l = [[0 for i in range(m)] for i in range(n)]
c = 0
i = 0
j = -1
while c != n*m:
    while j < m - 1 and l[i][j+1] == 0:   # move left
        j += 1
        c += 1
        l[i][j] = c
        # added rows
    while i < n - 1 and l[i+1][j] == 0:   # move down agin

       c += 1
       l[i][j] = c
    while j > 0 and l[i][j-1] == 0 :   # move right
       j -= 1
       c += 1
       l [i][j] = c
    while i > 0 and l[i - 1][j] == 0:   # двигаюсь вверх
       i -= 1
       c += 1
       l[i][j] = c
for row in l:
    print(*row)
