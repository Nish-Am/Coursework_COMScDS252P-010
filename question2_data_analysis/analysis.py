import pandas as pd

cleaned_data_path = 'question2_data_analysis/data/cleaned_books_data.csv'

class DataAnalyser:

    def analyse_data():
        books_data = pd.read_csv(cleaned_data_path)
    
        print(f'\n---- Descriptive Statistics ---')
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

        # test modify

        print(f'\n---- Inferential Statistics ---')