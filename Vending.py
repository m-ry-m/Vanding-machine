#The Vending Machine must have the following features as a minimum requirement:
 
#●	A menu of drinks and snacks presented via the console.
#  The number and range of items is up to you.
#●	A set of codes that the user can input to select a particular drink or snack.
#●	 A way of capturing the user’s inputted code.
#●	A way of managing money. The user should be able to input any amount of 
# money and have the correct change returned.
#●	A message that tells the user that a particular drink or snack has been dispensed.
#●	 A message that tells the user how much change they have received.
#●	 Comments in the code to explain key operations.
 
#Additional Features 
#●	A method of categorising items in the vending machine to improve the user experience (e.g. ‘Chocolate’ or ‘Hot Drinks’).

#Menu
print('Menu:')
#drinks
drinks=['Coke','Mineral water','Fanta','Monster drink','Orange juice','Sprite','Red Bull','Pepsi']
print('Drinks:')
for i in range(len(drinks)):
    print(i,drinks[i])
    
#Snacks
snacks=['Lays','Pringles','Oreo','Doritoz','Cheetoz','Ringos','Bugles','Potato Sticks']
print('\nSnacks:')
for i in range(len(snacks)):
    print(i,snacks[i])
