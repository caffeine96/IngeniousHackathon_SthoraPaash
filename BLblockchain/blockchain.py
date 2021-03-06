import hashlib as hasher
import datetime as date
from flask import Flask
from flask import request

app = Flask(__name__)

previous_block=""

class BoL:
	def __init__(self, containerType, quantity, weight, fromdate, todate, fromloc, toloc, price, description):
		self.containerType = containerType
		self.quantity = quantity
		self.weight = weight
		self.fromdate = fromdate
		self.todate = todate
		self.fromloc = fromloc
		self.toloc = toloc
		self.price = price
		self.description = description

class Block:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	def hash_block(self):
		sha = hasher.sha256()
		sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
		return sha.hexdigest()

def create_genesis_block():  #Manually done
	return Block(0,date.datetime.now(),"Genesis Block","0")

def next_block(last_block,data):
	this_index = last_block.index + 1
	this_timestamp = date.datetime.now()
	this_data = data
	this_hash = last_block.hash
	return Block(this_index, this_timestamp, this_data, this_hash)

@app.route('/txadd',methods=['POST'])
def trans_add():
	global previous_block
	data = request.get_json()
	block_to_add = next_block(previous_block,data)
  	blockchain.append(block_to_add)
  	previous_block = block_to_add
  	print "Block #{} has been added to the blockchain!".format(block_to_add.index)
  	print "Hash: {}\n".format(block_to_add.hash)
  	print "Data: {}\n".format(block_to_add.data)
  	return "Block created" 

# Create the blockchain and add the genesis block
if __name__ == "__main__":
	blockchain = [create_genesis_block()]	
	previous_block = blockchain[0]
	app.run(host='0.0.0.0',port=5006)