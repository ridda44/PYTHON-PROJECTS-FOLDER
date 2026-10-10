import json
import os
applications = []
if os.path.exists("applications.json"):
    try:
     with open("applications.json", "r") as file:
        applications = json.load(file)
    except json.JSONDecodeError:
        print("Error reading applications.json. Starting with an empty list.")
print("________Welcome to the Job Application Trackor!__________")
print("Please fill in the following information for your job application:")

def display_appl(application):
    print("\n--- Job Application ---")
    print(f"Company Name: {application['company']}")
    print(f"Position: {application['position']}")   
    print(f"Salary: {application['salary']}")
    print(f"Location: {application['location']}")   
    print(f"Contact Information: {application['contact_info']}")
    print(f"Working Time: {application['working_time']}")   
    print(f"Company Review: {application['company_review']}")
    print(f"Introduction: {application['introduction']}")       
    print(f"Merits: {application['merits']}")
    print(f"Demerits: {application['demerits']}")
    print(f"Distance from Home: {application['distance_from_home']} km")
    print(f"Interview Date: {application['interview_date']}")
    print(f"Interview Time: {application['interview_time']}")
    print(f"Application Status: {application['status']}")
    print("------------------------")
def save_applications():
    with open("applications.json", "w") as file:
        json.dump(applications, file, indent=4)
def add_application():
 while True:
   
    application = {
    "company": input("Company Name: "),
    "position": input("Position: "),
    "salary": input("Salary: "),
    "location": input("Location: "),
    "contact_info": input("Contact Information: "),
    "working_time": input("Working Time: "),
    "company_review": input("Company Review: "),
    "introduction": input("Introduction: "),
    "merits": input("Merits: "),
    "demerits": input("Demerits: "),
    "distance_from_home": input("Distance from Home (in km): "),
    "interview_date": input("Interview Date: "),
    "interview_time": input("Interview Time: "),
    "status": input("Application Status: "),
}
    applications.append(application)
    save_applications()
    print("\nThank you for submitting your job application!")
    more_applications = input("Would you like to submit another application? (yes/no): ").strip().lower()
    if more_applications != "yes":
        break


def search_company():
    search = input("\nEnter the company name to search for: ").strip()
    found = False
    for application in applications:
     if search.lower() == application['company'].lower():
        found = True
        display_appl(application)
        break

    if not found:
     print("No application found for that company.")

def delete_application():
  del_application=input("what company do you want to delete :")
  found=False
  for application in applications:
    if del_application.lower() == application['company'].lower():
        applications.remove(application)
        save_applications() 
        print(f"Application for {del_application} has been deleted.")
        found=True
        break
  if not found:
    print("No application found for that company.")
def update_salary():
  print("UPDATE SALARY FUNCTION STARTED")
  update_sal=input("what company do you want to update salary :").strip().casefold()
    
  found=False
  for application in applications:
    if update_sal == application['company'].strip().casefold():
        new_salary = input("Enter the new salary: ")
        application['salary'] = new_salary
        print(f"Salary for {update_sal} has been updated to {new_salary}.")
        found=True
        save_applications()
        break
  if not found:
        print("No application found for that company to update salary.")
  
def update_status():
  update_stat=input("what company do you want to update status :").strip().casefold()
  found=False
  for application in applications:
    if update_stat == application['company'].strip().casefold():
        new_status = input("Enter the new status: ")
        application['status'] = new_status
        print(f"Status for {update_stat} has been updated to {new_status}.")
        found=True
        save_applications()
        break
  if not found:
    print("No application found for that company to update status.")
  
while True:
    print("\n--- Job Application Tracker ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Search application")
    print("4. Delete application")
    print("5. Update salary")
    print("6. Update status")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_application()
    elif choice == "2":
        if len(applications) == 0:
            print("No applications have been added yet.")
        else:
            for application in applications:
                display_appl(application)
    elif choice == "3":
        search_company()
    elif choice =="4":
        delete_application()
    elif choice =="5":
        update_salary()
    elif choice =="6":
        update_status() 
    elif choice == "7":
        print("Exiting the Job Application Tracker. Goodbye!")
        break
    else:
     print("Invalid choice. Please enter a number from 1 to 7.") 