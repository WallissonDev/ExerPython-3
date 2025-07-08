valueOne = float(input('Write youre first grade note: '))
valueTwo = float(input('Wirte youre second grade note: '))
median = ( valueOne + valueTwo ) / 2
if median < 5.0:
    print(f'You reprove. Median: {median}')
elif 7.0 > median >= 5.0:
    print(f'You have to recovery, youre median is : {median}')
elif median >= 7.0:
    print(f'Youre aproved, youre median is: {median}')
