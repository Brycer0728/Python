primes = [2, 3, 5, 7, 11]
print(primes)
primes[1] = 17
# replaced 3 which is at index 1 with the number 17
print(primes)

primes.append(13)
# primes.append adds the number to the END of the list, no matter if its bigger or smaller than other numbers
print(primes)

characters = []
characters.append("a")
print(f"The length of the character list is {len(characters)}")

primes.insert(1, 3)
print(primes)

# primes.pop() removes the last element in the list since it's not specified
n = primes.pop(2)
print(f"Element {n} removed. The primes list became {primes}")

# primes.remove() removes a specific value, if nothing is put inbetween the parenthesis then it will give an error
primes.remove(5)
print(primes)