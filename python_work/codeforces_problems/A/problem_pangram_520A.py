n=int(input())
s=input().strip()
s_lower=s.lower()
if len(set(s_lower)) == 26:
    print('YES')
else:
    print('NO')
