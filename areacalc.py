from copyreg import pickle
from pickletools import read_unicodestring1


def calculate_square_area(side: float):
    return side * side

def calculate_rectangle_area(length: float, width: float):
    return length * width

def calculate_circle_area(radius: float):
    pi = 3.14
    return pi * radius ** 2

def calculate_rhombus_area(p: float, q: float):
    return (p * q) / 2

print("""
---------------
Area calculator
---------------
Select a shape:
""")
# \t is how to indent
selection = input("""\t'S' - Square
\t'R' - Rectangle
\t'C' - Circle
\t'Rh' - Rhombus
""")

def calculate_area(selection):
    area = 0
    if selection == 'S':
        side = input("Enter the side:")
        area = calculate_square_area(float(side))
    elif selection == 'R':
        length = input("Enther the length:")
        width = input("Enter the width:")
        area = calculate_rectangle_area(float(length), float(width))
    elif selection == 'C':
        radius = input("Enter the radius:")
        area = calculate_circle_area(float(radius))
    elif selection == 'Rh':
        p = input("Enter the p:")
        q = input("Enter the q:")
        area = calculate_rhombus_area(float(q), float(p))
    else:
        print("Invalid Selection.")

    return area

def get_shape_name(tag):
    shape = "Unknown"
    if tag == 'S':
        shape = "square"
    elif tag == 'R':
        shape = "rectangle"
    elif tag == 'C':
        shape = "circle"
    elif tag == 'Rh':
        shape = "rhombus"
    return shape

area = calculate_area(selection)

print(f"The area of the {get_shape_name(selection)} is {area}")