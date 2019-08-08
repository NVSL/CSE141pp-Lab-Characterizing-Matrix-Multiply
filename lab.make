CMD_LINE_ARGS=--engine papi --stat PAPI_L2_STM --stat rapl:::PACKAGE_ENERGY:PACKAGE0 --mat-small 96 --mat-large 768 --iterations 5
include $(ARCHLAB_ROOT)/compile.make

%.gprof: %.exe gmon.out
	prof %.exe > %.gprof

.PHONY: run-submission
run-submission: default

%.exe : %.o ../lab_files/main.o
	$(CXX) $(LDFLAGS) $^ -o $@

