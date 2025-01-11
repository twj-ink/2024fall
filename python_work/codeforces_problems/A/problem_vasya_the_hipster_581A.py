a,b=map(int,input().split())
answers=[]
ans1=min(a,b)
answers.append(ans1)
ans2=abs(a-b)//2
answers.append(ans2)
print(' '.join(map(str,answers)))