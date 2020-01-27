TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp

unix:!macx: LIBS += -L$$(SYSTEMC_HOME)/lib-linux/ -lsystemc-2.3.1

INCLUDEPATH += $$(SYSTEMC_HOME)/include
DEPENDPATH += $$(SYSTEMC_HOME)/include

HEADERS += \
    exe.h
