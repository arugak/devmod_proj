.SUFFIXES :

SRCCSV		= ${wildcard *.csv}

all : aurora.dat

aurora.dat  : ${SRCCSV}
	python csv2aurora.py > $@

clean :
	rm -f aurora.dat