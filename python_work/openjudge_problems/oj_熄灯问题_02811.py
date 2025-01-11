dx,dy=[0,0,-1,1,0],[0,-1,0,0,1]
def press(light,x,y):
    for i in range(5):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<5 and 0<=ny<6:
            light[nx][ny]^=1
def doit():
    for first_row in range(64):
        s=[row[:] for row in light]
        solution=[[0]*6 for _ in range(5)]
        for j in range(6):
            if (first_row >> j)&1:
                solution[0][j]=1
                press(s,0,j)

        for i in range(1,5):
            for j in range(6):
                if s[i-1][j]==1:
                    solution[i][j]=1
                    press(s,i,j)

        if all(s[4][j]==0 for j in range(6)):
            for i in solution:
                print(*i)

light=[[int(i) for i in input().split()] for _ in range(5)]
doit()
