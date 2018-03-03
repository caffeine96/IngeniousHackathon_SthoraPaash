from flask import Flask
from flask import request

node = Flask(__name__)

node_transactions=[]

@node.route('txion',methods=['POST'])
def transaction():
	if request.method=='POST':
		new_transac = request.get_json()
		node_transactions.append(new_transac)
		return "Success"

if __name__=="__main__":
	node.run()

