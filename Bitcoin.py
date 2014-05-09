
from urllib.request import urlopen
import json

def getURL(url):
 
	html = urlopen(url)
	data = html.read()
	return str(data)

def useData(data):
	return json.loads(data) 

def getSubtotal(json_data):
	return json_data['subtotal']['amount']

def getFees(json_data):
	return json_data['fees']

def getTotal(json_data):
	return json_data['total']

buy_url = getURL("https://coinbase.com/api/v1/prices/buy")[2:-1] 
buy_data = useData(buy_url)

sell_url = getURL("https://coinbase.com/api/v1/prices/sell")[2:-1]
sell_data = useData(sell_url)

"""Get Buying info"""
print('Current buy price of Bitcoin is:', str("$") + getSubtotal(buy_data), buy_data['currency']) 
print('Coinbase fee is:', str("$") + getFees(buy_data)[0]['coinbase']['amount'], getFees(buy_data)[0]['coinbase']['currency'])
print('Bank fee is: ', str("$") + getFees(buy_data)[1]['bank']['amount'], getFees(buy_data)[1]['bank']['currency'])
print('Final buy price is: ', str("$") + getTotal(buy_data)['amount'], getTotal(buy_data)['currency'])
print()
print()

"""Get Selling info"""
print('Current sell price of Bitcoin is:', str("$") + getSubtotal(sell_data), sell_data['currency']) 
print('Coinbase fee is:', str("$") + getFees(sell_data)[0]['coinbase']['amount'], getFees(sell_data)[0]['coinbase']['currency'])
print('Bank fee is: ', str("$") + getFees(sell_data)[1]['bank']['amount'], getFees(sell_data)[1]['bank']['currency'])
print('Final sell price is: ', str("$") + getTotal(sell_data)['amount'], getTotal(sell_data)['currency'])

