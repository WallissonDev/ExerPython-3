from datetime import date
actual = date.today().year
sex = str(input('Are you a man or woman?')).strip().upper()
if sex == 'MAN':
    born = int(input('Write the year you born: '))
    age = actual - born
    if age == 18:
        print(f'You have to alistate right now, youre current {age}')
    elif age < 18:
        print(f'You dont have to alistate yet, wait {18-age} years')
        print(f'You year of alistate is {born+18}')
    elif age > 18:
        print(f'Youre too late to alistate, you pass {age-18} years')
        print(f'You year of alistate is {born+18}')
elif sex == 'WOMAN':
    print('Youre a biological woman, alistate is not necessary.')
else:
    print('Unvalid Biological Gender, please insert Woman or Man, for a valid consideration.')



