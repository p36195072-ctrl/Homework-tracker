import json

try:
    with open("homeworktracker.json", "r") as file:
        homeworktracker = json.load(file)
except FileNotFoundError:
    homeworktracker = {}

def save_data():
    with open("homeworktracker.json", "w") as file:
        json.dump(homeworktracker, file, indent=4)

def add_homework():
    subject = input("Enter the subject name: ")
    if subject == "":
        print("Subject can't be empty")
        return

    homewk = input("Enter the pending h.w: ")
    if homewk == "":
        print("Homework can't be empty")
        return

    duedate = input("Enter the due date: ")
    if duedate == "":
        print("Due date can't be empty")
        return

    homeworktracker[subject] = {
        "homework": homewk,
        "due_date": duedate
    }

    save_data()
    print("Saved")

def view_homework():
    if not homeworktracker:
        print("No homework found")
        return

    for subject in homeworktracker:
        print("\nSubject =", subject)
        print("Homework Pending =", homeworktracker[subject]["homework"])
        print("Due Date =", homeworktracker[subject]["due_date"])

def searchdata():
    search = input("Enter the subject you wanna search: ")

    if search == "":
        print("Search can't be empty")
        return

    if search in homeworktracker:
        print("\nHomework Found")
        print("Subject =", search)
        print("Due Homework =", homeworktracker[search]["homework"])
        print("Due Date =", homeworktracker[search]["due_date"])
    else:
        print("Subject not found")

def deletedata():
    delete = input("Enter the subject you wanna delete: ")

    if delete in homeworktracker:
        confirm = input("Are you confirm you wanna delete (yes/no): ")

        if confirm.lower() == "yes":
            homeworktracker.pop(delete)
            save_data()
            print("Deleted successfully")
        else:
            print("Delete cancelled")
    else:
        print("Subject not found")

while True:
    print("\n=== Homework Tracker ===")
    print("1. Add Pending Homework")
    print("2. View Homework")
    print("3. Search Homework")
    print("4. Delete Homework")
    print("5. Exit")
    print("Total homework:", len(homeworktracker))

    choice = input("Enter the number: ")

    if choice == "1":
        add_homework()

    elif choice == "2":
        view_homework()

    elif choice == "3":
        searchdata()

    elif choice == "4":
        deletedata()

    elif choice == "5":
        print("Exiting...")
        save_data()
        break

    else:
        print("Invalid choice")