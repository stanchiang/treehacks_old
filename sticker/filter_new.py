#!/usr/bin/env python2

# usage: python HistoricalDataRequest.py <host-ip>

import pandas as pd 
import os
# import get_data
import argparse
import json
import ssl
import sys
import urllib2



def request(args,exchange):
	data = {
	"securities": exchange,
	"fields": ["DS318","DS588"]}
	req = urllib2.Request('https://{}/request?ns=blp&service=refdata&type=ReferenceDataRequest'.format(args.host))
	req.add_header('Content-Type', 'application/json')

	ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	ctx.load_verify_locations('bloomberg.crt')
	ctx.load_cert_chain('client.crt', 'client.key')

	try:
		res = urllib2.urlopen(req, data=json.dumps(data), context=ctx)
		print res.read()
		return res.read()
	except Exception as e:
		e
		print e
		return 1
	return 0


def main(exchange):
	parser = argparse.ArgumentParser()
	parser.add_argument('host', type=str)
	return request(parser.parse_args(),exchange)

def loop():
		# print data['Symbol'][i]
		if '  ' in data['Symbol'][i]:
			data['Symbol'][i]=data['Symbol'][i].replace('  ',' ')
			loop()
		# else:
		# 	return 0
if __name__ == "__main__":
		

	list_of_stock_exchange=["nasdaq"]#,"nyse]","amex"]
	directory= str(os.path.realpath(__file__)).replace('filter.py','')
	for exchange in list_of_stock_exchange:
		path=directory+exchange+".csv"

		data=pd.read_csv(path)
		for i in range(len(data)):
			data['Symbol'][i]=data['Symbol'][i]+" US Equity"
			loop()

		print list(data.Symbol)

		for 
		data=sys.exit(main(list(data.Symbol)[:100]))
		# f=open(exchange+'.json','w')
		# f.write(json.dumps(data))
		for item in data['data']:
			#business description
			print item["fieldData"]["DS318"]
			#DS588

	




	# print data.columns
