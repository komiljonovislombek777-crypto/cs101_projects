print("--- Running Total Calculator ---")

print("Enter numbers to add them up. Type 'done' to see the total.")
total=0
while True:
    number=input("Enter a number or 'done':")
    if number=="done":
        break
    number=float(number) 
    total+=number
print("Current total:",total)

