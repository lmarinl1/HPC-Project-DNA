# Design Under PCAM Methodology

## ¿What is PCAM?

This methodology structures the design process as four distinct stages: partitioning, communication, agglomeration, and   mapping. (The acronym PCAM may serve as a useful reminder of this structure.) In the first two stages, we focus on concurrency and scalability and seek to discover algorithms with these qualities. In the third and fourth stages, attention shifts to locality and other performance-related issues.

### P - Partitioning
The computation that is to be performed and the data operated on by this computation are decomposed into small tasks. Practical issues such as the number of processors in the target computer are ignored, and attention is focused on recognizing opportunities for parallel execution.

### C - Communication
The communication required to coordinate task execution is determined, and appropriate communication structures and algorithms are defined.
### A - Agglomeration
### M- Mapping

## References


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk5Njk3NDUxNCwtMTAzNjc3MTA5NV19
-->