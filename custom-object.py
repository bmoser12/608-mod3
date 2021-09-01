#use this to figure out a bill total including tip and tax

def tip_amount(total,tip_percent):
    return total*tip_percent
def tax_amount(total, tax_percent):
    return total*tax_percent
def bill_total(total,tax,tip):
    return total+tip_amount+tax_amount
    
total = 100
tip_percent = .20
tax_percent = .075

tax = tax_amount(total,tax_percent)
tip = tip_amount(total,tip_percent)

print('Tip amount:',tip)
print('Tax amount:', tax)
print('Bill total:',total+tax+tip)
