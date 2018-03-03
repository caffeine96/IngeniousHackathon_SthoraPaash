from flask import Flask, render_template, request
from negotiate import *

app = Flask(__name__)


@app.route('/')
def student():
   return render_template('/negotiate_customer.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print result
      temp=[]
      temp.append(result['ID'])
      temp.append(result['Custmor_name'])
      temp.append(result['Carrier_name'])
      temp.append(result['amount'])
      temp.append(result['deal'])
      add_data(temp)
      return "Data is added successfully!!"


if __name__ == '__main__':
   app.run(debug = True)