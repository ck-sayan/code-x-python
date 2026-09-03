# This is for practice purpose only. Do not use this code in production.

# Problem-1

# name = (input("What's your name, lad? = "))
# age = int(input("How old are you, lad? = "))
# fav_food = input("What's your favourite food, lad? = ")
# fav_prog_language = input("What's your favourite programming language, lad? = ")

# print(f"Hey {name}! It seems you are {age} years old buddy and your favourite food is {fav_food}. Also, you love coding in {fav_prog_language}. That's pretty cool!")

# Problem-2

# current_age = int(input("Heyy, what's your current age? = "))
# age_next_year = current_age + 1
# age_in_5_years = current_age + 5
# age_in_10_years = current_age + 10

# print(f"Heyy, if you are currently {current_age}\nthen next year you'll be {age_next_year}\nin 5 years you'll be {age_in_5_years} and\nin 10 years you'll be {age_in_10_years}.\nTime flies, doesn't it?")

# Problem-3

# item_name = input("Enter your item name: ")
# item_price = float(input("Enter the price of the item: ₹"))
# item_quantity = int(input("Enter the quantity of the item: "))

# print(f"Item: {item_name}")
# print(f"Price: ₹{item_price:.2f}")
# print(f"Quantity: {item_quantity}")

# print(f"\nTotal: ₹{item_price * item_quantity:.2f}\nThank you for shopping with us!")

# Problem-4

# age = int(input("Enter your age: "))

# if age > 18:
#     print("You are an adult, eligible for voting!")
# else:
#     print("You are not an adult, ineligible for voting")

# Problem-5

# amount_money = float(input("How much money do you have?\n"))
# cost_money = float(input("How much does the item cost?\n"))

# print(f"Money: {amount_money}")
# print(f"Price: {cost_money}")

# if cost_money > amount_money:
#     print("You can't afford it mate!")
# else:
#     print("Cheers! You can afford it")

# Problem-6

# temp_celsius = float(input("Enter the temperature in °C: "))

# if temp_celsius>=35:
#     print("It's goddamn hot!")
# elif temp_celsius>=25:
#     print("It's comfortably warm.")
# elif temp_celsius>=15:
#     print("It's pleasant.")
# elif temp_celsius<15:
#     print("It's really cold!")
# else:
#     print("The input is invalid!")

# Problem-7 = Restaurant Bill Generator

food_price = float(input("Food Price = ₹"))
quantity = int(input("Quantity = "))
tip = float(input("Tip = %"))

subtotal = food_price*quantity
tax = (18/100)*subtotal
tip = (tip/100)*subtotal
final_bill = subtotal+tax+tip

print("\nBill Summary:")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST: ₹{tax:.2f}")
print(f"Tip: ₹{tip:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")