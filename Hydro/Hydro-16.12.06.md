# Bezwirowy przepływ płynu nieściśliwego
> What happens without vorticity, stays without vorticity.
~ wniosek z twierdzenia Kelvina

Jeśli przepływ jest bezwirowy w $t_0$, to pozostanie on bezwirowy dla $t > t_0 (\vec{\omega} = 0)$

### Pochodzenie wirowości

W układzie laboratoryjnym, bez siły Coriolisa ($\vec{\Omega} = 0$).

Ciecz idealna wprowadzona w ruch bez delt Diraca w rozkładach (np. dwie warstwy płynu płynące w przeciwne strony) będzie się ruszała bez wirowości.

W płynie lepkim **brzegi** generują wirowość! Wirowość może pojawiać się na ściankach i powierzchniach swobodnych, po czym dyfunduje z brzegów do obszaru bezwirowego.

### Eksperyment: kulka w bezwirowym płynie

Nagle wprawiamy ją w ruch w chwili $t_0$. Przepływ jest teraz potencjalny i *na ogół nie spełnia warunku znikania stycznej składowej prędkości na brzegu*
$\vec{u} \times \vec{n}|_{\partial \Omega} = 0$, choć oczywiście spełnia
$\vec{u} \cdot \vec{n}|_{\partial \Omega} = 0$.

Zatem w $t = t_0$ mamy przy przegu nieskończony gradient prędkości, więc nieskończoną wirowość (deltę Diraca),
która następnie dyfunduje do cieczy. W czasie t wirowość dyfunduje na odległość $\sim\sqrt{t\nu}$

Ponadto wirowość jest *unoszona* (adwekcyjnie) w głąb cieczy.

### Przykład: płytka poruszająca się w głąb cieczy
Płytka poruszająca się w płynie z prędkością $U_0$ w jej układzie odniesienia: wybrany element płytki pozostaje w pobliżu płytki przez czas $\sim \frac{L}{U_0}$.

W tym czasie wirowość dyfunduje na odległość $\sqrt{\frac{\nu L}{U_0}}$.

Warunkiem na to, by zasięg penetracji wirowości był porównywalny z długością płyty:

$(\frac{\nu L}{U_0})^\frac{1}{2} \sim L$, czyli $\frac{\nu L}{U_0} = Re \sim 1$

* Jeśli $Re << 1$ to wirowość dyfunduje jednakowo we wszystkie strony.
* Jeśli $Re \sim 1$ to mamy powyższe: wirowość na mniej więcej taki zasięg jak długość płyty.
* Jeśli zaś $Re >> 1$ to wirowość jest skoncentrowana przy powierzchni płyty.

### Liczba Reynoldsa

Z równania Naviera Stokesa:
$$\frac{\partial\vec{u}}{\partial t} + (\vec{u}\cdot\nabla)\vec{u} =
 - \frac{\nabla p}{\rho} + \vec{F} + \nu \Big(\Delta \vec{u} + \frac{1}{3} \nabla (\nabla \cdot \vec{u})\Big)$$

$$ Re = |\frac{\rho (\vec{u}\cdot\nabla)\vec{u}}{\mu \Delta \vec{u}}|$$

Dla małych $Re$ możemy pominąć człon nieliniowy, zaś dla dużych: człon lepki.
Wtedy też mamy bardzo duże gradienty w bardzo małej **warstwie brzegowej** blisko
ciała.

### Siła nośna

Pochodzi właśnie od warstwy granicznej!

Dla $Re >> 1$ przepływ jest wszędzie z dużą dokładnością bezwirowy, z wyjątkiem
cienkich warstw wirowości przylegających do brył sztywnych.
Jednak warstwa przyścienna może się oddzielić od bryły sztywnej.

* Dla $Re < 10$ mamy mniej więcej przepływ laminarny.
* Dla $Re \sim 20$ przepływ jest mniej więcej taki jak dla wydłużonego walca, za kulą dwa wiry.
* Dalej warstwa przyścienna odrywa się i ze wzrostem $Re$ obszar niezerowej (?) wirowości wydłuża się.
Jest to tzw. **separacja** (oderwanie) warstwy przyściennej.
* Granica $Re \lim \inf$ jest osobliwa - szeregi którymi możemy to przybliżać są asymptotyczne.

Z doświadczenia wiadomo, że warstwa przyścienna odrywa się w takim punkcie (lub jego pobliżu), gdzie prędkość potencjalnego (bezwirowego) przepływu, jaki byłby, gdyby $\nu = 0$, ma maksimum. (Ten punkt jest bardzo blisko punktu maksymalnego ciśnienia.)

# Rozwój turbulencji
### Opływ walca
1. $Re \sim 1e-2$, równanie Stokesa bez członu nieliniowego $\nabla p = \mu \Delta \vec{u}$.
2. $Re \sim 2e1$, charakter przepływu się zmienił: nie można go uzyskać przez przeskalowanie poprzedniego.
3. ścieżka wirów von Karmana
  1. $Re \sim 1e2$, wiry odrywają się i porywa je przepływ za walcem. Można jeszcze rozpoznać w miarę regularne struktury.
  2. $Re \sim 1e4$, turbulencja "jeszcze trochę regularna"
4. Ślad turbulentny $Re \sim 1e6$

> Nie ma ogólnej teorii turbulencji, najwyżej statystyczne prawidłowości

### Przepływ we współosiowych walcach
$L/R << 1$, wewnętrzny walec obracany jest ze stałą prędkością kątową $\vec{\omega}$.
Pomiędzy walcami ciecz jest lepka.
Współczynnik charakteryzujący przepływ: Liczba Taylora $Ta = \frac{\omega^2 l^3 R}{\nu^2}$.

1. Przepływ laminarny $Ta < 1708 = Ta_{kr}$. Przepływ tylko dopasowuje się do różnicy prędkości. Powyżej - niestabilności!
2. $Ta > Ta_{kr} = 1708, pojawiają się komórki Taylora (torusy). Przepływ niepotencjalny, z niezerową wirowością.
3. $Ta$ jeszcze większa: oscylacje falowe
4. Oscylacje plus turbulencja, przepływ super chaotyczny z ciutką struktur
5. Czysta turbulencja

> Transport momentu pędu od wewnętrznego walca do zewnętrznego. Dla niskich $Re$ stabilny przepływ, satysfakcjonujący. Przy wyższych $Re$ nowy przepływ, turbulentny, robi się bardziej efektywny (jest minimum energetycznym).

# Transport ciepła
