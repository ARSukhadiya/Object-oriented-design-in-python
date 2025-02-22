from applicantion import Application, Applicant, EmergencyContact, Education, WorkExperience

def menu():
    print("\n\n---Manage Application---")
    print("1 - Add")
    print("2 - Search")
    print("3 - Update")
    print("4 - Delete")
    print("5 - Display")


def get_applicant_values():
    print("\nPlease Enter applicant details:")
    
    lname = input("Last-name:")
    fname = input("First-name:")
    mname = input("Middle-name:")
    dob = input("Date of Birth:")
    position = input("Position Applying:")
    addr = input("Address:")
    contact_home = input("Telephone(Home):")
    contact_mob = input("Telephone(Mobile):")
    email = input("Email address:")
    birthplace = input("Place of Birth:")
    citizenship = input("Citizenship:")
    major_skills = []
    while True:
        major_skills.append(input("Skill:"))
        option = input("Want to add other skill(y/n):")
        if option == 'y':
            continue
        else:
            break

    applicant_details = {"lname": lname, "fname": fname, "mname": mname, "dob": dob, "position": position, "addr": addr, "contact_home": contact_home,
                         "contact_mob": contact_mob, "email": email, "birthplace": birthplace, "citizenship": citizenship, "major_skills": major_skills}

    return applicant_details


def get_emergency_contacts():
    print("\nPlease Enter Emergency-contact details:")

    def get_detail():
        relationship = input("Relationship:")
        lname = input("Last-name:")
        fname = input("First-name:")
        mname = input("Middle-name:")
        contact_mob = input("Contact Number:")
        return relationship, lname, fname, mname, contact_mob

    emer_contacts = []
    print("Enter Primary contact details:")
    type = "Primary"
    relationship, lname, fname, mname, contact_mob = get_detail()
    emer_contacts.append([type, relationship, lname, fname, mname, contact_mob])
    
    print("Enter Secondary contact details:")
    type = "Secondary"
    relationship, lname, fname, mname, contact_mob = get_detail()
    emer_contacts.append([type, relationship, lname, fname, mname, contact_mob])
    
    return emer_contacts

def get_educations():
    print("\nPlease Enter Education details:")
    education_details = []

    while True:
        level = input("Education level:")
        school_name = input("School-name:")
        from_yr = input("From (year):")
        to_yr = input("To (year):")
        degree = input("Degree:")
        
        education_details.append([level, school_name, from_yr, to_yr, degree])
        if input("Do you want to add other education (y/n):") != "y":
            break

    return education_details


def get_experiences():
    print("\nPlease Enter Experience details:")
    experience_details = []

    for _ in range(3):    
        company_name = input("Company name:")
        address = input("Company address:")
        from_yr = input("From (year):")
        to_yr = input("To (year):")
        position = input("Position:")
        reason = input("Reason for leaving:")
        
        experience_details.append([company_name, address, from_yr, to_yr, position, reason])
        if input("Do you want to add other experience (y/n):") != "y":
            break   
        
    return experience_details


def main():

    company = "Telconnect Solutions"
    company_addr = "2002, Frederemp Commercial, Dermy, CA"
    application_no = 100

    app = Application(application_no+1, company, company_addr)

    while True:
        menu()
        option = int(input("Enter an option (from 1 to 5) to perform operation:"))
 
        if option == 1:                     # Add
            applicant_details = get_applicant_values()
            
            apt1 = Applicant(**applicant_details)
            for contact in get_emergency_contacts(): 
                emer_contact = EmergencyContact(contact[0], contact[1], contact[2], contact[3], contact[4], contact[5])
                apt1.add_emergency_contact(emer_contact)

            for edu in get_educations():
                apt1.add_education(Education(edu[0], edu[1], edu[2], edu[3], edu[4]))
            
            for exp in get_experiences():
                apt1.add_work_experience(WorkExperience(exp[0], exp[1], exp[2], exp[3], exp[4], exp[5]))

            app.add_applicant(apt1)
        
        elif option == 2:                   # Search
            while True:
                search_fname = input("Please enter applicant's first-name to search:")
                found_app = app.search_app_by_name(search_fname)
                if not found_app:
                    print("\nError: name not found!")
                    continue
                else:
                    print('\nApplicant found:')
                    print(found_app)
                    break

        elif option == 3:                   # Update
            update_applicant = input("Enter the applicant's first-name to update details of:")

            while True:
                print("---Options to update---")
                print("1 - Address")
                print("2 - Telephone (Home)")
                print("3 - Telephone (Mobile)")
                update_option = int(input("Enter the option to update (from 1 to 3): "))

                if update_option == 1:
                    new_addr = input("Enter address to update: ")
                    if app.update_app_by_name(fname=update_applicant, address=new_addr) == False:
                        print("Error! Something went wrong with updation!")
                elif update_option == 2:
                    new_contact_home = input("Enter new Telephone(Home) to update: ")
                    if app.update_app_by_name(fname=update_applicant, contact_home=new_contact_home) == False:
                        print("Error! Something went wrong with updation!")
                elif update_option == 3:
                    new_contact_mob = input("Enter new Telephone(Mobile) to update: ")
                    if app.update_app_by_name(fname=update_applicant, contact_mob=new_contact_mob) == False:
                        print("Error! Something went wrong with updation!")
                else:
                    print("Error! Invalid option (not from 1 to 3)!")
                    continue
                break

        elif option == 4:                   # Delete
            while True:
                remove_fname = input("Please enter applicant's first-name to remove:")

                if not app.remove_app_by_name(remove_fname):
                    print("Something went wrong!")
                    continue
                else:
                    print("Applicant has been deleted!")
                    break
        
        elif option == 5:
            app.display()
        else:
            print("Error: Invalid option (not from 1 to 5)!")
            continue

if __name__ == "__main__":    
    main()
