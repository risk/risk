# -*- coding:utf-8 -*-

CC := g++
CXX := g++
RM := rm -f
SED := sed
MV := mv

LIBS = -lpthread -lgmock_main -lgmock -lgtest

CXXFLAGS = -I"./" -I"include" -I"./google/include"
CPPFLAGS = 
LDFLAGS = -L"google/lib" $(LIBS)

VPATH = -./:include:./google/include

EXEC_EXT=exe

# sources
CPPS_ALL = $(wildcard *.cpp)
CPP_TESTS = $(wildcard *Test.cpp)
CPPS = $(filterout $(CPPTEST), $(CPPS_ALL))

# objcts
OBJ_TESTS = $(subst .cpp,.o,$(CPP_TESTS))
OBJS = $(subst .cpp,.o,$(CPPS))

# tests
BIN_TESTS = $(subst .cpp,.$(EXEC_EXT),$(CPP_TESTS))
TESTS = $(subst .cpp,,$(CPP_TESTS))

# dependencies
dependencies = $(subst .cpp,.d,$(CPPS_ALL))

.PHONY: all clean

all: $(TESTS)

$(BIN_TESTS): %.$(EXEC_EXT) : %.o $(OBJS)
	$(LINK.o) $(OBJS) $< -o $@

#$(TESTS): % : %.$(EXEC_EXT)
$(TESTS):
	./$@.$(EXEC_EXT)

.PHONY: clean

clean:
	$(RM) *.o *.$(EXEC_EXT) *.d

ifneq "$(MAKECMDGOALS)" "clean"
include $(dependencies)
endif

%.d: %.cpp
	$(CXX) $(CPPFLAGS) -M $< | \
	$(SED) 's,\($(notdir $*)\.o\) *:,$(dir $@)\1 $@: ,' >$@.tmp
	$(MV) $@.tmp $@

