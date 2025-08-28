# Coupon Collector Simulator

This project simulates the coupon collector problem, which calculates the expected number of purchases needed to collect all unique coupons.

## Prerequisites

- Python 3.11
- Docker (optional)

## Usage

### Running the simulation with Python

1.  Make sure you have Python 3.11 installed.
2.  Run the following command:

    ```bash
    python main.py
    ```

### Running the simulation with Docker

1.  Make sure you have Docker installed.
2.  Build the Docker image:

    ```bash
    docker build -t coupon_collector .
    ```

3.  Run the Docker container:

    ```bash
    docker run --rm -e NUM_COUPONS=10 -e NUM_SIMULATIONS=5000 coupon_collector
    ```

## Output

The script will output the following information:

- Number of coupons
- Number of simulations
- Average purchases (simulation)
- Expected purchases (formula)
- Whether the simulation results are consistent with the formula

## Files

- `main.py`: The Python script that simulates the coupon collector problem.
- `Dockerfile`: The Dockerfile for building the Docker image.
- `requirements.txt`: The requirements file for installing the Python dependencies.
- `GEMINI.md`: The original task description.
- `README.md`: This file.
