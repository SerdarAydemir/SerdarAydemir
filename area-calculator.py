def calculate_square_area(side: float):
    return side * side


def calculate_rectangle_area(length: float, width: float):
    return length * width


def calculate_circle_area(radius: float):
    pi = 3.14
    return pi * radius ** 2

def calculate_triangle_area(height: float, base: float):
    return height * base / 2

print("""
------------------------
    Area Calculator
------------------------
    Select a Shape :
""") 

selection = input("""\t'S'- Square
\t'R' - Rectangle
\t'C' - Circle
\t'T' - Triangle                  
""")


def calculate_area(selection):
    area = 0

    if selection == 'S':
        side = input("Enter the Side:")
        area = calculate_square_area(float(side))
    elif selection == 'R':
        length = input("=Enter the Length:")
        width = input("Enter the Width:")
        area = calculate_rectangle_area(float(length) , float(width))
    elif selection == 'C':
        radius = input("Enter the Radius:")
        area = calculate_circle_area(float(radius))
    elif selection == 'T':
        height = input("Enter the Height:")
        base = input("Enter the Base:")
        area = calculate_triangle_area(float(height), float(base))
    else:
        print("Invalid selection. Please choose 'K', 'DG', 'D' or 'U'.")
    return area

def get_shape_name(tag):
    shape = "Unknown"
    if tag == 'S':
        shape = "square"
    elif tag == 'R':
        shape = "rectangle"
    elif tag == "C" :
        shape = "circle"
    elif tag == 'T':
        shape = "triangle"
    return shape


area = calculate_area(selection)

print(f"The area of the {get_shape_name(selection)} is {area}")