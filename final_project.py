"""
This project is a program that helps calculate the amount of pay a person working
two jobs would get. We need to first identify the formula for pay for each job. 
We multiple the hours * wage unless there is overtime of > 40 hours worked in which
case it becomes wage * hours + 1.5 * wage - (hours -40). We use this equation for 
both jobs. We then ask the user to input the information of their hours and wage
to evaluate an answer.
"""
"""
def pay1
    if hour < 40
        pay1 = wage * hours
    else
        pay1 = (wage * 40) + ((1.5 * wage)-(hours - 40))
    return 1

def pay2
    if hour < 40
        pay2 = wage2 * hours2
    else
        pay2 = (wage2 * 40) + ((1.5 * wage2)-(hours2 - 40))
    return 2

Totalpay = []
Dictionary = {'job1': 'pay is ..', 'job2': 'pay is ..', 'totalpay': 'total pay is ..'}
hourlywage1 = input
hoursworked1 = input
job1pay = (hourlywage1, hoursworked1) 
append(job1pay)
print job1

hourlywage2 = input
hoursworked2 = input
job2pay = (hourlywage2, hoursworked2)
append(job2pay)
print job2
print Totalpay[0]+Totalpay[1]
"""

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