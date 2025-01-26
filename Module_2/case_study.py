# Evans Ayensu Donkor     ---    01/25/2025
# case_study.py    ---    Module 2 Case Study: if...else and while
# The purpose of this assignment is to apply your knowledge and skill
# in coding if...else and while statements in Python. 

# Problem: A program that asks the user to enter their last name, first name, and GPA.
# The program store this information in a list. The program continue to ask
# the user for this information until the user enters ZZZ for the last name. The program 
# then display the list of students who have made the Dean's List (GPA >= 3.5) and the Honor Roll
# (GPA >= 3.25). 
# Last Name    First Name    GPA
# Smith        John          3.4
# Jones        Mary          3.8
# Johnson      Mark          2.9
# Ayensu Donkor Evans         3.9
# Cloud        John          3.6
# 
# ZZZ

def get_student_classification(gpa):               # Function to determine student's classification
    if gpa >= 3.5:
        return "Dean's List"
    elif gpa >= 3.25:
        return "Honor Roll"
    return None

def main():
    SENTINEL = "ZZZ"
    students = []
    
    while True:                                # Loop to get student information
        last_name = input("Enter last name (or ZZZ to finish): ")
        if last_name == SENTINEL:
            break
        
        first_name = input("Enter first name: ")
        try:                                            # Try block to handle invalid GPA input
            gpa = float(input("Enter GPA: "))
        except ValueError:                              # Except block to handle invalid GPA input
            print("Invalid GPA. Please enter a number.")
            continue
        
        classification = get_student_classification(gpa)
        students.append({                             # Append student information to the list  
            'last_name': last_name,
            'first_name': first_name,
            'gpa': gpa,
            'classification': classification
        })
    
    print("\n--- Student Results ---")              # Print student results
    for student in students:
        if student['classification']:
            print(f"{student['last_name']}, {student['first_name']} ({student['gpa']:.2f}) - {student['classification']}")




if __name__ == "__main__":
    main()