class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width
        return self.width

    def set_height(self, new_height):
        self.height = new_height
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ''
            brick = '*'
            height = self.height
            width = self.width * brick
            for n in range(height):
                picture += width + '\n'
            return picture

    def get_amount_inside(self, figure):
        rect_area = self.get_area()
        other_fig_area = figure.get_area()
        result = rect_area // other_fig_area
        times_fit = result
        return result

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, height=width)
        self.width = width
        self.height = width

    def set_side(self, sides):
        self.width = sides
        return self.set_width

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_width(self, new_width):
        self.width = new_width
        return self.width

    def set_height(self, new_width):
        self.height = new_width
        return self.height

    def get_picture(self):
        if self.width > 50:
            return "Too big for picture."
        else:
            picture = ''
            brick = '*'
            height = self.width
            width = self.width * brick
            for n in range(height):
                picture += width + '\n'
            return picture


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

# TODO fix this one below
print(rect.get_amount_inside(sq))
