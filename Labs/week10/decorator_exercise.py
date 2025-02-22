class Something:
    def __init__(self, name) -> None:
        self.name = name

    def walk(self):
        print("Walking...")

    def sleep(self):
        print("Sleeping...")

class DecorateSomething(Something):
    def __init__(self, obj: Something) -> None:
        self.__obj = obj

    def walk(self):
        print("***")
        return self.__obj.walk()
        # self.walk()

    def sleep(self):
        print("***")
        return self.__obj.sleep()
    
    def read(self):
        print(f"{self.__obj.name} Reading...")

    def learn(self):
        print(f"{self.__obj.name} Learning...")


def main():
    p = Something("Peter")
    # p.walk()
    # p.sleep()

    # Decorate the p object
    p = DecorateSomething(p)
    p.walk()
    p.sleep()
    p.read()
    p.learn()

if __name__ == "__main__":
    main()
