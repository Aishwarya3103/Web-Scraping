import requests
from bs4 import BeautifulSoup
import pandas as pd


r=requests.get('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')


products=[] #List to store name of the product
# prices=[] #List to store price of the product
# ratings=[]

soup=BeautifulSoup(r.text,'html.parser')

for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
	name=a.find('div', attrs={'class':'_4rR01T'})
	# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	# star=a.find('div',attrs={'class':'hGSR34 _2lQ_WZ'})
	products.append(name.text)
	# prices.append(price.text)
	# ratings.append(star.text)

df = pd.DataFrame({'Product Name':products})
df.to_csv('products.csv', header=True, index=False, encoding='utf-8')
