import scrapy
from scrapy.crawler import CrawlerProcess
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup



# Function to fetch FIFA rankings using Scrapy and process the data
def fetch_and_process_fifa_rankings():
    with open('fifa_rankings.json', 'r') as f:
        fifa_rankings = json.load(f)
    return fifa_rankings # returns a dictionary of fifa rankings

def parse_match_data(row, competition_name, fifa_rankings, columns):
    cols = row.find_all(['th', 'td'])
    if len(cols) > 1 and cols[columns['home_team']].text.strip() != "":
        round_number = cols[columns['round']].text.strip()
        gameweek = cols[columns['gameweek']].text.strip()
        day_of_week = cols[columns['day_of_week']].text.strip()
        date = cols[columns['date']].text.strip()
        start_time = cols[columns['start_time']].text.strip()
        home_team = " ".join(cols[columns['home_team']].text.strip().split()[:-1]).lower()
        score = cols[columns['score']].text.strip() if 'score' in columns else ''
        away_team = " ".join(cols[columns['away_team']].text.strip().split()[1:]).lower()
        attendance = cols[columns['attendance']].text.strip() if 'attendance' in columns else ''
        venue = cols[columns['venue']].text.strip() if 'venue' in columns else ''
        referee = cols[columns['referee']].text.strip() if 'referee' in columns else ''
        match_report = cols[columns['match_report']].text.strip() if 'match_report' in columns else ''
        notes = cols[columns['notes']].text.strip() if 'notes' in columns else ''

        home_xg = cols[columns['home_xg']].text.strip() if 'home_xg' in columns else ''
        away_xg = cols[columns['away_xg']].text.strip() if 'away_xg' in columns else ''

        if "herz'na" in home_team or "rep." in home_team or "n." in home_team:
            home_team = home_team.replace("& herz'na", "and herzegovina").replace("n.", "north").replace("rep.", "republic")
        if "herz'na" in away_team or "rep." in away_team or "n." in away_team:
            away_team = away_team.replace("& herz'na", "and herzegovina").replace("n.", "north").replace("rep.", "republic")

        # Parse the score
        if score and len(score) == 3:
            home_goals, away_goals = int(score[0]), int(score[2])
        else:
            home_goals, away_goals = None, None

        match = {
            'competition': competition_name,
            'round': round_number,
            'gameweek': gameweek,
            'day_of_week': day_of_week,
            'date': date,
            'start_time': start_time,
            'home_team': home_team,
            'home_goals': home_goals,
            'away_team': away_team,
            'away_goals': away_goals,
            'attendance': attendance,
            'venue': venue,
            'referee': referee,
            'match_report': match_report,
            'notes': notes,
            'home_xg': home_xg,
            'away_xg': away_xg,
            'home_rank': int(fifa_rankings[home_team]) if home_team in fifa_rankings else None,
            'away_rank': int(fifa_rankings[away_team]) if away_team in fifa_rankings else None
        }
        return match
    return None

def scrape_and_prepare_data(url, competition_name, fifa_rankings, columns):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    matches = []

    for row in soup.select('table#sched_all tbody tr, table#sched_2024_676_1 tbody tr'):
        match = parse_match_data(row, competition_name, fifa_rankings, columns)
        if match:
            matches.append(match)

    matches_df = pd.DataFrame(matches)
    return matches_df

# Define columns for each competition
euro_2024_columns = {
    'round': 0,
    'gameweek': 1,
    'day_of_week': 2,
    'date': 3,
    'start_time': 4,
    'home_team': 5,
    'home_xg': 6,
    'score': 7,
    'away_xg': 8,
    'away_team': 9,
    'attendance': 10,
    'venue': 11,
    'referee': 12,
    'match_report': 13,
    'notes': 14
}

