import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

def train_model(data):
    X = data[['budget', 'cast_popularity', 'is_action']]
    y = data['revenue']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("R-squared:", r2_score(y_test, y_pred))
    print("MAE:", mean_absolute_error(y_test, y_pred))
    return model

if __name__ == "__main__":
    data = pd.read_csv('../data/movies_featured.csv')
    model = train_model(data)
    joblib.dump(model, '../models/regression_model.pkl')
