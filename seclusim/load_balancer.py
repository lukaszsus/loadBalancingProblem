import random
from typing import List

from seclusim.server import Server


class LoadBalancer:

    def __init__(self, servers: List[Server], algorithm: str):
        self._servers = servers
        self._algorithm = algorithm
        self._decide = self.switch_algorithm()
        self._last_server = -1
        self._server_weights = list()
        self._refresh_server_weights()

    def decide(self) -> int:
        return self._decide()

    def switch_algorithm(self):
        switcher = {
            "round_robin": self._round_robin,
            "w_round_robin": self._w_round_robin,
            "least_conn": self._least_conn,
            "w_least_conn": self._w_least_conn,
            "random": self._random
        }
        if self._algorithm not in switcher:
            raise ValueError("Algorithm isn't defined.")
        return switcher.get(self._algorithm, self._round_robin)

    def _refresh_server_weights(self):
        self._server_weights[:] = [s._weight for s in self._servers]

    def _round_robin(self) -> int:
        self._last_server = (self._last_server + 1) % len(self._servers)
        return self._last_server

    def _w_round_robin(self) -> int:
        if max(self._server_weights) == 0:
            self._refresh_server_weights()
        for i in range(len(self._server_weights)):
            if self._server_weights[i] > 0:
                self._server_weights[i] -= 1
                return i

    def _least_conn(self) -> int:
        num_servers_active_conn = [s.get_num_active_conn() for s in self._servers]
        return num_servers_active_conn.index(min(num_servers_active_conn))

    def _w_least_conn(self) -> int:
        servers_rate = [s.get_num_active_conn()/s._weight for s in self._servers]
        return servers_rate.index(min(servers_rate))

    def _random(self) -> int:
        return random.randint(0, len(self._servers)-1)