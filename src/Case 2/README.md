# Case 2: Water Layer - [`notebook`](water_surf_temp.ipynb)

Find Temperature of Water Surface, <img src="../../img/svgs_darkmode/59678b5b387bf797f0373126223862f5.svg?invert_in_darkmode" align=middle width=19.42550939999999pt height=22.465723500000017pt/>

## Nomenclature

* <img src="../../img/svgs_darkmode/e257acd1ccbe7fcb654708f1a866bfe9.svg?invert_in_darkmode" align=middle width=11.027402099999989pt height=22.465723500000017pt/> = Intensity of Solar Radiation (i.e. Solar Constant)
* <img src="../../img/svgs_darkmode/617df29b4912189585fe69e7e29f263e.svg?invert_in_darkmode" align=middle width=15.89887529999999pt height=14.15524440000002pt/> = water velocity
* <img src="../../img/svgs_darkmode/87cd0788f6b51bfd6ae5cb4ac878f2ec.svg?invert_in_darkmode" align=middle width=14.45666969999999pt height=14.15524440000002pt/> = wind velocity
* <img src="../../img/svgs_darkmode/f7c65c46dccd65632fc6e90e958f6b18.svg?invert_in_darkmode" align=middle width=15.928562099999992pt height=22.831056599999986pt/> = radiative heat transfer coefficient
* <img src="../../img/svgs_darkmode/b68428d9419541251ddb40e003804388.svg?invert_in_darkmode" align=middle width=15.345767249999989pt height=22.831056599999986pt/> = convective heat transfer coefficient
* <img src="../../img/svgs_darkmode/7063f3868a0debf878856a94132de800.svg?invert_in_darkmode" align=middle width=24.252422699999993pt height=21.95701200000001pt/> = flow rate of water
* <img src="../../img/svgs_darkmode/195b90bdbbbb5339aa20fcd02989c4e7.svg?invert_in_darkmode" align=middle width=16.49171369999999pt height=14.15524440000002pt/> = emissivity of water surface
* <img src="../../img/svgs_darkmode/69157a030fdee9e530106cffd4b9c164.svg?invert_in_darkmode" align=middle width=183.91371239999998pt height=26.76175259999998pt/> = Stefan-Boltzmann constant
* <img src="../../img/svgs_darkmode/59678b5b387bf797f0373126223862f5.svg?invert_in_darkmode" align=middle width=19.42550939999999pt height=22.465723500000017pt/> = water surface temperature
* <img src="../../img/svgs_darkmode/5bdf86f684b5b70a46fb2268c2b195b3.svg?invert_in_darkmode" align=middle width=16.736568749999993pt height=22.465723500000017pt/> = ambient air temperature
* <img src="../../img/svgs_darkmode/89f2e0d2d24bcf44db73aab8fc03252c.svg?invert_in_darkmode" align=middle width=7.87295519999999pt height=14.15524440000002pt/> = relative humidity
* <img src="../../img/svgs_darkmode/d21b54e2f85fabffacc7fb3123d1d151.svg?invert_in_darkmode" align=middle width=13.73865239999999pt height=14.15524440000002pt/> = fraction of solar radiation absorbed by water
* <img src="../../img/svgs_darkmode/170f61062a00c6aa774c665fdf4d5251.svg?invert_in_darkmode" align=middle width=18.37719839999999pt height=22.831056599999986pt/> = thermal conductivity of water
* <img src="../../img/svgs_darkmode/b534bf13756d01430237466cc980a357.svg?invert_in_darkmode" align=middle width=21.00656414999999pt height=22.465723500000017pt/> = length of water path

## Assumptions

1. Steady state
2. Water has creeping flow, i.e. water velocity <img src="../../img/svgs_darkmode/484f6a63bc9fbaa6c452cf02b00a0c70.svg?invert_in_darkmode" align=middle width=46.921573049999985pt height=21.18721440000001pt/> and <img src="../../img/svgs_darkmode/937eda0ac640f79f11dd57bb50cf32d3.svg?invert_in_darkmode" align=middle width=55.21115324999999pt height=21.95701200000001pt/>
3. Gentle breeze present (<img src="../../img/svgs_darkmode/4015d842dba09f9385f0e6786c10845b.svg?invert_in_darkmode" align=middle width=100.31284559999997pt height=24.65753399999998pt/>)
4. Length of water path = 5m
5. **P** on **Eq. 4** on [page 308](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf) means the Prandtl Number, **Pr**
6. Characteristic length (for calculating Gr) is same as length if water <img src="../../img/svgs_darkmode/b534bf13756d01430237466cc980a357.svg?invert_in_darkmode" align=middle width=21.00656414999999pt height=22.465723500000017pt/>

## Equations

Upon simplifying under our assumptions, **Eq. 15** becomes:

<p align="center"><img src="../../img/svgs_darkmode/c66ea755f2149fe472d5e1a3ae9f5a19.svg?invert_in_darkmode" align=middle width=151.54207695pt height=36.2778141pt/></p>

