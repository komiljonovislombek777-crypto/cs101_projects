#--- Running Total Calculator ---
print("--- Running Total Calculator ---")
#Enter numbers to add them up. Type 'done' to see the total.
print("Enter numbers to add them up. Type 'done' to see the total.")
total=0
#Enter a number or 'done': 10
while True:
    number=input("Enter a number or 'done':")
    if number=="done":
        break
    number=float(number) 
    total=number
print("Current total:",total)

#Current total: 10.0


#Enter a number or 'done': 5.5
while True:
    number=input("Enter a number or 'done':")
    if number=="done":
        break
    number=float(number) 
    total=number
print("Current total:",total)

#Current total: 15.5

#Enter a number or 'done': 20

#Current total: 35.5

#Enter a number or 'done': done


#--- Final Calculation ---

#The final sum of all numbers is: 35.5