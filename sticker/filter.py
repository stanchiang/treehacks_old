import pandas as pd 
import os
# import get_data
import json
def loop():
	# print data['Symbol'][i]
	if '  ' in data['Symbol'][i]:
		data['Symbol'][i]=data['Symbol'][i].replace('  ',' ')
		loop()
	# else:
	# 	return 0

list_of_stock_exchange=["nasdaq","nyse","amex"]
directory= str(os.path.realpath(__file__)).replace('filter.py','')
for exchange in list_of_stock_exchange:
	path=directory+exchange+".csv"

	data=pd.read_csv(path)
	for i in range(len(data)):
		data['Symbol'][i]=data['Symbol'][i]+" US Equity"
		loop()

	print list(data.Symbol)


	# data=get_data()
	# f=open(exchange+'.json','w')
	# f.write(json.dumps(data))


	# print data.columns
