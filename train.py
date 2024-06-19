import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model():
    # Load the combined data with FIFA rankings
    all_matches_df = pd.read_csv('all_matches_combined.csv')

    # Fill missing values for actual goals and xG
    all_matches_df['home_goals'].fillna(0, inplace=True)
    all_matches_df['away_goals'].fillna(0, inplace=True)
    all_matches_df['home_xg'].fillna(all_matches_df['home_goals']*0.5, inplace=True)
    all_matches_df['away_xg'].fillna(all_matches_df['away_goals']*0.5, inplace=True)

    # Define features and target
    features = ['home_rank', 'away_rank']
    target_home_goals = 'home_goals'
    target_away_goals = 'away_goals'
    target_home_xg = 'home_xg'
    target_away_xg = 'away_xg'

    X = all_matches_df[features]
    y_home_goals = all_matches_df[target_home_goals]
    y_away_goals = all_matches_df[target_away_goals]
    y_home_xg = all_matches_df[target_home_xg]
    y_away_xg = all_matches_df[target_away_xg]

    # Split the data
    X_train, X_test, y_train_home_goals, y_test_home_goals = train_test_split(X, y_home_goals, test_size=0.2, random_state=42)
    _, _, y_train_away_goals, y_test_away_goals = train_test_split(X, y_away_goals, test_size=0.2, random_state=42)
    _, _, y_train_home_xg, y_test_home_xg = train_test_split(X, y_home_xg, test_size=0.2, random_state=42)
    _, _, y_train_away_xg, y_test_away_xg = train_test_split(X, y_away_xg, test_size=0.2, random_state=42)

    # Initialize the models
    clf_home_goals = RandomForestRegressor(random_state=42)
    clf_away_goals = RandomForestRegressor(random_state=42)
    clf_home_xg = RandomForestRegressor(random_state=42)
    clf_away_xg = RandomForestRegressor(random_state=42)

    # Train the models
    clf_home_goals.fit(X_train, y_train_home_goals)
    clf_away_goals.fit(X_train, y_train_away_goals)
    clf_home_xg.fit(X_train, y_train_home_xg)
    clf_away_xg.fit(X_train, y_train_away_xg)

    # Save the models
    joblib.dump(clf_home_goals, 'home_goals_predictor.pkl')
    joblib.dump(clf_away_goals, 'away_goals_predictor.pkl')
    joblib.dump(clf_home_xg, 'home_xg_predictor.pkl')
    joblib.dump(clf_away_xg, 'away_xg_predictor.pkl')

    # Predictions for test set
    y_pred_home_goals = clf_home_goals.predict(X_test)
    y_pred_away_goals = clf_away_goals.predict(X_test)
    y_pred_home_xg = clf_home_xg.predict(X_test)
    y_pred_away_xg = clf_away_xg.predict(X_test)

    # Evaluate the models
    mse_home_goals = mean_squared_error(y_test_home_goals, y_pred_home_goals)
    mse_away_goals = mean_squared_error(y_test_away_goals, y_pred_away_goals)
    mse_home_xg = mean_squared_error(y_test_home_xg, y_pred_home_xg)
    mse_away_xg = mean_squared_error(y_test_away_xg, y_pred_away_xg)

    print(f"Mean Squared Error (Home Goals): {mse_home_goals}")
    print(f"Mean Squared Error (Away Goals): {mse_away_goals}")
    print(f"Mean Squared Error (Home xG): {mse_home_xg}")
    print(f"Mean Squared Error (Away xG): {mse_away_xg}")

train_model()
