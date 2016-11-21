import numpy as np
np.random.seed(0)
N = 100
#prostszy przykład z Goldberga
#populacja = np.array([[0,1,1,0,1],
#                      [0,1,0,0,0],
#                      [1,0,0,1,1],
#                      [1,1,0,0,0]])

populacja = np.random.randint(2, size=((N, 5)))

for generacja in range(10):
    # reprodukcja
    # print(populacja)
    wartości = np.sum(populacja, axis=1) + 1 # jesli populacja to same 0, bedzie 1/0
    # print(wartości)
    suma_wartosci = wartości.sum()
    print(wartości.max())
    ułamki = wartości / suma_wartosci
    print(ułamki)
    dystrybuanta = np.cumsum(ułamki)
    nowa_populacja = np.empty((N,5))
    # print(dystrybuanta)
    for i in range(N):
        x = np.random.random()
        x_przedzialow = x > dystrybuanta
        indeks = x_przedzialow.sum()
        wylosowany_osobnik = populacja[indeks]
        # print(x, x_przedzialow, indeks, wylosowany_osobnik)
        nowa_populacja[i] = populacja[indeks]
    # print(nowa_populacja)


    #krzyżowanko
    #skojarzyć w pary JAKOŚ LOL
    jeszcze_nowsza_populacja = nowa_populacja.copy()
    prawdopodobienstwo_crossover=0.1
    for i in range(0, N, 2):
        if i + 1 < N and np.random.random() < prawdopodobienstwo_crossover:
            # P. doradza kazirodztwo jako b. dobrą metaforę 
            cut_point = np.random.randint(0,5) #do sprawdzenia
            a, b = nowa_populacja[i, cut_point:], nowa_populacja[i+1, cut_point:]
            # print(a,b)
            jeszcze_nowsza_populacja[i+1, cut_point:], jeszcze_nowsza_populacja[i, cut_point:] = a, b
    # print(jeszcze_nowsza_populacja)

    #mutacyjki

    prawdopodobienstwo_mutacja = 0.01
    mutacje = np.random.random((N,5)) < prawdopodobienstwo_mutacja
    jeszcze_nowsza_populacja += mutacje
    jeszcze_nowsza_populacja %= 2
    #
    # for i in range(N):
    #     if np.random.random() < prawdopodobienstwo_mutacja:
    #         indeks = np.random.randint(0,5)
    #         c = jeszcze_nowsza_populacja[i, indeks]
    #         jeszcze_nowsza_populacja[i, indeks] = 1 - c

    # print(jeszcze_nowsza_populacja)

    populacja = jeszcze_nowsza_populacja[:]

print(populacja)
