n = int(input())
k = int(input())
x = 1
y = 1
a = n
A = n + 1

ryad = x
ost = k - 1
while ost != 0:
    if ryad % 2 != 0:
        if a <= ost:
            ost -= a
            ryad += 1
            x += 1
        else:
            y += ost
            ost = 0
    else:
        if A <= ost:
            ost -= A
            ryad += 1
            x += 1
        else:
            y += ost
            ost = 0
print(x, y)
