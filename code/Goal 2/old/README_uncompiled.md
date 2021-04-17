# Goal 2: Find Resultant Resistance and Heat Rate - [`notebook`](heat_flux_no_water.ipynb)

## Nomenclature

* $A$ = roof cross section area
* $h_o$ = outside convective heat transfer coefficient
* $h_i$ = inside convective heat transfer coefficient
* $k_i$ = thermal conductivity of $i^{th}$ layer
* $L_i$ = length of $i^{th}$ layer
* Layer **1**: Concrete
* Layer **2**: Brick
* Layer **3**: Lime
* $T_a$ = ambient air temperature
* $T_r$ = room temperature
* $v_o$ = wind velocity

## Equations

Total Resistance:
$$
R_{net} = \frac{1}{h_o} +\frac{L_1}{k_1A} + \frac{L_2}{k_2A} + \frac{L_3}{k_3A} + \frac{1}{h_i} \\
$$

Heat Flux through wall:
$$
\begin{align}
  q_x &= \frac{T_a - T_r}{R_{net}} \\ \\
      &= \frac{T_a - T_r}{\frac{1}{h_o} +\frac{L_1}{k_1A} + \frac{L_2}{k_2A} + \frac{L_3}{k_3A} + \frac{1}{h_i} }
\end{align}
$$

## Values

* $h_o = 22.78\ W/m^{2\circ}C$ (corresponding to $v_o = 10.2\ km/h$)
* $h_i = 8.4\ W/m^{2\circ}C$
* $k_1 = 0.72\ W/m^{\circ}C,\ L_1 = 0.05\ m$
* $k_2 = 0.71\ W/m^{\circ}C,\ L_2 = 0.10\ m$
* $k_3 = 0.73\ W/m^{\circ}C,\ L_3 = 0.05\ m$
* $A = 15.43\ m^2$
* $T_a =\ ?,\ T_r =\ ?$ (ambient air and room temperature)
