import pandas as pd

books_data = pd.read_csv('books_data.csv')
#print(books_data.head())
#print(books_data.info)

# Price standardization: Remove '£' symbol, convert to float
books_data['Price (£)'] = books_data['Price (£)'].str.replace('Â£', '')

# Rating conversion: Convert text ratings to numeric (1-5) - already numeric 
print(books_data['Star Rating'].dtype) # output is int64

#print(books_data.head())