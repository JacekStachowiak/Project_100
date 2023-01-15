
# Wymagania programowe dotyczące ekspresów do kawy
# 1. Poproś użytkownika, pytając „Co chcesz? (espresso/latte/cappuccino):”
# a. Sprawdź dane wprowadzone przez użytkownika, aby zdecydować, co dalej.
# b. Monit powinien wyświetlać się za każdym razem, gdy czynność została zakończona, np. gdy napój jest
# wydany. Monit powinien pojawić się ponownie, aby obsłużyć następnego klienta.
# 2. Wyłącz ekspres do kawy, wpisując „off” w monicie.
# a. Konserwatorzy ekspresu do kawy mogą użyć „off” jako tajnego słowa wyłączającego
# maszyna. Twój kod powinien zakończyć wykonywanie, gdy tak się stanie.
# 3. Wydrukuj raport.
# a. Gdy użytkownik wprowadzi „raport” w monicie, powinien zostać wygenerowany raport, który się pojawi
# aktualne wartości zasobów. np.
# Woda: 100 ml
# Mleko: 50 ml
# Kawa: 76g
# Pieniądze: 2,5 USD
# 4. Sprawdź, czy zasoby są wystarczające?
# a. Gdy użytkownik wybierze napój, program powinien sprawdzić, czy jest go wystarczająco dużo
# środków na zrobienie tego napoju.
# b. Np. jeśli Latte wymaga 200 ml wody, ale w urządzeniu pozostało tylko 100 ml. Powinno
# nie kontynuuj przygotowywania napoju, ale napisz: „Przepraszamy, ale nie ma wystarczającej ilości wody”.
# c. To samo powinno się stać w przypadku wyczerpania innego zasobu, np. mleko lub kawa.
# 5. Przetwarzaj monety.
# a. Jeśli są wystarczające zasoby, aby wybrać napój, program powinien
# poproś użytkownika o włożenie monet.
# b. Pamiętaj, że ćwiartki = 0,25 USD, dziesięciocentówki = 0,10 USD, grosze = 0,05 USD, grosze = 0,01 USD
# c. Oblicz wartość pieniężną wrzuconych monet. Np. 1 ćwiartka, 2 dziesięciocentówki, 1 nikiel, 2
# grosze = 0,25 + 0,1 x 2 + 0,05 + 0,01 x 2 = 0,52 USD
# 6. Sprawdź, czy transakcja się powiodła?
# a. Sprawdź, czy użytkownik wpłacił wystarczająco dużo pieniędzy, aby kupić wybrany przez siebie napój.
# Np. Latte kosztowało 2,50 $, ale włożyli tylko 0,52 $, a potem po przeliczeniu monet
# program powinien powiedzieć „Przepraszamy, to za mało pieniędzy. Pieniądze zwrócone.”.
# b. Ale jeśli użytkownik wpłaci wystarczającą ilość pieniędzy, koszt napoju zostanie dodany do kwoty
# maszynę jako zysk, co zostanie odzwierciedlone przy następnym uruchomieniu „raportu”. Np.
# Woda: 100 ml
# Mleko: 50 ml
# Kawa: 76g
# Pieniądze: 2,5 USD
# c. Jeśli użytkownik włożył za dużo pieniędzy, automat powinien zaproponować resztę.
# Np. „Oto 2,45 dolara reszty”. Zmianę należy zaokrąglić do 2 miejsc po przecinku
# miejsca.
# 7. Zrób kawę.
# a. Jeśli transakcja się powiedzie i jest wystarczająco dużo zasobów, aby zrobić napój
# wybrany przez użytkownika, należy odjąć składniki potrzebne do sporządzenia napoju
# zasoby ekspresu do kawy.
# Np. raport przed zakupem latte:
# Woda: 300 ml
# Mleko: 200 ml
# Kawa: 100g
# Pieniądze: 0 USD
# Raport po zakupie latte:
# Woda: 100 ml
# Mleko: 50 ml
# Kawa: 76g
# Pieniądze: 2,5 USD
# b. Po odjęciu wszystkich zasobów powiedz użytkownikowi „Oto twoja latte. Cieszyć się!". Jeśli
# latte było ich wyborem.