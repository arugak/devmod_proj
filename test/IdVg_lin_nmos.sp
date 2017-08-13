* IdVg Vd=50mV

m1 d g s b nmos L=0.6u W=15u
m2 d g s b nmos L=1.8u W=15u
m3 d g s b nmos L=15u  W=15u
m4 d g s b nmos L=15u  W=3u
m5 d g s b nmos L=15u  W=1.8u

vs s 0 0
vg g s 0
vd d s 50m
vb b s 0

.dc vg 0 5 0.1 vb 0 -3.0 -0.5

.temp 25
.print dc v(b) @m1[id]
.print dc v(b) @m2[id]
.print dc v(b) @m3[id]
.print dc v(b) @m4[id]
.print dc v(b) @m5[id]
.include nmos.l

.end
