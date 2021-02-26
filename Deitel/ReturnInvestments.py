def calculate_investment_return(p: float, r: float, n: float):
    """"
    p - pricipal
    r -rate[0->1]
    n- num of years
    returns the investment return according to the expression
    """
    return p * (1 + r) ** n


def main():
    p_given = 1000
    r_given = 7 / 100
    years_given = [10, 20, 30]

    for years in years_given:
        inv_returns = calculate_investment_return(p_given, r_given, years)
        print(f"year = {years}, return = {inv_returns:.2f}")


if __name__ == "__main__":
    main()
