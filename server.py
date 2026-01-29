from openreward.environments import Server

from hle import HLE

if __name__ == "__main__":
    server = Server([HLE])
    server.run()
