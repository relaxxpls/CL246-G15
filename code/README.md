# Solving Attempt 2 - [`desmos`](https://www.desmos.com/calculator/fj9gy8l2la)

## Goal 1: Find temperature of water surface, $T_w$

Using **Eq. 15** on [page 308](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf).

#### Nomenclature

* $S$ = Intensity of Solar Radiation (i.e. Solar Constant)
* $u_o$ = water velocity
* $v_o$ = wind velocity
* $h_r$ = radiative heat transfer coefficient
* $h_c$ = convective heat transfer coefficient
* $\dot{m}_w$ = flow rate of water
* $\epsilon_w$ = emissivity of water
* $\sigma = 5.67*10^{-8}\ W/m^2K^4$ = Stefan-Boltzmann constant
* $T_w$ = water surface temperature
* $T_a$ = ambient air temperature

#### Assumptions

1. Steady state
2. Water is at rest, i.e. water velocity $u_0 = 0$ and $\dot{m}_w=0$
3. Gentle breeze present ($v_o = 10\ km/h$)

#### Equations

Upon simplifying under our assumptions, **Eq. 15** becomes:

$$ T_{w} = \frac{H \cdot T_{s}+h_{1} \cdot \theta_1}{h_{1}+H} $$

with $\theta_1$ calculated at $x=0$ and $H$, $T_s$, $h_1$ and $R_0$ given by:

$$ H = h_r + h_c + R_0 \cdot R_1 $$
$$ T_s = \frac{\tau_1 \cdot S + H_1 \cdot T_A - R_0 \cdot R_2 \cdot (1-r)}{H} $$
$$ H_1 = h_r + h_c + \gamma \cdot R_0 \cdot R_1 $$
$$ R_0 = 0.013 \cdot h_c $$

The convection coefficients $h_r$ and $h_c$ can be calculated by:

$$ h_c = 5.678 \cdot (1 + 0.85*(v_o-u_o)) $$
$$ h_r = \epsilon_w\cdot\sigma\cdot \frac{(T_w+273.15)^4 - (T_a+261.15)^4}{T_w-T_a}$$

#### Known Values

* $\epsilon_w = 0.95$
* From assumptions, $u_o = 0$ and $v_o = 2.78\ m/s$
* $S = 1366\ W/m^2$
* From [page 310](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf), we get $R_1=325\ Pa/^\circ C$ and $R_2=-5155\ Pa$
