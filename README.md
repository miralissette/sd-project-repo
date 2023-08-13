# sd-project-repo
# Dog Intelligence Prediction App

This is a Streamlit web application that predicts the intelligence score of a dog based on its breed.

## Overview

This project aims to provide users with a simple tool to predict the intelligence score of a dog based on its breed. The prediction is made using a dataset that includes information about various dog breeds and their corresponding intelligence score ranges.

## Features

- User-friendly interface to predict dog intelligence based on breed.
- Dropdown list of available dog breeds for ease of selection.
- Insights on dog intelligence distribution based on size categories.
- Scatterplot visualizations of height vs. weight with color-coded repetitions.

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory using your terminal.
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For macOS / Linux

1. Install the required packages:
    pip install streamlit
    pip install pandas
    pip install plotly.express

2. Run the app:
    streamlit run app.py

## Usage

1. Once the app is running, you'll be presented with a user interface.
2. Select the breed of the dog from the dropdown list.
3. Click the "Predict Intelligence" button to receive a prediction of the dog's intelligence.

## Data Source

The dataset used in this project was found on Kaggle's public domain. It contains information about various dog breeds and their intelligence score ranges. 

Note: This project was created as part of a data science project and for educational purposes.