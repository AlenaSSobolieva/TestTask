import unittest
from main import Square, Rectangle, Circle, shapes_factory


class TestShapes(unittest.TestCase):

    def test_square_perimeter(self):
        square = Square(5)
        self.assertEqual(square.perimeter(), 20)

    def test_square_perimeter_zero(self):
        square = Square(0)
        self.assertEqual(square.perimeter(), 0)

    def test_square_area(self):
        square = Square(7)
        self.assertEqual(square.area(), 49)

    def test_square_area_zero(self):
        square = Square(0)
        self.assertEqual(square.area(), 0)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(2, 5)
        self.assertEqual(rectangle.perimeter(), 14)

    def test_rectangle_perimeter_zero(self):
        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.perimeter(), 0)

    def test_rectangle_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_rectangle_area_zero(self):
        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.area(), 0)

    def test_circle_perimeter(self):
        circle = Circle(5)
        self.assertEqual(circle.perimeter(), 31)

    def test_circle_perimeter_zero(self):
        circle = Circle(0)
        self.assertEqual(circle.perimeter(), 0)

    def test_circle_area(self):
        circle = Circle(7)
        self.assertEqual(circle.area(), 154)

    def test_circle_area_zero(self):
        circle = Circle(0)
        self.assertEqual(circle.area(), 0)


class TestShapesFactory(unittest.TestCase):

    def test_valid_square(self):
        result = shapes_factory(['Square', 'TopRight', 1, 1, 'Side', 1])
        self.assertIsInstance(result, Square)
        self.assertEqual(result.side, 1)

    def test_valid_rectangle(self):
        result = shapes_factory(['Rectangle', 'TopRight', 2, 2, 'BottomLeft', 1, 1])
        self.assertIsInstance(result, Rectangle)
        self.assertEqual(result.width, 1)
        self.assertEqual(result.height, 1)

    def test_valid_circle(self):
        result = shapes_factory(['Circle', 'Center', 1, 1, 'Radius', 2])
        self.assertIsInstance(result, Circle)
        self.assertEqual(result.radius, 2)

    def test_invalid_shape_type(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory(['Triangle', 'Point1', 5, 5, 'Point2', 8, 8, 'Point3', 10, 2])
        self.assertEqual(str(context.exception), "Unknown value of shape: Triangle")

    def test_invalid_arguments_square(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory(["Square"])
        self.assertEqual(str(context.exception), "Insufficient or too many arguments for Square")

    def test_invalid_arguments_rectangle(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory(["Rectangle", 2, 5, 4])
        self.assertEqual(str(context.exception), "Insufficient or too many arguments for Rectangle")

    def test_invalid_arguments_circle(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory(["Circle"])
        self.assertEqual(str(context.exception), "Insufficient or too many arguments for Circle")

    def test_negative_side_square(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory(["Square", "TopRight", 1, 1, "Side", -1])
        self.assertEqual(str(context.exception), "Side of Square must be a non-negative integer")

    def test_negative_width_rectangle(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory(['Rectangle', 'TopRight', -2, 2, 'BottomLeft', -1, 1])
        self.assertEqual(str(context.exception), "Width of Rectangle must be a non-negative integer")

    def test_negative_height_rectangle(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory(['Rectangle', 'TopRight', 2, -2, 'BottomLeft', 1, -1])
        self.assertEqual(str(context.exception), "Height of Rectangle must be a non-negative integer")

    def test_negative_radius_circle(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory(["Circle", "Center", 1, 1, "Radius", -2])
        self.assertEqual(str(context.exception), "Radius of Circle must be a non-negative integer")

    def test_no_input_data(self):
        with self.assertRaises(ValueError) as context:
            shapes_factory([])
        self.assertEqual(str(context.exception), "No input data provided")


if __name__ == '__main__':
    unittest.main()
