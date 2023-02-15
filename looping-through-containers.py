primes = [2, 3, 5, 7, 11]

#for number in primes:
#    print(number)

# same thing as above but with while statement
#index = 0
#while index < len(primes):
#    print(primes[index])
#    index += 1

#for number in primes:
#    if number % 2 == 0:
#        print(f"{number} is even")
#    else:
#        print(f"{number} is odd")

#collecting numbers in dedicated list
even_numbers = []
odd_numbers = []

for number in primes:
    if number % 2 == 0: #checking if the numbers are divisbile by 2
        #print(f"{number} is even")
        even_numbers.append(number)
    else:
        #print(f"{number} is odd")
        odd_numbers.append(number)

print("Even numbers(s)") # seperating the even numbers under a dedicated list
for i in even_numbers:
    print(i)

print("Odd Number(s)") # seperating the odd numbers under a dedicated list
for j in odd_numbers:
    print(j)

ssn_name_pairs = {"123-456-789": "John Appleseed", # dictionary
                    "000-000-002": "Dwight Schrute",
                    "000-000-0003": "Pam Beesly"}

keys = ssn_name_pairs.keys()
values = ssn_name_pairs.values()

print("Dictionary keys") # for-in loop for the dicitionary keys
for key in keys:
    print(key)

print("Dictionary values") # for-in loop for the dicitionary values
for value in values:
    print(value)

key_value_pairs = ssn_name_pairs.items() # assigning both keys and values of ssn_name_pairs to key_value_pairs

print("Key-value pairs") 
for key_value in key_value_pairs:
    print(key_value)

# print as tuple
print("Key-value pairs") 
for (key, value) in key_value_pairs:
    print(key, value)

