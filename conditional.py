balance = 5000
money = 100
if balance > money:
    balance -= money
    print(f"Current balance is {balance}")
    print("Transaction complete. Don't forget your card.")
else:
    print("Insufficient funds")
    print(f"Current balance is {balance}")

# the condition in this example is balance > money

is_raining = True

if is_raining:
    print("Take your umbrella.")

number = 12

if number % 2 == 0:
    print ("The number is even")
if number > 10:
    print("The number is greater than ten")
if number == 12:
    print("A dozen")

traffic_light = "green"

if traffic_light == "green":
    print("Go!")
elif traffic_light == "yellow":
    print("Slow down.")
elif traffic_light == "red":
    print("Stop!")
else:
    print("Invalied state.")

# nested conditionals example

traffic_light = "green"
is_blinking = True

if traffic_light == "red":
    if is_blinking:
         print("Stop! Proceed when safe.")
    else:
        print("Stop")

success = True
result_code = 200

if success == True and result_code == 200:
    print("Success")
else:
    print("Failure")

first_name = "Bryce"
last_name = "Steele"

if len(first_name) == 0 or len(last_name) == 0:
    print("Enter your name")
else:
    print(f"Welcome {first_name} {last_name}")

admin_user = True

if not admin_user:
    print("Permission denied!")
else:
    print("Welcome, user.")