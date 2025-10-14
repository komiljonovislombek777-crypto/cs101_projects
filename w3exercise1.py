print("--- Movie Ticket Pricer ---")

age=int(input("Please enter your age:"))

if age<=12:
    print("You fall into the 'Children' category.")
    print("Your ticket price is: $8")

elif 13<=age<=64:
    print("You fall into the 'Adult' category")
    print("Your ticket price is: $15")
else :
    print("You fall into the 'Seniors' category.")
    print("Your ticket price is: $10")
