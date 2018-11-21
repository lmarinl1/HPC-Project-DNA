# HPC-Project-DNA
Module HPC: Final project of Special Topics of Telematics 2018-2, EAFIT University.

## Contents

- [Members](#Members)
- [Configuration and installation](#Configuration-and-installation)
	- [MPI4PY](#MPI4PY)
	- [Python](#Python)
- [Running the code](#Running-the-code)
- [References](#References)

## Members

**Professor Guide:**
- Edwin Nelson Montoya Munera

**Students**
- Luis Miguel Marín Loaiza
- José Orlando Rengifo Caicedo


## Configuration and installation

This section specifies how to install and configure the technologies used to carry out this project.

### MPI4PY

the **Message Passing Interface**, is a standardized and portable message-passing system designed to function on a wide variety of parallel computers. The standard defines the syntax and semantics of library routines and allows users to write portable programs in the main scientific programming languages (Fortran, C, or C++).

[**Official installation link**](https://pypi.org/project/mpi4py/)

using pip:
~~~
$ [sudo] pip install mpi4py
~~~

or alternatively _setuptools_  **easy_install** (deprecated):
~~~
$ [sudo] easy_install mpi4py
~~~

This package provides Python links for the standard message passing interface (MPI). It is implemented on the MPI-1/2/3 specification and exposes an API that is based on the standard C ++ links of MPI-2.




[**Instructional link**](https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html)

### Python

[Python](https://www.python.org/) is a modern, easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming with dynamic typing and dynamic binding. It supports modules and packages, which encourages program modularity and code reuse. Python’s elegant syntax, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

[**MPI for Python**](https://mpi4py.readthedocs.io/en/stable/)

MPI for Python provides an object oriented approach to message passing which grounds on the standard MPI-2 C++ bindings. The interface was designed with focus in translating MPI syntax and semantics of standard MPI-2 bindings for C++ to Python. Any user of the standard C/C++ MPI bindings should be able to use this module without need of learning a new interface.

To import the library use:
~~~
$ from mpi4py import MPI
~~~

## Running the code

~~~
$ mpirun -n <<processes>> python script.py
~~~

Here the -n << processes >> tells MPI to use the number of processes that you tell him, this number can not pass the number of cores you have on the machine to use. Then we tell MPI to run the python script named script .py

## References
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzE1NjM5Mjk4LDEzMzI1MDY0OTksLTE0ND
kxNjc0MzksLTE4MzQxODcyOSwtMTk5MjYyNjU1LC0xNDI4MTMz
NzEwLDIwMzU5NDM0MzYsLTk3NjkzNjk5OCwtODA3NzgzNSwtMT
Q3MzM5MjAwLC0xODIwMDQ1ODEyLC05MzQ2ODYwMjUsLTI2MDQ3
MjM4MCwtOTE5NzkxNzY4LDEwMTU4ODMyMDVdfQ==
-->