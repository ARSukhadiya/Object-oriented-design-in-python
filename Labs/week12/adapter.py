from functools import reduce


class OldMath:
    def add(self, x: int, y: int) -> int:
        return x + y

class NewMath:
    def add(self, x: int, y: int, z: int) -> int:
        return x + y + z

class MathAdapter(OldMath):
    def __init__(self, math: NewMath) -> None:
        self.__obj = math
    
    def add(self, x: int, y: int) -> int:
        return self.__obj.add(x, y, 0)

class MathFactory:
    @staticmethod
    def get_math() -> OldMath:
        # return OldMath()
        return MathAdapter(NewMath())
    
# Client's application
def main():
    # math = MathFactory.get_math()
    # sum = math.add(10, 5)

    # print('sum:', sum)

    nums = [2, 4, 6, 8]
    sumw = reduce(lambda x, y: x + y , nums)

    print(sum)

main()