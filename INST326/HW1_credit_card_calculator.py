"""Perform credit card calculations."""
from argparse import ArgumentParser
import sys

def get_min_payment(balance, fees = 0):
    """Computes the minimum credit card payment and determines if it's below 25
    Args:
        balance (float): total amount of the balance in an account left to pay
        fees (float): fees associated with the credit card account
        b: balance in account (for min_payment calculation)
        m: percent of balance that needs to be paid (for min_payment calculation)
        f: amount of fees paid per month (for min_payment calculation)
        min_payment(float): minimum payment 
    Returns:
        min_payment (float)
    """

    b = balance
    m = 0.02
    f = fees

    min_payment = ((b*m)+f)

    #if minimum payment is below 25, set to 25
    if (min_payment < 25):
        min_payment = 25

    return min_payment

def interest_charged(balance, apr): 
    """Computes the amount of interest accrued in the next payment 
    Args:
        balance (float): balance of the credit card left to pay
        apr (int): annual APR, percent
        a: APR, float point (for interest accured formula)
        y: amount of days in a year
        b: balance in the account (for interest accured formula)
        d: num of days in a billing cycle 
        i: amount of interest accured 
    Returns:
        i (float)
    """

    #expressed as floating point(decimal)
    a = apr/100
    y = 365
    b = balance 
    d = 30

    i = (a/y)*b*d

    return i

def remaining_payments(balance, apr, targetamount, credit_line = 5000, fees = 0):
    """Computes the number of payments required to pay off credit card balance
    Args:
        balance (float): balance of the credit card left to pay
        apr (int): annual APR, percent
        targetamount (int): target payment
        credit_line (int): maximum amount of balance that account holder can keep in account
        fees (float): amount of fees and minimum payment
        count_months_75 (int): num of months balance is over 75%
        count_months_50 (int): num of months balance is over 50%
        count_months_25 (int): num of months balance is over 25%
        payment_for_balance(int): amount to be paid 
    Returns:
        countTuple(tuple): tuple of counts
    """
    count_months_75 = 0
    count_months_50 = 0
    count_months_25 = 0
    payments_performed = 0
   
    while(balance > 0):
        if(targetamount == None):
            payment_amount = get_min_payment(balance, fees)
        else: 
            payment_amount = targetamount

        payment_for_balance = payment_amount - interest_charged(balance, apr)

        if(payment_for_balance < 0):
            print("Card balance cannot be paid off")
            quit()

        balance -= payment_for_balance

        payments_performed += 1

        #months > 25% keeps counting even if > 50 or 75, not exclusive to 25 < x < 50
        if (balance > credit_line*0.75):
            count_months_75 += 1
        if (balance > credit_line*0.5):
            count_months_50 += 1   
        if (balance > credit_line*0.25):
            count_months_25 += 1
    
        

    #tuple stores counts
    countTuple = (payments_performed, count_months_75, count_months_50, count_months_25)
    return countTuple

def main(balance, apr, targetamount = None, credit_line = 5000, fees = 0):
    """Computes the number of months spent over 25%, 50%, and 75% over the credit limit
    Args:
        balance (float): balance of the credit card left to pay
        apr (int): annual APR, percent 
        targetamount (int): target payment
        credit_line (int): maximum amount that can be kept in account
        fees (float): amount of fees and minimum payment
        pays_minimum (boolean): whether user chose to pay minimum payment each month or not
        total_numP_required (int): total number of payments required

    Returns:
        months spent over 25%, 50%, and 70% credit line
    """

    #compute and display rec min payment
    rec_min = get_min_payment(balance, fees)
    print (f"Your recommended minimum payment is ${rec_min}.")

    pays_minimum = False 

    if (targetamount == None):
        pays_minimum = True
    elif (targetamount < rec_min):
        print("Your target payment is less than the minimum payment for this credit card")
        quit()

    #tuple variable, used to access counters from remaining payments tuple
    total_numP_required = remaining_payments(balance, apr, targetamount, credit_line, fees)
    
    if(pays_minimum == True):
        #total_numP_required[0] gets to total payments performed
        print(f"If you pay the minimum payment each month, you will pay off the balance in {total_numP_required[0]} payments.")
    else: 
        print(f"If you make payments of ${targetamount}, you will pay off the balance in {total_numP_required[0]} payments.")

    return f"You will spend a total of {total_numP_required[3]} months over 25% of credit line. \nYou will spend a total of {total_numP_required[2]} months over 50% of credit line. \nYou will spend a total of {total_numP_required[1]} months over 75% of credit line."

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    parser = ArgumentParser()
    parser.add_argument('balance_amount', type = float, help = 'The total amount of balance left on the credit account')
    parser.add_argument('apr', type = int, help = 'The annual APR, should be an int between 1 and 100')
    parser.add_argument('credit_line', type = int, help = 'The maximum amount of balance allowed on the credit line.')
    parser.add_argument('--payment', type = int, default = None, help = 'The amount the user wants to pay per payment, should be a positive number')
    parser.add_argument('--fees', type = float, default = 0, help = 'The fees that are applied monthly.')
    # parse and validate arguments
    args = parser.parse_args(args_list)
    if args.balance_amount < 0:
        raise ValueError("balance amount must be positive")
    if not 0 <= args.apr <= 100:
        raise ValueError("APR must be between 0 and 100")
    if args.credit_line < 1:
        raise ValueError("credit line must be positive")
    if args.payment is not None and args.payment < 0:
        raise ValueError("number of payments per year must be positive")
    if args.fees < 0:
        raise ValueError("fees must be positive")
    return args

if __name__ == "__main__":
    try:
        arguments = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))

    print(main(arguments.balance_amount, arguments.apr, credit_line = arguments.credit_line, targetamount = arguments.payment, fees = arguments.fees))
