while True:
    s=float(input())
    i=2
    n=1/i
    if s!=0.00:
        while s>n:
            i+=1;n+=1/i
        print(str(i-1)+' card(s)')
    else:
        break

import math
while True:
    s=float(input())
    if math.isclose(s,0.00,rel_tol=1e-5):  #比较浮点数与0
        break
    i=2
    n=1/i
    while s>n:
        i+=1;n+=1/i
    print(str(i-1),'card(s)')
