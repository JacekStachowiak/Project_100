'''
randrange([start,] stop[, krok])
randint(a, b)
Zwraca losową liczbę całkowitą N spełniającą nierówność a <= N <= b.

choice(seq)
Zwraca losowo wybrany element niepustej sekwencji seq

shuffle(x[, random])
Miesza elementy sekwencji x w miejscu. Opcjonalny argument random jest zeroargumentową funkcją zwracającą losową liczbę zmiennoprzecinkową z przedziału [0.0, 1.0). Domyślnie używana jest funkcja random().
Należy zauważyć, ze nawet dla małych wartości len(x), całkowita liczba permutacji sekwencji x jest większa, niż cykl większości generatorów liczb losowych. Oznacza to, że w przypadku długich sekwencji większość permutacji nie zostanie wygenerowana.

sample(populacja, k)
Zwraca listę o długości k zawierającą unikatowe elementy wybrane z sekwencji reprezentującej populację. Używana do wybierania losowych elementów bez zwracania. Dodano w wersji 2.3.
Zwrócona lista zawiera elementy wybrane z przekazanej jako argument populacji, jednak oryginalna populacja pozostaje niezmieniona. Lista wynikowa zawiera elementy uporządkowane w kolejności wynikającej z kolejności losowania elementów z populacji, wobec czego wszystkie podlisty listy wynikowej można również traktować jako próbki losowe. Pozwala to na podzielenie zwycięzców loterii (próbka) na głównego zwycięzcę oraz zwycięzców drugiej nagrody (podlisty).

Elementy populacji nie muszą być elementami haszowalnymi (tj. umożliwiającymi wywołanie na nich funkcji skrótu) ani elementami unikatowymi. Jeżeli populacja zawiera powtórzenia, wówczas każde wystąpienie powtarzającej się wartości może zostać wybrane w wyniku losowania.

Aby wybrać próbkę z zakresu liczb całkowitych, jako argumentu należy użyć funkcji xrange. W ten sposób uzyska się szybki i wydajny pamięciowo wybór próby z dużej populacji: sample(xrange(10000000), 60).

Następujące funkcje generują specyficzne rozkłady zmiennych losowych o wartościach rzeczywistych. Nazwy parametrów funkcji pochodzą od nazw odpowiednich zmiennych w równaniach opisujących rozkład, co jest dość powszechną matematyczną praktyką. Większość spośród tych równań można odnaleźć w tekstach dotyczących statystyki.

The following functions generate specific real-valued distributions. Function parameters are named after the corresponding variables in the distribution's equation, as used in common mathematical practice; most of these equations can be found in any statistics text.

random()
Zwraca kolejną losową liczbę zmiennoprzecinkową z zakresu [0.0, 1.0).

'''