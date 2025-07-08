rA = int(input('Write A metric: '))
rB = int(input('Write B metric: '))
rC = int(input('Wirte C metric: '))
if rA + rB > rC and rB + rC > rA and rC + rA > rB:
    print('Triangle Possible    ')
    if rA == rB == rC:
        print('Is a Equilateral Triangle. ')
    elif rA != rB != rC != rA:
        print('Is a Scaleneo Triangle. ')
    else:
        print('Is a Isoceles Triangle. ')
else:
    print('Its not possible to form a triangle. ')