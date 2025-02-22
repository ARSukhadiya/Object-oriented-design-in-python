

class GradePolicy:
    def __init__(self, semester, assignments_weight: int, test_weight: int, final_exam_weight: int) -> None:
        self.__semester = semester
        self.__assignments_weight = assignments_weight
        self.__test_weight = test_weight
        self.__final_exam_weight = final_exam_weight

    def __str__(self) -> str:
        return f"Semester: {self.__semester} | Assignments' weight: {self.__assignments_weight} | Tests' weight: {self.__test_weight} | Final exam's weight: {self.__final_exam_weight} "

    def display(self) -> None:
        print(self)


def main():
    pass


if __name__ == "__main__":
    main()
