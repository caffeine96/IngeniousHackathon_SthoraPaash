from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('/student.html')

def add_data(d):
	temp=[]
	temp.append(101)
	temp.append(d['Container_type'])
	temp.append(d['Quantity'])
	temp.append(d['Price'])
	temp.append(d['Cargo ready from'])
	temp.append(d['Cargo ready to'])
	temp.append(d['pickup_Country'])
	temp.append(d['pickup_Port'])
	temp.append(d['destination_Country'])
	temp.append(d['destination_Port'])
	filename="logcomp1.csv"
	with open(filename, 'a') as f:
		writer = csv.writer(f)
		writer.writerow(temp)



@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print result
      add_data(result)
      return render_template("/result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)