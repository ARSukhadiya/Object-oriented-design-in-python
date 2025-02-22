from gradebook import Gradebook, GradePolicy, AssessmentType
from student import Student
from gradebook_repos import StudentRepository, GradePolicyRepository


class GradebookApp:
    def __init__(self):
        self.__grade_policy_repo = GradePolicyRepository()
        self.__student_repo = StudentRepository()

        try:
            grade_policy = self.__grade_policy_repo.load()
        except FileNotFoundError:
            grade_policy = GradePolicy(0, 0, 0)

        self.__gradebook = Gradebook(grade_policy)
        self.__gradebook.students = self.__student_repo.load()


    def main_menu(self):
        while True:
            print("""
S - Set up new semester
A - Add student
P - Record programming assignment grades
T - Record test grades
F - Record final exam grades
C - Change a grade
G - Calculate final grades
O - Output grade data
Q - Quit""")
            choice = input("\nEnter your choice: ").upper()
            if choice == 'S':
                self.setup_new_semester()

            elif choice == 'A':
                self.add_student()

            elif choice in ['P', 'T', 'F']:
                assessment_type = {
                    'P': AssessmentType.ASSIGNMENT,
                    'T': AssessmentType.TEST,
                    'F': AssessmentType.FINAL_EXAM
                }.get(choice)
                self.record_grade(assessment_type)

            elif choice == 'C':
                self.change_grade()

            elif choice == 'G':
                self.calculate_final_grades()

            elif choice == 'O':
                self.output_grade_data()

            elif choice == 'Q':
                self.quit_application()
                break

            else:
                print("Invalid option, please try again!")

    def setup_new_semester(self):
        print("Setting up a new semester. \nEnter the grading policy details:")

        num_assignments = self.get_valid_input("Enter the no of assignments (0 to 6): ", 0, 6)
        num_tests = self.get_valid_input("Enter the no of tests (0 to 4): ", 0, 4)
        num_final_exams = self.get_valid_input("Enter the no of final exams (0 to 1): ", 0, 1)

        assign_weight, test_weight, final_exam_weight = self.get_valid_weights()

        self.__gradebook.grade_policy = GradePolicy(assign_weight, test_weight, final_exam_weight, num_assignments, num_tests, num_final_exams)
        self.__grade_policy_repo.save(self.__gradebook.grade_policy)
        self.__student_repo.clear()
        self.__gradebook.students = []
        print("New semester setup completed. All previous data cleared.")

    def get_valid_input(self, prompt, min_val, max_val):
        while True:
            try:
                value = int(input(prompt))
                if min_val <= value <= max_val:
                    return value
                print(f"Value must be between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def get_valid_weights(self):
        while True:
            try:
                assign_weight = float(input("Enter the weight for assignments: "))
                test_weight = float(input("Enter the weight for tests: "))
                final_exam_weight = float(input("Enter the weight for the final exam: "))
                if assign_weight + test_weight + final_exam_weight == 100:
                    return assign_weight, test_weight, final_exam_weight
                print("Weights must sum to 100%. Please re-enter the values.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def add_student(self):
        try:
            student_id = int(input("Enter student ID (1-9999): "))
            if any(s.student_id == student_id for s in self.__gradebook.students):
                print("This student ID already exists. Please try a different one.")
                return
            if student_id < 1 or student_id > 9999:
                print("Student ID must be between 1 and 9999.")
                return

            first_name = input("Enter student's first name (max 20 chars): ").strip()
            last_name = input("Enter student's last name (max 20 chars): ").strip()

            if len(first_name) > 20 or len(last_name) > 20:
                print("Names must not exceed 20 characters.")
                return

            new_student = Student(student_id, first_name, last_name, self.__gradebook.grade_policy.num_assignments,
                                  self.__gradebook.grade_policy.num_tests)
            self.__gradebook.students.append(new_student)
            self.__student_repo.save(self.__gradebook.students)
            print("Student added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def record_grade(self, assessment_type: AssessmentType):
        self.__gradebook.grade_policy = self.__grade_policy_repo.load()

        max_count = {
            AssessmentType.ASSIGNMENT: self.__gradebook.grade_policy.num_assignments,
            AssessmentType.TEST: self.__gradebook.grade_policy.num_tests,
            AssessmentType.FINAL_EXAM: 1
        }[assessment_type]

        if max_count == 0:
            print(f"No {assessment_type.name.lower()}s are set up for this semester.")
            return

        if assessment_type != AssessmentType.FINAL_EXAM:
            try:
                index = int(input(f"Enter {assessment_type.name.lower()} number (1 to {max_count}): ")) - 1
                if not (0 <= index < max_count):
                    print(f"Invalid number. Please enter a number between 1 and {max_count}.")
                    return
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return
        else:
            index = 0

        for student in self.__gradebook.students:
            print(f"Student ID: {student.student_id}, Name: {student.first_name} {student.last_name}")
            try:
                grade = float(input(f"Enter grade for {assessment_type.name} {index + 1}: "))
                student.record_specific_grade(assessment_type, grade, index)
                print(f"Grade recorded for {student.first_name} {student.last_name}.")
            except ValueError:
                print("Invalid input for grade. Please enter a valid number.")
        self.__student_repo.save(self.__gradebook.students)

    def change_grade(self):
        try:
            student_id = int(input("Enter student ID: "))
            assessment_type_str = input(
                "Enter assessment type (P/T/F): ").upper()

            type_mapping = {
                'P': AssessmentType.ASSIGNMENT,
                'T': AssessmentType.TEST,
                'F': AssessmentType.FINAL_EXAM
            }

            if assessment_type_str not in type_mapping:
                print("Invalid assessment type.")
                return

            assessment_type = type_mapping[assessment_type_str]
            index = None

            if assessment_type == AssessmentType.ASSIGNMENT or assessment_type == AssessmentType.TEST:
                max_index = self.__gradebook.grade_policy.num_assignments if assessment_type == AssessmentType.ASSIGNMENT \
                    else self.__gradebook.grade_policy.num_tests
                index = int(input(f"Enter {assessment_type.name.lower()} number (1 to {max_index}): ")) - 1
                if not (0 <= index < max_index):
                    print(f"Invalid number | Please enter a number between 1 and {max_index}.")
                    return

            grade = float(input("Enter a new grade: "))
            student = next((s for s in self.__gradebook.students if s.student_id == student_id), None)

            if not student:
                print("Student not found.")
                return

            if assessment_type == AssessmentType.FINAL_EXAM:
                if student.final_exam:
                    student.final_exam.record_grade(grade)
                else:
                    print("No final exam recorded for this student.")
            else:
                if assessment_type == AssessmentType.ASSIGNMENT:
                    items = student.assignments
                else:
                    items = student.tests

                if len(items) > index:
                    items[index].record_grade(grade)
                else:
                    print(f"No {assessment_type.name.lower()} recorded at position {index + 1}.")

            self.__student_repo.save(self.__gradebook.students)
            print("Grade changed successfully.")

        except ValueError as e:
            print("Error processing the change. Please check your inputs and try again.", str(e))

    def calculate_final_grades(self):
        for student in self.__gradebook.students:
            final_grade = student.calculate_final_grade(self.__gradebook.grade_policy)
            print(f"Student ID: {student.student_id}, Name: {student.first_name} {student.last_name},"
                  f" final grade: {final_grade: .2f}")

    def sort_students_by_name(self, student):
        return student.last_name, student.first_name

    def sort_students_by_id(self, student):
        return student.student_id

    def output_grade_data(self):
        order = input("Output ordered by (N)ame or (I)D? (N/I): ").upper()
        if order == 'N':
            sorted_students = sorted(self.__gradebook.students, key=self.sort_students_by_name)
        else:
            sorted_students = sorted(self.__gradebook.students, key=self.sort_students_by_id)

        for student in sorted_students:
            assignment_grades = ', '.join(f"{a.grade:.2f}" for a in student.assignments if a.grade is not None)
            test_grades = ', '.join(f"{t.grade:.2f}" for t in student.tests if t.grade is not None)
            final_exam_grade = f"{student.final_exam.grade:.2f}" if student.final_exam and student.final_exam.grade is not None else "N/A"

            print(f"Student ID: {student.student_id}, Name: {student.first_name} {student.last_name}")
            print(f"Assignment Grades: {assignment_grades}")
            print(f"Test Grades: {test_grades}")
            print(f"Final Exam Grade: {final_exam_grade}")
            print(f"Final Grade: {student.calculate_final_grade(self.__gradebook.grade_policy):.2f}\n")

    def quit_application(self):
        self.__student_repo.save(self.__gradebook.students, "grades.dat")
        self.__grade_policy_repo.save(self.__gradebook.grade_policy, "policy.dat")
        print("Data saved. Application closed.")


def main():
    app = GradebookApp()
    app.main_menu()


if __name__ == "__main__":
    main()
