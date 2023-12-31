import math


class Shape:
    def perimeter(self):
        raise NotImplementedError('This method should be implemented by any  subclass.')

    def area(self):
        raise NotImplementedError('This method should be implemented by any  subclass.')


class Square(Shape):
    def __init__(self, side):
        self.side = side
        if not isinstance(side, int) or side < 0:
            raise ValueError(f'Side of Square must be a non-negative integer')

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if not isinstance(width, int) or width < 0:
            raise ValueError(f'Width of Rectangle must be a non-negative integer')
        elif not isinstance(height, int) or height < 0:
            raise ValueError(f'Height of Rectangle must be a non-negative integer')

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        if not isinstance(radius, int) or radius < 0:
            raise ValueError(f'Radius of Circle must be a non-negative integer')

    def perimeter(self):
        return round(2 * math.pi * self.radius)

    def area(self):
        return round(math.pi * (self.radius ** 2))


class Triangle(Shape):
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3


    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3



def shapes_factory(parts):
    if not parts:
        raise ValueError("No input data provided")

    shape_type = parts[0]
    expected_lengths = {
        'Square': 6,
        'Rectangle': 7,
        'Circle': 6,
        'Triangle': 10,
    }
    expected_length = expected_lengths.get(shape_type)
    if expected_length is None:
        raise ValueError(f'Unknown value of shape: {shape_type}')

    if len(parts) != expected_length:
        raise ValueError(f'Insufficient or too many arguments for {shape_type}')

    if shape_type == 'Square':
        side = parts[-1]

        shape = Square(side)
        return shape
    elif shape_type == 'Rectangle':
        top_right = (parts[2], parts[3])
        bottom_left = (parts[5], parts[6])
        width = top_right[0] - bottom_left[0]
        height = top_right[1] - bottom_left[1]
        return Rectangle(width, height)
    elif shape_type == 'Circle':
        radius = parts[-1]
        return Circle(radius)
    elif shape_type == 'Triangle':
        point1 = (parts[2], parts[3])
        point2 = (parts[5], parts[6])
        point3 = (parts[8], parts[9])
        side_1 = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
        side_2 = math.sqrt((point2[0]-point3[0])**2 + (point2[1]-point3[1])**2)
        side_3 = math.sqrt((point3[0]-point1[0])**2 + (point3[1]-point1[1])**2)
        return Triangle(side_1, side_2, side_3)


if __name__ == '__main__':
    while True:
        input_data = input('Enter the data >>')

        parts = input_data.split()
        for i, part in enumerate(parts):
            if part.isdigit():
                parts[i] = int(part)
        print(parts)
        try:
            result = shapes_factory(parts)
            print(f'{parts[0]}: Perimeter: {result.perimeter()}; Area: {result.area()}')
        except ValueError as error:
            print(error)

# Sample input:
# Square TopRight 1 1 Side 1
# Rectangle TopRight 2 2 BottomLeft 1 1
# Circle Center 1 1 Radius 2
# Triangle Point1 5 5 Point2 8 8 Point3 10 2
#
# Sample output:
# Square Perimeter 4 Area 1
# Rectangle Perimeter 4 Area 1
# Circle Perimeter 1 Area 2
