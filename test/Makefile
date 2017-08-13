.SUFFIXES :

SRCSP		= ${wildcard *.sp}
DESTLIS		= ${SRCSP:.sp=.lis}

all : nmos.l ${DESTLIS}

nmos.l : ../nmos_iv/pyeda.l ../mos_cv/nmos_cv.l param_comm
	echo '* 16PTS SPICE MODEL' > $@
	echo '.MODEL NMOS NMOS'    >> $@
	cat param_comm             >> $@
	cat ../nmos_iv/pyeda.l ../mos_cv/nmos_cv.l >> $@

pmos.l : ../pmos_iv/pyeda.l ../mos_cv/pmos_cv.l param_comm
	echo '* 16PTS SPICE MODEL' > $@
	echo '.MODEL PMOS PMOS'    >> $@
	cat param_comm             >> $@
	cat ../pmos_iv/pyeda.l ../mos_cv/pmos_cv.l >> $@

%.lis : %.sp nmos.l pmos.l
	ngspice -b $< > $@
clean :
	rm -f nmos.l pmos.l *.lis
