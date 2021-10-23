import math
import argparse


def monthly_payment(loan, period, interest):
    rate = interest / 12 / 100
    rate_and_1 = 1 + rate
    numerator = rate * rate_and_1 ** period
    denominator = (rate_and_1 ** period) - 1
    payment = math.ceil(loan * (numerator / denominator))

    print("Your annuity payment = {0}!".format(payment))

    total = payment * period
    overpayment(loan, total)


def how_many_payments(loan, payment, interest):
    rate = interest / 12 / 100

    x = payment / (payment - rate * loan)
    base = 1 + rate
    months = math.ceil(math.log(x, base))

    total = payment * months

    if months == 1:
        print("It will take 1 month to repay this loan!")
    elif months < 12:
        print("It will take {0:.0f} months to repay this loan!".format(months))
    elif months == 12:
        print("It will take 1 year to repay this loan!")
    else:
        years = 0
        while months >= 12:
            months -= 12
            years += 1
        if years == 1 and months == 1:
            print("It will take 1 year and 1 month to repay this loan!")
        elif years == 1 and months > 1:
            print("It will take 1 year and {0} months to repay this loan!".format(months))
        elif years > 1 and months == 0:
            print("It will take {0} years to repay this loan!".format(years))
        elif years > 1 and months == 1:
            print("It will take {0} years and 1 month to repay this loan!".format(years))
        else:
            print("It will take {0} years and {1} months to repay this loan!".format(years, months))

    overpayment(loan, total)


def loan_principal(payment, periods, interest):
    rate = interest / 12 / 100
    rate_and_1 = 1 + rate
    numerator = rate * rate_and_1 ** periods
    denominator = (rate_and_1 ** periods) - 1
    principal = math.floor(payment / (numerator / denominator))

    print("Your loan principal = {0}!".format(principal))

    total = payment * periods
    overpayment(principal, total)


def differentiated(principal, periods, interest):
    rate = interest / 12 / 100
    month = 1
    total_payment = 0
    factor_1 = principal / periods

    while month <= periods:
        numerator = principal * (month - 1)
        payment = math.ceil(factor_1 + rate * (principal - (numerator / periods)))
        print("Month {0}: payment = {1}".format(month, payment))
        total_payment += payment
        month += 1

    print()
    overpayment(principal, total_payment)


def overpayment(principal, total_payment):
    print("Overpayment = {0}\n".format(round(total_payment - principal)))


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=float, default=0)
parser.add_argument("--principal", type=float, default=0)
parser.add_argument("--periods", type=int, default=0)
parser.add_argument("--interest", type=float, default=0)

args = parser.parse_args()

error_message = "Incorrect parameters"

no_negatives = True
values_list = [args.payment, args.principal, args.periods, args.interest]
if min(values_list) < 0:
    no_negatives = False

if args.type in ("diff", "annuity") and no_negatives:
    if args.type == "diff" and args.principal and args.periods and args.interest:
        differentiated(args.principal, args.periods, args.interest)
    elif args.type == "annuity" and args.principal and args.periods and args.interest:
        monthly_payment(args.principal, args.periods, args.interest)
    elif args.type == "annuity" and args.payment and args.periods and args.interest:
        loan_principal(args.payment, args.periods, args.interest)
    elif args.type == "annuity" and args.payment and args.principal and args.interest:
        how_many_payments(args.principal, args.payment, args.interest)
    else:
        print(error_message)
else:
    print(error_message)
