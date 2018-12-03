# Load Balancing Problem
Academic project. Implementing and comparing load balancing algorithms
by the example of balancing clients connections to a server cluster.

#Reading input
Input data - sets of connections are located in `input/*` as `.pickle` files.
Naming convention:
_tx<sub>t</sub>sx<sub>s</sub>mx<sub>m</sub>.pickle_
* _x<sub>t</sub>_ - time, number of iterations,
* _x<sub>s</sub>_ - number of servers, 
* _x<sub>m</sub>_ - maximum weight of one server.

Prefix *least_* means that these data were generated in unfair way to show weakness of round robin algorithm in comparison to least connections algorithm.


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
 
c) 6 servers weights:
 * 2 servers with equal weight,
 * 2 servers with weights: 1, 5,
 * 4 servers with equal weight,
 * 4 servers with weights: 1, 2, 2, 5,
 * 10 servers with equal weights,
 * 10 servers with weights: 1, 1, 2, 3, 4, 4, 6, 7, 8, 10.

#### Testing data were generated in 2 ways:
a) fair way,
b) way showing weakness of round robin algorithm in comparison to least connections algorithm.
