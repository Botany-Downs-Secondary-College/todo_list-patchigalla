#todo_list.py
#creates and displays To Do List
#P.Patchigalla, March 2020

# Create an empty list to store the tasks
todo_list = []
#name = ""

# Function that prints out the menu so the user knows what options there are and get user's choice
def menu():

    print("Hello")

    mode = input("""Choose a mode by entering the number:
    1: Add a task 2: View list 3: Exit :""")
    return mode

# Function that allows user to add a task to their to do list
def add_tasks():
    while True:
        new_task = input("Enter the task to add or type 'end' to return to menu: ").strip().lower()
        if new_task == "end":
            break
        else:            
            # If the user hasn't entered end, add their new task to the list
            todo_list.append(new_task)
            
# Function that shows current tasks in the To Do List
def view_list():
    for task in todo_list: #for loop repeats to print tasks in todo_list
        print(taks = 1,").",todo_list[task]





print("Welcome to To Do List programme")
name = input("What is your name? ")
print("Hello", name)

while True:
    
    chosen_option = menu()

    if chosen_option == "1":
        #Run the add_tasks function if the user chooses 1
        add_tasks()
        
    elif chosen_option == "2":
        print("Here is your To Do List:")
        view_list()
    elif chosen_option == "3":
        break
    else:
        print("That wasn't an option, please try again")

print("Goodbye!")
