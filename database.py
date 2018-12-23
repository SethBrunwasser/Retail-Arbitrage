import sqlite3

class Database:
	def __init__(self):

		try:
			self.conn = sqlite3.connect("products.db") # or use :memory: to put it in RAM
		except Error as e:
			print(e)

		cursor = self.conn.cursor()
		

		cursor.execute("""CREATE TABLE IF NOT EXISTS offerup (
			id integer primary key,
			product_name text, 
			price float,
			condition integer, 
			post_date text)""")

	def insert_product(self, name, price, condition, date):
		print(name, price, date)
		cursor = self.conn.cursor()
		cursor.execute("""INSERT INTO offerup (product_name, price, condition, post_date) VALUES (?, ?, ?, ?);""",  (name, price, condition, date))
		self.conn.commit()

	def fetch_all(self):
		cursor = self.conn.cursor()
		cursor.execute("""SELECT * FROM offerup;""")
		return cursor.fetchall()

	def get_connection(self):
		return self.conn

	def clear(self):
		cursor = self.conn.cursor()
		cursor.execute("""DROP TABLE offerup;""")
		self.conn.commit()