print("HELLO, WELCOME TO OUR CAFE ")
print("HOW CAN I HELP YOU TODAY?")
menu={ "Chai": 80,
       "Doodh Patti": 120,
       "Cold Drink": 100,
       "Water Bottle": 60,
       "Anda Burger": 180,
       "Veg Burger": 150,
       "Chicken Burger": 200,
       "French Fries": 150,
       "Veg Pizza": 250,
       "Chicken Pizza": 350,
       "Veg Sandwich": 200,
       "Chicken Sandwich": 300,
       "Veg Roll": 150,
       "Chicken Roll": 250,
        "Veg Momos": 150,}
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs. {price}")  
total = 0 
while True:
 order = input("Please enter the item you want to order: ").lower().strip()

 for item in menu:
    if order == item.lower():
        quantity = int(input("Please enter the quantity(1,2,3,4): "))

        total += menu[item] * quantity

        print(f"You have ordered {quantity} {item}(s).")
        print(f"Your total is Rs. {total}.")
        break
 else:
    print("Sorry, we don't have that item on the menu.")
 more = input("Do you want to order another item? (yes/no): ").lower().strip()
 if more != "yes":
    print("Thank you for visiting our cafe. Have a great day!")
    break
 else:
    print("Please continue with your order.")
print("Your final total is Rs.", total)


