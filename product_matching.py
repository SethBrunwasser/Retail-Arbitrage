from database import Database
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from numpy.linalg import norm
import numpy as np

db = Database()
offerup_df = pd.read_sql("""SELECT * FROM offerup;""", db.get_connection())

product1 = offerup_df['product_name'][0]
rest_of_products = offerup_df['product_name'][1:]

# Feature distance using cosine similarity
def cosine_similarity(a, b):
	return np.inner(a, b) / (norm(a) * norm(b))

products_list = list(offerup_df['product_name'].head(10))
extractions = [process.extractOne(p, products_list[:idx] + products_list[idx + 1:]) for idx, p in enumerate(products_list)]

augmented_df = offerup_df.head(10)
augmented_df['extraction_product'] = [e[0] for e in extractions]
augmented_df['extraction_score'] = [e[1] for e in extractions]

ordinal_df = augmented_df[['price', 'condition', 'extraction_score']]
print(ordinal_df)

def best_cosine_similarity(query, options):

	return max(list(map(cosine_similarity, query, options)))

ordinal_2d = ordinal_df.as_array()
print(ordinal_2d)