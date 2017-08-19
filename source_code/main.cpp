//#include <cmath>
//#include <Python.h>
#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    w.show();

    //Close python interpreter when exiting the application
    Py_Finalize();

    return a.exec();
}
