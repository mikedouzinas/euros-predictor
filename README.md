# Euro 2024 Predictor

Welcome to the Euro 2024 Predictor! This project uses machine learning to predict the outcomes of the Euro 2024 football matches. The model is trained on historical match data, including goals scored, expected goals (xG), and FIFA rankings, to forecast the results of upcoming games.

## Current Predictions

### Group A
|    | Squad       | MP | W | D | L | GF | GA | GD | Pts | xG    | xGA   |
|----|-------------|----|---|---|---|----|----|----|-----|-------|-------|
|  0 | Germany     |  3 | 2 | 1 | 0 |  8 |  3 |  5 |   7 | 4.529 | 1.890 |
|  1 | Switzerland |  3 | 2 | 1 | 0 |  6 |  3 |  3 |   7 | 4.863 | 3.536 |
|  2 | Hungary     |  3 | 0 | 1 | 2 |  3 |  6 | -3 |   1 | 3.673 | 4.513 |
|  3 | Scotland    |  3 | 0 | 1 | 2 |  3 |  8 | -5 |   1 | 2.020 | 5.145 |

### Group B
|    | Squad   | MP | W | D | L | GF | GA | GD | Pts | xG    | xGA   |
|----|---------|----|---|---|---|----|----|----|-----|-------|-------|
|  0 | Spain   |  3 | 3 | 0 | 0 |  7 |  1 |  6 |   9 | 6.017 | 4.622 |
|  1 | Italy   |  3 | 1 | 1 | 1 |  5 |  5 |  0 |   4 | 5.428 | 4.151 |
|  2 | Croatia |  3 | 1 | 1 | 1 |  4 |  6 | -2 |   4 | 5.363 | 4.687 |
|  3 | Albania |  3 | 0 | 0 | 3 |  2 |  6 | -4 |   0 | 1.781 | 5.129 |

### Group C
|    | Squad    | MP | W | D | L | GF | GA | GD | Pts | xG    | xGA   |
|----|----------|----|---|---|---|----|----|----|-----|-------|-------|
|  0 | England  |  3 | 2 | 1 | 0 |  4 |  1 |  3 |   7 | 2.947 | 1.438 |
|  1 | Serbia   |  3 | 1 | 1 | 1 |  3 |  3 |  0 |   4 | 2.403 | 3.089 |
|  2 | Denmark  |  3 | 0 | 3 | 0 |  3 |  3 |  0 |   3 | 4.063 | 2.816 |
|  3 | Slovenia |  3 | 0 | 1 | 2 |  2 |  5 | -3 |   1 | 2.563 | 4.634 |

### Group D
|    | Squad       | MP | W | D | L | GF | GA | GD | Pts | xG    | xGA   |
|----|-------------|----|---|---|---|----|----|----|-----|-------|-------|
|  0 | France      |  3 | 3 | 0 | 0 |  6 |  2 |  4 |   9 | 4.963 | 2.888 |
|  1 | Netherlands |  3 | 2 | 0 | 1 |  5 |  3 |  2 |   6 | 4.882 | 3.472 |
|  2 | Austria     |  3 | 1 | 0 | 2 |  2 |  4 | -2 |   3 | 2.651 | 5.169 |
|  3 | Poland      |  3 | 0 | 0 | 3 |  3 |  7 | -4 |   0 | 3.175 | 4.143 |

### Group E
|    | Squad    | MP | W | D | L | GF | GA | GD | Pts | xG    | xGA   |
|----|----------|----|---|---|---|----|----|----|-----|-------|-------|
|  0 | Romania  |  3 | 2 | 0 | 1 |  5 |  3 |  2 |   6 | 2.746 | 3.114 |
|  1 | Belgium  |  3 | 1 | 1 | 1 |  3 |  2 |  1 |   4 | 3.657 | 2.104 |
|  2 | Slovakia |  3 | 1 | 1 | 1 |  4 |  4 |  0 |   4 | 2.926 | 3.528 |
|  3 | Ukraine  |  3 | 0 | 2 | 1 |  3 |  6 | -3 |   2 | 2.486 | 3.068 |

### Group F
|    | Squad    | MP | W | D | L | GF | GA | GD | Pts | xG    | xGA   |
|----|----------|----|---|---|---|----|----|----|-----|-------|-------|
|  0 | Portugal |  3 | 3 | 0 | 0 |  7 |  1 |  6 |   9 | 5.080 | 0.797 |
|  1 | Türkiye  |  3 | 1 | 1 | 1 |  4 |  3 |  1 |   4 | 3.691 | 3.854 |
|  2 | Czechia  |  3 | 0 | 2 | 1 |  3 |  4 | -1 |   2 | 1.860 | 2.872 |
|  3 | Georgia  |  3 | 0 | 1 | 2 |  2 |  8 | -6 |   1 | 2.178 | 5.286 |


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

The Euro 2024 Predictor project aims to provide insights and predictions for the Euro 2024 football tournament. By leveraging historical data and advanced machine learning techniques, the project forecasts match outcomes, including goals scored by each team.

## Features

- **Data Collection**: Scrapes historical match data and FIFA rankings.
- **Data Processing**: Cleans and prepares the data for training.
- **Model Training**: Utilizes a RandomForestClassifier to train the prediction model.
- **Prediction**: Generates predictions for upcoming Euro 2024 matches.
- **Group Statistics**: Calculates group standings based on predicted match outcomes.

## Data Sources

- [FBref](https://fbref.com/) for match fixtures and results.
- [FIFA](https://www.fifa.com/) for national team rankings.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mikedouzinas/euros-predictor.git
   cd euros-predictor
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure Data:**
   Run the `configure_data.py` script to fetch and prepare the data.

   ```bash
   python configure_data.py
   ```

2. **Train the Model:**
   Run the `train_model.py` script to train the machine learning model.

   ```bash
   python train_model.py
   ```

3. **Predict Outcomes:**
   Run the `predict_outcomes.py` script to generate predictions for upcoming matches.

   ```bash
   python predict_outcomes.py
   ```

## Results

The predicted outcomes, along with group standings, are saved in CSV files. You can view the predictions and standings using any CSV viewer or load them into a DataFrame for further analysis.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact Mike Veson at [mike@douzinas.com](mailto:mike@douzinas.com).

