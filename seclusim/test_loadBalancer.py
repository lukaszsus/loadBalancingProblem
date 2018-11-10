from unittest import TestCase

from seclusim.load_balancer import LoadBalancer
from seclusim.server import Server


class TestLoadBalancer(TestCase):
    servers = [Server(5), Server(3), Server(1)]

    def test__round_robin(self):
        balancer = LoadBalancer(TestLoadBalancer.servers, "round_robin")
        decisions = list()
        for i in range(12):
            decisions.append(balancer.decide())

        self.assertEqual(len([i for i in decisions if i == 0]), len([i for i in decisions if i == 1]))
        self.assertEqual(len([i for i in decisions if i == 0]), len([i for i in decisions if i == 2]))

    def test__w_round_robin(self):
        balancer = LoadBalancer(TestLoadBalancer.servers, "w_round_robin")
        decisions = list()
        for i in range(12):
            decisions.append(balancer.decide())

        self.assertEqual(8, len([i for i in decisions if i == 0]))
        self.assertEqual(3, len([i for i in decisions if i == 1]))
        self.assertEqual(1, len([i for i in decisions if i == 2]))

    def test__refresh_server_weights(self):
        balancer = LoadBalancer(TestLoadBalancer.servers, "round_robin")
        balancer._refresh_server_weights()
        weights = balancer._server_weights
        self.assertEqual(weights, [5, 3, 1])

    def test__least_conn(self):
        balancer = LoadBalancer(TestLoadBalancer.servers, "least_conn")

        TestLoadBalancer.servers[0]._active_connections_times_to_close = [1, 2]
        TestLoadBalancer.servers[1]._active_connections_times_to_close = [5, 2, 4, 8]
        TestLoadBalancer.servers[2]._active_connections_times_to_close = [1]

        decision = balancer.decide()
        self.assertEqual(decision, 2)

    def test__w_least_conn(self):
        balancer = LoadBalancer(TestLoadBalancer.servers, "w_least_conn")

        TestLoadBalancer.servers[0]._active_connections_times_to_close = [1, 2]
        TestLoadBalancer.servers[1]._active_connections_times_to_close = [5, 2, 4, 8]
        TestLoadBalancer.servers[2]._active_connections_times_to_close = [1]

        decision = balancer.decide()
        self.assertEqual(decision, 0)