# Przestrzeń wymiarowa
  Możemy zdefiniować **przestrzeń wymiarową** $\Pi$ - zbiór elementów {A, B, C} -
  metry, kilogramy, sekundy lub ich liczbowe przeskalowania - z następującą algebrą:
    1. Każdym dwóm elementom (A, B) należącym do $\Pi$ przyporządkowany jest element
    ab też w $\Pi$ zwany ich iloczynem.
    Działanie mnożenia jest przy tym:
      1. Symetryczne AB = BA
      2. (AB)C = A(BC)
      3. Istnieje element rozwiązujący $\forall_{A, B \in \Pi} \exists_X AX = B$
    2. W przestrzeni $\Pi$ określone jest działanie potęgowania:
      $$\forall_{A \in \Pi} \forall_{\a in R} A ^ a \in \Pi$$
      Działanie to ma następujące własności:
      $$A^{a+b} = A^a A^b$$
      $$(A^a)^b = A^{ab}$$
      $$(AB)^a = A^a B^a$$
      $$A^0 = 1 = Q \in R_+$$
      Zatem liczby rzeczywiste dodatnie  stanowią podprzestrzeń wielkości bezwymiarowych.
    3. Istnieje element jednostkowy
      $$AI = IA = A$${

# Analiza wymiarowa
  Przestrzeń wymiarowa $\Pi$ ma własności przestrzeni wektorowej, gdzie mnożenie wielkości
  wymiarowych to działanie składania wektorów. Dlatego analogicznie do pojęcia niezależności
  liniowej wektorów wprowadzamy pojęcie **niezależności wymiarowej** *wielkości wymiarowych*.

  Def. wielkości $A_1, A_2, ...., A_n \in \Pi$ są wymiarowo niezależne (np. kg, m, s)
  jeżeli $A_1^{a_1} A_2^{a_2} A_3^{a_3} ... A_n^{a_n} = Q \in R_+ \implies a_1 = a_2 = ... a_n = 0 $$
  (analogia do $\lambda_1 v_1 + \lambda^2 v_2 + \lambda_n v_n = 0$ z mnożeniem zastępującym dodawanie i potęgowaniem zastępującym mnożenie)

  To mówi tyle, że z wielkości wymiarowo niezależnych nie da się utworzyć wielkości bezwymiarowej Q przy $a_i \neq 0$.

### Baza tej przestrzeni
  W przestrzeni $\Pi$ można wyznaczyć maksymalną liczbę wymiarowo niezależnych elementów
  $X_j, j = 1, 2, ...$, które tworzą **bazę** dla $\Pi$.
  Każdy element A można przedstawić jednoznacznie jako $Q \prod_{j=1}^n X_j^{a_j}$

  W przestrzeni wymiarowej można oczywiście wyznaczyć wiele różnych baz, wśród nich wyróżniają się bazy
  w postaci układów jednostek podstawowych *(jako **ortogonalne**)*, np.
  * trójwymiarowy układ podstawowy cgs
  * wielowymiarowy układ międzynarodowy SI
  * układ MKS

    Można tworzyć dowolne bazy na podstawie układu jednostek podstawowych.
  Niech elementy wymiarowe $A_i$ będą kandydatami na utworzenie bazy w przestrzeni $\Pi$
  z układem jednostek podstawowych $X_i$. Należy dowieść, że są one wymiarowo niezależne.

  Zapiszmy $A_i$ w bazie $X_i$: $A_i = Q_i \prod_{j=1}^n X_j^{a_{ij}}$

  W przestrzeniach wektorowych przejście $e_i' = B_{ij}e_j$ wymaga nieosobliwości tego przekstrzałcenia,
  więc $\det B_{ij} \neq 0$.

  Zatem aby $A_i$ były bazą dla $\Pi$, wystarczy by $\det{a_{ij}} \neq 0$.

### przykład
* N - moc
* D - średnica układu
* $\mu$ - współczynnik lepkości

Sprawdźmy czy mogą tworzyć bazę dla $\Pi$. Zapiszmy je w cgs.

* $[N] = [F * v] = [m * a * v] = g * cm/s * cm/s^2 = g * cm^2 * s^-3 = x_1_^2 x_2^1 x_3^{-3}$
* $[D] = [cm] = x_1^1 x_2^0 x_3^0$
* $[\mu] = cm^-1 g s = x_1^{-1} x_2^1 x_3 ^{-1}$

Stąd macierz $a_{ij}$ ma postać (po wpisaniu powyższych w rzędy)
```
[[2  1 -3]
 [1  0  0]
 [-1 1 -1]]
```
$\det a_{ij} = 2 \neq 0$
Zatem powyższe wielkości mogą tworzyć bazę dla $\Pi$.


### Związek między bazami
Niech $X_i$, $Y_i$ będą dwiema bazami w przestrzeni $\Pi$. Związek między nimi wyraża się:

$$X_i = $$

Wielkość wymiarowa A w bazie $X_i$ przybiera postać:

$$ A = Q \Pi_{i=1}^n X_i^{b_i} $$

Więc w bazie $Y_i$:

$$ A = Q \Pi_{i=1}^n (\xi_i \prod_{j=1}^n Y_j^{a_{ij}})^{b_i} $$

### Przykład: zmiana układu jednostek CGS na MKS.

Niech $Y_i$ stanowią bazę w MKS, $X_i$ w cgs. Niech:

$X_1 = g$ (masa)
$$X_2 = cm$$
$$X_3 = s$$


$Y_1 = kg$ (siła)
$$Y_2 = m$$
$$Y_3 = s$$

Wyrażając $X_i$ przez $Y_i$ dostajemy mnożniki $\xi_1 = (9.81e3)^{-1}, \xi_2 = 1e-2, \xi_3 = 1$

### Twierdzenie Buckinghama?
Zmianę bazy w przestrzeni $\Pi$ można potraktować jako **dualne przekształcenie wymiarowe**.

$$\Gamma: A \to B, B = \Gamma A$$
Nazwiemy go przekształceniem podstawowym w przestrzeni wymiarowej $\Pi$. Własności:

1. $\forall_{Q \in R_+} \Gamma Q = Q$
2. $\forall_{A, B \in \Pi} \Gamma (A B) = \Gamma(A) \Gamma(B)$
3. $\forall_{\alpha \in R} \Gamma (A^a) = (\Gamma(A))^a$

Wśród zbioru przekształceń $\Gamma$ istotne znaczenie ma przekształcenie jednorodne postaci $\Gamma A = kA$, $k \in R_+$. Dotyczy ono zmiany skal poszczególnych wielkości bazowych.

Spodziewamy się z fizyki, że postać praw fizycznych musi pozostawać niezmieniona przy zmianie układu jednostek pomiarowych. Zasada ta uniezależniająca relacje fizyczne od konwencji wyboru jednostek nakłada na postać związków funkcyjnych określone ograniczenia - postulaty:

1. **postulat niezmienniczości wymiarowej**:
  * dla każdej funkcji wymiarowej $\phi$ zależnej od m argumentów wymiarowych $A_i$
    i dla każdego przekształcenia podstawowego $\Gamma$ w $\Pi$ musi zachodzić zależność
    $$\phi(\Gamma A_1, \Gamma A_2... \Gamma A_m) = \Gamma \phi(A_1, A_2,... A_m)$$
    Funkcje które to spełniają nazywają się **wymiarowo niezmienniczymi**. *(wszystkie fizycznie sensowne funkcje).

    Bazując na tym postulacie można wyznaczyć ogólną postać $\phi$ - różną w przypadku gdy liczba argumentów
    $A_i$ jest
      1. mniejsza lub równa wymiarowi przestrzeni n
        1. Aby funkcja wymiarowa $\phi$ zależna od m argumentów wymiarowo niezależnych $A_i$ była wymiarowo niezmiennicza, konieczne i wystarczające jest żeby miała ona następującą postać.
          $$\phi(A_1, A_2, ... A_m) = \psi A_1^{f_1} A_2^{f_2}...A_m^f_m, f_i\in R, \psi \in R_+
      2. gdy jest ona większa
        1. Tw. Buckinghama - aby funkcja wymiarowa \psi zależna od m argumentów wymiarowych $A_i$ (m>n) była wymiarowo niezmiennicza, konieczne i wystarczające jest aby
          $$(\phi(A_1, A_2,...$A_n, A_{n+1}, ... A_m)) = \psi(\pi_1, \pi_2, ..., \psi_{m-n}) A_1^{f_1} A_2^{f^1}
        gdzie argumenty $A_1, A_2, A_n$ są wymiarowo niezależne i mogą tworzyć bazę przestrzeni $\Pi$, a $\Pi_i$ są wielkościami bezwymiarowymi.
