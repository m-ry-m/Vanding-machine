menu=['coke','mineral water','fanta','monster']
for i in range(len(menu)):
    print(i,menu[i])

def cal():
    num=int(input('What would you like to add to your shopping list? '))
    for i in range(len(menu)):
        if num==i:
            print('You added',menu[i],'to your shopping cart.')
            cart=menu[i]
            
cal()
amount=0
j=0
while j<=1:
    k=input('Do you want to quit?(yes/no)')
    if k=='yes' or k=='Yes' or k=='YES':
        break
    else:
        cal()
        amount=amount+1
print('Your total is:',amount)