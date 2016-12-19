# Strategie ewolucyjne - operator mutacji mutacji
$$\sigma(t) \to \sigma(t+1) = \sigma(t) \exp{(\eta(t))}$$

Strategie ewolucyjne nadają się najbardziej do optymalizacji wektorów w $R^k$.
# Programowanie genetyczne - John Koza
Wykorzystanie algorytmu genetycznego do "pisania" programu.

Osobnikiem jest **program**, algorytm optymalizuje jego strukturę. Robili to w LISP (LISt Processing).

> Ja się uczyłem FORTRANa.
> A potem już programowałem obiektowo, czyli studentami.

Tworzymy zbiór symboli - **atomów**, np.
* 37
* znak +
* "I love Mary"

Niektóre z tych symboli to **terminale** (inputy, outputy).
Listy zawierają:
* atomy
* inne listy

Na przykład
* L1 = (+, 3, 7) i to oznacza 3 + 7.
* L2 = (-, x, y) = x - y
* L3 = (NOT, A) = NOT A
* (*, L1 L2) = *(+3, 7)(-,x,y)

Obrazujemy to za pomocą **drzew** zamiast pętli.
* "*" (**Korzeń** drzewa)
  * "+"
    * 3 (**liść** drzewa, powinien zawierać inputy)
    * 7
  * "-"
    * x
    * y
      * ... instrukcja na y
      * "-"
        * input1
        * input2
      * "sqrt" (przykład operatora unarnego w sensie jeden output)
        * input3

Operator przesunięcia w czasie (takie `time.sleep' czy kwantowy U).
Przykład zastosowania: optymalizacja działania gracza giełdowego:
* inputy
  * kursy walut
  * transakcje
  * to samo wczoraj, bo może wpływa na dzisiejszą strategię?
  * to samo przedwczoraj

### Przykład: r = sqrt(x^2+y^2) przez PG
Program do stworzenia to funkcja sqrt(x^2 + y^2).

Atomy:
* x
* y
* sqrt
* plus
* razy
* przypisanie
1. Losujemy populację początkową.

Populacja:
* plus (sqrt(x^2) + y)
  * x
    * przypisanie
      * sqrt
        * razy
          * x
          * x
  * y
* razy
  * x
  * y
* sqrt (osobnik nieżywotny bo ma tylko jedno wejście), usuwamy
  * x
  * y

Fitness function - norma typu chi^2 od tego, co chcemy uzyskać, na jakichś ustalonych przykładach.

2. Usuwamy nieżywotne osobniki
3. **Krzyżowanie**: wybieramy po jednym węźle z dwóch drzew i zamieniamy je (przez wskaźniki!)
4. **Mutacja**: Bierzemy losowy element i wymieniamy go na inny obiekt tego samego typu (operator binarny, unarny, zmienna)


> Paweł: dopasowanie dowolnego ogólnego wzoru analitycznego do danej krzywej doświadczalnej.

> Program napisany w LISPie może przetwarzać inny program napisany w LISPie.

# Modelowanie chorób genetycznych

## Model Pennny chorób dziedziczonych genetycznie
### Starzenie się organizmu
### Hipotezy śmierci na skutek wieku
1. Ubytki telomerów
2. Niszczenie DNA przez procesy utleniania
3. Ciągłe mutacje genetyczne przenoszą się z pokolenia na pokolenie i ujawniają
   się gdy osobnik przekracza pewien wiek

### **mortality rate**, wskaźnik śmiertelności
1. historycznie najpierw:

q(a) = prawdopodobieństwo zgonu w roku a+1 dla osobnika który dożył wieku a. $q(a) \sim \exp{(ba)}$

$N(a)$ - liczba osobników w wieku a.

$$q(a) = -\frac{N(a+1) - N(a)}{N(a)} \approx -\frac{d\log{N(a)}}{da} \approx
\log{N(a)} - \log{N(a+1)}$$

Gdzie należy pamiętać że $\Delta a = 1$. I to ostatnie przyjmujemy jako nową definicję
śmiertelności:

$$q(a) = \log{N(a)} - \log{N(a+1)}$$

> źródło: $(Oliveira)^2$, Stauffer: *Evolution, Money, War and Computers*

Prawdopodobieństwo śmierci ma dip koło 15 lat, jeden niewielki koło 25 lat.
Maksima koło 0, 20, 100 (globalne) - do 100 idzie wzrost liniowy.

$$q(a) = A \exp{(b(a-x))}, b \approx 0.1/Y, x \approx 102, A \approx 11 \pm 2$$

Stała x zdaje się być stała, ale stała b zdaje się rosnąć liniowo w czasie od 1800 do teraz.
q(a) zbiega więc do funkcji schodkowej Heaviside'a.

### Model

Genom: 32 bitów, 1 bit to 1 rok życia.
Jeśli bit = 1, to w danym roku ujawnia się choroba która będzie dolegała do końca życia.
Jeśli liczba jedynek osiąga krytyczną wartość, RIP.

```import smiertelnosc```
