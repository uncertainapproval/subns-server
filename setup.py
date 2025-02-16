from gremlin_python.driver import client


# Gremlin Server connection details
GREMLIN_SERVER_URL = "ws://gremlin-server:8182/gremlin"
gremlin_client = client.Client(GREMLIN_SERVER_URL, "g")