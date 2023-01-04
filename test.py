amount=50
csh=int(input("Enter your cash: "))

def perfect_cash(amount,csh):
    change=csh-amount
    print("\nYour change is:",change,'Aed')
def more_cash(amount,csh):
    print('Please add more cash to purchase:')
    more=amount-csh
    print("More amount needed:",more)
    cas=int(input("Enter more amount: "))
    csh=csh+cas

#In case if more cash
if csh>amount:
    perfect_cash(amount,csh)    
elif csh<amount:
    more_cash(amount,csh)
    if csh>amount:
        perfect_cash(amount,csh)
print("Enjoy!!")



#next user
#Promotion going on, buy for 10 dhs anything and get an item for half the price
#A message that tells the user that a particular drink or snack has been dispensed.