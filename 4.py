a = int(input())
if a % 10 == 0 or 5 <= a % 10 <= 9 or 11 <= a % 100 <= 14:
    print(a, 'попугаев')
elif a % 10 == 1:
    print(a, 'попугай')
elif 2 <= a % 10 <= 4:
    print(a, 'попугая')


