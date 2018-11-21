# HPC-Project-DNA
Module HPC: Final project of Special Topics of Telematics 2018-2, EAFIT University.

## Contents

- [Members](#Members)
- [Configuration and installation](#Configuration-and-installation)
	- [MPI4PY](#MPI4PY)
	- [Python](#Python)
- [Running the code](#Running-the-code)

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

## Running the code

~~~
$ mpirun -n <<processes>> python script.py
~~~

Here the -n << processes >> tells MPI to use the number of processes that you tell him, this number can not pass the number of cores you have on the machine to use. Then we tell MPI to run the python script named script .py
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MzQxODcyOSwtMTk5MjYyNjU1LC0xND
I4MTMzNzEwLDIwMzU5NDM0MzYsLTk3NjkzNjk5OCwtODA3Nzgz
NSwtMTQ3MzM5MjAwLC0xODIwMDQ1ODEyLC05MzQ2ODYwMjUsLT
I2MDQ3MjM4MCwtOTE5NzkxNzY4LDEwMTU4ODMyMDVdfQ==
-->