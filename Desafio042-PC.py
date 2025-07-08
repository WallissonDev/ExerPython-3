triangle_A = int(input('Write size of A metric: '))
triangle_B = int(input('Write size of B metric: '))
triangle_C = int(input('Write size of C metric: '))
#
# The objective is to calculate the size and type of triangle.
#
possible_Triangle = triangle_A + triangle_B > triangle_C
if triangle_A == triangle_B == triangle_C:
    print('Is Equilateral Triangle. ')
elif triangle_A == triangle_B and triangle_A + triangle_B > triangle_C:
    print('Is Isoceles Triangle. ')
elif triangle_B == triangle_C and triangle_B + triangle_C > triangle_A:
    print('Is Isoceles Triangle. ')
elif triangle_A == triangle_C and triangle_C + triangle_A > triangle_B:
    print('Is Isoceles Triangle. ')
elif triangle_B + triangle_A < triangle_C or triangle_B + triangle_C < triangle_A or triangle_C + triangle_A < triangle_B:
    print('Is not a triangle.')
else:
    print('Is Escaleneo Triangle.')