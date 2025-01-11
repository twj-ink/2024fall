while True:
    n=int(input())
    if n==0:
        break
    a=sorted(list(map(int,input().split())))
    b=sorted(list(map(int,input().split())))
    ai,aj,bi,bj,win,lose=0,n-1,0,n-1,0,0

    while ai<=aj and ai<n and aj>=0 and bi<n and bj>=0:
        if a[ai]>b[bi]:
            win+=1
            ai+=1
            bi+=1
        elif a[aj]>b[bj]:
            win+=1
            aj-=1
            bj-=1
        else:
            if a[ai]<b[bj]:
                lose+=1
            ai+=1
            bj-=1

        #        print(win,lose)
    print(200*(win-lose))

