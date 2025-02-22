from __future__ import annotations
from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)
from random import randrange


@acts_as_state_machine
class DriverLicenseApplicationProcess:
    # define states
    ready = State(initial=True)
    informationEntry = State()
    informationComplete = State()
    browseoffices = State()
    knowledgeTest = State()
    visionTest = State()
    drivingTest = State()
    applicationDenial = State()
    finalReview = State()
    issued = State()

    # Define transictions
    enter_information = Event(from_states=ready, to_state=informationEntry)
    cancel_application = Event(from_states=informationEntry, to_state=ready)
    
    submit_information = Event(from_states=informationEntry, to_state=informationComplete)
    select_dmv_office = Event(from_states=informationComplete, to_state=browseoffices)
    schedule_knowledge_test = Event(from_states=browseoffices, to_state=knowledgeTest)
    pass_knowledge_test = Event(from_states=knowledgeTest, to_state=visionTest)
    pass_vision_test = Event(from_states=visionTest, to_state=drivingTest)
    take_driving_test = Event(from_states=drivingTest, to_state=finalReview)
    approve_application = Event(from_states=finalReview, to_state=issued)
    deny_application = Event(from_states=(knowledgeTest, visionTest, finalReview), to_state=applicationDenial)
    try_again = Event(from_states=applicationDenial, to_state=ready)

    def __init__(self, dmv: DMV) -> None:
        self.dmv = dmv

    @after('take_driving_test')
    def after_take_driving_test(self):
        # Get a  random number
        test_mark = randrange(0, 100)
        if test_mark >= 60:
            print("Test marks:", test_mark)
            return True
        else:
            print("Test marks:", test_mark)
            return False


class DMV:
    def __init__(self) -> None:
        self.process = DriverLicenseApplicationProcess(self)
        self.applicant_fname = None
        self.applicant_lname = None
        self.applicant_dob = None
        self.applicant_address = None
        self.applicant_selected_dmv = None

    def enter_information(self, fname, lname, dob, address):
        self.applicant_fname = fname
        self.applicant_lname = lname
        self.applicant_dob = dob
        self.applicant_address = address
        self.process.enter_information()

    def cancel_application(self):
        self.process.cancel_application()

    def submit_information(self):
        self.process.submit_information()

    def select_dmv_office(self, dmv):
        self.applicant_selected_dmv = dmv
        self.process.select_dmv_office()

    def schedule_knowledge_test(self):
        self.process.schedule_knowledge_test()

    def pass_knowledge_test(self):
        self.process.pass_knowledge_test()

    def pass_vision_test(self):
        self.process.pass_vision_test()

    def take_driving_test(self):
        self.process.take_driving_test()

    def approve_application(self):
        self.process.approve_application()

    def deny_application(self):
        self.process.deny_application()

    def try_again(self):
        self.process.try_again()

    def get_current_process(self):
        return self.process.current_state


def show_menu():
    print("===MENU===")
    print("1. Enter applicant information")
    print("2. Cancel application")
    print("3. Submit infomation")
    print("4. Select DMV office")
    print("5. Schedule knowledge test")
    print("6. Pass knowledge test")
    print("7. Pass vision test")
    print("8. Take driving test")
    print("9. Approve application")
    print("10. Deny application")
    print("11. Try again")
    print("12. Exit")


def show_dmv_offices(DMV_offices):
    print("\nAvailable DMV offices")
    for id, name in DMV_offices.items():
        print(f"{id} - {name}")


def main():
    dmv = DMV()
    DMV_offices = {1: "Office 1", 2: "Office 2", 3: "Office 3", 4: "Office 4", 5: "Office 5"}
    
    while True:
        show_menu()
        try:
            option = int(input("Enter your option: "))
            if option == 1:
                fname = input("Enter firstname: ")
                lname = input("Enter lastname: ")
                dob = input("Enter DOB: ")
                address = input("Enter Address: ")
                dmv.enter_information(fname, lname, dob, address)

            elif option == 2:
                dmv.cancel_application()

            elif option == 3:
                dmv.submit_information()

            elif option == 4:
                while True:
                    show_dmv_offices(DMV_offices)
                    dmv_office = int(input("Enter your choice: "))
                    if dmv_office in DMV_offices:
                        break
                    print("DMV office selection is wrong!")

                selected_dmv = DMV_offices[dmv_office]
                dmv.select_dmv_office(selected_dmv)

            elif option == 5:
                dmv.schedule_knowledge_test()
            
            elif option == 6:
                dmv.pass_knowledge_test()
            
            elif option == 7:
                dmv.pass_vision_test()
            
            elif option == 8:
                dmv.take_driving_test()
            
            elif option == 9:
                dmv.approve_application()
            
            elif option == 10:
                dmv.deny_application()
            
            elif option == 11:
                dmv.try_again()
            
            else:
                break
            print(f"\nNow is in {dmv.get_current_process()} state\n")
        except ValueError as ex:
            print(f"Could not perform option {option} in {dmv.get_current_process()}")


if __name__ == "__main__":
    main()