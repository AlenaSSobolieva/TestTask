import math


class Shape:
    def perimeter(self):
        raise NotImplementedError('This method should be implemented by any  subclass.')

    def area(self):
        raise NotImplementedError('This method should be implemented by any  subclass.')


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return round(2 * math.pi * self.radius)

    def area(self):
        return round(math.pi * (self.radius ** 2))


def shapes_factory(parts):
    shape_type = parts[0]
    if shape_type == 'Square':
        side = parts[-1]
        shape = Square(side)
        return shape
    elif shape_type == 'Rectangle':
        top_right = ((parts[2]), (parts[3]))
        bottom_left = ((parts[5]), (parts[6]))
        width = (top_right[0] - bottom_left[0])
        height = (top_right[1] - bottom_left[1])
        return Rectangle(width, height)
    elif shape_type == 'Circle':
        radius = parts[-1]
        return Circle(radius)
    else:
        raise ValueError(f'Unknown value of shape: {shape_type}')


if __name__ == '__main__':
    while True:
        input_data = input('Enter the data >>')
        if not input_data:
            break
        parts = input_data.split()
        for i, part in enumerate(parts):
            if part.isdigit():
                parts[i] = int(part)

        try:
            result = shapes_factory(parts)
            print(f'{parts[0]}: Perimeter: {result.perimeter()}; Area: {result.area()}')
        except ValueError as error:
            print(error)


# Perimeter: {shape.perimeter()}; Area: {shape.area()}'
# Sample input:
# Square TopRight 1 1 Side 1
# Rectangle TopRight 2 2 BottomLeft 1 1
# Circle Center 1 1 Radius 2
#
# Sample output:
# Square Perimeter 4 Area 1
# Rectangle Perimeter 4 Area 1
# Circle Perimeter 1 Area 2
