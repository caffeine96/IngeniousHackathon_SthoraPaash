import pandas as pd
import csv   


def make_dataframe():
	filename="data.csv"
	data = [[101,'logcomp1','carrier1',3500,4000,0,0],[102,'logcomp2','carrier1',4500,6000,0,0],[103,'logcomp3','carrier2',5000,6000,5500,1]]
	df = pd.DataFrame(data,columns=['ID','logcomp','carrier','lp','cp','final','status'])
	df.to_csv(filename, sep=',', encoding='utf-8')

def add_data(fields):
	filename="data.csv"
	with open(filename, 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)


if __name__ == "__main__":
	make_dataframe()
	add_data([105,'logcomp5','carrier4',6000,8000,7000,1])
	