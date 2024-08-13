# IB-with-backtrader

This project integrates Interactive Brokers (IB) with Backtrader, a popular Python framework for backtesting trading strategies. The setup allows for seamless interaction between IB's API and Backtrader, enabling users to backtest their strategies using historical market data and then execute trades in live markets.

## Project Structure

The code is organized in the following directory structure:

Project/
│
├── IBJts/
│   ├── source/
│   │   └── backtest.py
│   └── ...
└── ...


### Path to `backtest.py`

To run or modify the backtesting script, navigate through the following path:

- **Project**: The root directory containing all project files.
- **IBJts**: This directory contains the Interactive Brokers' Java Trading System (JTS) files and additional scripts related to IB.
- **source**: This folder houses the main source code files for the project.
- **backtest.py**: This is the main Python script where you can define, backtest, and refine your trading strategies.

### Running the Backtest

To run the backtest, navigate to the `source` directory and execute the `backtest.py` script:

```bash
cd Project/IBJts/source
python backtest.py
