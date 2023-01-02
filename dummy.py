#List of drink

drinks=['coke','Fanta','Orange juice','Mountain Dew']

#List of Snacks

snacks=['Lays','Pringles','Oreo','Doritoz','Cheetoz','Ringos','Bugles','Potato Sticks']
    
#Printing Drink's List

print('\nDrinks:')
for i in range(len(drinks)):
    print(i,drinks[i])

#Printing Snack's List

print("\nSnacks:")
for j in range(len(snacks)):
    print(j,snacks[j])
k=1
cart=[]


while k<=1:
    item=input('Would you like snack or drink?')
    if item=='snack':
        chose=input('Which snack item would you like to add in you cart?')
        for l in range(len(snacks)):
            if chose==snacks[l]:
                cart.append(snacks[l])
    elif item=='quit':
        break
print(cart)
print(len(cart))