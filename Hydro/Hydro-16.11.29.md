# Potencjał zespolony i odwzorowanie konforemne

### Założenia
1. Ciecz nielepka $\mu = 0$
2. Ciecz nieściśliwa $\nabla \cdot \vec{u} = 0$
3. Przepływ dwuwymiarowy $(U_x, U_y)(x, y)$, skrzydło ma nieskończoną długość w kierunku osi $z$
4. $\vec{U}_\infty = U \hat{x}$, rotacja w nieskończoności zerowa
    * Skoro tak, to z twierdzenia Kelvina bezwirowa i przy skrzydle
    * $\vec{u} = \nabla \phi$

### Problem do rozwiązania w dwóch przypadkach

1. z założenia 2: $\Delta \phi = 0$ plus warunki brzegowe
2. z 2 i 3: $\vec{u} = \nabla \times (\Psi \hat{z})$
    * $\omega = \nabla \times \vec{u} = \nabla \times (\nabla \times (\Psi \hat{z})) = 0$
    * więc $\Delta \Psi = 0$, z warunkami brzegowymi, to alternatywne podejście do problemu

### Strategia

Z prostego problemu typu przepływ wokół cylindra czy sfery przechodzimy do problemu skomplikowanego typu przepływ wokół naszego śmiechowego skrzydła

### Opływ walca
Równania:

1. $\Delta \phi = 0$
2. $\nabla \phi \cdot \hat{n} = 0$ gdy $r = a$
3. $\nabla \phi \to U \hat{x}$ gdy $r \to \infty$

Pomijając proste wyprowadzenie.

$$ \phi(r, \theta) = U(r + \frac{a^2}{r}) \cos{\theta} $$

Można też oczywiście policzyć funkcję prądu:

$$ \Psi(r, \theta) = U(r - \frac{a^2}{r}) \sin{\theta} $$

### Cyrkulacyjny opływ walca - wir liniowy
Wir ma prędkość i potencjał (uzyskany z superpozycji):
$$\vec{u} = - \frac{\gamma}{2 \pi r} \hat{\theta}$$
$$ \phi(r, \theta) = U (r + a^2 /r)\cos{\theta} - \frac{\Gamma \theta }{2\pi}$$

### Punkty stagnacji
Tam, gdzie zeruje się prędkość, mamy punkty stagnacji. W tym przypadku dla $r = a$ dostajemy $u_r = 0$, $u_\theta$ =

# Prawo Kutty-Żukowskiego
Dla dowolnego ciała jeśli mamy przepływ wirowy z cyrkulacją $Fx = 0$, $Fy = \rho U \gamma$

### Potencjał zespolony

Nasze trzy równania
$$\nabla \cdot \vec{u} = 0$$
$$\nabla \times \vec{u} = 0$$
$$\vec{u} = (u, v)$$

$$\Delta \phi = 0$$
$$\Delta \Psi = 0$$

$$ u = \frac{\partial \phi}{\partial x} = \frac{\partial \psi}{\partial y}$$
$$ v = \frac{\partial \phi}{\partial y} = -\frac{\partial \psi}{\partial x}$$

Więc możemy zbudować funkcję analityczną - potencjał zespolony - postaci

$$w(z) = \phi(x, y) + i \psi(x,y)$$
gdzie $z = x + iy$

Oraz prędkość zespoloną
$$\frac{dw}{dz} = \frac{\partial \phi}{\partial x} + i \frac{\partial \psi}{\partial x} = \frac{\partial \psi}{\partial y} - i \frac{\partial \phi}{\partial y}$$


### Odwzorowania konforemne
