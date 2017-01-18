"""Problem set 2/

Each month, a credit card statement will come with the option for you to pay a
minimum amount of your charge, usually 2% of the balance due. However, the
credit card company earns money by charging interest on the balance that you
don't pay. So even if you pay credit card payments on time, interest is still
accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest
rate and a 2% minimum monthly payment rate. If you only pay the minimum
monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume
you owe an amount we will call b0 (b for balance; subscript 0 to indicate this
is the balance at month 0).

Any payment you make during that month is deducted from the balance. Let's
call the payment you make in month 0, p0. Thus, your unpaid balance for month
0, ub0, is equal to b0 - p0.

    ub0 = b0 - p0

At the beginning of month 1, the credit card company will charge you
interest on your unpaid balance. So if your annual interest rate is r, then at
the beginning of month 1, your new balance is your previous unpaid balance
ub0, plus the interest on this unpaid balance for the month. In algebra, this
new balance would be

    b1 = ub0 + r/12.0 * ub0

In month 1, we will make another payment, p1. That payment has to cover some
of the interest costs, so it does not completely go towards paying off the
original charge. The balance at the beginning of month 2, b2, can be
calculated by first calculating the unpaid balance after paying p1, then by
adding the interest accrued:

    ub1 = b1 - p1
    b2 = ub1 + r/12.0 * ub1

If you choose just to pay off the minimum monthly payment each month, you will
see that the compound interest will dramatically reduce your ability to lower
your debt.
"""


def calc_balance(balance, annualInterestRate, monthlyPaymentRate):
    """Calculate the credit card balance after one year.

    Write a program to calculate the credit card balance after one year if a
    person only pays the minimum monthly payment required by the credit card
    company each month.

    For each month, calculate statements on the monthly payment and remaining
    balance. At the end of 12 months, print out the remaining balance. Be sure
    to print out no more than two decimal digits of accuracy - so print

        Remaining balance: 813.41

    instead of

        Remaining balance: 813.4141998135

    So your program only prints out one thing: the remaining balance at the
    end of the year in the format:

        Remaining balance: 4784.0

    Args:
        balance (float): the outstanding balance on the credit card
        annual_interest_rate (float): annual interest rate as a decimal
        monthly_payment_rate (float): minimum monthly payment rate as a decimal
    """

    for i in range(12):
        ub = balance - balance * monthlyPaymentRate
        nb = ub + ub * (annualInterestRate / 12.0)
        balance = nb

    return 'Remaining balance: {}'.format('%.2f' % balance)


def test_calc_balance():
    assert calc_balance(42, 0.2, 0.04) == 'Remaining balance: 31.38'
    assert calc_balance(484, 0.2, 0.04) == 'Remaining balance: 361.61'


def calc_fixed_monthly_payment(balanace, annualInterestRate):
    """Calculates the minimum fixed monthly payment.

    Now write a program that calculates the minimum fixed monthly payment
    needed in order pay off a credit card balance within 12 months. By a fixed
    monthly payment, we mean a single number which does not change each month,
    but instead is a constant amount that will be paid each month.

    In this problem, we will not be dealing with a minimum monthly payment
    rate.

    The program should print out one line: the lowest monthly payment that
    will pay off all debt in under 1 year, for example:

        Lowest Payment: 180

    Args:
        balance (float): the outstanding balance on the credit card
        annualInterestRate (float): annual interest rate as a decimal
    """



def test_calc_fixed_monthly_payment():
    assert calc_fixed_monthly_payment(3329, 0.2) == 'Lowest Payment: 310'
    assert calc_fixed_monthly_payment(4773, 0.2) == 'Lowest Payment: 440'
    assert calc_fixed_monthly_payment(3926, 0.2) == 'Lowest Payment: 360'
