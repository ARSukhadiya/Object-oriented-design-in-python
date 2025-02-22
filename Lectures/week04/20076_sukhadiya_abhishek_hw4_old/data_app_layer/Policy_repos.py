from GradePolicy import GradePolicy


class GradesPolicyRepository:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def save_grades(self, GradePolicies: list[GradePolicy]):
        with open(self.__filename, 'w', newline='') as file:
            for GradePolicy in GradePolicies:
                file.write(str(GradePolicy) + "\n")

    def read_grades(self) -> list:
        students = []
        with open(self.__filename, 'r', newline='') as file:
            for row in file.readlines():
                print(row)
        return students


def main():
    policy1 = GradePolicy(assignments_weight=25, test_weight=25, final_exam_weight=50)
    policy2 = GradePolicy(assignments_weight=35, test_weight=35, final_exam_weight=30)

    policies: list[GradePolicy] = []
    policies.append(policy1)
    policies.append(policy2)

    repos = GradesPolicyRepository("policy.dat")
    repos.save_grades(policies)

    policies2 = repos.read_grades()
    for policy in policies2:
        print(policy)


if __name__ == "__main__":
    main()
