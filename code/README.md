# Solving Attempt 2 - [`desmos`](https://www.desmos.com/calculator/fj9gy8l2la)

## Goal 1: Find temperature of water surface, <img src="svgs/59678b5b387bf797f0373126223862f5.svg?invert_in_darkmode" align=middle width=19.42550939999999pt height=22.465723500000017pt/>

Using **Eq. 15** on [page 308](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf).

#### Nomenclature

* <img src="svgs/e257acd1ccbe7fcb654708f1a866bfe9.svg?invert_in_darkmode" align=middle width=11.027402099999989pt height=22.465723500000017pt/> = Intensity of Solar Radiation (i.e. Solar Constant)
* <img src="svgs/617df29b4912189585fe69e7e29f263e.svg?invert_in_darkmode" align=middle width=15.89887529999999pt height=14.15524440000002pt/> = water velocity
* <img src="svgs/87cd0788f6b51bfd6ae5cb4ac878f2ec.svg?invert_in_darkmode" align=middle width=14.45666969999999pt height=14.15524440000002pt/> = wind velocity
* <img src="svgs/f7c65c46dccd65632fc6e90e958f6b18.svg?invert_in_darkmode" align=middle width=15.928562099999992pt height=22.831056599999986pt/> = radiative heat transfer coefficient
* <img src="svgs/b68428d9419541251ddb40e003804388.svg?invert_in_darkmode" align=middle width=15.345767249999989pt height=22.831056599999986pt/> = convective heat transfer coefficient
* <img src="svgs/7063f3868a0debf878856a94132de800.svg?invert_in_darkmode" align=middle width=24.252422699999993pt height=21.95701200000001pt/> = flow rate of water
* <img src="svgs/195b90bdbbbb5339aa20fcd02989c4e7.svg?invert_in_darkmode" align=middle width=16.49171369999999pt height=14.15524440000002pt/> = emissivity of water
* <img src="svgs/69157a030fdee9e530106cffd4b9c164.svg?invert_in_darkmode" align=middle width=183.91371239999998pt height=26.76175259999998pt/> = Stefan-Boltzmann constant
* <img src="svgs/59678b5b387bf797f0373126223862f5.svg?invert_in_darkmode" align=middle width=19.42550939999999pt height=22.465723500000017pt/> = water surface temperature
* <img src="svgs/5bdf86f684b5b70a46fb2268c2b195b3.svg?invert_in_darkmode" align=middle width=16.736568749999993pt height=22.465723500000017pt/> = ambient air temperature

#### Assumptions

1. Steady state
2. Water is at rest, i.e. water velocity <img src="svgs/484f6a63bc9fbaa6c452cf02b00a0c70.svg?invert_in_darkmode" align=middle width=46.921573049999985pt height=21.18721440000001pt/> and <img src="svgs/937eda0ac640f79f11dd57bb50cf32d3.svg?invert_in_darkmode" align=middle width=55.21115324999999pt height=21.95701200000001pt/>
3. Gentle breeze present (<img src="svgs/4015d842dba09f9385f0e6786c10845b.svg?invert_in_darkmode" align=middle width=100.31284559999997pt height=24.65753399999998pt/>)

#### Equations

Upon simplifying under our assumptions, **Eq. 15** becomes:

<p align="center"><img src="svgs/d4c5e96b65184f88b2b2769863985f35.svg?invert_in_darkmode" align=middle width=151.54207695pt height=36.2778141pt/></p>

with <img src="svgs/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode" align=middle width=14.269439249999989pt height=22.831056599999986pt/> calculated at <img src="svgs/8436d02a042a1eec745015a5801fc1a0.svg?invert_in_darkmode" align=middle width=39.53182859999999pt height=21.18721440000001pt/> and <img src="svgs/7b9a0316a2fcd7f01cfd556eedf72e96.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/>, <img src="svgs/27a2cc055174e7d2697e894d18356d74.svg?invert_in_darkmode" align=middle width=15.81055739999999pt height=22.465723500000017pt/>, <img src="svgs/5a95dbebd5e79e850a576db54f501ab8.svg?invert_in_darkmode" align=middle width=16.02366149999999pt height=22.831056599999986pt/> and <img src="svgs/12d208b4b5de7762e00b1b8fb5c66641.svg?invert_in_darkmode" align=middle width=19.034022149999988pt height=22.465723500000017pt/> given by:

<p align="center"><img src="svgs/89bcd1ef87cb8df418a2440ff629173e.svg?invert_in_darkmode" align=middle width=160.78003755pt height=13.881256950000001pt/></p>
<p align="center"><img src="svgs/363cf0f185a1768eb4816d481741f5a0.svg?invert_in_darkmode" align=middle width=283.81447049999997pt height=34.7253258pt/></p>
<p align="center"><img src="svgs/cb5637a1b62799d8fef70f6a46e80fb9.svg?invert_in_darkmode" align=middle width=188.11477574999998pt height=14.611878599999999pt/></p>
<p align="center"><img src="svgs/7b0cfc77c829a2bcaf6e933827c5c08a.svg?invert_in_darkmode" align=middle width=106.43437529999999pt height=13.881256950000001pt/></p>

The convection coefficients <img src="svgs/f7c65c46dccd65632fc6e90e958f6b18.svg?invert_in_darkmode" align=middle width=15.928562099999992pt height=22.831056599999986pt/> and <img src="svgs/b68428d9419541251ddb40e003804388.svg?invert_in_darkmode" align=middle width=15.345767249999989pt height=22.831056599999986pt/> can be calculated by:

<p align="center"><img src="svgs/c19be0d9563290103f88b2f33d509fb9.svg?invert_in_darkmode" align=middle width=238.120971pt height=16.438356pt/></p>
<p align="center"><img src="svgs/216e88a0f3d92042efaed594a3b48003.svg?invert_in_darkmode" align=middle width=321.40475729999997pt height=38.2431621pt/></p>

#### Known Values

* <img src="svgs/3aa9b7fa00814e793510c8689bfccac6.svg?invert_in_darkmode" align=middle width=68.45508614999999pt height=21.18721440000001pt/>
* From assumptions, <img src="svgs/9b8ad8123297acea7ab148105e71298c.svg?invert_in_darkmode" align=middle width=46.85761079999999pt height=21.18721440000001pt/> and <img src="svgs/7efc7d974942822b0f7a1785101f1eef.svg?invert_in_darkmode" align=middle width=102.25728149999999pt height=24.65753399999998pt/>
* <img src="svgs/0e811d1830927814a2200c33ad975b0d.svg?invert_in_darkmode" align=middle width=116.48789459999998pt height=26.76175259999998pt/>
* From [page 310](../docs/papers/Experimental_validation_of_a_thermal_mod.pdf), we get <img src="svgs/f809470268ef3f91e86c966f635f3666.svg?invert_in_darkmode" align=middle width=122.13750614999998pt height=24.65753399999998pt/> and <img src="svgs/84860de70d3e4f2af7a3599c7adb47f0.svg?invert_in_darkmode" align=middle width=114.44120654999999pt height=22.465723500000017pt/>
