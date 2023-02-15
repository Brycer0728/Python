part1 = "Stay hungry."
part2 = "Stay foolish."

quote = part1 + " " + part2
print(quote)

quote = f"{part1} {part2}"
print(quote)

name = "Michael"
age = 32
message = f"Your name is {name}, and you are {age} years old."
print(message)

car = "Tesla Roadster"
acceleration = 1.9
message = f"The {car} goes 0-60 mph in {acceleration} seconds"

print(message)

pi = 3.14159265359
message = f"The number pi is approximately equal to {pi}"
print(message)

print(len(message))

message = "Stay hungry. Stay foolish."
uppercase_message = message.upper()
print(uppercase_message)

lowercase_message = message.lower()
print(lowercase_message)

stay_count = message.count("Stay")
print(f"Count of Stay in {message} is {stay_count}")

message = "The red fox ate some red apples on a red carpet"
red_count = message.count("red")
print(f"Count of Red in {message} is {red_count}")