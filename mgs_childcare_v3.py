"""Program for a child day-care centre to keep track of children throughout
the day - v3
Choice 2 - pick up a child
Created By Jeongmin Kim
"""

def dropOff():
    name_dropOff = input("Enter child's name: ")
    child_list = [name_dropOff].append(name_dropOff)
    print(f"{name_dropOff} is added to our list. Thank you")
    print()

def pickUp()
    name_pickUp = input("Enter child's name: ")
    child_list = [name_pickUp]

# Main routine
choice = 0
while choice != 5:
    print("************************************************************")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("************************************************************")
    print()
    print("1. Drop off a child")
    print("2. Pick up a child")
    print("3. Calculate cost")
    print("4. Print roll")
    print("5. Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        dropOff()

    elif choice == 2:
        pickUp()