def calculate_square_area(side):
    return side * side
    # "side" is a parameter, used when defining the function

area = calculate_square_area(5)
print(f"The area of the square is {area}")
#"5" is known as an argument and is used when calling the function, not defining

def calculate_square_area(side: int = 2) -> int:
    return side * side
    # "side" is a parameter, used when defining the function

area = calculate_square_area()
print(f"The area of the square is {area}")
# when calling the function without an argument it will use the default value, when an argument is present it overrides the default value

#changing global area function
area = 0    # global variable 

def calculate_square_area(side: int = 2) -> int:
    global area
    area = side * side # local variable
    print(f"The area is {area}")
    return area
    # "side" is a parameter, used when defining the function

calculate_square_area(4)
print(f"The area of the square is {area}")