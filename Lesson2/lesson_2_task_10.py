def bank (x,y):
    for i in range (1, y+1):
        count = x + (x/10)
        x = count
    print (round(count, 2))
bank(15000, 10)


percent = 0.1
def bank (deposit, years):
    for i in range (years):
        deposit = deposit + (deposit * percent)
    return print (round(deposit, 2))
bank(15000, 10)