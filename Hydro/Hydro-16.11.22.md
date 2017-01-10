# Parametry bezwymiarowe
### Liczba Rosby'ego

$$\rho \frac{D\vec{u}}{Dt} = -\nabla p -2\rho \vec{\Omega} \times \vec{u} + \mu \nabla^2 \vec{u}$$

Jesteśmy w układzie nieinercjalnym, a jedyna siła masowa to siła Coriolisa $-2\rho \vec{\Omega} \times \vec{u}$.
Zakładamy też przepływ nieściśliwy $\nabla \cdot \vec{u} = 0$.

Kiedy siła Coriolisa jest istotna? Przy wystarczająco szybkiej rotacji. W przepływach geofizycznych zwykle interesują nas procesy quasistatyczne (nie termodynamicznie, a takie że $|\frac{\partial u}{\partial t}| << |(u \cdot \nabla) u|$.

> Ludzie od prognozy pogody by się ze mną oczywiście nie zgodzili - tam są potrzebne faktycznie te szybkie skale czasowe.

Zatem o znaczeniu siły coriolisa decyduje stosunek $|\frac{2\rho \vec{\Omega} \times \vec{u}}{(u \cdot \nabla) u}|$. Więc musimy porównać $|\Omega|$ z czymś. Potrzebujemy więc skali prędkości.

> Gorzej jeżeli są pochodne - wtedy trzeba szacować zmiany wielkości w układzie.

Definiujemy:
* $L$ jako charakterystyczną odległość (niekoniecznie wielkość całego dostępnego obszaru).
  *  Dla atmosfery na przykład 1000km.
    *  Jeśli badamy pionową konwekcję w garnku (jeden wir konwekcyjny na garnek), to $L$ to mniej więcej wysokość garnka.
      *  W bardzo turbulentnej konwekcji musielibyśmy przyjąć mniejsze $L$.
  * Przepływ lepki wytwarzający warstwę graniczną daje dwie skale charakterystyczne:
    * grubość warstwy przepływu
    * grubość warstwy granicznej.
* $U$ jako charakterystyczną skalę prędkości.
  * Dla atmosfery $U \sim 20 m/s$ - to typowa prędkość przepływu w skali 1000km.
  * Tornado miałoby $L \sim 100m$, $U \sim 300-400 km/h \sim 100 m/s$.
  * Ogólnie: $U \sim L$ (nieliniowo!)

Gdy już mamy skale:

$$|\frac{2\vec{\Omega} \times \vec{u}}{(u \cdot \nabla) u}| \sim |\frac{2 \Omega U}{U \frac{U}{L}}|  = |\frac{2 \Omega L}{U}| = 1/ R_o$$
Gdzie $R_o$ nazywamy liczbą Rossby'ego. Im mniejsza, tym istotniejsza siła Coriolisa.

Umownie: przepływ jest **wielkoskalowy** gdy $R_o < 1$ (zależnie od skali U!)
* dla Golfsztromu (prądu zatokowego) $L \sim 100 km$, $U \sim 1m/s$, $R_o \sim 0.07$  - wielkoskalowy.
* Atmosfera $L \sim 1000km$, $U \sim 20m/s$, $R_o \sim 0.14$ - mniej wielkoskalowa niż Golfsztrom.

### Liczba Ekmana

$$\rho \frac{D\vec{u}}{Dt} = -\nabla p -2\rho \vec{\Omega} \times \vec{u} + \mu \nabla^2 \vec{u}$$

$$ E = |\frac{\mu \nabla^2 \vec{u}}{2\vec{\Omega}\times\vec{u}}| \sim \frac{\nu}{2\Omega L^2}$$

### Liczba Reynoldsa

$$ Re = \frac{(\vec{u} \cdot \nabla)\vec{u}}{\nu \nabla^2 \vec{u}} \sim \frac{UL}{\nu}$$

# Twierdzenie Kelvina i wirowość



Założenia:
* Ciecz **nieściśliwa** ($\nabla \cdot \vec{u}$), **niejednorodna gęstość** ($\frac{D\rho}{Dt} = 0$)
* Układ obracający się ze stałą prędkością kątową $\vec{\Omega}$
* Siła odśrodkowa, jako potencjalna, zostaje wrzucona do ciśnienia

$$\frac{D\vec{u}}{Dt} = -\frac{\nabla p}{\rho} -2 \vec{\Omega} \times \vec{u} + \nu \nabla^2 \vec{u}$$

* C - krzywa materialna zamknięta
* A - dowolna powierzchnia rozpięta na C

Cyrkulacją, widzianą w układzie nieinercjalnym rotującym, wzdłuż C, nazywamy

$$ \Gamma = \int_C \vec{u} d\vec{r} = \int\int_A {\omega \cdot n} dA$$

Chcemy znaleźć $\frac{d\Gamma}{dt}$, $\Gamma = \Gamma(t)$,

## Wirowość absolutna
widziana z układu inercjalnego.

$$\omega_a = \nabla \times (u + \Omega \times r) = \omega + 2 \Omega$$

### Cyrkulacja absolutna

Równanie gwiazdka *:
$$\frac{d\Gamma_a}{dt} = \int\int \vec{n} \cdot (...) dA $$


# twierdzenie Kelvina
Założenia:
1. Ciecz jest barotropowa = $p = p(\rho)$ (ciśnienie u) funkcją gęstośći
  2. $\nabla p = \frac{dp}{d\rho}\nabla\rho$
  3. Ciecz jest nielepka $\neq 0$
  4. siły masowe są potencjalne
To:
* cyrkulacja abolutna (cyrkulacja cyrkulacja prędkości mierzonej w układzie inercjalnym) wzdłuż krzywej materialnej, a zatem strumień wirowości przez powierzchnię materialną są stałe w czasie.

$$ \frac{d \Gamma_a}{dt} = 0$$
$\Gamma_a$ pozostaje stałe. Linie wirowości są liniami materialnymi.

Wnioski:
1. W układzie inercjalnym$\Gamma = \Gamma_a$ czyli * opisuje zmianę "zwykłej" cyrkulacji czyli strumienia wirowości.
2. W układzie obracającym się strumień $\gamma$ może się zmieniać nawet, gdy prawa strona * jest zero. Wtedy:
  $$ \frac{d\Gamma}{dt} = -2 \Omega \frac{dA_n}{dt} $$
  ($A_n$ - pole rzutu powierzchni $A$ na płasczyznę prostopadłą do $\vec{\Omega}$).
  Rys. 1
  $A_n$, rośnie, czyli zmienia się w czasie, strumień wirowości maleje. Jeśli zmienia się $A_n$, to musi się pojawić wirowanie.

3. Fizyczne przyczyny zmiany $\Gamma_0$ to:
  1. Niebarotropowy rozkład gęstości (np. baroklinowy)
  2. dyfuzja wirowości na skutek lepkości
  3. Niepotencjalne siły masowe (np. siła Lorentza)
4. Linie wirowości są liniami materialnymi jeśli r.h.s. * = 0

  Dowód:
  R7

  Spełnione są założenia twierdzenia Kelvina, zatem:

  R8

  Dostajemy równanie wirowości w cieczy idealnej. Zmiana $\omega$ wynika tylko z rozciągania (obecności gradientu prędkości wzdłuż $\vec{\omega}$)

  Można to łatwo porównać z ewolucjią długości linii materialnej w wyniku rozciągania
  R9

  Jeśli z warunku początkowego $\omega \times dL$ implikuje że to jest dalej zero, to pokazaliśmy że linie wirowości są liniami materialnymi


  ....

  Dowolna pochodna $\omega \times dL$ jest zero, jeśli zaczęliśmy od zero; więc ono dalej będzie zero.

  Zatem linie krzywe całkowe pola $\omega$ linie wirowości są liniami materialnymi.

  Jeśli $\omega \times dL$ w $t=0$ jest zero, to $\omega \times dL = 0$ dla każdego późniejszego czasu.

5. Rozciąganie linii wirowości absolutnej oznacza zwiększanie wartości $|\omega_a|$.

> Twierdzenie Kelwina powinno się państwu kojarzyć tak: przy spełnionych założeniach linie wirowości są liniami materialnymi, a strumień wirowości jest zachowany.

* TO SAMO CO FREEZE IN W MHD
* Twierdzenie Helmholtza (geometria różniczkowa)
* Tu zaniedbaliśmy lepkość, tam zaniedbujemy opór
