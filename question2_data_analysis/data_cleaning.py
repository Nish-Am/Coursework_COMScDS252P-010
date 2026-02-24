import pandas as pd
import csv

class DataFeature:   

    @staticmethod 
    def get_price_category(price):
        ''' categorize prices accord to the amount '''

        if price < 20: 
            return 'Budget'
        elif price > 40: 
            return 'Premium'
        else : 
            return 'Mid-range'

    @staticmethod    
    def extract_star_rating(star_class):
        ''' Convert star rating text to number '''

        rating_dict = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        for key in rating_dict:
            if key in star_class:
                return rating_dict[key]
        return None
    
    @staticmethod
    def clean_data(raw_data_path, cleaned_data_path):
        ''' clean data and save separately '''

        books_data = pd.read_csv(raw_data_path)

        # Price standardization: Remove '£' symbol, convert to float
        books_data['Price (£)'] = books_data['Price (£)'].str.replace('Â£', '').astype(float)        

        # Rating conversion: Convert text ratings to numeric (1-5) - already numeric 
        books_data['Star Rating'] = books_data['Star Rating'].apply(DataFeature.extract_star_rating)
        
        # Handle missing data: Identify and address null values
        print(books_data.isna().sum()) # no null values 

        # Remove duplicates
        print(books_data.duplicated().sum()) # no duplicates

        # Create derived columns
        books_data['price_category'] = books_data['Price (£)'].apply(DataFeature.get_price_category)
        print(books_data[['Price (£)', 'price_category']] )
        
        # in_stock: Boolean based on availability
        books_data['in_stock'] = books_data['Availability'].eq('In stock')
        print(books_data[['Availability', 'in_stock']])

        print(books_data.head())
        print(books_data.info)
        print(books_data.shape)

        # Save to CSV
        books_data.to_csv(cleaned_data_path, index=False, quoting=csv.QUOTE_ALL)

        print(f'\nCleaning complete! {len(books_data)} books saved to cleaned_books_data.csv')