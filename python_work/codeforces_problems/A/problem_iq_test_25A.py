n = int(input())
a = list(map(int, input().split()))

if n == 3:
    if a[0] % 2 == a[1] % 2:
        if a[2] % 2 != a[0] % 2:
            print(3)
    elif a[0] % 2 == a[2] % 2:
        print(2)
    else:
        print(1)
else:
    for i in range(n - 2):
        if a[i] % 2 != a[i + 1] % 2:
            if a[i + 1] % 2 != a[i + 2] % 2:
                print(i + 2)
            else:
                print(i + 1)
            break

# Read the input
n = int(input())
numbers = list(map(int, input().split()))

# Lists to store indices of even and odd numbers
even_indices = []
odd_indices = []

# Classify the numbers by evenness
for i in range(n):
    if numbers[i] % 2 == 0:
        even_indices.append(i + 1)  # Store 1-based index
    else:
        odd_indices.append(i + 1)  # Store 1-based index

# Find the outlier
if len(even_indices) == 1:
    print(even_indices[0])
else:
    print(odd_indices[0])
