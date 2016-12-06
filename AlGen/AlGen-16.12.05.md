# Klasyfikatory
$S_i(t)$ = siła klasyfikatora
Brygada kubełkowa: system rozliczeń między klasyfikatorami.
1. Za zadanie głosu trzeba płacić, $S_i(t)$ maleje
2. Za prawidłowe zabranie głosu jest nagroda (grupa zyskuje)
3. Za milczenie (obecność w systemie) też trzeba płacić (jeśli ktoś nigdy nie zabiera głosu, grupa nie zyskuje)
4. Klasyfikatory bardziej specyficzne winny mieć pierwszeństwo

$$ S_i(t+1) = S_i(t) + R_i(t) - C_{bid} S_t S_i(t) - C_{tax} S_i(t)$$
* $R_i(t)$ - *revenue*, nagroda przyznawana dla danego klasyfikatora
* $C_bid$ - podatek obrotowy, możliwość działania, współczynnik ofert
* $S(t) = {0, 1}$ - zależnie od tego czy klasyfikator działa czy nie działa
* $C_{tax}$ - podatek który się zawsze płaci, za to że klasyfikator jest w systemie

## Przykładowa symulacja
$C_{bid} = 0.1$
$C_{tax} = 0.01$

### t = 0

Numer klasyfikatora  | Klasyfikator  | Siła   | Komunikat | Dopasowania  | Oferta | Siła (t++) | Komunikat | Dopasowanie | Oferta
--|---|---|---|---|---|---|---|---|---
1  | 01##:0000   | 200 | 0000 | Environment | 200*0.1=20 (znika do środowiska) | 200-20-2 = 178 | 0000 |-|
2  | 00#0:1100   | 200 |      |             |             | 198            |      |1| 19.8
3  | 11##:1000   | 200 |      |             |             | 198            |      |-|
4  | ##00:0001   | 200 |      |             |             | 198            |      |1| 19.8
Środowisko: 0 -> 0111. Ma 20 po pierwszej ofercie

### t = 2

Numer klasyfikatora  | Klasyfikator  | Siła   | Komunikat | Dopasowania  | Oferta | Siła (t++) | Komunikat | Dopasowanie | Oferta
--|---|---|---|---|---|---|---|---|---
1  | 01##:0000   | 215.8 | ---- |   |      | 213.6 | ---- |-|
2  | 00#0:1100   | 178.2 | 1100 |   |      | 213.8 | ---- |-|
3  | 11##:1000   | 196   | ---- | 2 | 19.6 | 174.4 | 1000 |2|17.4
4  | ##00:0001   | 178.2 | 0001 | 2 | 17.8 | 158.4 | 0001 |2|15.8
Środowisko: 0 -> 0111. Ma 20 po pierwszej ofercie

### t = 4

Numer klasyfikatora  | Klasyfikator  | Siła   | Komunikat | Dopasowania  | Oferta | Siła (t++) | Komunikat | Dopasowanie | Oferta
--|---|---|---|---|---|---|---|---|---
1  | 01##:0000   | 211.4 | ---- |   | 209.3  | 213.6 | ---- |-|
2  | 00#0:1100   | 244.9 |      |   | 242.5 | ---- |-|
3  | 11##:1000   | 155.3 |      | 2 | 153.7 | 174.4 | 1000 |2|17.4
4  | ##00:0001   | 140.6 | 0001 | 3 | 175.4 | 158.4 | 0001 |2|15.8
Środowisko: 0 -> 0111. Ma 20 po pierwszej ofercie


> Cały ten system ma na celu wyłonienie klasyfikatorów lepszych i gorszych - dążymy do zróżnicowania sił po pewnym czasie

> Pierwsze przybliżenie: wszystkie oferty które są stawiane są przyjmowane. Tak nie powinno być!

> Zespół ekspertów myślał i myślał, ustalił tylko jeden komunikat.
> Środowisko nagradza zespół temu kto zabierał głos, przez +50
> Miał

> Widzę na mnie jadący samochód na chodniku, mój odruch powinien być: uciekać na ulicę bo może tam nic
