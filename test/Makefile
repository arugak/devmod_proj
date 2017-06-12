.SUFFIXES :

SRCSP		= ${wildcard *.sp}
DESTLIS		= ${SRCSP:.sp=.lis}

all : nmos.l ${DESTLIS}

nmos.l : head.nmos ../nmos_iv/pyeda.l ../mos_cv/nmos_cv.l
	cat head.nmos ../nmos_iv/pyeda.l ../mos_cv/nmos_cv.l > $@

%.lis : %.sp nmos.l
	ngspice -b $< > $@
clean :
	rm -f nmos.l *.lis
