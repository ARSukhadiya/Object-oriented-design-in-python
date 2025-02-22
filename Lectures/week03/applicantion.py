class Person:
    def __init__(self, lname: str, fname: str, mname: str, contact_mob: str, dob: str="", addr: str="", 
                 contact_home: str="", email: str="", birthplace: str="", citizenship:str="") -> None:
        self.name = lname + ", " + fname + " " + mname
        self.__fname = fname
        self.__lname = lname
        self.__mname = mname
        self.__dob = dob
        self.__birthplace = birthplace
        self.__addr = addr
        self.email = email
        self.__contact_home = contact_home
        self.contact_mob = contact_mob
        self.__citizenship = citizenship

    def __str__(self) -> str:
        return f" Name = {self.name} | Date of Birth = {self.__dob} | Place of Birth = {self.__birthplace} | Address= {self.__addr} | Email = {self.email} | Contact(Home) = {self.__contact_home} | Contact(Mobile) = {self.contact_mob} | Citizenship = {self.__citizenship}\n"

    def __repr__(self) -> str:
        return str(self)

    @property
    def fname(self) -> str:
        return self.__fname
    
    @property
    def addr(self) -> str:
        return self.__addr
    
    @addr.setter
    def addr(self, addr: str) -> None:
        self.__addr = addr

    @property
    def contact_home(self) -> str:
        return self.__contact_home
    
    @contact_home.setter
    def contact_home(self, contact_home) -> None:
        self.__contact_home = contact_home

    def display(self) -> None:
        print(self)


class EmergencyContact(Person):
    def __init__(self, type: str, relationship: str, lname: str, fname: str, mname: str, contact_mob: str) -> None:
        super().__init__(lname=lname, fname=fname, mname=mname, contact_mob=contact_mob)
        self.__type = type  # Primary / Secondary
        self.__relationship = relationship

    def __str__(self) -> str:
        return f"Type = {self.__type}\n Name = {self.name}\n Relationship = {self.__relationship}\n Contact-Mobile = {self.contact_mob}\n"

    def __repr__(self) -> str:
        return str(self)

    def display(self) -> None:
        print(self)


class Education:
    def __init__(self, level: str, school_name: str, from_yr: int, to_yr: int, degree: str) -> None:
        self.__level = level
        self.__school_name = school_name
        self.__from_yr = from_yr
        self.__to_yr = to_yr
        self.degree = degree

    def __str__(self) -> str:
        return f" Level = {self.__level}\n SchoolName = {self.__school_name}\n From '{self.__from_yr}' | To '{self.__to_yr}'\n Degree = {self.degree}\n"

    def __repr__(self) -> str:
        return str(self)

    def display(self) -> None:
        print(self)


class WorkExperience:
    def __init__(self, company_name: str, company_addr: str, from_yr: int, to_yr: int, 
                 position: str, leaving_reason: str) -> None:
        self.__company_name = company_name
        self.__company_addr = company_addr
        self.__from_yr = from_yr
        self.__to_yr = to_yr
        self.__position = position
        self.__leaving_reason = leaving_reason

    def __str__(self) -> str:
        return f" CompanyName = {self.__company_name}\n CompanyAddress = {self.__company_addr}\n From '{self.__from_yr}' | To '{self.__to_yr}'\n Position = {self.__position}\n LeavingReason = {self.__leaving_reason}\n"

    def __repr__(self) -> str:
        return str(self)

    def display(self) -> None:
        print(self)


class Applicant(Person):
    def __init__(self, position: str, major_skills: str, lname: str, fname: str, mname: str, dob: str, addr: str, 
                 contact_home: str, contact_mob: str, email: str, birthplace: str, citizenship: str) -> None:
        super().__init__(lname=lname, fname=fname, mname=mname, dob=dob, addr=addr, contact_home=contact_home, contact_mob=contact_mob, email=email, birthplace=birthplace, citizenship=citizenship)
        self.__position = position
        self.__major_skills = major_skills
        self.educations: list[Education] = []
        self.__emer_contacts: list[EmergencyContact] = []
        self.__work_experience_list: list[WorkExperience] = []

    def __str__(self) -> str:
        result = super().__str__()
        result += f" Position Applying = {self.__position}\n Major Skills = {self.__major_skills}\n\n"
        
        for contact in self.__emer_contacts:
            result += str(contact) + "\n\n"

        for education in self.educations:
            result += str(education) + "\n\n"

        for work_experience in self.__work_experience_list:
            result += str(work_experience) + "\n\n"

        return result 

    def __repr__(self) -> str:
        return str(self)

    def add_emergency_contact(self, contact: EmergencyContact) -> None:
        self.__emer_contacts.append(contact)

    def add_education(self, education: Education) -> None:
        self.educations.append(education)
        
    def add_work_experience(self, work_experience: WorkExperience) -> None:
        self.__work_experience_list.append(work_experience)

    def display(self) -> None:
        print(self)


class Application:
    def __init__(self, app_id: int, company_name: str, company_addr: str) -> None:
        self.__app_id = app_id
        self.__company_name = company_name
        self.__company_addr = company_addr
        self.__applicants: list[Applicant] = []

    def __str__(self) -> str:
        result = f"Application ID = {self.__app_id}\n Company Name = {self.__company_name}\n Company Address = {self.__company_addr}\n\n"
        
        for applicant in self.__applicants:
            result += str(applicant) + "\n\n"
        
        return result

    def __repr__(self) -> str:
        return str(self)

    def add_applicant(self, applicant: Applicant) -> None:
        self.__applicants.append(applicant)
        print("\nApplicant added successfully!\n")

    def search_app_by_name(self, fname) -> Applicant:
        for applicant in self.__applicants:
            if applicant.fname == fname:
                return applicant

    def update_app_by_name(self, fname, address="", contact_home="", contact_mob="") -> bool:
        updated = False

        for applicant in self.__applicants:
            if applicant.fname == fname:
                if address:
                    applicant.addr = address
                    updated = True
                    print("\nApplicant updated successfully!\n")
                if contact_home:
                    applicant.contact_home = contact_home
                    updated = True
                    print("\nApplicant updated successfully!\n")
                if contact_mob:
                    applicant.contact_mob = contact_mob
                    updated = True
                    print("\nApplicant updated successfully!\n")
        return updated
    
    def remove_app_by_name(self, fname) -> bool:
        removed = False
        for i in range(len(self.__applicants)):
            if self.__applicants[i].fname == fname:
                self.__applicants.pop(i)
                removed = True
        
        return removed

    def display(self) -> None:
        print(self)
