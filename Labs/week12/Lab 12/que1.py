class FirstSystem:
    def foo(self, data: int) -> str:
        return str(data)
    
class SecondSystem:
    def bar(self, text: str) -> int:
        return int(text)
    
class Adapter(FirstSystem):
    def __init__(self, obj: SecondSystem) -> None:
        self.__obj = obj

    def foo(self, data: int) -> str:
        return str(self.__obj.bar(str(data)))


class Factory:    
    @staticmethod
    def get_system() -> FirstSystem:
        return Adapter(SecondSystem())
    

def main():
    system = Factory.get_system()
    res = system.foo(1234)
    print(res)
    print(type(res))


if __name__ == "__main__":
    main()
