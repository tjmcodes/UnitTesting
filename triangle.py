# first brainstorm

def triangle_calc():
    print("Enter the number of the length of each triangle sides: ")

    try:
        x = int(input("side x: "))
    except ValueError:
        print("Invalid number, please re-start"), triangle_calc()
    try:
        y = int(input("side y: "))
    except ValueError:
        print("Invalid number, please re-start"), triangle_calc()
    try:
        z = int(input("side z: "))
    except ValueError:
        print("Invalid number, please re-start"), triangle_calc()

    if x == y == z:  # all sides equal
        print("This is an Equilateral triangle"), triangle_calc()
    elif x == y or y == z or z == x:  # at least 2 sides equal
        print("This is an Isosceles triangle"), triangle_calc()
    else:
        print("This is a Scalene triangle"), triangle_calc()


triangle_calc()
