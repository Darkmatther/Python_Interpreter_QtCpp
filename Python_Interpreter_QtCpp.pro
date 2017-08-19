#-------------------------------------------------
#
# Project created by QtCreator 2017-07-31T01:37:01
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Python_Interpreter_QtCpp
TEMPLATE = app

DEFINES += QT_DEPRECATED_WARNINGS


SOURCES += \
        main.cpp \
        mainwindow.cpp \
        PythonConsole.cpp

HEADERS += \
        mainwindow.h \
        PythonConsole.h

FORMS += \
        mainwindow.ui


#Required lines to enable python scripting inside C++ program
INCLUDEPATH += C:\Anaconda2\include
LIBS += C:\Anaconda2\libs\python27.lib

#Required windows setup
# - Add anaconda to "Path" system environment variable
# - Add anaconda to user environment variable "PYTHONPATH"

#Required lines in each python files to be read:
# - import os (?)
# - import sys
# - sys.path.append('pathToPythonFileFolder')
#   ex: 'H:/Matthieu/Perso/Programmation/Qt/test3'

#Information:
# - When pressing "Run program" button, the chosen file path is put into the python argument argv[0] so that the program can find related python files (in case of multiple imports)
# - When pressing "Run program" button, the "input arguments" string is split and put in the python arguments argv[i] using PySys_SetArgv()

#WARNINGS:
# - The program is not able to read python files line by line with dynamic output/error printing, and is not able to interact with the user through the console.
#   Instead, the program simply runs the whole python program and then prints the output/error after the end of the program execution.
#   It it then only possible to run python programs (single file or with multiple external files inclusions) that does not interact with the user. In particular it can generate an output file to be used later in the C++ code
#   http://www.qtcentre.org/threads/22664-How-to-display-the-output-of-a-process-in-a-TextEdit-widget-in-real-time

# - Program doesn't work with python module "panda" (why??)

# - Program doesn't work with matplotlib (why??)
#   -->   Seems to be due to the 32B version of MINGW.
#         Qt creator is shipped with MINGW 32Bit, not 64Bit,
#         but python module matplotlib (and maybe also panda) require 64Bit
#   --> Solution: install MINGW-w64 and configure everything by hand
