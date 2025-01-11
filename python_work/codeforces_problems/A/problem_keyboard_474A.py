key='''qwertyuiop
asdfghjkl;
zxcvbnm,./'''
keys=key.splitlines()

x=input()
s=input()
a=''
if x=='L':
    x=1
else:
    x=-1
for i in s:
    for line_index,line in enumerate(keys):
        try:
            i_index=line.index(i)
            a+=line[i_index+x]
        except ValueError:
            pass
print(a)
