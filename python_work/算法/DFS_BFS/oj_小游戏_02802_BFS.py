from collections import deque
dx,dy=[0,-1,1,0],[-1,0,0,1]
def bfs(x1,y1,seg,dir,segs):
    q=deque()
    q.append((x1,y1,seg,dir))
    inq=set()
    inq.add((x1,y1,dir))
    while q:
        for _ in range(len(q)):
            x,y,seg,dir=q.popleft()
            if (x,y)==(x2,y2):
                segs.append(seg)
                break
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n+2 and 0<=ny<m+2 and (nx,ny,i) not in inq:
                    new_seg=seg+(1 if dir!=i else 0)
                    new_dir=i
                    if (nx,ny)==(x2,y2):
                        segs.append(new_seg)
                        continue
                    if s[nx][ny]==' ':
                        q.append((nx,ny,new_seg,new_dir))
                        inq.add((nx,ny,i))
    if segs:
        return min(segs)
    else:
        return False

idx=0
while True:
    idx+=1
    m,n=map(int,input().split())
    if {m,n}=={0}:
        break
    s=[' '*(m+2)]+[' '+input()+' ' for _ in range(n)]+[' '*(m+2)]
    print(f'Board #{idx}:')
    a=[]
    i=0
    while True:
        i+=1
        y1,x1,y2,x2=map(int,input().split())
        if {x1,x2,y1,y2}=={0}:
            break
        ans=bfs(x1,y1,0,-1,[])
        if ans:
            print(f'Pair {i}: {ans} segments.')
        else:
            print(f'Pair {i}: impossible.')
    print()