lib_LTLIBRARIES = libascenario.la

libascenario_la_SOURCES=ascenario.c
#noinst_HEADERS=alsactl.h

alsaincludedir = ${includedir}/alsa

#alsainclude_HEADERS = ascenario.h

CFLAGS += -Wall

libascenario_la_LDFLAGS = \
	-version-info $(LT_VERSION) \
	-release $(LT_RELEASE) \
	-no-undefined \
	-export-dynamic
