include $(ARCHLAB_ROOT)/compile.make

SUBDIRS=submission solution lab_files


default:
	for i in $(SUBDIRS); do if [ -d $$i ]; then $(MAKE) -C $$i $@; fi; done
clean:
	for i in $(SUBDIRS); do if [ -d $$i ]; then $(MAKE) -C $$i $@; fi; done
#hello
