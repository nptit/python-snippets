def outstanding_balance(rate=0.18, start_balance=5000, monthly_payment_percent=0.02, nmonth=12):
    '''calculate outstanding balance after nmonth, given rate, start_balance, and monthly_payment'''
    results = []
    for m in range(nmonth+1):
        payment = start_balance * monthly_payment_percent
        unpaid_balance = start_balance - payment
        interest = unpaid_balance * rate /12.0
        start_balance = unpaid_balance + interest
        results.append([payment, interest, start_balance])
    return results



def yearbalance(monthlyPaymentRate=0.02, balance=5000, annualInterestRate=0.18):
    total_paid = 0
    for m in range(13):
        payment = balance * monthlyPaymentRate
        unpaid_balance = balance - payment
        interest = unpaid_balance * annualInterestRate /12.0
        new_balance = unpaid_balance + interest
        print "Month: {}".format(m)
        print "Minimum monthly payment: {}".format(round(payment, 2))
        print "Remaining balance: {}".format(round(balance, 2))
        balance = new_balance
        total_paid += payment

    print "Total paid: {}".format(round(total_paid, 2))
    print "Remaining balance: {}".format(round(balance, 2))

#print yearbalance()

balance = 4213; annualInterestRate = 0.2; monthlyPaymentRate = 0.04

def yearbalance(monthlyPaymentRate=0.02, balance=5000, annualInterestRate=0.18):
    total_paid = 0
    for m in range(12):
        payment = balance * monthlyPaymentRate
        unpaid_balance = balance - payment
        interest = unpaid_balance * annualInterestRate /12.0
        new_balance = unpaid_balance + interest
        print "Month: {}".format(m+1)
        print "Minimum monthly payment: {}".format(round(payment, 2))
        print "Remaining balance: {}".format(round(new_balance, 2))
        balance = new_balance
        total_paid += payment

    print "Total paid: {}".format(round(total_paid, 2))
    print "Remaining balance: {}".format(round(balance, 2))


def payoffbalance(lowest_payment=0, balance=5000, annualInterestRate=0.18):
    total_paid = 0
    for m in range(12):
        payment = balance * monthlyPaymentRate
        unpaid_balance = balance - lowest_payment
        interest = unpaid_balance * annualInterestRate /12.0
        new_balance = unpaid_balance + interest
        print "Month: {}".format(m+1)
        print "Minimum monthly payment: {}".format(round(payment, 2))
        print "Remaining balance: {}".format(round(new_balance, 2))
        balance = new_balance
        total_paid += payment

    print "Total paid: {}".format(round(total_paid, 2))
    print "Remaining balance: {}".format(round(balance, 2))


def payoffbalance(fixed_payment=100, balance=1000, annualInterestRate=0.2):
    total_paid = 0
    for m in range(12):
        unpaid_balance = balance - fixed_payment
        interest = unpaid_balance * annualInterestRate /12.0
        new_balance = unpaid_balance + interest
        balance = new_balance
        total_paid += fixed_payment

    return balance

def bruteforce_search(balance=balance, annualInterestRate=annualInterestRate):
    payment = 0
    while True:
        remaining_balance = payoffbalance(fixed_payment=payment, balance=balance, annualInterestRate=annualInterestRate)
        #print payment, remaining_balance
        if remaining_balance <= 0:
            print 'Lowest payment: {}'.format(payment)
            break
        payment += 10


def binary_search(balance=balance, annualInterestRate=annualInterestRate):
    payment = 0
    eps = 0.01
    lo = balance / 12.0
    hi = balance * (1 + annualInterestRate / 12.0)**12 / 12.0
    while True:
        #print lo, hi
        payment = (lo + hi) / 2.
        remaining_balance = payoffbalance(fixed_payment=payment, balance=balance, annualInterestRate=annualInterestRate)

        if remaining_balance > eps:
            lo = payment
        elif remaining_balance < -eps:
            hi = payment
        else:
            print 'Lowest payment: {}'.format(round(payment,2))
            break

balance=320000; annualInterestRate=0.2
binary_search(balance=balance, annualInterestRate=annualInterestRate)
#binary_search(balance=320000, annualInterestRate=0.2)

binary_search(balance=999999, annualInterestRate=0.18)




