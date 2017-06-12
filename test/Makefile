.SUFFIXES :

SRCSP		= ${wildcard *.sp}
DESTLIS		= ${SRCSP:.sp=.lis}

all : nmos.l ${DESTLIS}

%.lis : %.sp
	ngspice -b $< > $@
clean :
	rm -f nmos.l *.lis
