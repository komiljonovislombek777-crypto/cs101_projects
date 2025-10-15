print("--- FizzBuzz Challenge (1-100) ---")
for num in range (1,101):
    if num % 15==0:
        print("fizz")
    elif num % 3==0:
        print("buzz")
    elif num % 5==0:
        print("fizzbuzz")
    else:
        print(num)
