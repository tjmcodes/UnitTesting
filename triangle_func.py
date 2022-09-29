def triangle_type(a, b, c):
    # validate entry first
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)) or not isinstance(c, (float, int)):
        return "Invalid. Only accepts integer"

    # this block will run if the above is true
    # different triangle types:
    # doesn't accept negative integers
    if a < 0 or b < 0 or c < 0:
        return "Error"
    else:
        # start with validation
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            if a == b or b == c or a == c:
                return "Isosceles"
            if a != b or b != c or a != c:
                return "Scalene"
        else:
            return "Not a triangle"


my_triangle_type = triangle_type(10, 2, 1)
print(my_triangle_type)
