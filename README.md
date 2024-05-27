# Euro 2024 Predictor

Welcome to the Euro 2024 Predictor! This project uses machine learning to predict the outcomes of the Euro 2024 football matches. The model is trained on historical match data, including goals scored, expected goals (xG), and FIFA rankings, to forecast the results of upcoming games.

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

4. **Run All Steps:**
   Alternatively, you can run all the steps sequentially using the `run_pipeline.py` script.

   ```bash
   python run_pipeline.py
   ```

## Results

The predicted outcomes, along with group standings, are saved in CSV files. You can view the predictions and standings using any CSV viewer or load them into a DataFrame for further analysis.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact Mike Veson at [mike@douzinas.com](mailto:mike@douzinas.com).