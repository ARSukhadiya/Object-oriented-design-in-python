from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)

@acts_as_state_machine
class DriverLicenseApplicationProcess:
    #define 7 states
    ready = State(initial=True)
    informationEntry = State()
    informationComplete = State()
    browseOffice = State()
    knowledgeTest = State()
    visionTest = State()
    drivingTest = State()
    finalReview = State()
    issued = State()
    drivingTest = State()
    applicationDenial =State()

    # define transitions (events)
    enter_information = Event(from_states=(ready), to_state=informationEntry)
    submit_information = Event(from_states=(informationEntry), to_state=informationComplete)
    cancle_application = Event(from_states=(informationEntry), to_state=ready)
    select_DMV_office = Event(from_states=(informationComplete), to_state=browseOffice)
    schedule_knowledge_test = Event(from_states=(browseOffice), to_state=knowledgeTest)
    pass_knowledge_test = Event(from_states=(knowledgeTest), to_state=visionTest)
    deny_applicaton = Event(from_states=(knowledgeTest, visionTest,finalReview), to_state=applicationDenial)
    pass_vision_test = Event(from_states=(visionTest), to_state=drivingTest)
    take_driving_test = Event(from_states=drivingTest, to_state=finalReview)
    approve_application = Event(from_states=finalReview, to_state=issued)
    try_again = Event(from_states=(applicationDenial), to_state=ready)


class DMV:
    def _init_(self):
        self.application_process = DriverLicenseApplicationProcess()

    @before("Start application")
    def enter_information(self, fname, lname, dob, address):
        print("Entering information entry")
        # Accessing attributes from the constructor
        self.applicant_fname = fname
        self.applicant_lname = lname
        self.applicant_dob = dob
        self.applicant_address = address
        self.process.enter_information()        
        self.application_process.enter_information()
        
    @after("Information Submitted")
    def submit_information(self):
        print("Entering information complete")
        self.application_process.submit_information()

    def select_DMV_office(self):
        print("Browse and select DMV office")
        self.application_process.select_DMV_office()

    def schedule_knowledge_test(self):
        print("Knowledge test scheduled")
        self.application_process.schedule_knowledge_test()

    
    def pass_knowledge_test(self):
        print("knowledge test passed")
        self.application_process.pass_knowledge_test()

    def deny_applicaton(self):
        print("Knowledge test fail application denied")
        self.application_process.deny_applicaton()

    def pass_vision_test(self):
        print("Vision test passed.")
        self.application_process.pass_vision_test()

    def take_driving_test(self):
        print("Take driving test")
        self.application_process.take_driving_test()

    def approve_application(self):
        print("Driving test passed! Application approved")
        self.application_process.approve_application()

    def try_again(self):
        print("Application denied, try again")
        self.application_process.try_again()

    def cancle_application(self):
        print("Enter application details again")
        self.application_process.cancle_application()

    def get_current_state(self):
        return self.process.current_state

    def after_state_transition(self, event, from_state, to_state):
        print(f"Transitioned from {from_state.name} to {to_state.name} via {event.name}")


    # def process_application(self):
    #     try:
    #         self.application_process.enter_information()
    #         self.application_process.submit_information()
    #         self.application_process.select_DMV_office()
    #         self.application_process.schedule_knowledge_test()
    #         self.application_process.pass_knowledge_test()
    #         self.application_process.pass_vision_test()
    #         self.application_process.take_driving_test()
    #         self.application_process.approve_application()
    #     except InvalidStateTransition as e:
    #         print(f"Invalid transition: {e}")

def show_menu():
    print("Driver's License Application Process:")
    print("1. Start Application Process, Enter Information: ")
    print("2. Submit Information")
    print("3. Select DMV Office")
    print("4. Schedule Knowledge Test")
    print("5. Knowledge test passed")
    print("6. Applicaton denied")
    print("7. Vision test passed")
    print("8. Take driving test")
    print("9. Approve application")
    print("10. Try Again")
    print("11. Cancle application")
    print("12. Exit")
    
def main():
    dmv = DMV()

    while True:
        show_menu()
        try:
            option = input("Enter your option: ")
            if option == "1":
                firstName = input("Enter your first name: ")
                lastName = input("Enter your last name: ")
                DOB = input("Enter your DOB: ")
                address = input("Enter your address: ")
                dmv.enter_information(firstName, lastName, DOB, address)
            elif option == "2":
                dmv.application_process.submit_information()
            elif option == "3":
                dmv.application_process.select_DMV_office()
            elif option == "4":
                dmv.application_process.schedule_knowledge_test()
            elif option == "5":
                dmv.application_process.pass_knowledge_test()
            elif option == "6":
                dmv.application_process.deny_applicaton()
            elif option == "7":
                dmv.application_process.pass_vision_test()
            elif option == "8":
                dmv.application_process.take_driving_test()
            elif option == "9":
                dmv.application_process.approve_application()
            elif option == "10":
                dmv.application_process.try_again()
            elif option == "11":
                dmv.application_process.cancle_application()
            elif option == "12":
                print("Exiting")
                break
            else: 
                print("Invalid choice. Please choose again.")
        except InvalidStateTransition as ex:
            print(f"Could not perform option {option} in {dmv.get_current_state()} state")


if __name__ == "__main__":
    main()
