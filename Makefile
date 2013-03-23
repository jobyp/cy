.PHONY: all
all: setup.py hw.pyx
	python setup.py build_ext --inplace

.PHONY: clean
clean:
	rm -rf build *.o *.so *~ $(patsubst %.pyx,%.c,$(wildcard *.pyx))