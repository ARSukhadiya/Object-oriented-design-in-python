from student import GradePolicy, AssessmentType
from gradebook_repos import StudentRepository, GradePolicyRepository


class Gradebook:
    def __init__(self, grade_policy: GradePolicy):
        self.__policy_repo = GradePolicyRepository()
        self.__student_repo = StudentRepository()
        self.__grade_policy = grade_policy
        self.__students = []

    @property
    def policy_repo(self):
        return self.__policy_repo

    @policy_repo.setter
    def policy_repo(self, policy_repo: GradePolicyRepository):
        self.__policy_repo = policy_repo

    @property
    def student_repo(self):
        return self.__student_repo

    @student_repo.setter
    def student_repo(self, student_repo: StudentRepository):
        self.__student_repo = student_repo

    @property
    def grade_policy(self):
        return self.__grade_policy

    @grade_policy.setter
    def grade_policy(self, grade_policy: GradePolicy):
        self.__grade_policy = grade_policy

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        self.__students = students


    def calculate_final_grade(self, student_id: int):
        for student in self.__students:
            if student.student_id == student_id:
                return student.calculate_final_grade(self.__grade_policy)
        return None

    def __str__(self):
        return f"The gradebook with {len(self.__students)} students"

    def save_to_files(self):
        self.__student_repo.save(self.__students)
        self.__policy_repo.save(self.__grade_policy)

    def record_grade(self, student_id: int, assessment_type: AssessmentType, grade: float):
        for student in self.__students:
            if student.student_id == student_id:
                student.record_grade(assessment_type, grade, getattr(self.__grade_policy, f"{assessment_type.name.lower()}_weight"))
                break

    def load_from_files(self):
        self.__students = self.__student_repo.load()
        self.__grade_policy = self.__policy_repo.load()
