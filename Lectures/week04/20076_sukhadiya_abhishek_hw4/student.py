from enum import Enum, auto
from typing import Optional
from abc import ABC


class AssessmentType(Enum):
    ASSIGNMENT = auto()
    TEST = auto()
    FINAL_EXAM = auto()


class Assessment(ABC):
    def __init__(self, weight: float, assessment_type: AssessmentType) -> None:
        self.__weight = weight
        self.__assessment_type = assessment_type
        self.__grade: Optional[float] = None

    @property
    def grade(self) -> Optional[float]:
        return self.__grade

    @grade.setter
    def grade(self, grade: Optional[float]) -> None:
        self.__grade = grade

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float) -> None:
        self.__weight = weight

    @property
    def assessment_type(self) -> AssessmentType:
        return self.__assessment_type

    @assessment_type.setter
    def assessment_type(self, assessment_type: AssessmentType) -> None:
        self.__assessment_type = assessment_type

    def record_grade(self, grade: float) -> None:
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.__assessment_type.name}: Weight - {self.__weight}, Grade - {self.__grade if self.__grade is not None else 'Not graded'}"


class Assignment(Assessment):
    def __init__(self, weight: float) -> None:
        super().__init__(weight, AssessmentType.ASSIGNMENT)


class Test(Assessment):
    def __init__(self, weight: float) -> None:
        super().__init__(weight, AssessmentType.TEST)


class FinalExam(Assessment):
    def __init__(self, weight: float) -> None:
        super().__init__(weight, AssessmentType.FINAL_EXAM)


class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, num_assignments: int, num_tests: int) -> None:
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__assignments = []

        for i in range(num_assignments):
            self.__assignments.append(Assignment(0))
        
        self.__tests = []
        for i in range(num_tests):
            self.__tests.append(Test(0))
        
        self.__final_exam = FinalExam(0)

    @property
    def student_id(self) -> int:
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id: int) -> None:
        self.__student_id = student_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self.__first_name = first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    @property
    def assignments(self):
        return self.__assignments

    @assignments.setter
    def assignments(self, assignments):
        self.__assignments = assignments

    @property
    def tests(self):
        return self.__tests

    @tests.setter
    def tests(self, tests):
        self.__tests = tests

    @property
    def final_exam(self) -> FinalExam:
        return self.__final_exam

    @final_exam.setter
    def final_exam(self, final_exam: FinalExam) -> None:
        self.__final_exam = final_exam

    def add_assignment(self, assignment: Assignment) -> None:
        self.__assignments.append(assignment)

    def add_test(self, test: Test) -> None:
        self.__tests.append(test)

    def set_final_exam(self, final_exam: FinalExam) -> None:
        self.__final_exam = final_exam

    def calculate_final_grade(self, grade_policy) -> float:
        total_weighted_score = 0.0
        total_weights = 0.0

        normalized_assignment_weight = grade_policy.assignment_weight / 100
        normalized_test_weight = grade_policy.test_weight / 100
        normalized_final_exam_weight = grade_policy.final_exam_weight / 100

        for assignment in self.__assignments:
            if assignment.grade is not None:
                total_weighted_score += assignment.grade * normalized_assignment_weight
                total_weights += normalized_assignment_weight

        for test in self.__tests:
            if test.grade is not None:
                total_weighted_score += test.grade * normalized_test_weight
                total_weights += normalized_test_weight

        if self.__final_exam and self.__final_exam.grade is not None:
            total_weighted_score += self.__final_exam.grade * normalized_final_exam_weight
            total_weights += normalized_final_exam_weight

        if total_weights > 0:
            return total_weighted_score / total_weights
        else:
            return 0.0

    def record_specific_grade(self, assessment_type: AssessmentType, grade: float, index: int):
        if assessment_type == AssessmentType.ASSIGNMENT:
            self.__assignments[index].record_grade(grade)
        elif assessment_type == AssessmentType.TEST:
            self.__tests[index].record_grade(grade)
        elif assessment_type == AssessmentType.FINAL_EXAM:
            self.__final_exam.record_grade(grade)

    def __str__(self) -> str:
        return f"Student-ID: {self.__student_id}, Name: {self.__first_name} {self.__last_name}"


class GradePolicy:
    def __init__(self, assign_weight: float, test_weight: float, final_exam_weight: float, num_assignments=0,
                 num_tests=0, num_final_exams=0):
        self.__num_assignments = num_assignments
        self.__num_tests = num_tests
        self.__num_final_exams = num_final_exams
        self.__assign_weight = assign_weight
        self.__test_weight = test_weight
        self.__final_exam_weight = final_exam_weight

    @property
    def num_assignments(self) -> int:
        return self.__num_assignments

    @num_assignments.setter
    def num_assignments(self, num_assignments: int) -> None:
        self.__num_assignments = num_assignments
        
    @property
    def num_tests(self) -> int:
        return self.__num_tests

    @num_tests.setter
    def num_tests(self, num_tests: int) -> None:
        self.__num_tests = num_tests

    @property
    def assignment_weight(self) -> float:
        return self.__assign_weight

    @assignment_weight.setter
    def assignment_weight(self, assignment_weight: float) -> None:
        self.__assign_weight = assignment_weight

    @property
    def final_exam_weight(self) -> float:
        return self.__final_exam_weight

    @final_exam_weight.setter
    def final_exam_weight(self, final_exam_weight: float) -> None:
        self.__final_exam_weight = final_exam_weight

    @property
    def num_final_exams(self) -> int:
        return self.__num_final_exams

    @num_final_exams.setter
    def num_final_exams(self, num_final_exams: int) -> None:
        self.__num_final_exams = num_final_exams

    @property
    def test_weight(self) -> float:
        return self.__test_weight

    @test_weight.setter
    def test_weight(self, test_weight: float) -> None:
        self.__test_weight = test_weight
