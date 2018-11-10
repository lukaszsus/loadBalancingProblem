import random

def generate_connections(time: int, servers_capacity: int):
    """
    Generates list of list of connections' durations.
    It uses Weibull distribution to generate_connections connection duration which has two parameters:
    - k - shape parameter
    - lambda_ - scale parameter - time in which 1-1/e (~63,2%) of population will die =>
                => cumulative dist fun will have a value of 1-1/e in labmda time
    :param time: duration of program (num of iterations)
    :param servers_capacity: sum of servers weights
    :return: list of list of connections' durations and time to end for all of them
    """
    k = 2
    lambda_ = 10
    active_conn = list()
    connections = list()

    for i in range(time):
        active_conn = [conn for conn in active_conn if conn > 0]
        for i in range(len(active_conn)):
            active_conn[i] -= 1

        new_conn = list()
        if i in [0,1]:          # first two iterations have a lot of new connections
            for j in range(servers_capacity):
                new_conn.append(round(random.weibullvariate(lambda_, k) + 1))       # don't want to have 0
        else:
            num_new_conn = round(random.weibullvariate(servers_capacity, k))\
                if len(active_conn) <= servers_capacity*10 else 0
            for j in range(num_new_conn):
                new_conn.append(round(random.weibullvariate(lambda_, k) + 1))       # don't want to have 0

        connections.append(new_conn)
        active_conn.extend(new_conn)

    return connections, (len(connections)+max(active_conn))