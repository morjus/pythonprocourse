from unittest import TestCase

from main import Point, GuiRectangle


class TestGame(TestCase):
    def test_distance_between_points_by_x(self):
        x = Point(3, 0)
        y = Point(0, 0)
        self.assertEqual(x.distance_from_point(y), x.x)

    def test_distance_between_points_by_y(self):
        x = Point(0, 0)
        y = Point(0, 3)
        self.assertEqual(x.distance_from_point(y), y.y)

    def test_rectangle_area(self):
        lower_left = Point(0, 0)
        upper_right = Point(3, 3)
        rectangle = GuiRectangle(point1=lower_left, point2=upper_right)
        current_area = upper_right.x * upper_right.y
        self.assertEqual(rectangle.area, current_area)

    def test_is_point_inside(self):
        lower_left = Point(1, 1)
        upper_right = Point(3, 3)
        point = Point(2, 2)
        rectangle = GuiRectangle(point1=lower_left, point2=upper_right)
        self.assertTrue(rectangle.is_point_inside(point=point))

    def test_is_point_not_inside(self):
        lower_left = Point(1, 1)
        upper_right = Point(3, 3)
        point = Point(4, 4)
        rectangle = GuiRectangle(point1=lower_left, point2=upper_right)
        self.assertFalse(rectangle.is_point_inside(point=point))
