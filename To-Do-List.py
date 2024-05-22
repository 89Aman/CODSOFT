print("To Do List")

tasks = []
def create():
    task = input("Enter your task - ")
    task.append(tasks + "/n")


def update():
    print("Select The serial number from below  which you want to delete")
    to_del = input("enter -")
    tasks.pop(to_del)

def track():
    print(tasks)

while True:
    user_input = input("Enter the selection /n1.Create Tasks /n2.Update Tasks /n3.Track Tasks")
    if user_input == "1":
        create()
    elif user_input == "2":
        update()
    elif user_input =="3":
        track()
    else:
        print("invalid Selection")

    
    