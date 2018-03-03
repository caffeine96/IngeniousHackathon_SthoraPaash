from flask import Flask
from flask import request
import requests
import json

node = Flask(__name__)

state={"logcomp1":100,"logcomp2":100,"logcomp3":100,"carrier1":100}

node_transactions=[]
url="http://localhost:5006/txadd"

def isValidTransac(new_transac):
	if state[new_transac["from"]]<new_transac["token"]:
		return False
	else:
		state[new_transac["from"]]=state[new_transac["from"]]-new_transac["token"]
		state[new_transac["to"]]=state[new_transac["to"]]+new_transac["token"]
		return True


@node.route('/txion',methods=['POST'])
def transaction():
	if request.method=='POST':
		new_transac = request.get_json()
		flag = isValidTransac(new_transac)
		if flag==False:
			return "Transaction failed due to lack of funds"		
		data = new_transac
    	headers = {'Content-Type' : 'application/json'}
    	r = requests.post(url, data=json.dumps(data), headers=headers)
    	node_transactions.append(new_transac)
    	print state
    	print r.text
    	return "Success"

if __name__=="__main__":
	node.run(host='0.0.0.0',port=5007)


