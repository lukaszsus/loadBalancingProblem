import gc

import pandas as pd
import pickle
from typing import List

from seclusim import generate_connections, Server, LoadBalancer

num_sample = 1000
times = [100] # , 1000] # , 10000]
server_weights = [[1, 1],
                  [1, 5],
                  [1, 1, 1, 1],
                  [1, 2, 2, 5],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 2, 3, 4, 4, 6, 7, 8, 10]]
algorithms = ["round_robin",
              "w_round_robin",
              "least_conn",
              "w_least_conn",
              "random"]


def test_cases_to_file():
    for time in times:
        for weights in server_weights:
            name = 't' + str(time) + 's' + str(len(weights)) + 'm' + str(max(weights)) + '.pickle'

            with open('../input/' + name, "wb") as f:
                for i in range(num_sample):
                    connections, duration = generate_connections(time, sum(weights))
                    # write a file
                    pickle.dump(connections, f)
                    pickle.dump(duration, f)


def special_test_cases_to_file():
    """
    Special test cases to show that least connections is quite good.
    :return:
    """
    for time in times:
        for weights in server_weights:
            name = 'least_t' + str(time) + 's' + str(len(weights)) + 'm' + str(max(weights)) + '.pickle'

            with open('../input/' + name, "wb") as f:
                for i in range(num_sample):
                    connections, duration = generate_connections(time, sum(weights), len(weights))
                    # write a file
                    pickle.dump(connections, f)
                    pickle.dump(duration, f)


def solve_test_cases_to_file():
    for time in times:
        for weights in server_weights:
            output = list()
            columns_names = ["algorithm", "time"]
            columns_names.extend([str(w) for w in weights])
            for algorithm in algorithms:
                input_name = 'least_t' + str(time) + 's' + str(len(weights)) + 'm' + str(max(weights)) + '.pickle'
                output_name = 'least_t' + str(time) + 's' + str(len(weights)) + 'm' + str(max(weights)) + '.csv'
                with open('../input/' + input_name, "rb") as f:
                    for i in range(num_sample):
                        print(algorithm + '_' + output_name + '_' + str(i))
                        # read from a file
                        connections = pickle.load(f)
                        duration = pickle.load(f)

                        servers = [Server(w) for w in weights]
                        mean_loads = solve_single_test_case(algorithm, servers, connections, duration)

                        output.append([algorithm, time])
                        output[-1].extend(mean_loads)
            df = pd.DataFrame.from_records(output, columns=columns_names)
            df.to_csv('../output/' + output_name, index=False)
        print("Invoking garbage collector...")
        gc.collect()


def solve_single_test_case(algorithm: str, servers: List[Server], connections: List[list], duration: int) -> list:
    balancer = LoadBalancer(servers, algorithm)
    for i in range(duration):
        for s in servers:
            s.decrement_active_conn()
        if i < len(connections):
            for duration in connections[i]:
                decision = balancer.decide()
                servers[decision].add_connection(duration)
        for s in servers:
            s.save_num_conn_to_history()
    return [s.get_mean_load() for s in servers]




if __name__ == '__main__':
    # test_cases_to_file()
    # special_test_cases_to_file()
    solve_test_cases_to_file()
