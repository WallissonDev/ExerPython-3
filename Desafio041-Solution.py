from datetime import date
born_Year = int(input('Write the year you born: '))
current_Year = date.today().year
classification_Year = current_Year - born_Year
if classification_Year <= 9:
    print('Classification: Mirim')
elif classification_Year <= 14:
    print('Classification: Child')
elif classification_Year <= 19:
    print('Classification: Junior')
elif classification_Year <= 25:
    print('Classification: Senior')
else: 
    print('Classification: Master')