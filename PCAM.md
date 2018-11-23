# Design Under PCAM Methodology

## Contents

- [¿What is PCAM?](#what-is-pcam)
	- [P - Partitioning](#p---partitioning)
	- [C - Communication](#C---Communication)
	- [A - Agglomeration](#A---Agglomeration)
	- [M - Mapping](#M---Mapping)
- [Designing our parallel algorithm](#Designing-our-parallel-algorithm)
	- [Performance analysis](#Performance-analysis)


## ¿What is PCAM?

This methodology structures the design process as four distinct stages: partitioning, communication, agglomeration, and   mapping. (The acronym PCAM may serve as a useful reminder of this structure.) In the first two stages, we focus on concurrency and scalability and seek to discover algorithms with these qualities. In the third and fourth stages, attention shifts to locality and other performance-related issues.

![problem](images/problem.png)

### P - Partitioning
The computation that is to be performed and the data operated on by this computation are decomposed into small tasks. Practical issues such as the number of processors in the target computer are ignored, and attention is focused on recognizing opportunities for parallel execution.

![Partitioning](images/partition.png)

### C - Communication
The communication required to coordinate task execution is determined, and appropriate communication structures and algorithms are defined.

![Communication](images/communicate.png)

### A - Agglomeration
The task and communication structures defined in the first two stages of a design are evaluated with respect to performance requirements and implementation costs. If necessary, tasks are combined into larger tasks to improve performance or to reduce development costs.

![Agglomeration](images/agglomerate.png)

### M - Mapping
Each task is assigned to a processor in a manner that attempts to satisfy the competing goals of maximizing processor utilization and minimizing communication costs. Mapping can be specified statically or determined at runtime by load-balancing algorithms.

![Agglomeration](images/map.png)

![PCAM](images/PCAM.gif)

## Designing our parallel algorithm

**Basic cycle of a parallel program:**

1. Algorithm design
2. Analytical performance modeling
3. Election of the "paradigm" of parallel programming that will be used
	- Paradigm of parallel programming with shared memory (SM).
	- Paradigm of parallel programming with message passing (MP).
4. Language / library / development tools selection that is
will use for the creation of the program
5. Codification
6. Testing and debugging
7. Quantitative performance studies
8. "Optimization

## References

[1]https://www.mcs.anl.gov/~itf/dbpp/text/node15.html
[2]http://homepage.physics.uiowa.edu/~ghowes/teach/ihpc12/lec/ihpc12Lec_DesignHPC12.pdf


<!--stackedit_data:
eyJoaXN0b3J5IjpbOTExNDk4NjM5LC0yNjQyNjQ2NzAsLTIwNz
MyODk4MTAsMTA4NTYxNzg4OV19
-->