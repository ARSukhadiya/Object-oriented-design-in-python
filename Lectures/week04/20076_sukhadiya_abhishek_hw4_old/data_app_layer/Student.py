import random, string


class Student():
    def __init__(self, std_id: int, fname: str="", lname: str="", username=None, assignment_scores={}, test_scores={}, final_scores=None) -> None:
        self.__std_id: int = std_id
        self.__fname: str = fname
        self.__lname: str = lname
        self.__username: str = username or self.create_user()
        

        self.__assignment_scores: dict = assignment_scores     # {"<assi_id>"": <score>}
        self.__test_scores: dict = test_scores           # {"<test_id>"": <score>}
        self.__final_scores: int = final_scores         # {"<final_id>"": <score>}

    @property
    def std_id(self):
        return self.__std_id
    
    @property
    def fname(self):
        return self.__fname
    
    @property
    def lname(self):
        return self.__lname
    
    @property
    def username(self):
        return self.__username
    
    @property
    def assignment_scores(self):
        return self.__assignment_scores
    
    @property
    def test_scores(self):
        return self.__test_scores

    @property
    def final_scores(self):
        return self.__final_scores


    # def convert_to_list(self) -> list[str]:
    #     lst = []
    #     lst.append(self.__std_id)
    #     lst.append(self.__username)
    #     lst.append(self.__assignment_scores)
    #     lst.append(self.__test_scores)
    #     lst.append(self.__final_scores)
    #     return lst
    
    def create_user(self) -> None:
        postfix = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=7))
        self.__username = f"{self.__lname}_{self.__fname}_{postfix}"

    def __str__(self) -> str:
        # output = f"Student-id: {self.__std_id} | Username: {self.__username}"
        output = f"{self.__std_id}, {self.__username}, "
        
        if self.__assignment_scores:
            # output += " || "
            output += ", "
            for assi_id, score in self.__assignment_scores.items():
                output += f"{assi_id}: {score}, "
        
        if self.__test_scores:
            # output += " || "
            output += ", "
            for test_id, score in self.__test_scores.items():
                output += f"{test_id}: {score}, "

            
        if self.__final_scores:
            output += ", "
            output += f"{score}" 
           
        return output
    
    def __eq__(self, obj) -> bool:
        return isinstance(obj, Student) and self.__fname == obj.__fname and self.__lname == obj.__lname

    def add_assignment_score(self, ass_id, marks) -> bool:
        pass

    def update_assignment_score(self, ass_id, marks) -> bool:
        pass

    def add_test_score(self, test_id, marks) -> bool:
        pass

    def update_test_score(self, test_id, marks) -> bool:
        pass

    def calculate_final_grade(self) -> None:
        pass

    def display(self):
        print(self)




def main():
    pass


if __name__ == "__main__":
    main()
