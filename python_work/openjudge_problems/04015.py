while True:
    try:
        s=input()
        count=s.count('@')
        if count!=1:
            print('NO')
        else:
            if s[0]=='.' or s[0]=='@' or s[-1]=='.' or s[-1]=='@':
                print('NO')
            else:
                x=s.index('@')
                if s[x-1]=='.' or s[x+1]=='.':
                    print('NO')
                else:
                    count1=s.count('.',x,-1)
                    if count1==0:
                        print('NO')
                    else:
                        print('YES')
    except EOFError:
        break
