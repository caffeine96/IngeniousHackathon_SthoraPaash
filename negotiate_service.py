from flask import Flask, render_template, request
from negotiate import *
import requests,json
import pandas as pd
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
      temp.append(result['amount_Customer'])
      temp.append(result['amount_Carrier'])
      temp.append(result['deal'])
      add_data(temp)
      if result['deal']=="yes":
      	df=pd.read_csv(str(result['Custmor_name'])+".csv")
      	df_json=df.to_json(orient='split')
      	print df_json
        data = {"from":result['Carrier_name'],"to":result['Custmor_name'],"token":50,"data":df_json}
        test_url="http://10.20.34.227:5007/txion"
        headers = {'Content-Type' : 'application/json'}
        print "OK!!!!!!!"
        r = requests.post(test_url, data=json.dumps(data), headers=headers)
        #print r.text
        return "Deal is successfully closed!!"
      else:
      	return "Data is updated successfully!!"


if __name__ == '__main__':
   app.run(debug = True)