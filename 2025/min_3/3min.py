from itertools import combinations as x

with open("3.txt", "r") as z:
    rs = list(z.readlines())


def d(s, x):
    s = s * 10 + x[0]
    return d(s, x[1:]) if len(x) > 1 else s


def b(r, f):
    h = int(r[0])
    t = r[1:]

    if len(t) > f:
        j = b(t, f)

        p = [j]
        for q in x(j, f - 1):
            p.append(tuple([h] + list(q)))
        return max(p)
    else:
        return tuple([h] + list(map(int, t[:-1])))


for f in [2, 12]:
    s = 0
    for r in rs:
        j = b(r, f)
        s += d(0, j)

    print(s)
