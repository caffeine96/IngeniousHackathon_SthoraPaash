import pandas as pd
import csv   


filename="logcomp1.csv"
data=[]
df = pd.DataFrame(data,columns=['ID','Container_type','Quantity','Price','Cargo ready from','Cargo ready to','pickup_Country','pickup_Port','destination_Country','destination_Port'])
df.to_csv(filename, sep=',', encoding='utf-8')
