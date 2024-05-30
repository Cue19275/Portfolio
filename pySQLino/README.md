# pySQLino
Public repository of the library responsible for automating and synchronizing the use of embedded systems and databases through Python.
# Prerequisite Software
->Have SQL Server downloaded and ensure it can be accessed both by SQL Server Security User and by Windows Authentication.
->The internal libraries of pySQLino are native to the standard Python installation. In case of errors, check the imports section of the code and complete the missing imported libraries in that section.
->ArduinoIDE to load the .ino code file onto an ARDUINO UNO board exclusively.
# Using pySQLino
->Clone the repository or download the following two files: pySQLino.py and pySQLino.ino.
->Place the pySQLino.py file in the same active directory as the Python code file implementing the library.
->Load the code contained in pySQLino.ino onto an ARDUINO UNO board. For each new use of the board with a new process instance using the Python library, it is strongly recommended to press the reset button on the board.

As a reference, a pruebaslib.py file is included where you can see how the library is implemented with all its functions
