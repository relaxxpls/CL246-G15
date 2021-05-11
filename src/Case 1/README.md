# Case 1: No Water Layer - [`notebook`](heat_flux_no_water.ipynb)

Find Resultant Resistance and Heat Rate

## Nomenclature

* <img src="../../img/svgs_darkmode/5bdf86f684b5b70a46fb2268c2b195b3.svg?invert_in_darkmode" align=middle width=16.736568749999993pt height=22.465723500000017pt/> = ambient air temperature (outside)
* <img src="../../img/svgs_darkmode/78543ca0738739880432659c1a7f290d.svg?invert_in_darkmode" align=middle width=16.06363439999999pt height=22.465723500000017pt/> = room temperature (inside)
* <img src="../../img/svgs_darkmode/b22615dd642e1ba890adf269cdc19e6e.svg?invert_in_darkmode" align=middle width=33.428566049999986pt height=22.465723500000017pt/> = Nusselt number of air
* <img src="../../img/svgs_darkmode/ebd111934a8279eb01536610b8da831b.svg?invert_in_darkmode" align=middle width=30.31594829999999pt height=22.465723500000017pt/> = Rayleigh number of air
* <img src="../../img/svgs_darkmode/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode" align=middle width=10.57650494999999pt height=14.15524440000002pt/> = thermal diffusivity of air
* <img src="../../img/svgs_darkmode/eb4513540706477e80b47eb048eeaa9d.svg?invert_in_darkmode" align=middle width=15.68825939999999pt height=22.831056599999986pt/> = thermal conductivity of air
* <img src="../../img/svgs_darkmode/f7c65c46dccd65632fc6e90e958f6b18.svg?invert_in_darkmode" align=middle width=15.928562099999992pt height=22.831056599999986pt/> = heat transfer coefficient for room air
* Roof layers:
  * 1: Concrete
  * 2: Brick
  * 3: Lime
* <img src="../../img/svgs_darkmode/ec71f47b6aee7b3cd545386b93601915.svg?invert_in_darkmode" align=middle width=13.20877634999999pt height=22.831056599999986pt/> = thermal conductivity of <img src="../../img/svgs_darkmode/3def24cf259215eefdd43e76525fb473.svg?invert_in_darkmode" align=middle width=18.32504519999999pt height=27.91243950000002pt/> roof layer
* <img src="../../img/svgs_darkmode/6af2b4e795d7f62666e31c283eb02410.svg?invert_in_darkmode" align=middle width=15.838142099999992pt height=22.465723500000017pt/> = length of <img src="../../img/svgs_darkmode/3def24cf259215eefdd43e76525fb473.svg?invert_in_darkmode" align=middle width=18.32504519999999pt height=27.91243950000002pt/> roof layer
* <img src="../../img/svgs_darkmode/886420e78c2c7a0eae7fc784e45bf6b8.svg?invert_in_darkmode" align=middle width=13.79576054999999pt height=14.15524440000002pt/> = radiative heat transfer (per unit area)
* <img src="../../img/svgs_darkmode/7c9a374605e54760ce4ffa2f36666ca5.svg?invert_in_darkmode" align=middle width=13.21296404999999pt height=14.15524440000002pt/> = convective heat transfer (per unit area)
* <img src="../../img/svgs_darkmode/88101fdb8c6c5c5b9ddad575a78144b7.svg?invert_in_darkmode" align=middle width=12.30410444999999pt height=14.15524440000002pt/> = net heat transfer into the room (per unit area)
* <img src="../../img/svgs_darkmode/8217ed3c32a785f0b5aad4055f432ad8.svg?invert_in_darkmode" align=middle width=10.16555099999999pt height=22.831056599999986pt/> = coefficient of thermal expansion
* <img src="../../img/svgs_darkmode/b49211c7e49541e500c32b4d56d354dc.svg?invert_in_darkmode" align=middle width=9.16670204999999pt height=14.15524440000002pt/> = dynamic Viscosity
* <img src="../../img/svgs_darkmode/bf0eb1d093be7d37eb1b31df2cc15af0.svg?invert_in_darkmode" align=middle width=17.91555644999999pt height=22.465723500000017pt/> = total emissive power of a Blackbody
* <img src="../../img/svgs_darkmode/8eb543f68dac24748e65e2e4c5fc968c.svg?invert_in_darkmode" align=middle width=10.69635434999999pt height=22.465723500000017pt/> = radiosity

