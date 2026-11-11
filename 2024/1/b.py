from collections import Counter

left, right = [], []

with open('data.txt') as fh:
    for line in fh.readlines():
        x, y = map(int, line.split())

        left.append(x)
        right.append(y)

left.sort()
right = Counter(right)

sum = 0

for x in left:
    sum += x * right[x]

print(sum)
