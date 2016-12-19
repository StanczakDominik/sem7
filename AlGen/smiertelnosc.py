"""agentowy model śmiertelności człowieka odzwierciedlający prawo Gompesa
modelujemy ludzki genom jako 32bitowy string
agenci oddziałują przez dostępność zasobów w populacji"""
import numpy as np

genom = np.zeros(32, dtype=bool)
T = 10 # krytyczna ilosc chorób przy której trup
c = 4
b = 25 # wiek przy którym osobnik zaczyna płodzić przez kopiowanie, c potomków o tym samym składzie
genom[5] = 1 #choroba ujawniona w wieku 5 lat

def czy_zyje(genom, T=T):
    return genom.sum() < T

"""
jeśli
genom[:b] = 1
to osobnik nie dożyje na pewno wieku rozrodczego i nie przekaże swoich genów
geny przekażą tylko ci, dla których jedynki są daleko:
genom[:-T] = 1
przy przekazywaniu materiału genetycznego zachodzą mutacje (flip 0, 1)
Współczynnik Verhulsta $V$ - prawdopodobieństwo przeżycia na skutek przeludnienia
= $1 - |V(t)|/N_max$
V(t) - zasoby dostępne dla populacji, np żywność
N_max - maksymalna populacja

Zdarzają się katastroficzne okresy wymierania

9 stycznia kolokwium
16 - projekt
23 - projekt
"""
