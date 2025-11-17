a = input()
if len(a) != 4:
    print('ERROR')
elif a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[1] == a[2] or a[1] == a[3] or a[2] == a[3]:
    print('ERROR')
elif 1900 <= int(a) <= 2050:
    print('ERROR')
else:
    print('OK')