## Assumptions

* Room is maintained at constant temperature, i.e. <img src="../../img/svgs_darkmode/63fc6e69abc8df3f03089a338dceb3aa.svg?invert_in_darkmode" align=middle width=137.43554715pt height=22.63850490000001pt/>
* Main source of radition is the sun (solar radation)
* Dimensions of roof <img src="../../img/svgs_darkmode/36388ef4fce98fd7ad3e9828c4a460fb.svg?invert_in_darkmode" align=middle width=137.36307585pt height=21.18721440000001pt/>

## Equations

Nu correlations,
<p align="center"><img src="../../img/svgs_darkmode/b66b864e3818127f6225cfbfe044e5f2.svg?invert_in_darkmode" align=middle width=355.59175739999995pt height=51.66200325pt/></p>

<p align="center"><img src="../../img/svgs_darkmode/2433661e00474b0d727cd3248c4457f2.svg?invert_in_darkmode" align=middle width=200.8438047pt height=35.77743345pt/></p>

Also,
<p align="center"><img src="../../img/svgs_darkmode/646f5ce1839eb53155382dbe55a315b4.svg?invert_in_darkmode" align=middle width=149.22309105pt height=145.77025154999998pt/></p>

Roof layers:
<p align="center"><img src="../../img/svgs_darkmode/02dc4abc738b77a4685d61bf4ac142dd.svg?invert_in_darkmode" align=middle width=140.453148pt height=47.35857885pt/></p>
Thus finally,
<p align="center"><img src="../../img/svgs_darkmode/0bb056f69fb537532ba5a66a74757e5b.svg?invert_in_darkmode" align=middle width=90.6253458pt height=36.09514755pt/></p>

## Values

* <img src="../../img/svgs_darkmode/8bb3dabed5fea4bfdedd8a7997e74bed.svg?invert_in_darkmode" align=middle width=93.74241029999999pt height=26.76175259999998pt/>
* <img src="../../img/svgs_darkmode/b351cf1982c146528afb5afadd490d61.svg?invert_in_darkmode" align=middle width=74.02206074999998pt height=22.465723500000017pt/> thick with,
  * Cement = <img src="../../img/svgs_darkmode/ca41edaf1facf152e012dc3051b8ede7.svg?invert_in_darkmode" align=middle width=35.245557599999984pt height=21.18721440000001pt/>
  * Brick = <img src="../../img/svgs_darkmode/6cfca9fd624cd5e4b6ab75343c772208.svg?invert_in_darkmode" align=middle width=43.46476694999999pt height=21.18721440000001pt/>
  * Lime = <img src="../../img/svgs_darkmode/ca41edaf1facf152e012dc3051b8ede7.svg?invert_in_darkmode" align=middle width=35.245557599999984pt height=21.18721440000001pt/>
* <img src="../../img/svgs_darkmode/655ca15e2b101fb431577b12d4442580.svg?invert_in_darkmode" align=middle width=18.61211054999999pt height=22.465723500000017pt/>, Conductivity of each layer,
  * Cement = <img src="../../img/svgs_darkmode/81a4b850e73574c8ddb485c89d42a5ca.svg?invert_in_darkmode" align=middle width=93.81908084999999pt height=24.65753399999998pt/>
  * Brick = <img src="../../img/svgs_darkmode/bdd016cacecf68269fa25b4cca0a926b.svg?invert_in_darkmode" align=middle width=93.81908084999999pt height=24.65753399999998pt/>
  * Lime = <img src="../../img/svgs_darkmode/a1fdd021324963918c21db9d276da4c9.svg?invert_in_darkmode" align=middle width=93.81908084999999pt height=24.65753399999998pt/>
