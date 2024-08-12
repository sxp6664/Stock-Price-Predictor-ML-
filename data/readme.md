# Data Directory

## Overview

This directory contains both raw and processed data files used for the ML Stock Price Predictor project.

## Raw Data

- **`stock_prices.csv`**: Contains raw stock price data sourced from [Yahoo Finance](https://finance.yahoo.com/). The dataset includes the following columns:
  - `Date`: The date of the stock price record.
  - `Open`: The opening price of the stock.
  - `High`: The highest price of the stock during the trading day.
  - `Low`: The lowest price of the stock during the trading day.
  - `Close`: The closing price of the stock.
  - `Volume`: The number of shares traded.

## Processed Data

- **`processed_stock_prices.csv`**: This file contains the cleaned and preprocessed version of the raw stock price data. The preprocessing steps may include:
  - Handling missing values.
  - Normalizing or scaling features.
  - Removing or imputing outliers.

## Data Sources

- Data was downloaded from [Yahoo Finance](https://finance.yahoo.com/). For more details, refer to the dataset's original source.
