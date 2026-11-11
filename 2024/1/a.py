left, right = [], []

with open('data.txt') as fh:
    for line in fh.readlines():
        x, y = map(int, line.split())

        left.append(x)
        right.append(y)

left.sort()
right.sort()
sum = 0

for x, y in zip(left, right):
    sum += abs(x - y)

print(sum)
