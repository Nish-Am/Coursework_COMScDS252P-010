from scraper import Scrpaer
from data_cleaning import DataFeature
from analysis import DataAnalyser
from visualization import Visualizer
from prediction import Predict

raw_data_path = 'question2_data_analysis/data/raw_books_data.csv'
cleaned_data_path = 'question2_data_analysis/data/cleaned_books_data.csv'

def main():
   Scrpaer.scrape_data(raw_data_path) 
   DataFeature.clean_data(raw_data_path, cleaned_data_path)
   DataAnalyser.analyse_data(cleaned_data_path)
   Visualizer.visualize_data(cleaned_data_path)
   Predict.linear_reg_model(cleaned_data_path)


if __name__ == '__main__':
    main()