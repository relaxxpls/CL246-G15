# Goal 2: No Water Layer - [`notebook`](heat_flux_no_water.ipynb)

Find Resultant Resistance and Heat Rate

## Nomenclature

* $Nu_L$ = Nusselt number
* $Ra_L$ = Rayleigh number
* $\alpha$ = Thermal diffusivity
* $\beta$ = Coefficient of thermal expansion
* $\nu$ = Dynamic Viscosity

## Equations

$$
Ra_L = \frac{g\cdot \beta\cdot (T_s - T_{\infty})\cdot L^{3}}{\nu\cdot\alpha}
$$

$$
\overline {Nu}_L = 0.54Ra_L^{1/4} \quad (10^4\le Ra_L\le 10^7,\ Pr \ge0.7)
$$

$$
\overline {Nu}_L = 0.15Ra_L^{1/3} \quad (10^7\le Ra_L\le 10^{11},\ \text{all Pr})
$$

$$
q_i = (E_{bi} - J_i)\cdot \frac{\epsilon_i\cdot A_i}{1-\epsilon_i}
$$

## Values

* $g = 9.8\ m/s^2$
* $L = 0.2\ m$ thick with,
  * Cement = $5\ cm$
  * Brick = $10\ cm$
  * Lime = $5\ cm$
* Table A.4, air ($T_f = 320K$):
  * $\nu = 18 \cdot 10^{-6}\ m^2/s$
  * $\alpha = 25 \cdot 10^{-6}\ m^2/s$
  * $Pr = 0.702$
  * $k = 27.7 \cdot 10^{-3}\ W/m\cdot K$
* $\beta = \frac{1}{T_f} = 0.0031\ K^{-1}$
* $\epsilon_{concrete} = 0.85,\quad \epsilon_{brick} = 0.93,\quad \epsilon_{lime} = 0.90$

## Solving

$$
\begin{align}
Ra_L &= \frac{g\cdot \beta\cdot (T_s - T_{\infty})\cdot L^{3}}{\nu\cdot\alpha} \\ \\
     &= \frac{9.8\cdot 0.0031\cdot (T_s - T_{\infty})\cdot (0.2)^{3}}{18 \cdot 10^{-6}\cdot 25 \cdot 10^{-6}} \\ \\
     &= 5.4 \cdot 10^5 \cdot(T_s - T_{\infty}) \\ \\
\\
Nu_L &= 0.15 \cdot (5.4 \cdot 10^5)^{1/3} \cdot(T_s - T_{\infty})^{1/3} \\ \\
     &= 12.21 \cdot(T_s - T_{\infty})^{1/3} \\ \\
\\
\bar{h}_t &= \frac{K}{L} \cdot Nu_L \\ \\
          &= \frac{27.7 \cdot 10^{-3}}{0.2} \cdot 12.21 \cdot (T_s - T_{\infty})^{1/3} \\ \\
          &= 1.69 \cdot (T_s - T_{\infty})^{1/3} \\ \\
\end{align}
$$
