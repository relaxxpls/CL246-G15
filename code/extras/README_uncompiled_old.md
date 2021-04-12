# Solving Attempt 2 - [`desmos`](https://www.desmos.com/calculator/fj9gy8l2la)

**NOTE:** if your using GitHub's light mode, either [view the README here](README_light.md) where $\LaTeX$ is rendered specifically for light mode or [switch to dark mode](https://github.com/settings/appearance).


## Goal 1: Find temperature of water surface, $T_w$

Using **Eq. 15** on [page 308](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf).

#### Nomenclature

* $S$ = Intensity of Solar Radiation (i.e. Solar Constant)
* $u_o$ = water velocity
* $v_o$ = wind velocity
* $h_r$ = radiative heat transfer coefficient
* $h_c$ = convective heat transfer coefficient
* $\dot{m}_w$ = flow rate of water
* $\epsilon_w$ = emissivity of water surface
* $\sigma = 5.67*10^{-8}\ W/m^2K^4$ = Stefan-Boltzmann constant
* $T_w$ = water surface temperature
* $T_a$ = ambient air temperature
* $\gamma$ =
* $r$ = relative humidity
* $\tau_1$ = fraction of solar radiation absorbed by water
* $k_w$ = thermal conductivity of water
* $L_w$ = length of water path
* $P$ =

#### Assumptions

1. Steady state
2. Water has creeping flow, i.e. water velocity $u_0 = 0$ and $\dot{m}_w=0$
3. Gentle breeze present ($v_o = 10\ km/h$)
4. Length of water path = 5m
5. **P** on **Eq. 4** on [page 308](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf) means the Prandtl Number, **Pr**
6. Characteristic length (for calculating Gr) is same as length if water $L_w$

#### Equations

Upon simplifying under our assumptions, **Eq. 15** becomes:

$$ T_{w} = \frac{H \cdot T_{s}+h_{1} \cdot \theta_1}{h_{1}+H} $$

with $\theta_1$ calculated at $x=0$, and:

$$
\begin{align}
  H &= h_r + h_c + R_0 \cdot R_1 \\ \\
  H_1 &= h_r + h_c + \gamma \cdot R_0 \cdot R_1 \\ \\
  T_s &= \frac{\tau_1\cdot S + H_1\cdot T_A - R_0\cdot R_2\cdot(1-r)}{H}
\end{align}
$$

also:
$$
\begin{align}
  h_1 &= \frac{k_w}{L_w} \cdot [0.14\cdot(Gr\cdot Pr)^{1/3} + 0.644\cdot (Pr\cdot Re)^{1/3}] \\ \\
  Gr &= \frac{g\cdot\beta\cdot(T_w-T_a)\cdot(L)^{3}}{\nu^2} \\
  \nu &= \frac{\mu}{\rho} \\
  \beta &= \frac{2}{T_w+T_a} \\ \\
  Pr &= \frac{\mu\cdot c_p}{k} \\ \\
  Re &= \frac{\rho \cdot u_o \cdot L_w}{\mu}
\end{align}
$$

The convection coefficients $h_r$ and $h_c$ can be calculated by:

$$
\begin{align}
  R_0 &= 0.013 \cdot h_c \\ \\
  h_c &= 5.678 \cdot (1 + 0.85\cdot(v_o-u_o)) \\ \\
  h_r &= \epsilon_w\cdot\sigma\cdot \frac{(T_w+273.15)^4 - (T_a+261.15)^4}{T_w-T_a}
\end{align}
$$

#### Known Values

* $\epsilon_w = 0.95$
* From assumptions, $u_o = 0$ and $v_o = 2.78\ m/s$
* $S = 1366\ W/m^2$
* From [page 310](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf), we get $R_1=325\ Pa/^\circ C$ and $R_2 = -5155\ Pa$
* $T_a \in [30,60]\ ^\circ C$
* $\gamma=0.27$ (approx average over a day)
* $r = 0.5$
* $\tau_1=0.54$
* $L_w = 5\ m$ (approx)
* $g = 9.8\ m/s^2$
* $\beta = \frac{1}{T_a}$ (approx)
* $Re = 0$ (Compared to Gr and under Creeping Flow)
* $k_w, \mu, \rho, Pr$ from **Table A.6**, taken at $T_a$
<!-- * $k_w \in [300,340]\ W/m^{2\circ}C$ -->

#### After Substitution

$$
\begin{align}
  h_c &= 5.678 \cdot (1 + 0.85 \cdot 2.78) \\
      &= 19.1 \\
  R_0 &= 0.013 \cdot h_c \\
      &= 0.2483 \\
  h_r &= 5.3865\cdot 10^{−8}\cdot \frac{(T_w+273.15)^4 - (T_a+261.15)^4}{T_w-T_a} \\
  Gr  &= \frac{9.8\cdot\frac{1}{T_a}\cdot(T_w-T_a)\cdot(5)^{3}}{\nu^2} \\
      &= \frac{1225}{\nu^2} \cdot \left( \frac{T_w}{T_a}-1 \right) \\
  h_1 &= (\frac{300}{5})\cdot 0.14\cdot(Gr\cdot Pr)^{1/3}\\
      &= 8.4\cdot(Gr\cdot Pr)^{1/3}
\end{align}
$$
