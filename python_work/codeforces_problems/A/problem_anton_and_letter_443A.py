s=input()
if s=='{}':
    print(0)
else:
    content=s[1:-1]
    num=content.split(', ')
    print(len(set(num)))