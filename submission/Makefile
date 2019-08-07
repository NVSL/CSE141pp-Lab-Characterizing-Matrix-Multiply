include ../lab.make

default: code.out

.PHONY: run-submission
run-submission: default

%.exe : %.o ../lab_files/main.o
	$(CXX) $^ $(LDFLAGS) -o $@ 
