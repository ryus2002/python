from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

'''
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
print (name)
# strip() 函數用於去除前後空格
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print (price)

with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, price, datetime.now()])
'''

quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND']
data = []
for pg in quote_page:
 	page = urlopen(pg)
 	soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip() # strip() is used to remove starting and trailing  
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
data.append((name, price))

with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	for name, price in data:
		writer.writerow([name, price, datetime.now()])