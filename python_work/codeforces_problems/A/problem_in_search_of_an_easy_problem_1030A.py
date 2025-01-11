n=int(input().strip())
answers=list(map(int,input().split()))
if 1 in answers:
    print('HARD')
else:
    print('EASY')