import json
from student import Student, GradePolicy, Assignment, Test, FinalExam
from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def save(self, data, filename: str):
        pass

    @abstractmethod
    def load(self, filename: str):
        pass


class StudentRepository(Repository):
    def save(self, all_students: list[Student], filename: str = "grades.dat") -> None:
        students_data = [
            {
                "student_id": student.student_id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "assignments": [{"grade": a.grade} for a in student.assignments],
                "tests": [{"grade": t.grade} for t in student.tests],
                "final_exam": {"grade": student.final_exam.grade} if student.final_exam else None
            }
            for student in all_students
        ]

        with open(filename, 'w') as file:
            json.dump(students_data, file, indent=4)

    def load(self, filename: str = "grades.dat") -> list[Student]:
        try:
            with open(filename, 'r') as f:
                students_data = json.load(f)

            students = []
            grade_policy_repo = GradePolicyRepository()
            grade_policy = grade_policy_repo.load()
            
            for student_data in students_data:
                student = Student(student_data["student_id"], student_data["first_name"], student_data["last_name"],
                                  grade_policy.num_assignments, grade_policy.num_tests)
            
                for assignment_data in student_data.get("assignments", []):
                    assignment = Assignment(grade_policy.assignment_weight)
                    assignment.record_grade(assignment_data["grade"])
                    student.assignments.append(assignment)
            
                for test_data in student_data.get("tests", []):
                    test = Test(grade_policy.test_weight)
                    test.record_grade(test_data["grade"])
                    student.tests.append(test)
            
                if student_data.get("final_exam"):
                    final_exam = FinalExam(grade_policy.final_exam_weight)
                    final_exam.record_grade(student_data["final_exam"]["grade"])
                    student.set_final_exam(final_exam)
            
                students.append(student)
            
            return students
        
        except FileNotFoundError:
            print(f"No existing {filename} found. Starting with an empty student list.")
            return []
        
        except json.JSONDecodeError:
            return []

    def clear(self, filename: str = "grades.dat"):
        with open(filename, 'w') as f:
            f.write("[]")


class GradePolicyRepository(Repository):
    def save(self, grade_policy: GradePolicy, filename: str = "policy.dat") -> None:
        grade_policy_data = {
            "assignment_weight": grade_policy.assignment_weight,
            "test_weight": grade_policy.test_weight,
            "final_exam_weight": grade_policy.final_exam_weight,
            "num_assignments": grade_policy.num_assignments,
            "num_tests": grade_policy.num_tests,
            "num_final_exams": grade_policy.num_final_exams
        }

        with open(filename, 'w') as f:
            json.dump(grade_policy_data, f, indent=4)

    def load(self, filename: str = "policy.dat") -> GradePolicy:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            return GradePolicy(data["assignment_weight"], data["test_weight"], data["final_exam_weight"],
                               data["num_assignments"], data["num_tests"], data["num_final_exams"])
        except FileNotFoundError:
            return GradePolicy(0, 0, 0)
        except json.JSONDecodeError:
            return GradePolicy(0, 0, 0)

