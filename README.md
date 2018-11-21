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

~~~
$ from mpi4py import MPI
~~~

## Execution


~~~
$ mpirun -n <<processes>> python script.py
~~~

Here the -n << processes >> tells MPI to use the number of processes that you tell him, this number can not pass the number of cores you have on the machine to use. Then we tell MPI to run the python script named script .py
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MjgxMzM3MTAsMjAzNTk0MzQzNiwtOT
c2OTM2OTk4LC04MDc3ODM1LC0xNDczMzkyMDAsLTE4MjAwNDU4
MTIsLTkzNDY4NjAyNSwtMjYwNDcyMzgwLC05MTk3OTE3NjgsMT
AxNTg4MzIwNV19
-->