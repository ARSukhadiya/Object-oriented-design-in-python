def calculate_interest(amount, interest):
    """
    Calculate interest with passed parameters
    """
    return (amount * interest / 100)

def main():
    print("A bank's certificate of deposit (CD) program\n")

    while True:
        # Get user inputs
        investment_amount = int(input("Enter initial investment amount: "))
        annual_per_yield = float(input("Enter annual percentage yield (APY): "))
        no_of_months = int(input("Enter number of months for the CD term: "))
        compunding_freq = input("Enter compounding frequency (monthly, quarterly, annually): ").lower()

        # compounding frequencies months
        if compunding_freq == 'monthly':
            compunding_freq_months = 1
        elif compunding_freq == 'quarterly':
            compunding_freq_months = 3
        elif compunding_freq == 'annually':
            compunding_freq_months = 12
        else:
            print("Error! Invalid compounding frequency")

        print("\nMonth        CD Value")
        print("-----        --------")

        # Calculate CD value and total interest
        cd_value = investment_amount
        total_interest = 0

        for term in range(1, no_of_months+1):

            interest = calculate_interest(cd_value, annual_per_yield/12)
            total_interest += interest

            if term % compunding_freq_months == 0:
                cd_value = investment_amount + total_interest
            
            print(f"{term:3d}           ${cd_value :,.2f}")

        print(f"\nTotal interest earned: ${total_interest :,.2f}\n\n")

        confirm = input("Do you want to continue (y/n)? ")
        if confirm.lower() != 'y':
            break


if __name__ == "__main__":
    main()
