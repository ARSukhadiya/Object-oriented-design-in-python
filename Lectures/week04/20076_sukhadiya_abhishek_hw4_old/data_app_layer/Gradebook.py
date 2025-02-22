from GradePolicy import GradePolicy
from Student import Student


class Gradebook(GradePolicy):
    def __init__(self, semester, assignments_weight: int, test_weight: int, final_exam_weight: int) -> None:
        # self.__semester = semester
        super().__init__(semester, assignments_weight, test_weight, final_exam_weight)
        self.__students_grade_list = [Student]

    def __str__(self) -> str:
        output = f"Semester: {self.__semester}"
        output += super().__str__(self)

    def display(self) -> None:
        print(self)

    def set_assessment_weight(self, assignments_weight: int, test_weight: int, final_exam_weight: int) -> bool:
        super().__init__(assignments_weight, test_weight, final_exam_weight)

    def add_student(self, student:Student):
        if student not in self.__students_grade_list:
            self.__students_grade_list.append(Student)

    

def main():
    pass


if __name__ == "__main__":
    main()
