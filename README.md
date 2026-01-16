# Trading Strategy Backtester

## Overview
A Python-based trading strategy backtester that implements a **moving average crossover strategy** using historical stock data from Yahoo Finance.

The project generates buy/sell signals, evaluates strategy performance, and visualizes results against market returns.

## Strategy Used
- Short-term Moving Average: 20 days  
- Long-term Moving Average: 50 days  
- Buy Signal: Short MA crosses above Long MA  
- Sell Signal: Short MA crosses below Long MA  

## Features
- Fetches historical stock data using `yfinance`
- Generates trading signals automatically
- Computes market and strategy returns
- Visualizes price, indicators, and trade signals

## Tech Stack
- Python
- pandas
- matplotlib
- yfinance

## How to Run
```bash
pip install yfinance pandas matplotlib
python backtester.py

