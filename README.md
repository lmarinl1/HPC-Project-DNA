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

~~~
$ 
~~~


[**Instructional link**](https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html)

### Python

## Execution


~~~
$ mpirun -n <<>> python script.py
~~~

Here the -n 4 tells MPI to use four processes, which is the number of cores I have on my laptop. Then we tell MPI to run the python script named script.py.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzc5NzY2MTQ0LC04MDc3ODM1LC0xNDczMz
kyMDAsLTE4MjAwNDU4MTIsLTkzNDY4NjAyNSwtMjYwNDcyMzgw
LC05MTk3OTE3NjgsMTAxNTg4MzIwNV19
-->