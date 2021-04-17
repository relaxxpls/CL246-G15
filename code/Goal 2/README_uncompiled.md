# Without Water (Attempt 3)

## Nomenclature

* $T_a$ = ambient air temperature (outside)
* $T_r$ = room temperature (inside)
* $Nu_L$ = Nusselt number of air
* $Ra_L$ = Rayleigh number of air
* $\alpha$ = thermal diffusivity of air
* $k_a$ = thermal conductivity of air
* $h_r$ = heat transfer coefficient for room air
* Roof layers:
  * **1**: Concrete
  * **2**: Brick
  * **3**: Lime
* $k_i$ = thermal conductivity of $i^{th}$ roof layer
* $L_i$ = length of $i^{th}$ roof layer
* $q_{r}$ = radiative heat transfer (per unit area)
* $q_{c}$ = convective heat transfer (per unit area)
* $q_{t}$ = net heat transfer into the room (per unit area)
* $\beta$ = coefficient of thermal expansion
* $\nu$ = dynamic Viscosity
* $E_b$ = total emissive power of a Blackbody
* $J$ = radiosity

## Assumptions

* Room is maintained at constant temperature, i.e. $T_r = 27^\circ C = 300K$
* Main source of radition is the sun (solar radation)
* Dimensions of roof $5\ m \times 5\ m \times 0.2\ m$

## Equations

Nu correlations,
\begin{align*}
  \overline {Nu}_L &= 0.54Ra_L^{1/4} \quad (10^4\le Ra_L\le 10^7,\ Pr \ge0.7) \\
  \overline {Nu}_L &= 0.15Ra_L^{1/3} \quad (10^7\le Ra_L\le 10^{11},\ \text{all Pr})\\
\end{align*}

$$
Ra_L = \frac{g\cdot \beta\cdot (T_s - T_{\infty})\cdot L^{3}}{\nu\cdot\alpha}
$$

Also,
\begin{align*}
  h_c &= \frac{k_a}{L}\cdot Nu_L \\
  q_c &= h_c\cdot (T_s - T_{\infty}) \\
  q_r &= (E_b - J)\cdot \frac{\epsilon}{1 - \epsilon} \\ \\
  q_t &= q_c + q_r
\end{align*}

Roof layers:
$$
R_{net} = \frac{1}{h_r} + \sum_{i=1}^{3} \frac{L_i}{k_i}
$$
Thus finally,
$$
q_t = \frac{T_s - T_r}{R_{net}}
$$

## Values

* $g = 9.8\ m/s^2$
* $L = 2.5\ m$ thick with,
  * Cement = $5\ cm$
  * Brick = $10\ cm$
  * Lime = $5\ cm$
* $K_i$, Conductivity of each layer,
  * Cement = $0.72\ W/m^{\circ}C$
  * Brick = $0.71\ W/m^{\circ}C$
  * Lime = $0.73\ W/m^{\circ}C$
* Table A.4, air ($T_f = 320K$):
  * $\nu = 18 \cdot 10^{-6}\ m^2/s$
  * $\alpha = 25 \cdot 10^{-6}\ m^2/s$
  * $Pr = 0.702$
  * $k = 27.7 \cdot 10^{-3}\ W/m\cdot K$
* $k_a =27.7 \cdot 10^{-3}W/m^{\circ}C$
* $h_r = 8.4 W/m^2\cdot K$
* $\beta = \frac{1}{T_f} = 0.0031\ K^{-1}$
* $\epsilon = \epsilon_{concrete} = 0.85$
* $E_b = \sigma \cdot T_\infty^4 = 5.67 \cdot 10^{-8} \cdot T_\infty^4$
* $J=0$
* $T_r =\ 27^\circ C$ (Room Temperature)

## Solving

\begin{align*}
  Ra_L &= \frac{g\cdot \beta\cdot (T_s - T_{\infty})\cdot L^{3}}{\nu\cdot\alpha} \\ \\
       &= \frac{9.8\cdot 0.0031\cdot (T_s - T_{\infty})\cdot (0.2)^{3}}{18 \cdot 10^{-6}\cdot 25 \cdot 10^{-6}} \\ \\
       &= 5.4 \cdot 10^5 \cdot(T_s - T_{\infty}) \\
\\
  Nu_L &= 0.15 \cdot (5.4 \cdot 10^5)^{1/3} \cdot(T_s - T_{\infty})^{1/3} \\ \\
       &= 12.21 \cdot(T_s - T_{\infty})^{1/3} \\
\\
   h_c &= \frac{K}{L} \cdot Nu_L \\ \\
       &= \frac{27.7 \cdot 10^{-3}}{0.2} \cdot 12.21 \cdot (T_s - T_{\infty})^{1/3} \\ \\
       &= 1.69 \cdot (T_s - T_{\infty})^{1/3} \\
\\
   q_c &= 1.69 \cdot (T_s - T_{\infty})^{4/3} \\
\\
   q_r &= (5.67 \cdot 10^{-8} \cdot T_\infty^4 - 0)\cdot \frac{0.85}{1-0.85} \\ \\
       &= 3.21 \cdot 10^{-7} \cdot T_\infty^4\cdot \\ \\
   q_t &= 3.21 \cdot 10^{-7} \cdot T_\infty^4+ 1.69 \cdot (T_s - T_{\infty})^{4/3}\\
\\
\end{align*}

Resistance net,
\begin{align*}
R_{net} &= \frac{1}{h_r} + \sum_{i=1}^{3} \frac{L_i}{k_i} \\ \\
  &= \frac{1}{8.4} + \frac{0.05}{0.72} + \frac{0.10}{0.71} + \frac{0.05}{0.73} \\ \\
  &= 0.398\ m^2K/W \\ \\
\end{align*}

Thus finally,
$$
3.21 \cdot 10^{-7} \cdot T_\infty^4+ 1.69 \cdot (T_s - T_{\infty})^{4/3} = \frac{T_s - 300}{0.398}
$$

Finally, solve above equation for $T_s$ and $q_{net}$ with varying $T_{\infty}$.
