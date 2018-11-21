# HPC-Project-DNA
Module HPC: Final project of Special Topics of Telematics 2018-2, EAFIT University.

## Contents

- [Members](#Members)
- [Configuración e instalación](#Configuración-e-instalación)
	- [MPI4PY](#MPI4PY)
	- [Python](#Python)
- [Ejecución](#Ejecución)

## Members

**Professor Guide:**
- Edwin Nelson Montoya Munera

**Students**
- Luis Miguel Marín Loaiza
- José Orlando Rengifo Caicedo


## Configuration and installation

This section specifies how to install and configure the technologies used to carry out this project.

### MPI4PY

[**Official installation link**](https://pypi.org/project/mpi4py/)

This package provides Python links for the standard message passing interface (MPI). It is implemented on the MPI-1/2/3 specification and exposes an API that is based on the standard C ++ links of MPI-2.




[**Instructional link**](https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html)

### Python

[**MPI for Python**](https://mpi4py.readthedocs.io/en/stable/)
To import the library use:
~~~
$ from mpi4py import MPI
~~~

## Execution


~~~
$ mpirun -n <<processes>> python script.py
~~~

Here the -n << processes >> tells MPI to use the number of processes that you tell him, this number can not pass the number of cores you have on the machine to use. Then we tell MPI to run the python script named script .py
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNzM5NjA2MjIsLTE5OTI2MjY1NSwtMT
QyODEzMzcxMCwyMDM1OTQzNDM2LC05NzY5MzY5OTgsLTgwNzc4
MzUsLTE0NzMzOTIwMCwtMTgyMDA0NTgxMiwtOTM0Njg2MDI1LC
0yNjA0NzIzODAsLTkxOTc5MTc2OCwxMDE1ODgzMjA1XX0=
-->