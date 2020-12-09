def pay(wage, hours):
    if hours <= 40:
        payout = wage * hours
    else: 
        payout = (wage * 40) + ((1.5 * wage)-(hours - 40))
    return payout


def pay2(wage2, hours2):
    if hours2 <= 40:
        payout2 = wage2 * hours2
    else: 
        payout2 = (wage2 *40) + ((1.5 * wage2)-(hours2 - 40))
    return payout2

Totalpay = []
dict = {'Job1': 'Pay for job one is: '}
hourlyWage = eval(input("Enter hourly wage from job 1: "))
hoursWorked = eval(input("Enter hours worked from job 1: "))
Payoutjob1 = pay(hoursWorked, hourlyWage)
Totalpay.append(Payoutjob1)
print (dict['Job1'], (Payoutjob1))


dict = {'Job2': 'Pay for job two is: ', 'TotalPayout': 'Total pay for both jobs is: '}
hourlyWage2 = eval(input("Enter hourly wage from Job 2: "))
hoursWorked2 = eval(input("Enter hours worked from job 2: "))
Payoutjob2 = pay2(hourlyWage2, hoursWorked2)
Totalpay.append(Payoutjob2)
print (dict['Job2'], (Payoutjob2))
print (dict['TotalPayout'], Totalpay[0] + Totalpay[1])
