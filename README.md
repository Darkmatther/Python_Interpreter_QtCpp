# Embedded Python Interpreter inside C++/Qt application
## Author : Matthieu Kieffer

### Description
This little project shows how to execute external python programs/scripts from inside a C++/Qt widget application. 
Elements from the source code (and more specifically the method MainWindow::launchPythonProgram()) could be reimplemented in another Qt application to enable running external python programs in an easy/fast way, for example reading/writing into files or launch a complex algorithm with many dependencies (e.g. object-oriented python code with many includes) that is not practical to code in C++.<br/><br/>

![Main window of the application](https://user-images.githubusercontent.com/25090342/29821873-b9be613c-8cc9-11e7-91f8-e8f8e50e5acd.png#right "Main window of the application")


### Motivations
I have initially written this program for two reasons:
- To be able to run some machine learning scripts that rely on the scikit-learn python library, directly within a C++/Qt window application and do further treatment with the output data using C++ code.
- To learn how to wrap a programming language into a C++ application.

After some research I figured out that staying with pure python code and using the pyQt library for the window application would be a better choice than wrapping, but I was still interested into finishing this C++/Qt project, for self-learning satisfaction but also to provide a functional program to people who could be interested in such a C++/python embedding functionality into their own programs.

### Details about the implementation
Python wrapping functionalities have been <strong>implemented</strong> using the Very High Level Layer of the Python/C API. Here are some useful links:<br/>
https://docs.python.org/2/c-api/index.html<br/>
https://docs.python.org/2/c-api/veryhigh.html<br/>
https://docs.python.org/2/extending/embedding.html

