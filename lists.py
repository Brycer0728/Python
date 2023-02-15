primes = list()
print(primes)

priems = []

primes = [1, 2, 3, 4, 5]
primes.append(6)
primes.append(7)
primes.append(8)
print(primes)

names = ["Michael", "Dwight", "Pam"]

values = [True, False, False, True]

bag = [1, 2, 3]
bag.append("Pam")
bag.append(True)
bag.append(4)
print(bag)

list = ["Michael", "Dwight", "Pam"]
# remember that index starts with 0, so Michael = 0, Dwight = 1, Pam = 2
name = list[2]
# if print(name) was exucuted, it would print Pam

# 0 <= valid_index < len(list)

def is_valid_index(index: int, list: list) -> bool:
    result = False
    if 0 <= index and index < len(list):
        result = True
    return result

index = 2
print(f"Index {index} is valid" if is_valid_index(index, list) else f"Index {index} is out of range.")