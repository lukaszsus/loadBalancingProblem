# Load Balancing Problem
Academic project. Implementing and comparing load balancing algorithms
by the example of balancing clients connections to a server cluster.

# Reading output
Outcomes are located in `output/*` as `.csv` files.
 First row in `.csv` files contains column names.
 First column contains algorithm name, second column contains
 'time' which is equal to number of iterations. Next columns names
 are weight of servers in a cluster. Server with *5w* weight serving
 5 times more connections than server with *w* weight has the same load.
 Algorithms evaluation is based on equality of servers' loads.
 
#### Test are done for:

 a) 5 algorithms:
 * round robin,
 * weighted round robin,
 * least connections,
 * weighted least connections,
 * random
 
 b) 2 duration times:
 * 100 iterations,
 * 1000 iterations
 
c) for 6 servers weights:
 * 2 servers with equal weight,
 * 2 servers with weights: 1, 5,
 * 4 servers with equal weight,
 * 4 servers with weights: 1, 2, 2, 5,
 * 10 servers with equal weights,
 * 10 servers with weights: 1, 1, 2, 3, 4, 4, 6, 7, 8, 10.