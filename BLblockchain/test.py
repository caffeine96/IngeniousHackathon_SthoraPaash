import requests,json

data = {"from":"carrier1","to":"logcomp1","token":50,"data":{"Something":"Something"}}

test_url="http://localhost:5007/txion"
headers = {'Content-Type' : 'application/json'}
r = requests.post(test_url, data=json.dumps(data), headers=headers)
print r.text
