class LegacyRectangle:
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    def get_height(self) -> float:
        return self.__height

    def get_width(self) -> float:
        return self.__width


class ModernShape:
    def __init__(self, area: float, perimeter: float) -> None:
        self.__area = area
        self.__perimeter = perimeter

    def get_area(self) -> float:
        return self.__area

    def get_perimeter(self) -> float:
        return self.__perimeter


# Adapters
class RectangleAdapter(ModernShape):
    def __init__(self, obj: LegacyRectangle) -> None:
        self.__obj = obj

    def get_area(self) -> int:
        return self.__obj.get_height() * self.__obj.get_width()

    def get_perimeter(self) -> int:
        return 2 * (self.__obj.get_height() + self.__obj.get_width())


class ShapeAdapter(LegacyRectangle):
    def __init__(self, obj: ModernShape) -> None:
        self.__obj = obj

    def find_h_w(self) -> tuple[float, float]:
        perimeter_for_one_side = -(self.__obj.get_perimeter() / 2)
        area = self.__obj.get_area()
        discriminant = (perimeter_for_one_side**2) - (4 * area)
        length = (-perimeter_for_one_side + (discriminant**0.5)) / 2
        width = area / length
        return length, width

    def get_height(self) -> float:
        return self.find_h_w()[0]

    def get_width(self) -> float:
        return self.find_h_w()[1]
    


# Factories
class ShapeFactory:
    def __init__(self, height: float, width: float) -> None:
        self.__height = height
        self.__width = width
    
    def get_shape(self) -> ModernShape:
        return RectangleAdapter(LegacyRectangle(self.__height, self.__width))


class ShapeFactory2:
    @staticmethod
    def get_rectange(area: float, perimeter: float) -> LegacyRectangle:
        return ShapeAdapter(ModernShape(area, perimeter))


# Main method
def main():
    shape = ShapeFactory(10.0, 5.0).get_shape()
    print(f"area = {shape.get_area()}")
    print(f"perimeter = {shape.get_perimeter()}")

    shape2 = ShapeFactory2.get_rectange(50.0, 30.0)
    print(f"width = {shape2.get_width()}")
    print(f"height = {shape2.get_height()}")

if __name__ == "__main__":
    main()