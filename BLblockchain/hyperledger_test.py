from hyperledger.client import Client 

c=Client(base_url="http://localhost")
#c.peer_list(){u'peers': [{u'type': 1, u'ID': {u'name': u'vp1'}, u'address': u'10.20.33.185:8080'}]}

print c.new_chain("x")