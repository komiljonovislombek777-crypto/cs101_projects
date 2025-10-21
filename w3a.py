#=== Car Wash Service Calculator ===
print("=== Car Wash Service Calculator ===")
#Enter service package: basic, deluxe, or premium
print("Enter service package: basic, deluxe, or premium")
#Type 'done' when finished selecting services
print("Type 'done' when finished selecting services")
subtotal=0
while True:
    package=input("Enter service package:")
    if package=="done":
        break
    elif package=="basic":
        price=10
        subtotal=subtotal+price
        print(f"Price: ${price: 2f}")
        print(f"Current total: ${subtotal}")
    elif package=="deluxe":
        price=17
        subtotal=subtotal+price
        print(f"Price: ${price: 2f}")
        print(f"Current total: ${subtotal}")
    elif package=="premium":
        price=25
        subtotal=subtotal+price
        print(f"Price: ${price: 2f}")
        print(f"Current total: ${subtotal}")
if subtotal>=45:
    saving=6
    total=subtotal-saving
else:
    saving=0
    total=subtotal
print("\n=== Service Summary ===")
print(f"Subtotal: ${subtotal}")
print(f"Membership Savings: -${saving}")
print(f"Final Total: ${total}")
print("Thank you for choosing our service!")
