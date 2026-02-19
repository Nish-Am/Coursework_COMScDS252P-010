import pandas as pd

def get_price_category(price):
    if price < 20: 
        return 'Budget'
    elif price > 40: 
        return 'Premium'
    else : 
        return 'Mid-range'

books_data = pd.read_csv('books_data.csv')

# Price standardization: Remove '£' symbol, convert to float
books_data['Price (£)'] = books_data['Price (£)'].str.replace('Â£', '').astype(float)

print(books_data.head())
print(books_data.info)
print(books_data.shape)

# Rating conversion: Convert text ratings to numeric (1-5) - already numeric 
print(books_data['Star Rating'].dtype) # output is int64

# Handle missing data: Identify and address null values
print(books_data.isna().sum()) # no null values 

# Remove duplicates
print(books_data.duplicated().sum()) # no duplicates

# Create derived columns
books_data['price_category'] = books_data['Price (£)'].apply(get_price_category)
print(books_data[['Price (£)', 'price_category']] )
''''''
# in_stock: Boolean based on availability
books_data['in_stock'] = books_data['Availability'].eq('In stock')
print(books_data[['Availability', 'in_stock']])

# Central tendency: mean, median, mode for prices
price_mean = round(books_data['Price (£)'].mean(), 2)
price_median = round(books_data['Price (£)'].median(), 2)
price_mode = round(books_data['Price (£)'].mode(), 2)

print(f' price mean - {price_mean}\n price median - {price_median} \n price mode - {price_mode}')

# Dispersion: standard deviation, range
price_std = books_data['Price (£)'].std()
price_range = books_data['Price (£)'].max() - books_data['Price (£)'].min()
print(f'Price range is {price_range}')

# Group statistics: average price by category (top 5)
print(books_data.groupby('Category')['Price (£)'].mean().round(2))

# Rating distribution: frequency count
print(books_data['Star Rating'].value_counts().sort_index())

#print(books_data.head())