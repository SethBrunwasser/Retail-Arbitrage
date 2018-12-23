import requests
import json
from database import Database
import pandas as pd

class OfferupProDuct:
	def __init__(self, product_name, product_price):
		self.name = product_name
		self.price = product_price

	def get_name():
		return self.name

	def get_price():
		return self.price


db = Database()
response = requests.get("https://api.offerupnow.com/api/search/v4/feed/?accuracy=100&q='xbox one'")
json = json.loads(response.text)
items = json['data']['feed_items']

for item in items:
	title = item['item']['title']
	price = item['item']['price']
	post_date = item['item']['post_date']
	condition = item['item']['condition']
	db.insert_product(title, price, condition, post_date)

offerup_df = pd.read_sql("""SELECT * FROM offerup;""", db.get_connection())
print(offerup_df)


