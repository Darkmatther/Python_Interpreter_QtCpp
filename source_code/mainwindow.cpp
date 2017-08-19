#include <cmath>
#include <Python.h>
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <QDebug>
#include <fstream>
#include <string>
#include <QFile>
#include <QString>
#include <QStringList>
#include <QTextStream>
#include <QFileDialog>
#include <QRegExp>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    //Insert python console
    this->_pythonConsole = new PythonConsole();
    this->ui->widgetConsole->layout()->addWidget(_pythonConsole);
    this->_pythonConsole->setReadOnly(true);

    //Initialise buttons
    this->ui->button_runProgram->setEnabled(0);

    //Connect signals to slots
    QObject::connect(ui->button_runProgram, SIGNAL(clicked()), this, SLOT(LaunchPythonProgram()));
    QObject::connect(ui->button_fileSelection, SIGNAL(clicked()), this, SLOT(SelectPythonFile()));
    QObject::connect(ui->lineEdit_fileName, SIGNAL(textChanged(QString)), this, SLOT(UpdateRunButton(QString)));

}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::SelectPythonFile()
{
    QString fileName = QFileDialog::getOpenFileName(this, "File selection", QString("../"), "Python files (*.py)");
    if (fileName != "")
    {
        this->ui->lineEdit_fileName->setText(fileName);
    }
}


void MainWindow::UpdateRunButton(QString text)
{
    QRegExp Exp("(.py)$");

    if ( text.contains(Exp) )
    {
        this->ui->button_runProgram->setEnabled(1);
    }
    else
    {
        this->ui->button_runProgram->setEnabled(0);
    }
}


char* MainWindow::convertStringToChar(QString s)
{
    return strdup(s.toStdString().c_str());
}


void MainWindow::LaunchPythonProgram()
{

    /// CATCH INPUT PYTHON FILE AND ARGUMENTS FROM THE GUI --------------

    //Defining path for the python program
    QString file_name_string = this->ui->lineEdit_fileName->text();
    char * file_name = this->convertStringToChar(file_name_string);

    //Defining input arguments for the python program
    QStringList input_arguments_string;
    QString input_text = this->ui->lineEdit_inputArguments->text();
    if (input_text != "")
    {
        input_arguments_string = input_text.split(' ', QString::SkipEmptyParts);
    }
    else
    {
        input_arguments_string = QStringList();
    }

    //Writing path and input arguments into a char* (to be used with PySys_SetArgv())
    int nb_arguments = input_arguments_string.length() + 1;
    char *input_arguments[nb_arguments];
    input_arguments[0] = file_name;
    for (int i = 1 ; i < nb_arguments ; i++)
    {
        input_arguments[i] = this->convertStringToChar(input_arguments_string[i-1]);
    }


    /// RUN PYTHON PROGRAM  --------------

    //Open python interpreter
    Py_Initialize();


    //Run python program header to redirect standard output and error
    std::string stdOutErr =
"import sys\n\
class CatchOutErr:\n\
    def __init__(self):\n\
        self.value = ''\n\
    def write(self, txt):\n\
        self.value += txt\n\
catchOutErr = CatchOutErr()\n\
sys.stdout = catchOutErr\n\
sys.stderr = catchOutErr\n\
";
    PyRun_SimpleString(stdOutErr.c_str());


    //Set input arguments to python interpreter
    PySys_SetArgv(nb_arguments, input_arguments);


    //Open python file and read its content into a string
    QFile file(file_name_string);
    qDebug() << "File exists?" << file.exists();
    file.open(QIODevice::ReadOnly |QIODevice::Text);
    QTextStream fileStream(&file);
    QString fileContent(fileStream.readAll());


    //Run python program
    PyRun_SimpleString(fileContent.toStdString().c_str());


    //Catch standard output and error into C++ code
    PyObject *pModule = PyImport_AddModule("__main__"); //create main module
    PyObject *catcher = PyObject_GetAttrString(pModule,"catchOutErr"); //get catchOutErr created above
    PyObject *output = PyObject_GetAttrString(catcher,"value"); //get stdout and stderr from catchOutErr object
    QString outputConsole = PyString_AsString(output); //Get output as a QString


    //Write standard output and errors into ui->pythonConsole (QTextEdit)
    this->_pythonConsole->insertPlainText(outputConsole);


    //Scroll to the end of the python console
    QTextCursor c = this->_pythonConsole->textCursor();
    c.movePosition(QTextCursor::End);
    this->_pythonConsole->setTextCursor(c);


    //Note: Closing python interpreter is done only once in main.cpp (to avoid problems with multiple import of complex python modules such as numpy)

}
