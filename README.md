## Аналитическое решение задачи

$$
u(1, \varphi, t) = 0, \quad r = 1
$$

$$
u(r, t) = Ar\sin(\omega t)
$$

$$
\frac{\partial u(r, \varphi, 0)}{\partial t} = 0
$$

$$
u(r, \varphi, 0) = 0
$$

$$
\Delta u = \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial u}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 u}{\partial \varphi^2} \quad \left(\frac{\partial^2 u}{\partial \varphi^2} = 0\right)
$$

$$
\frac{\partial^2 u}{\partial t^2} = \frac{a^2}{r}\frac{\partial}{\partial r}\left(r\frac{\partial u}{\partial r}\right) + Ar\sin(\omega t)
$$

```math
\begin{cases}
\dfrac{\partial^2 u}{\partial t^2} = a^2 \left(\dfrac{\partial^2 u}{\partial r^2} + \dfrac{1}{r}\dfrac{\partial u}{\partial r}\right) + Ar\sin(\omega t) \\[10pt]
u(1, \varphi, t) = 0 \\[6pt]
\dfrac{\partial u(r, \varphi, 0)}{\partial t} = 0, \quad u(r, \varphi, 0) = 0
\end{cases}
```

$$
u(r, t) = R(r) \cdot T(t)
$$

$$
R(r)T''(t) = a^2 T(t)R''(r) + \frac{a^2}{r}R'(r)T(t) \quad \Big| \cdot \frac{1}{R(r)T(t)}
$$

$$
\frac{T''(t)}{T(t)} = a^2\frac{R''(r)}{R(r)} + \frac{a^2}{r}\frac{R'(r)}{R(r)} = -\lambda^2
$$

$$
a^2 R''(r) + \frac{a^2}{r}R'(r) + \lambda^2 R(r) = 0 \quad \Big| \cdot r^2
$$

Уравнение Бесселя (функции нулевого порядка):

$$
a^2 r^2 R''(r) + a^2 r R'(r) + (\lambda r)^2 R(r) = 0
$$

$$
R(r) = C_1 J_0(\lambda r) + C_2 Y_0(\lambda r)
$$

$$
Y_0(\lambda r) \to \infty \Rightarrow C_2 = 0
$$

$$
R_k(r) = C_k J_0(\lambda_k r), \quad R_k(1) = J_0(\lambda_k) = 0
$$

где $`\lambda_k`$ — корни уравнения.

Решение для однородного уравнения:

$$
u(r, t) = \sum_{k=1}^{\infty} C_k T_k(t) J_0(\lambda_k r)
$$

Разложение $Ar\sin(\omega t)$ по функциям Бесселя:

$$
\sum_{k=1}^{\infty} f_k(t) J_0(\lambda_k r) = Ar\sin(\omega t)
$$

$$
f_k(t) = C_k \sin(\omega t)
$$

$$
\sum_{k=1}^{\infty} C_k \sin(\omega t) \cdot J_0(\lambda_k r) = Ar\sin(\omega t)
$$

$$
\sum_{k=1}^{\infty} C_k J_0(\lambda_k r) = Ar
$$

$$
C_k = \frac{\displaystyle\int_0^1 Ar \cdot r J_0(\lambda_k r)\,dr}{\|J_0(\lambda_k r)\|^2}
$$

$$
\|J_0(\lambda_k r)\|^2 = \int_0^1 r J_0^2(\lambda_k r)\,dr = \frac{1}{2}J_1^2(\lambda_k)
$$

Интегрирование по частям (из свойства $`\dfrac{d(x J_1(x))}{dx} = x J_0(x)`$):

$$
u = r, \quad du = dr
$$

$$
dv = r J_0(\lambda_k r)\,dr, \quad v = \frac{1}{\lambda_k}r J_1(\lambda_k r)
$$

$$
\int_0^1 r^2 J_0(\lambda_k r)\,dr = \left.\frac{r^2}{\lambda_k}J_1(\lambda_k r)\right|_0^1 - \frac{1}{\lambda_k}\int_0^1 r J_1(\lambda_k r)\,dr = \frac{1}{\lambda_k}J_1(\lambda_k) - \frac{1}{\lambda_k}\int_0^1 r J_1(\lambda_k r)\,dr
$$

$$
C_k = \frac{2A\left(\dfrac{1}{\lambda_k}J_1(\lambda_k) - \dfrac{1}{\lambda_k}\displaystyle\int_0^1 r J_1(\lambda_k r)\,dr\right)}{J_1^2(\lambda_k)}
$$

$$
C_k = \frac{2A}{\lambda_k} \cdot \frac{J_1(\lambda_k) - \displaystyle\int_0^1 r J_1(\lambda_k r)\,dr}{J_1^2(\lambda_k)}
$$

Подставим $`u(r, t) = \sum_{k=1}^{\infty} T_k(t) J_0(\lambda_k r)`$ в уравнение:

$$
\sum_{k=1}^{\infty} T''_k(t) J_0(\lambda_k r) = -a^2 \sum_{k=1}^{\infty} T_k(t)\lambda_k^2 J_0(\lambda_k r) + Ar\sin(\omega t)
$$

$$
\sum_{k=1}^{\infty} \left(T''_k(t) + (a\lambda_k)^2 T_k(t)\right) \cdot J_0(\lambda_k r) = Ar\sin(\omega t)
$$

$$
\sum_{k=1}^{\infty} \left(T''_k(t) + (a\lambda_k)^2 T_k(t)\right) J_0(\lambda_k r) = \sum_{k=1}^{\infty} C_k \sin(\omega t) \cdot J_0(\lambda_k r)
$$

$$
T''_k(t) + (a\lambda_k)^2 T_k(t) = C_k \sin(\omega t)
$$

Однородное решение:

$$
T_k(t) = A_1 \cos(a\lambda_k t) + A_2 \sin(a\lambda_k t)
$$

Частное решение ищем в виде $`T_{\text{ч}}(t) = B_k \sin(\omega t)`$:

$$
-B_k \omega^2 \sin(\omega t) + (a\lambda_k)^2 B_k \sin(\omega t) = C_k \sin(\omega t)
$$

$$
B_k = \frac{C_k}{(a\lambda_k)^2 - \omega^2}
$$

Общее решение:

$$
T_k(t) = A_1 \cos(a\lambda_k t) + A_2 \sin(a\lambda_k t) + \frac{C_k \sin(\omega t)}{(a\lambda_k)^2 - \omega^2}
$$

$$
T_k(0) = 0 \Rightarrow A_1 = 0
$$

$$
T'_k(0) = 0 \Rightarrow A_2 = -\frac{\omega C_k}{a\lambda_k\left((a\lambda_k)^2 - \omega^2\right)}
$$

$$
T_k(t) = \frac{C_k}{(a\lambda_k)^2 - \omega^2}\left(\sin(\omega t) - \frac{\omega}{a\lambda_k}\sin(a\lambda_k t)\right)
$$

$$
u(r, t) = \sum_{k=1}^{\infty} \frac{C_k \cdot J_0(\lambda_k r)}{(a\lambda_k)^2 - \omega^2}\left(\sin(\omega t) - \frac{\omega}{a\lambda_k}\sin(a\lambda_k t)\right),
$$

где

$$
C_k = \frac{2A}{\lambda_k} \cdot \frac{J_1(\lambda_k) - \displaystyle\int_0^1 r J_1(\lambda_k r)\,dr}{J_1^2(\lambda_k)}
$$
