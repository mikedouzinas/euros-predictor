import pandas as pd
import joblib
from tabulate import tabulate

def predict_outcomes():
    # Load the fixtures data for Euro 2024
    euro_2024_fixtures_df = pd.read_csv('euro_2024_matches.csv')

    # Define the features
    features = ['home_rank', 'away_rank']

    # Ensure there are no missing values in the rankings
    euro_2024_fixtures_df['home_rank'] = euro_2024_fixtures_df['home_rank'].fillna(0)
    euro_2024_fixtures_df['away_rank'] = euro_2024_fixtures_df['away_rank'].fillna(0)

    # Extract features for the upcoming fixtures
    X_upcoming_fixtures = euro_2024_fixtures_df[euro_2024_fixtures_df['played'] == False][features]

    # Load the trained models
    clf_home_goals = joblib.load('home_goals_predictor.pkl')
    clf_away_goals = joblib.load('away_goals_predictor.pkl')
    clf_home_xg = joblib.load('home_xg_predictor.pkl')
    clf_away_xg = joblib.load('away_xg_predictor.pkl')

    # Predict the scores for the upcoming fixtures
    euro_2024_fixtures_df.loc[euro_2024_fixtures_df['played'] == False, 'predicted_home_goals'] = clf_home_goals.predict(X_upcoming_fixtures)
    euro_2024_fixtures_df.loc[euro_2024_fixtures_df['played'] == False, 'predicted_away_goals'] = clf_away_goals.predict(X_upcoming_fixtures)
    euro_2024_fixtures_df.loc[euro_2024_fixtures_df['played'] == False, 'predicted_home_xg'] = clf_home_xg.predict(X_upcoming_fixtures)
    euro_2024_fixtures_df.loc[euro_2024_fixtures_df['played'] == False, 'predicted_away_xg'] = clf_away_xg.predict(X_upcoming_fixtures)

    # Fill NaN values with zeros before rounding and converting to integers
    euro_2024_fixtures_df['predicted_home_goals'].fillna(0, inplace=True)
    euro_2024_fixtures_df['predicted_away_goals'].fillna(0, inplace=True)
    
    # Round the predicted goals to the nearest integer
    euro_2024_fixtures_df['predicted_home_goals'] = euro_2024_fixtures_df['predicted_home_goals'].round().astype(int)
    euro_2024_fixtures_df['predicted_away_goals'] = euro_2024_fixtures_df['predicted_away_goals'].round().astype(int)

    # Update the predictions with actual results for played games
    played_games_mask = euro_2024_fixtures_df['played'] == True
    euro_2024_fixtures_df.loc[played_games_mask, 'predicted_home_goals'] = euro_2024_fixtures_df.loc[played_games_mask, 'home_goals']
    euro_2024_fixtures_df.loc[played_games_mask, 'predicted_away_goals'] = euro_2024_fixtures_df.loc[played_games_mask, 'away_goals']
    euro_2024_fixtures_df.loc[played_games_mask, 'predicted_home_xg'] = euro_2024_fixtures_df.loc[played_games_mask, 'home_xg']
    euro_2024_fixtures_df.loc[played_games_mask, 'predicted_away_xg'] = euro_2024_fixtures_df.loc[played_games_mask, 'away_xg']

    # Determine the winning team or if it's a draw based on actual or predicted goals
    def determine_winner(row):
        if row['played']:
            if row['home_goals'] > row['away_goals']:
                return row['home_team']
            elif row['away_goals'] > row['home_goals']:
                return row['away_team']
            else:
                return 'Draw'
        else:
            if row['predicted_home_goals'] > row['predicted_away_goals']:
                return row['home_team']
            elif row['predicted_away_goals'] > row['predicted_home_goals']:
                return row['away_team']
            else:
                return 'Draw'

    euro_2024_fixtures_df['winner'] = euro_2024_fixtures_df.apply(determine_winner, axis=1)

    # Save the predictions to a new CSV file
    euro_2024_fixtures_df.to_csv('euro_2024_score_predictions_with_winner.csv', index=False)

    # Print the predictions including the winner
    print(euro_2024_fixtures_df[['home_team', 'away_team', 'home_goals', 'away_goals', 'predicted_home_goals', 'predicted_away_goals', 'predicted_home_xg', 'predicted_away_xg', 'winner']])

    # Count the number of wins for each team
    wins = euro_2024_fixtures_df['winner'].value_counts()

    # Exclude draws from the count
    wins = wins.drop('Draw', errors='ignore')

    # Find the maximum number of wins
    max_wins = wins.max()

    # Find all teams with the maximum number of wins
    teams_with_most_wins = wins[wins == max_wins].index.tolist()

    # Define the teams and their respective groups
    group_mapping = {
        'germany': 'Group A', 'hungary': 'Group A', 'scotland': 'Group A', 'switzerland': 'Group A',
        'croatia': 'Group B', 'italy': 'Group B', 'spain': 'Group B', 'albania': 'Group B',
        'denmark': 'Group C', 'england': 'Group C', 'serbia': 'Group C', 'slovenia': 'Group C',
        'austria': 'Group D', 'france': 'Group D', 'netherlands': 'Group D', 'poland': 'Group D',
        'belgium': 'Group E', 'romania': 'Group E', 'slovakia': 'Group E', 'ukraine': 'Group E',
        'czechia': 'Group F', 'portugal': 'Group F', 'türkiye': 'Group F', 'georgia': 'Group F'
    }

    # Define the function to calculate group statistics
    def calculate_group_statistics(predicted_df):
        # Initialize the group statistics dictionary
        group_stats = {
            'Group A': pd.DataFrame(),
            'Group B': pd.DataFrame(),
            'Group C': pd.DataFrame(),
            'Group D': pd.DataFrame(),
            'Group E': pd.DataFrame(),
            'Group F': pd.DataFrame(),
        }

        # Initialize a dictionary to hold team stats
        team_stats = {}

        # Initialize all teams with zero stats
        for team in group_mapping.keys():
            team_stats[team] = {
                'MP': 0, 'W': 0, 'D': 0, 'L': 0,
                'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0,
                'xG': 0, 'xGA': 0
            }

        # Update stats based on the prediction results
        for _, row in predicted_df.iterrows():
            home_team = row['home_team'].lower()
            away_team = row['away_team'].lower()
            if row['played']:
                home_goals = row['home_goals']
                away_goals = row['away_goals']
                home_xg = row['predicted_home_xg']
                away_xg = row['predicted_away_xg']
            else:
                home_goals = row['predicted_home_goals']
                away_goals = row['predicted_away_goals']
                home_xg = row['predicted_home_xg']
                away_xg = row['predicted_away_xg']
                
            winner = row['winner'].lower()

            # Update matches played
            team_stats[home_team]['MP'] += 1
            team_stats[away_team]['MP'] += 1

            # Update goals for and against
            team_stats[home_team]['GF'] += home_goals
            team_stats[home_team]['GA'] += away_goals
            team_stats[away_team]['GF'] += away_goals
            team_stats[away_team]['GA'] += home_goals

            # Update expected goals for and against
            team_stats[home_team]['xG'] += home_xg
            team_stats[home_team]['xGA'] += away_xg
            team_stats[away_team]['xG'] += away_xg
            team_stats[away_team]['xGA'] += home_xg

            # Update goal difference
            team_stats[home_team]['GD'] = team_stats[home_team]['GF'] - team_stats[home_team]['GA']
            team_stats[away_team]['GD'] = team_stats[away_team]['GF'] - team_stats[away_team]['GA']

            # Update points and win/draw/loss counts
            if home_goals > away_goals:
                team_stats[home_team]['W'] += 1
                team_stats[away_team]['L'] += 1
                team_stats[home_team]['Pts'] += 3
            elif home_goals < away_goals:
                team_stats[away_team]['W'] += 1
                team_stats[home_team]['L'] += 1
                team_stats[away_team]['Pts'] += 3
            else:
                team_stats[home_team]['D'] += 1
                team_stats[away_team]['D'] += 1
                team_stats[home_team]['Pts'] += 1
                team_stats[away_team]['Pts'] += 1

        # Create group tables
        for team, stats in team_stats.items():
            group = group_mapping[team]
            team_df = pd.DataFrame([{'Squad': team.capitalize(), **stats}])
            group_stats[group] = pd.concat([group_stats[group], team_df], ignore_index=True)

        # Sort each group by Points, Goal Difference, and Goals For
        for group in group_stats:
            group_stats[group] = group_stats[group].sort_values(
                by=['Pts', 'GD', 'GF'], ascending=[False, False, False]
            ).reset_index(drop=True)

        return group_stats

    ## Print Group Stats
    group_stats = calculate_group_statistics(euro_2024_fixtures_df)
    for group, df in group_stats.items():
            print(f"\n{group}")
            print(tabulate(df, headers='keys', tablefmt='grid'))

predict_outcomes()