# main method
def configure_data():
    # Fetch and process FIFA rankings
    fifa_rankings = fetch_and_process_fifa_rankings() # Dictionary of fifa rankings

    # URLs for Euro Qualifying 2024, World Cup 2022, and Euro 2021
    euro_qualifying_url = 'https://fbref.com/en/comps/678/schedule/UEFA-Euro-Qualifying-Scores-and-Fixtures'
    world_cup_2022_url = 'https://fbref.com/en/comps/1/schedule/World-Cup-Scores-and-Fixtures'
    euro_2021_url = 'https://fbref.com/en/comps/676/2021/schedule/2021-European-Championship-Scores-and-Fixtures'
    euro_2024_url = 'https://fbref.com/en/comps/676/schedule/European-Championship-Scores-and-Fixtures'

    # Columns for Euro Qualifying 2024 and World Cup 2022 (if different)
    euro_qualifying_columns = {
        'round': 0,
        'gameweek': 1,
        'day_of_week': 2,
        'date': 3,
        'start_time': 4,
        'home_team': 5,
        'score': 6,
        'away_team': 7,
        'attendance': 8,
        'venue': 9,
        'referee': 10,
        'match_report': 11,
        'notes': 12
    }

    world_cup_2022_columns = {
        'round': 0,
        'gameweek': 1,
        'day_of_week': 2,
        'date': 3,
        'start_time': 4,
        'home_team': 5,
        'home_xg': 6,
        'score': 7,
        'away_xg': 8,
        'away_team': 9,
        'attendance': 10,
        'venue': 11,
        'referee': 12,
        'match_report': 13,
        'notes': 14
    }

    # Scrape and prepare data for Euro Qualifying 2024, World Cup 2022, and Euro 2021
    euro_qualifying_df = scrape_and_prepare_data(euro_qualifying_url, 'Euro Qualifying 2024', fifa_rankings, euro_qualifying_columns)
    world_cup_2022_df = scrape_and_prepare_data(world_cup_2022_url, 'World Cup 2022', fifa_rankings, world_cup_2022_columns)
    euro_2021_df = scrape_and_prepare_data(euro_2021_url, 'Euro 2021', fifa_rankings, world_cup_2022_columns)  # Assuming columns are same as world_cup_2022_columns

    # Fetch the fixtures for Euro 2024
    euro_2024_fixtures_df = scrape_and_prepare_data(euro_2024_url, 'Euro 2024', fifa_rankings, euro_2024_columns)
    
    # Add a column to indicate whether a game has been played
    euro_2024_fixtures_df['played'] = euro_2024_fixtures_df['home_goals'].notna() & euro_2024_fixtures_df['away_goals'].notna()
    
    euro_2024_fixtures_df.to_csv('euro_2024_matches.csv', index=False)

    # Create a DataFrame for only the played games
    euro_2024_played_df = euro_2024_fixtures_df[euro_2024_fixtures_df['played']]
    
    # Combine all the data into one DataFrame
    all_matches_df = pd.concat([euro_qualifying_df, world_cup_2022_df, euro_2021_df, euro_2024_played_df], ignore_index=True)

    # Feature Engineering
    all_matches_df['goal_difference'] = all_matches_df['home_goals'] - all_matches_df['away_goals']
    
    def determine_match_result(row):
        if row['home_goals'] > row['away_goals']:
            return 'win'
        elif row['home_goals'] < row['away_goals']:
            return 'loss'
        else:
            if row['notes']:
                extra_time_winner = row['notes'].split()[0]
                if extra_time_winner.lower() in row['home_team'].lower():
                    return 'win'
                elif extra_time_winner.lower() in row['away_team'].lower():
                    return 'loss'
            return 'draw'

    all_matches_df['match_result'] = all_matches_df.apply(determine_match_result, axis=1)
    
    # Add a column to indicate whether a game has been played
    all_matches_df['played'] = all_matches_df['home_goals'].notna() & all_matches_df['away_goals'].notna()

    # Save combined data
    all_matches_df.to_csv('all_matches_combined.csv', index=False)

if __name__ == "__main__":
    configure_data()
