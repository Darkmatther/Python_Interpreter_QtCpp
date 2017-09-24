# Embedded Python Interpreter inside C++/Qt application
## Author : Matthieu Kieffer

### Description
This little project shows how to execute external python programs/scripts from inside a C++/Qt widget application.<br/>
Elements from the source code (and more specifically the method MainWindow::launchPythonProgram()) could be reimplemented in another Qt application to enable running external python programs in an easy/fast way, for example reading/writing into files or launch a complex algorithm with many dependencies (e.g. object-oriented python code with many includes) that is not practical to code in C++.<br/><br/>
![Main window of the application](https://user-images.githubusercontent.com/25090342/29821873-b9be613c-8cc9-11e7-91f8-e8f8e50e5acd.png "Main window of the application")

### Motivations
I have initially written this program for two reasons:
- To be able to run some machine learning scripts that rely on the scikit-learn python library, directly within a C++/Qt window application and do further treatment with the output data using C++ code.
- To learn how to wrap a programming language into a C++ application.

After some tests I figured out that staying with pure python code and using the pyQt library for the window application would be a better choice than wrapping, but I was still interested into finishing this C++/Qt project, for self-learning satisfaction but also to provide a functional program to people who could be interested in such a C++/python embedding functionality into their own programs.

### Details about the implementation
Python wrapping functionalities have been <strong>implemented</strong> using the Very High Level Layer of the Python/C API.<br/>
Here are some useful links:<br/>
https://docs.python.org/2/c-api/index.html<br/>
https://docs.python.org/2/c-api/veryhigh.html<br/>
https://docs.python.org/2/extending/embedding.html

To make the application run properly, a working version of python2.7 must be installed onto your computer, with PATH and PYTHONPATH environment variables set correctly.
If running python script that include libraries such as numpy and scikit-learn, I recommand installing Anaconda instead. 

### Limitations
- The program is not able to read python files line by line with dynamic output/error printing, and is not able to interact with the user through the console. Instead, the program simply runs the whole python program and then prints the output/error after the end of the program execution.<br/>
In consequence, it is only possible to run python programs (single file or with multiple file inclusions) that does not interact with the user at run time.<br/>
Interaction with the user would be more complex to implement. Here is a link that could help you if you get interrested by coding such a feature: http://www.qtcentre.org/threads/22664-How-to-display-the-output-of-a-process-in-a-TextEdit-widget-in-real-time
<br/><br/>
- For an unknown reason, the program doesn't work with python module "panda" (apparently this is a common issue with the Python/C API)
<br/><br/>
- The current version of the program doesn't work with matplotlib. This seems to be due to the 32bits version of MINGW.
Qt creator is shipped with MINGW 32Bit, not 64Bit, but python module matplotlib apparently require 64bits to work (I've already encountered that problem when using python2.7 32bits in a Visual Studio project, and matplotlib was suddenly working when changing to python2.7 64bits)
--> Possible solution to the problem: install Qt Creator with MINGW-w64 (need then to be configured by hand)


(coming soon)
