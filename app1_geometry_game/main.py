from random import randint
import turtle

from draw_helper import penup_always


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class GuiPoint(Point):
    @penup_always
    def draw(self, canvas, size=5, color="red"):
        canvas.goto(x=self.x, y=self.y)
        canvas.pendown()
        canvas.color(color)
        canvas.dot(size=size)
        canvas.color("black")


class Rectangle:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    @property
    def area(self):
        return (self.point1.x - self.point2.x) * (self.point1.y - self.point2.y)

    def is_point_inside(self, point: Point):
        return (
            self.point1.x < point.x < self.point2.x
            and self.point1.y < point.y < self.point2.y
        )


class GuiRectangle(Rectangle):
    @penup_always
    def draw(self, canvas):
        angle = 90
        length = self.point2.x - self.point1.x
        height = self.point2.y - self.point1.y

        canvas.goto(x=self.point1.x, y=self.point1.y)
        canvas.pendown()
        canvas.forward(length)
        canvas.left(angle)
        canvas.forward(height)
        canvas.left(angle)
        canvas.forward(length)
        canvas.left(angle)
        canvas.forward(height)


def main():
    max_num = 100
    lower_left = Point(x=randint(0, max_num), y=randint(0, max_num))
    upper_right = Point(x=randint(10, max_num), y=randint(10, max_num))
    rectangle = GuiRectangle(point1=lower_left, point2=upper_right)

    print(
        f"Rectangle Coordinates: "
        f"Left bottom angle (X={rectangle.point1.x}, Y={rectangle.point1.y}) "
        f"and Right top angle (X={rectangle.point2.x}, Y={rectangle.point2.y})"
    )
    print("Try to guess dot inside in rectangular! Type coordinate!")

    user_point = GuiPoint(
        x=float(input("Guess X: ")),
        y=float(input("Guess Y: ")),
    )

    user_area = float(input("Guess rectangle area: "))

    point_message = f"Your point was inside rectangle: {rectangle.is_point_inside(point=user_point)}"
    area_message = f"Your area {user_area} was off by: {rectangle.area - user_area}"
    print(point_message)
    print(area_message)
    input("Press enter to visualisation and exit...")

    myturtle = turtle.Turtle()
    myturtle.hideturtle()
    rectangle.draw(canvas=myturtle)
    user_point.draw(canvas=myturtle)
    myturtle.write(
        point_message + "\n" + area_message,
        align="center",
        font=("Arial", 15, "normal"),
    )
    turtle.done()


if __name__ == "__main__":
    main()
