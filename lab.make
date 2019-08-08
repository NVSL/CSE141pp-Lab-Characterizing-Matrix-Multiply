CMD_LINE_ARGS=--engine papi --stat PAPI_L2_STM --stat rapl:::PACKAGE_ENERGY:PACKAGE0 --mat-small 128 --mat-large 1024 --iterations 10
include $(ARCHLAB_ROOT)/compile.make

%.gprof: %.exe gmon.out
	prof %.exe > %.gprof

.PHONY: run-submission
run-submission: default

%.exe : %.o ../lab_files/main.o
	$(CXX) $(LDFLAGS) $^ -o $@

