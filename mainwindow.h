#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <cmath>
#include <Python.h>
#include <QMainWindow>
#include <QContextMenuEvent>
#include "PythonConsole.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

public slots:
    void SelectPythonFile();
    void UpdateRunButton(QString text);
    char* convertStringToChar(QString s);
    void LaunchPythonProgram();

private:
    Ui::MainWindow *ui;
    PythonConsole* _pythonConsole;

};

#endif // MAINWINDOW_H
