def rectangle(length, width):
    def validation():
        return "Enter valid values!"

    def area():
        rectangle_area = length * width
        return rectangle_area

    def perimeter():
        rectangle_perimeter = 2 * (length + width)
        return rectangle_perimeter

    if type(length) != int or type(width) != int or length < 0 or width < 0:
        return validation()

    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'

