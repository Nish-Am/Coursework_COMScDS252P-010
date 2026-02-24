from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import pandas as pd

class Predict:
    def linear_reg_model(cleaned_data_path):
        ''' Perform Linear Regression '''
        # read data
        books_data = pd.read_csv(cleaned_data_path)      

        # Encode Category
        X = pd.get_dummies(books_data[['Star Rating', 'Category']], drop_first=True)
        y = books_data['Price (£)']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        print(f'R² score: {r2:.3f}')
        print(f'Mean Absolute Error: £{mae:.2f}')

        coeffs = pd.Series(model.coef_, index=X.columns)
        coeffs_sorted = coeffs.abs().sort_values(ascending=False)

        print('Top features by influence on price:')
        print(coeffs_sorted.head(5))
        