with <img src="../../img/svgs_darkmode/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode" align=middle width=14.269439249999989pt height=22.831056599999986pt/> calculated at <img src="../../img/svgs_darkmode/8436d02a042a1eec745015a5801fc1a0.svg?invert_in_darkmode" align=middle width=39.53182859999999pt height=21.18721440000001pt/>, and:

<p align="center"><img src="../../img/svgs_darkmode/ee5fa7450d4d893d06f73ad01b81e653.svg?invert_in_darkmode" align=middle width=288.22084334999994pt height=132.60666705pt/></p>

also:
<p align="center"><img src="../../img/svgs_darkmode/16ab23b23cb9d67717efe335c9f4285e.svg?invert_in_darkmode" align=middle width=373.11418649999996pt height=318.4908309pt/></p>

The convection coefficients <img src="../../img/svgs_darkmode/f7c65c46dccd65632fc6e90e958f6b18.svg?invert_in_darkmode" align=middle width=15.928562099999992pt height=22.831056599999986pt/> and <img src="../../img/svgs_darkmode/b68428d9419541251ddb40e003804388.svg?invert_in_darkmode" align=middle width=15.345767249999989pt height=22.831056599999986pt/> can be calculated by:

<p align="center"><img src="../../img/svgs_darkmode/d824f6162e249675edc47a63e62db50f.svg?invert_in_darkmode" align=middle width=324.51025365pt height=136.12450005pt/></p>

## Values

* <img src="../../img/svgs_darkmode/3aa9b7fa00814e793510c8689bfccac6.svg?invert_in_darkmode" align=middle width=68.45508614999999pt height=21.18721440000001pt/>
* From assumptions, <img src="../../img/svgs_darkmode/9b8ad8123297acea7ab148105e71298c.svg?invert_in_darkmode" align=middle width=46.85761079999999pt height=21.18721440000001pt/> and <img src="../../img/svgs_darkmode/7efc7d974942822b0f7a1785101f1eef.svg?invert_in_darkmode" align=middle width=102.25728149999999pt height=24.65753399999998pt/>
* <img src="../../img/svgs_darkmode/0e811d1830927814a2200c33ad975b0d.svg?invert_in_darkmode" align=middle width=116.48789459999998pt height=26.76175259999998pt/>
* From [page 310](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf), we get <img src="../../img/svgs_darkmode/f809470268ef3f91e86c966f635f3666.svg?invert_in_darkmode" align=middle width=122.13750614999998pt height=24.65753399999998pt/> and <img src="../../img/svgs_darkmode/79888fd7a9d3c46c6e67e11d2da4edce.svg?invert_in_darkmode" align=middle width=114.44120654999999pt height=22.465723500000017pt/>
* <img src="../../img/svgs_darkmode/72106b5b75088f10a698aa02ba602b21.svg?invert_in_darkmode" align=middle width=112.92596534999998pt height=24.65753399999998pt/>
* <img src="../../img/svgs_darkmode/2adbc189b9c5f0c8240c67692ea900d6.svg?invert_in_darkmode" align=middle width=60.565343849999984pt height=21.18721440000001pt/> (approx average over a day)
* <img src="../../img/svgs_darkmode/5ea383d362e973dd996284f75dbf6601.svg?invert_in_darkmode" align=middle width=50.79522854999999pt height=21.18721440000001pt/>
* <img src="../../img/svgs_darkmode/e4d866561e8cfc5e95bc019f969b9061.svg?invert_in_darkmode" align=middle width=65.70204794999998pt height=21.18721440000001pt/>
* <img src="../../img/svgs_darkmode/ea7250ff10f872e209b45d805d37ee03.svg?invert_in_darkmode" align=middle width=71.87783789999999pt height=22.465723500000017pt/> (approx)
* <img src="../../img/svgs_darkmode/8bb3dabed5fea4bfdedd8a7997e74bed.svg?invert_in_darkmode" align=middle width=93.74241029999999pt height=26.76175259999998pt/>
* <img src="../../img/svgs_darkmode/ad9ee256696ea92cbc46a08d4d49b546.svg?invert_in_darkmode" align=middle width=49.00712519999998pt height=27.77565449999998pt/> (approx)
* <img src="../../img/svgs_darkmode/00a4c91798bdaa5c46e6314d6501cb4d.svg?invert_in_darkmode" align=middle width=50.39944799999999pt height=22.465723500000017pt/> (Compared to Gr and under Creeping Flow)
* <img src="../../img/svgs_darkmode/de717fa1002ddac7aafd527c27eb5148.svg?invert_in_darkmode" align=middle width=96.66860444999998pt height=22.831056599999986pt/> from **Table A.6**, taken at <img src="../../img/svgs_darkmode/5bdf86f684b5b70a46fb2268c2b195b3.svg?invert_in_darkmode" align=middle width=16.736568749999993pt height=22.465723500000017pt/>

## Solving

<p align="center"><img src="../../img/svgs_darkmode/889ab8594699bd23a1040d142dc1fe4d.svg?invert_in_darkmode" align=middle width=367.6305567pt height=294.1957821pt/></p>

## References

* Using **Eq. 15** on [page 308](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf)
