import math
a, b, c = map(int, input().split())
if a - abs(b - c) - 1 < abs(b - c) - 1:
    print(a - abs(b - c) - 1)
else:
    print(abs(b - c) - 1)