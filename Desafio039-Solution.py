from datetime import date
actual = date.today().year
born = int(input('Write the year you born: '))
age = actual - born
if age == 18:
    print('You have to go Military Alistation, current 18 years old')
elif age < 18:
    print(f'You dont have to go Military, until 18, wait {18-age} year')
    print(f'You have to alistate in {born+18}')
elif age > 18:
    print(f'You are too late to Military Alistation, you are {age} old!')
    print(f'You should go to alistation in {born+18}')
