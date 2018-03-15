RUNTEST=python3 -m unittest -v -b

ALLMODULES=$(patsubst %.py, %, $(wildcard *_test.py))
CLEAN_PYC=rm -r __pycache__

all:
	${RUNTEST} ${ALLMODULES}; ${CLEAN_PYC}

% : %_test.py
	${RUNTEST} $@_test; ${CLEAN_PYC}

clean:
	${CLEAN_PYC}
