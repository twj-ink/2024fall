while True:
    try:
        n=input()
        sorted_n=sorted(n)
        l=len(n)
        f=True
        for i in range(1,l+1):
            num=int(n)*i
            num=str(num)
            if len(num)<l:
                num='0'*(l-len(num))+num
            if sorted(num)!=sorted_n:
                f=False
                break
        if f:
            print(n+' is cyclic')
        else:
            print(n+' is not cyclic')
    except EOFError:
        break

