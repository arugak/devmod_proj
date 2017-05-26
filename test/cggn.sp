* CggVg

m1 0 g 0 0 nmos L=120u W=120u
vg g 0 0v

.dc vg -5.0 5.0 0.1

.TEMP 25
.print dc @m1[cgg]

.include nmos.l

.end
