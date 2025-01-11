#s=input()
#i=0
#try:
#    while s[i]!='h':
#        i+=1
#    i+=1
#    while s[i]!='e':
#        i+=1
#    i+=1
#    while s[i]!='l':
#        i+=1
#    i+=1
#    while s[i]!='l':
#        i+=1
#    i+=1
#    while s[i]!='o':
#        i+=1
#    print('YES')
#except IndexError:
#    print('NO')

import re
s = input()
r = re.search('h.*e.*l.*l.*o', s)
print(['YES', 'NO'][r==None])
#.匹配任意字符，.*表示任意数量个任意字符