import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

class Visualizer:
    def visualize_data(cleaned_data_path):
        ''' Data Visualization '''

        # read data
        books_data = pd.read_csv(cleaned_data_path)
        price_mean = round(books_data['Price (£)'].mean(), 2)

        # Histogram : Price distribution with mean line
        plt.figure(figsize=(8,5))
        plt.hist(books_data['Price (£)'], bins=20)
        plt.axvline(price_mean)

        plt.title('Price Distribution')
        plt.xlabel('Price (£)')

        # Box plot : Price comparison across top 5 categories
        top5 = books_data['Category'].value_counts().head(5).index

        filtered = books_data[books_data['Category'].isin(top5)]

        plt.figure(figsize=(10,6))
        sns.boxplot(data=filtered, x='Category', y='Price (£)')

        plt.xticks(rotation=45)
        plt.title('Price Comparison Across Top 5 Categories')

        #  Scatter plot : Price vs. Rating with regression line

        plt.figure(figsize=(8,5))
        sns.regplot(data=books_data, x='Star Rating', y='Price (£)')

        plt.title('Price vs Star Rating')
        plt.xlabel('Star Rating')
        plt.ylabel('Price (£)')

        # Bar chart : Average rating by category (top 8)
        avg_rating = (
            books_data
            .groupby('Category')['Star Rating']
            .mean()
            .sort_values(ascending=False)
            .head(8)
        )

        plt.figure(figsize=(10,6))
        avg_rating.plot(kind='bar')

        plt.title('Average Rating by Category (Top 8)')
        plt.ylabel('Average Rating')
        plt.xticks(rotation=45)

        # show all the plots 
        plt.show()

        avg_rating = (
            books_data
            .groupby('Category')['Star Rating']
            .mean()
            .sort_values(ascending=False)
            .head(8)
            .reset_index()
        )

        fig = px.bar(
            avg_rating,
            x='Category',
            y='Star Rating',
            title='Interactive: Average Rating by Category (Top 8)'
        )

        fig.show()