* Table A.4, air (<img src="../../img/svgs_darkmode/9416b5ada5d012dd819ba0fd39351272.svg?invert_in_darkmode" align=middle width=79.8402297pt height=22.465723500000017pt/>):
  * <img src="../../img/svgs_darkmode/ab57350ed56c22bdbd0567edba565077.svg?invert_in_darkmode" align=middle width=136.6932831pt height=26.76175259999998pt/>
  * <img src="../../img/svgs_darkmode/a0536eb180a6ac09da870c4c9c02740e.svg?invert_in_darkmode" align=middle width=138.1030992pt height=26.76175259999998pt/>
  * <img src="../../img/svgs_darkmode/b67c20ed043746453ddd8d51de205fed.svg?invert_in_darkmode" align=middle width=80.07041954999998pt height=22.465723500000017pt/>
  * <img src="../../img/svgs_darkmode/01330b5637501310669802cac0680ad9.svg?invert_in_darkmode" align=middle width=177.29818755pt height=26.76175259999998pt/>
* <img src="../../img/svgs_darkmode/59d0a2496609317436f9bf66a3efa198.svg?invert_in_darkmode" align=middle width=172.72629824999999pt height=26.76175259999998pt/>
* <img src="../../img/svgs_darkmode/00005401715a0dc4c56c2af4841f8761.svg?invert_in_darkmode" align=middle width=132.69020984999997pt height=26.76175259999998pt/>
* <img src="../../img/svgs_darkmode/e2d20334a09c749ceb8fa028a61d79e2.svg?invert_in_darkmode" align=middle width=156.22998764999997pt height=27.77565449999998pt/>
* <img src="../../img/svgs_darkmode/e123e310125ab26fb1ca77335ff5989a.svg?invert_in_darkmode" align=middle width=137.4866856pt height=21.18721440000001pt/>
* <img src="../../img/svgs_darkmode/69dcca8985e20d5edcbfbefbf10465c8.svg?invert_in_darkmode" align=middle width=217.72670205pt height=26.76175259999998pt/>
* <img src="../../img/svgs_darkmode/bb3ed15ad93881249645e6f2e0ca2927.svg?invert_in_darkmode" align=middle width=40.83319019999999pt height=22.465723500000017pt/>
* <img src="../../img/svgs_darkmode/482ecc1ff4a5e1af2cc3b4aa53d8e037.svg?invert_in_darkmode" align=middle width=81.20273204999998pt height=22.63850490000001pt/> (Room Temperature)

## Solving

<p align="center"><img src="../../img/svgs_darkmode/309d7217a9bacae60b135a432b68e59d.svg?invert_in_darkmode" align=middle width=320.82551159999997pt height=672.21206085pt/></p>

Resistance net,
<p align="center"><img src="../../img/svgs_darkmode/ab8ef8f5a99ffe9edae1223e0aae79cb.svg?invert_in_darkmode" align=middle width=237.3076167pt height=166.05840405pt/></p>

Thus finally,
<p align="center"><img src="../../img/svgs_darkmode/1041d80cc030ac59861cea8a576e35d0.svg?invert_in_darkmode" align=middle width=350.75082899999995pt height=33.62942055pt/></p>

Finally, solve above equation for <img src="../../img/svgs_darkmode/27a2cc055174e7d2697e894d18356d74.svg?invert_in_darkmode" align=middle width=15.81055739999999pt height=22.465723500000017pt/> and <img src="../../img/svgs_darkmode/ed529d3d2fadeb925283ab80c1e7e98e.svg?invert_in_darkmode" align=middle width=26.667045899999987pt height=14.15524440000002pt/> with varying <img src="../../img/svgs_darkmode/8f23ba996b847263bdd855451a8dc3fb.svg?invert_in_darkmode" align=middle width=22.711268249999986pt height=22.465723500000017pt/>.
