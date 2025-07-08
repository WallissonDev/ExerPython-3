age_median = 0
girls = 0
older = 0
older_name = ''
for i in range (1,5):
    name = str(input('Name: '))
    age = int(input('Age: '))
    sex = str(input('Sex[M/F]: ')).strip().upper()
    age_median += age
    if sex in 'Ff' and age < 20:
        girls += 1
    if i == 1 and sex in 'Mm':
        older = age
        older_name = name
    if sex in 'Mm' and age > older:
        older = age
        older_name = name
print(f'The name of older man: {older_name} he has {older} years.')
print(f'Group Median Age: {age_median/4}')
print(f'Womans under 20 years: {girls}')
