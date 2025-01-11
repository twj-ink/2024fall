def pFactors(n):
    """Finds the prime factors of 'n'"""
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1:
        pFact.append(int(num))
    return pFact

n=int(input())
s=pFactors(n)
print(s)
if len(s)!=len(set(s)):
    print('0')
else:
    print('1' if len(s)%2==0 else '-1')