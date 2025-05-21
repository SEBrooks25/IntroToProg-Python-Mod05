# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sophia Brooks,05/21/2025, Edited Script
# ------------------------------------------------------------------------------------------ #
#to work with json files

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = []  # one row of student data (Change: Changed this to a Dictionary)
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError:
    print(f"Note: '{FILE_NAME}' not found. Starting with empty data.")
except json.JSONDecodeError:
    print(f"Warning: '{FILE_NAME}' is empty or invalid. Starting with empty data.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

# Present and Process the data; main loop
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
            course_name = input("Please enter the name of the course: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        if not students:
            print("No registrations found.")
        else:
            print("-" * 50)
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
            print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Please only choose option 1, 2, 3, or 4.")

print("Program Ended")
