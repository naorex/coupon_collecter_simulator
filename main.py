import math
import random


def simulate_coupon_collection(num_coupons):
    """
    Simulates the coupon collector problem.

    Args:
        num_coupons: The number of unique coupons.

    Returns:
        The number of purchases needed to collect all coupons.
    """
    collected_coupons = set()
    num_purchases = 0
    while len(collected_coupons) < num_coupons:
        coupon = random.randint(1, num_coupons)
        collected_coupons.add(coupon)
        num_purchases += 1
    return num_purchases


def calculate_expected_purchases(num_coupons):
    """
    Calculates the expected number of purchases using the formula.

    Args:
        num_coupons: The number of unique coupons.

    Returns:
        The expected number of purchases.
    """
    expected_purchases = num_coupons * sum(1 / i for i in range(1, num_coupons + 1))
    return expected_purchases


import os

if __name__ == "__main__":
    num_coupons = int(os.environ.get("NUM_COUPONS", 5))
    num_simulations = int(os.environ.get("NUM_SIMULATIONS", 1000))

    total_purchases = 0
    for _ in range(num_simulations):
        total_purchases += simulate_coupon_collection(num_coupons)

    average_purchases = total_purchases / num_simulations
    expected_purchases = calculate_expected_purchases(num_coupons)

    print(f"Number of coupons: {num_coupons}")
    print(f"Number of simulations: {num_simulations}")
    print(f"Average purchases (simulation): {average_purchases:.2f}")
    print(f"Expected purchases (formula): {expected_purchases:.2f}")

    if abs(average_purchases - expected_purchases) < 1:
        print("The simulation results are consistent with the formula.")
    else:
        print("The simulation results are NOT consistent with the formula.")
