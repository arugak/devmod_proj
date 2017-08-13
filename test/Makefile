.SUFFIXES :

SRCSP		= ${wildcard *.sp}
DESTLIS		= ${SRCSP:.sp=.lis}

all : mos.lib ${DESTLIS}

nmos.l : ../nmos_iv/pyeda.l ../mos_cv/nmos_cv.l param_comm
	echo '*' > $@
	echo '.MODEL NMOS NMOS'    >> $@
	cat param_comm             >> $@
	cat ../nmos_iv/pyeda.l ../mos_cv/nmos_cv.l >> $@

pmos.l : ../pmos_iv/pyeda.l ../mos_cv/pmos_cv.l param_comm
	echo '*' > $@
	echo '.MODEL PMOS PMOS'    >> $@
	cat param_comm             >> $@
	cat ../pmos_iv/pyeda.l ../mos_cv/pmos_cv.l >> $@

mos.lib : nmos.l pmos.l
	cat head nmos.l pmos.l > $@

%.lis : %.sp nmos.l pmos.l
	ngspice -b $< > $@
clean :
	rm -f nmos.l pmos.l mos.lib *.lis
