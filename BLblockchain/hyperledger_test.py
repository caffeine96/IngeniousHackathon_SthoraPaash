from hyperledger.client import Client 

c=Client(base_url="http://localhost")
c.peer_list()