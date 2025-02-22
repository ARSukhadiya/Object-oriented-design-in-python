from typing import Optional

class Person:
    def __init__(self, name=None) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name) -> None:
        self.__name = name

    def __eq__(self, __value: object) -> bool:
        return self.__name == __value.name
    
    def __str__(self) -> str:
        return f"name = {self.__name}\n"
    
    def __repr__(self) -> str:
        return str(self)

    def display(self) -> None:
        print(self)

    def dowork(self) -> None:
        pass


class Programmer(Person):
    def __init__(self, name: str, skills: str, salary: float) -> None:
        super().__init__(name)
        self.__skills = skills
        self.__salary = salary

    @property
    def skills(self) -> str:
        return self.__skills
    
    @skills.setter
    def skills(self, skills) -> None:
        self.__skills = skills

    @property
    def salary(self) -> float:
        return self.__salary
    
    @salary.setter
    def salary(self, salary) -> None:
        self.__salary = salary

    def __str__(self) -> str:
        return str(super().__str__()) + f"skills = {self.__skills}\nsalary = {self.__salary}\n"
 
    def __repr__(self) -> str:
        return str(self)

    def display(self) -> None:
        print(self)
    
    def get_annual_income(self) -> float:
        return self.__salary * 12
    
    def dowork(self) -> None:
        print(f"Programmer - {super().name} is writing a program.")


class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus: float) -> None:
        super().__init__(name, skills, salary)
        self.__bonus = bonus

    @property
    def bonus(self) -> float:
        return self.__bonus
    
    @bonus.setter
    def bonus(self, bonus) -> None:
        self.__bonus = bonus

    def __str__(self) -> str:
        return super().__str__() + f"bonus = {self.__bonus}\n"
    
    def __repr__(self) -> str:
        return str(self)

    def display(self) -> None:
        print(self)
    
    def dowork(self) -> None:
        print(f"Manager {self.name} is supervising a team of programmers.")
    
    def get_annual_income(self) -> float:
        return super().get_annual_income() + self.__bonus


class Project:
    def __init__(self, projname: str, budget: float = 0.0, active: bool = False) -> None:
        self.__projname = projname
        self.__budget = budget
        self.__active = active

    @property
    def budget(self) -> float:
        return self.__budget
    
    @property
    def active(self) -> bool:
        return self.__active
    
    def __str__(self) -> str:
        return f"projname = {self.__projname}\nbudget = {self.__budget}\nactive = {self.__active}\n"

    def __repr__(self) -> str:
        return str(self)
    
    def display(self) -> None:
        print(self)

class Group:
    def __init__(self, groupname: str) -> None:
        self.__groupname = groupname
        self.__members: list[Programmer] = []

    def __str__(self) -> str:
        res = "The group has these members: \n"
        for member in self.__members:
            res += str(member) + "\n"

        return res
    
    def add_member(self, member: Programmer) -> None:
        if member not in self.__members:
            self.__members.append(member)

    def remove_member(self, name: str) -> None:
        for i in range(len(self.__members)):
            if self.__members[i].name == name:
               self.__members.pop(i)

    def ask_anyone_dowork(self) -> None:
        for member in self.__members:
            member.dowork()


    def ask_manager_dowork(self) -> None:
        for member in self.__members:
            if isinstance(member, Manager):
                member.dowork()


    def get_allMembers_morethan(self, income: float) -> list[Programmer]:
        members: list[Programmer] = []
        for member in self.__members:
            if member.get_annual_income() > income:
                members.append(member)

        return members
    
    def get_largest_member(self) -> Optional[Programmer]:
        big_member: Optional[Programmer] = None
        for member in self.__members:
            if big_member is None or member.get_annual_income() > big_member.get_annual_income():
                big_member = member
        return big_member

    def display(self) -> None:
        print(self)


class ITGroup(Group):
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname)
        self.__projects: list[Project] = []

    def __str__(self) -> str:
        res = super().__str__() + "The group has these projects: \n"
        for project in self.__projects:
            res += str(project) + "\n"

        return res + "\n"
        
    def add_project(self, project: Project) -> None:
        self.__projects.append(project)

    def find_largest_project(self) -> Optional[Project]:
        if len(self.__projects) == 0:
            print("No projects found!")
            return None
        
        mx_project = self.__projects[0]
        for project in self.__projects:
            if project.budget > mx_project.budget:
                mx_project = project

        return mx_project

    def display(self) -> None:
        return super().display()
    
    def get_active_projects(self) -> list[Project]:
        projects: list[Project] = []

        for project in self.__projects:
            if project.active:
                projects.append(project)

        return projects


def main():
    p1: Programmer = Programmer("Lily", "C++, Java", 10000)
    p2: Programmer = Programmer("Judy", "Python, Java", 18000)
    m: Manager = Manager("Peter", "Management", 20000, 20000)
    proj1: Project = Project("MAX-5", 200000, True)
    proj2: Project = Project("FOX-4", 100000, False)
    proj3: Project = Project("FOX-XP", 500000, True)

    itgrp: ITGroup = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)
    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)
    itgrp.display()

    p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
    itgrp.add_member(p3)
    itgrp.ask_anyone_dowork()
    print()
    itgrp.ask_manager_dowork()
    
    print("\nGet the largest project...")
    maxProj: Optional[Project] = itgrp.find_largest_project()
    if maxProj is not None:
        maxProj.display()
    
    print("\nGet the acive projects...")
    projects: list[Project] = itgrp.get_active_projects()
    for proj in projects:
        proj.display()
        print()

    itgrp.display()
    itgrp.remove_member(p3.name)    
    
    print("\nGet the members with high income...")
    members: list[Programmer] = itgrp.get_allMembers_morethan(200000)
    for member in members:
        member.display()
        print()


if __name__ == "__main__":
    main()