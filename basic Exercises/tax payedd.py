payable = int(input("Income: "))
bracket1 = 10000
bracket2 = 20000

tax = 0

if payable >= bracket2:
    bracket_pay = payable - bracket2
    tax = (bracket_pay * 0.20) + ((bracket2 - bracket1) * 0.10)
elif payable < bracket2 and payable > bracket1:
    bracket_pay = payable - bracket2
    tax = ((payable - bracket1) * 0.10)
else:
    tax = 0
    
print (tax)

