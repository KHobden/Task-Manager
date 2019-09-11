#Task Management System
#Kieran Hobden
#29-Aug-'19

import datetime



#Class for all tasks
class Task:

    #Initialise properties, asigning basic details to the task
    def __init__(self, title, details, date_to_complete, status=False):
        self.title = title
        self.details = details
        self.date_to_complete = date_to_complete
        self.status = status

    #Prints the entirety of a given task
    def print_task(self):
        print("==============")
        print("Title:", self.title)
        print("Details:", self.details)
        print("To complete by:", self.date_to_complete)
        print("Completed:", self.status)
        print("==============")


    
#Array to contain all tasks for organisation/ sorting etc.
tasks = []

#Adding or deleting given tasks
def add_task(input_title, input_details, input_date_to_complete):
    new_task = Task(title=input_title, details=input_details, date_to_complete=input_date_to_complete)
    tasks.append(new_task)

def del_task(delete_title):
    for i in tasks:
        if i.title.lower() == delete_title.lower():
            tasks.remove(i)

#Alternates the status of a task given a task title
def change_status(change_title):
    for i in tasks:
        if i.title.lower() == change_title.lower():
            if i.status == True:
                i.status = False
            else:
                i.status = True

#Print all tasks using print_task function
def print_all_tasks(tasks):
    for i in tasks:
        i.print_task()

#Sort tasks, organising by given properties then comparing to unsorted list and appending objects to a new sorted list    
def sorting(unsorted_list, sorted_list):
    sorted_tasks = []
    for i in range(len(sorted_list)):
        for j in range(len(unsorted_list)):
            if sorted_list[i] == unsorted_list[j]:
                sorted_tasks.append(tasks[j])
    return sorted_tasks

#Alphabetical sorting
def alpha_sort_tasks(tasks):
    unsorted_list = []
    for i in tasks:
        unsorted_list.append(i.title)
    sorted_list = sorted(unsorted_list)
    tasks = sorting(unsorted_list, sorted_list)
    return tasks

#Completion date sorting by most recent date first
def desc_date_sort_tasks(tasks):
    #List of unsorted dates
    unsorted_list = []
    for i in tasks:
        unsorted_list.append(i.date_to_complete)

    #comparison_list provides a list through an immutable tuple that is unchanged by subsequent operations to allow comparison
    comparison_tuple = tuple(unsorted_list)
    comparison_list = list(comparison_tuple)

    #Bubble sort list of dates and assign result to sorted_list
    for i in range(len(unsorted_list)):
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    sorted_list = unsorted_list
    tasks = sorting(comparison_list, sorted_list)
    return tasks

#Completion date sorting by furthest date first
def asc_date_sort_tasks(tasks):
    tasks = tasks[::-1]
    return tasks

#Checks to see if a user suggested title is a real task title
def check_title(tasks, user_title):
    for i in tasks:
        if i.title.lower() == user_title.lower():
            return True
        else:
            return False



if __name__ == "__main__":

    #Some tasks have been added manually to allow the system to be tested
    add_task("Shopping", "Buy 5 potatoes and 2 eggs", datetime.date(2021, 12, 5))
    add_task("Jerry", "Wish Jerry a Happy Birthday", datetime.date(2024, 3, 29))
    add_task("Taxes", "File taxes", datetime.date(2019, 10, 17))
    add_task("Exercise", "Run 10km", datetime.date(2022, 1, 14))

    #Introductory messages and commands
    print("==============")
    print("Hello and welcome to Task Manager")
    print("To add or delete a new task, type 'add' or 'delete' respectively")
    print("To print all tasks, type 'print'")
    print("To change the status of a task, type 'status'")
    print("To sort the tasks alphabetically by title, type 'sort' and 'alpha'")
    print("To sort the tasks by ascending or descending completion date, type 'sort' and 'asc' or 'desc' respectively")
    print("For help, type 'help'")
    print("To leave, type 'leave'")
    print("==============")

    while True:
        value = input()
        if value == 'add':
            title = input("Enter your task title: ")
            details = input("Enter any extra details about your task: ")
            year = input("Enter the year you need to complete the task by: ")
            month = input("Enter the month you need to complete the task by: ")
            date = input("Enter the date you need to complete the task by: ")
            completion_date = datetime.date(int(year), int(month), int(date))
            add_task(title, details, completion_date)
        elif value == 'delete':
            title = input("Enter the title of the task you wish to delete: ")
            #Check to see if proposed title is actually a title
            if check_title(tasks, title) == True:
                del_task(title)
            else:
                print("That is not a task title. Please start again")
        elif value == "print":
            print_all_tasks(tasks)
        elif value == "status":
            title = input("Enter the title of the task you would like to change the status of: ")
            #Check to see if proposed title is actually a title
            if check_title(tasks, title) == True:
                del_task(title)
            else:
                print("That is not a task title. Please start again")
            change_status(title)
        elif value == "sort":
            sort_method = input("Enter how you would like to sort your tasks: ")
            if sort_method == "alpha":
                tasks = alpha_sort_tasks(tasks)
            elif sort_method == "asc":
                tasks = asc_date_sort_tasks(tasks)
            elif sort_method == "desc":
                    tasks = desc_date_sort_tasks(tasks)
            print_all_tasks(tasks)
        elif value == "help":
            print("==============")
            print("To add a new task, type 'add'")
            print("To delete a task, type 'delete'")
            print("To print all tasks, type 'print'")
            print("To change the status of a task, type 'status'")
            print("To sort the tasks type 'sort'")
            print("To sort the tasks alphabetically, type 'sort' then 'alpha'")
            print("To sort the tasks by ascending completion date, type 'sort' then 'asc'")
            print("To sort the tasks by descending completion date, type 'sort' then 'desc'")
            print("To leave, type 'leave'")
            print("==============")
        elif value == "leave":
            break
        else:
            print("The command was mistyped")
    print("Thank you for using Task Manager")
