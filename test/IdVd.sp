* IdVd Vb=0V

m1 d g s b nmos L=0.6u W=15u
m2 d g s b nmos L=1.8u W=15u
m3 d g s b nmos L=15u  W=15u
m4 d g s b nmos L=15u  W=3u
m5 d g s b nmos L=15u  W=1.8u

vs s 0 0
vg g s 0
vd d s 0
vb b s 0

.dc vd 0 5 0.1 vg 0 5.0 0.5

.temp 25
.print dc v(g) @m1[id]
.print dc v(g) @m2[id]
.print dc v(g) @m3[id]
.print dc v(g) @m4[id]
.print dc v(g) @m5[id]

.include nmos.l

.end
