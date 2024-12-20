
def calculate_capital(K0, interest_rate, years):
    K = K0
    year = 1
    while year <= years:
        K = K + (K * interest_rate / 100)
        print(f"Capital after year {year}: {K}")
        year += 1
    return K
K0 = float(input("Enter the initial balance (K0): "))
interest_rate = float(input("Enter the interest rate (in %): "))
years = int(input("Enter the number of years: "))
K1 = calculate_capital(K0, interest_rate, years)
print(f"\nFinal capital after {years} years: {K1}")
