from flask import Flask
from flask import request

node = Flask(__name__)

state={"logcomp1":100,"logcomp2":100,"logcomp3":100,"carrier1":100}

node_transactions=[]

def isValidTransac(new_transac):
	if state[new_transac["from"]]<new_transac["token"]:
		return False
	else:
		return True


@node.route('/txion',methods=['POST'])
def transaction():
	if request.method=='POST':
		new_transac = request.get_json()
		flag = isValidTransac(new_transac)
		if flag==False:
			return "Transaction failed due to lack of funds"		
		node_transactions.append(new_transac)
		return "Success"

if __name__=="__main__":
	node.run()

