message = "The red fox eats red apples on the red carpet"
red_count = message.count("red")
print(f"The number of times red appears in {message} is {red_count}")

a = 2
b = 4
c = a - a + b + b
print(c)
#

balance = 12
withdraw = 11

if balance > withdraw:
    balance -= withdraw
    print(f"${balance} left in the piggy bank.")
else:
    print("Insuficient funds.")
# even or odd
number = 3

if int(number) % 2 == 0:
    print("Even")
else:
    print("Odd")

#print how far mars is from the sun
planet = "Mars"
distnace_from_sun = "227.9"

if planet == "Mars":
    print(f"{planet} is {distnace_from_sun} million km away from the Sun")

#
def calculate_square_area(side: int = 2) -> int:
    return side * side
    # "side" is a parameter, used when defining the function

area = calculate_square_area()
print(f"The area of the square is {area}")

def build_ferrari(color = "red"):
    print(f"Built a {color} Ferrari")

build_ferrari("green")
