from django.shortcuts import render

def marketdata(request):
	import requests
	import json

	# Grab Stocks News
	stocknews_request = requests.get("https://newsapi.org/v2/top-headlines?sources=cnbc&apiKey=590911a636c14163a52a1e72c5b6a9ff")
	stocknews = json.loads(stocknews_request.text)

	# Grab Stocks Prices
	stockprice_request = requests.get("https://api.iextrading.com/1.0/stock/market/batch?symbols=spy,amzn,googl,aapl,msft,fb,v,ma,baba,nflx,pypl,tcehy,dis,gld,adbe,unh,ba,avgo,brk.b,jpm,intu&types=quote&range=1m&last=5")
	stockprice = json.loads(stockprice_request.content.decode('utf-8'))

	#Grab Most Active Stocks
	mostactive_request = requests.get("https://api.iextrading.com/1.0/stock/market/list/mostactive")
	mostactive = json.loads(mostactive_request.content.decode('utf-8'))

	return render(request, 'marketdata.html', {'mostactive': mostactive, 'stockprice': stockprice, 'stocknews': stocknews})
