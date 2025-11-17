a, b, c = map(int, input().split())
mx = md = mn = 0
if a >= b and a >= c:
    mx = a
    if b >= c:
        md, mn = b, c
    else:
        md, mn = c, b
elif b >= a and b >= c:
    mx = b
    if a >= c:
        md, mn = a, c
    else:
        md, mn = c, a
else:
    mx = c
    if a >= b:
        md, mn = a, b
    else:
        md, mn = b, a
print(mx, md, mn)

