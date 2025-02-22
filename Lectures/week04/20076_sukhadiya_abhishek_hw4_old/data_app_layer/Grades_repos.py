from Student import Student
import json


class GradesRepository:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def save_grades(self, students: list[Student]):
        # with open(self.__filename, 'w', newline='') as file:
        #     for student in students:
        #         file.write(str(student) + "\n")
            # def save(self, students: list[Student], filename: str = "grades.dat") -> None:
        students_data = [
            {
                "std_id": student.std_id,
                "fname": student.fname,
                "lname": student.lname,
                "assignment_scores": [{"grade": a.grade} for a in student.assignment_scores],
                "test_scores": [{"grade": t.grade} for t in student.test_scores],
                "final_scores": {"grade": student.final_scores.grade} if student.final_scores else None
            }
            for student in students
        ]

        with open(self.__filename, 'w', newline='') as file:
            json.dump(students_data, file, indent=4)


    def read_grades(self) -> list:
        students = []
        with open(self.__filename, 'r', newline='') as file:
            for row in file.readlines():
                # data = row.split(', ,')
                std_id_uname, ass, test, final = tuple(row.split(', ,'))
                std_id, uname = tuple(std_id_uname.split(', '))
                
                student = Student(std_id=std_id, username=uname, assignment_scores=ass)
                students.append()
        return students
    

def main():
    std1 = Student(1000, "Abhi", "Patel", "Patel_Abhi2gs2s", {"LAC1": 8, "LAB1": 10}, {"test1": 9, "test2": 9.5}, 60)
    std2 = Student(1001, "Karan", "Patel", "Patel_Karan2ee2s", {"LAC1": 7, "LAB1": 9}, {"test1": 8, "test2": 8.5}, 65)

    students: list[Student] = []
    students.append(std1)
    students.append(std2)

    repos = GradesRepository("Grades.dat")
    repos.save_grades(students)

    students2 = repos.read_grades()
    for student in students2:
        print(student)


if __name__ == "__main__":
    main()
