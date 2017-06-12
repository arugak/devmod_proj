* IdVg Vd=50mV

.param L=0.6um W=15um

m1 d g s b nmos L=0.6u W=15u
m2 d g s b nmos L=1.8u W=15u
m3 d g s b nmos L=15u  W=15u
m4 d g s b nmos L=15u  W=3u
m5 d g s b nmos L=15u  W=1.8u

vs s 0 0
vg g s 0
vd d s 50m
vb b s 0

.op
.width out=256

.temp 25
.include nmos.l

.end
