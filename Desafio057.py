m = ''
while m != 'M' and m != 'F':
    m = str(input('Gender: ')).upper()
    if m != 'M' and m != 'F':
        print('Invalid Gender')
    else:
        print(f'Gender: {m}')



