'''
1.Jeśli rok jest równomiernie podzielny przez 4, przejdź do kroku 2. Jeśli nie, przejdź do kroku 5.
2.Jeśli rok jest równomiernie podzielny przez 100, przejdź do kroku 3. Jeśli nie, przejdź do kroku 4.
3.Jeśli rok jest równomiernie podzielny przez 400, przejdź do kroku 4. Jeśli nie, przejdź do kroku 5.
4.Rok jest rokiem przestępnym (ma 366 dni).
5.Rok nie jest rokiem przestępnym (ma 365 dni).
'''

rok = int(input('Wprowadź rok '))

if rok % 4 == 0:
    if rok % 100 == 0:
        if rok % 400 == 0:
            print('To jest rok przestępny')        
        else:
            print('To nie jest rok przestęny')    
    else:
        print('To jest rok przestępny')        
else:
    print('To nie jest rok przestęny')    