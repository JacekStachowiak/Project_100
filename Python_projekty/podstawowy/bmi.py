# kalkulator BMI --> waga i wzrost
# BMI = waga/wzrost do 2
'''
19-24 lata – BMI 19-24,
25-34 lat – BMI 20-25,
35-44 lat – BMI 21-26,
45-54 – BMI 23-28,
powyżej 65 lat – BMI 24-29.
'''

wzrost = float(input('Podaj wzrost w m: '))
waga = float(input('Podaj wagę w kg: '))

BMI = waga/wzrost**2

if BMI < 18.5:
    print(f'Twoje BMI wynosi: {round(BMI,2)} --> masz niedowagę')
elif BMI >= 18.5 and BMI <= 25:
    print(f'Twoje BMI wynosi: {round(BMI,2)} --> masz normalną wagę')
elif BMI >= 25 and BMI <= 30:
    print(f'Twoje BMI wynosi: {round(BMI,2)} --> masz nadwagę')    
elif BMI >= 30 and BMI <= 35:
    print(f'Twoje BMI wynosi: {round(BMI,2)} --> masz otyłość')
elif BMI > 35:
    print(f'Twoje BMI wynosi: {round(BMI,2)} --> masz kliniczną otyłość')            


