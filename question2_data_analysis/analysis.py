import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import ttest_ind

class DataAnalyser:

    def analyse_data(cleaned_data_path):
        ''' Statistical Analysis on cleaned data '''

        # read data
        books_data = pd.read_csv(cleaned_data_path)
    
        print(f'\n---- Descriptive Statistics ---')
        # Central tendency: mean, median, mode for prices
        price_mean = round(books_data['Price (£)'].mean(), 2)
        price_median = round(books_data['Price (£)'].median(), 2)
        price_mode = round(books_data['Price (£)'].mode()[0], 2)

        print(f'price mean - {price_mean}\nprice median - {price_median} \nprice mode - {price_mode}')

        # Dispersion: standard deviation, range
        price_std = books_data['Price (£)'].std()
        price_range = books_data['Price (£)'].max() - books_data['Price (£)'].min()
        print(f'Price range is {price_range}')

        # Group statistics: average price by category (top 5)
        print(f'\nAverage Price by Category - Top 05')
        print(books_data.groupby('Category')['Price (£)'].mean().round(2).head(5))

        # Rating distribution: frequency count
        print(books_data['Star Rating'].value_counts().sort_index())

        # --------- Inferential Statistics ---------------------------------

        print(f'\n---- Inferential Statistics ---\n')

        # Outlier Detection
        Q1 = books_data['Price (£)'].quantile(0.25)
        Q3 = books_data['Price (£)'].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = books_data[(books_data['Price (£)'] < lower_bound) | (books_data['Price (£)'] > upper_bound)]

        print('Lower Bound for Price:', lower_bound)
        print('Upper Bound for Price:', upper_bound)

        if outliers.empty:
            print('There\'s no outliers for Price.')
        else:
            print('Outliers are - ', outliers['Price (£)'])

        # Correlation analysis: Pearson correlation between price and rating
        correlation = pearsonr(books_data['Price (£)'], books_data['Star Rating'])
        print('\nCorrelation between Price and Rating is :', round(correlation[0], 2))

        # Hypothesis Testing
        fiction_prices = books_data[books_data['Category'] == 'Fiction']['Price (£)']
        nonfiction_prices = books_data[books_data['Category'] != 'Non-Fiction']['Price (£)']

        t_stat, p_value = ttest_ind(fiction_prices, nonfiction_prices)

        print('\nHypthesis Testing')

        print('T-statistic:', round(t_stat, 2))
        print('P-value:', round(p_value, 2))

        if p_value < 0.05:
            print('Reject H0 → Significant difference in average prices.')
        else:
            print('Fail to reject H0 → No significant difference.')

        