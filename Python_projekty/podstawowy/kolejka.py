# dodajemy 45 - 55 bilet za 0 

wzrost = int(input('Jaki masz wzrost w cm? '))
age = int(input('Ile masz lat? '))    
bill = 0 # rachunek

if wzrost >= 120:
    print('Możesz jechać')
    if age < 12:
        bill = 5
        print('Cena biletu wynosi 5')
    elif age <= 18:
        bill = 7
        print('Cena biletu wynosi 7')        
    elif age >=45 and age <=55:
        bill = 0 
        print('Przejazd masz za darmo !!!')   
    else:
        bill = 12
        print('Cena biletu wynosi 12')
            
    photo = input('Do you want a photo taken? Y or N. ')
    if photo == 'Y':
        bill += 3
        
    print(f'Twój rachunek wynosi: {bill}')
    
else:
    print('Nie spełniasz warunku') 