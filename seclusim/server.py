class Server:

    def __init__(self, weight: int):
        self._active_connections_times_to_close = list()
        self._weight = weight
        self._connections_number_history = list()

    def add_connection(self, time_to_close):
        self._active_connections_times_to_close.append(time_to_close)

    def get_num_active_conn(self) -> int:
        return len(self._active_connections_times_to_close)

    def decrement_active_conn(self):
        for conn in self._active_connections_times_to_close:
            conn -= 1
        self._active_connections_times_to_close[:] = [conn for conn in self._active_connections_times_to_close
                                                      if conn > 0]

    def save_num_conn_to_history(self):
        self._connections_number_history.append(len(self._active_connections_times_to_close))
