kn = int(input())
ga = kn // (17 * 29)
si = (kn - ga * 17 * 29) // 29
kn = kn - ga * 17 * 29 - si * 29
if ga != 0:
    print(ga, 'галеонов')
if si != 0:
    print(si, 'сиклей')
if kn != 0:
    print(kn, 'кнатов')



