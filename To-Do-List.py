class todo:
    tasks = []

    def create(self):
        task = input("Enter your task - " )
        self.tasks.append(task)


    def update(self):
        print("Select The serial number from below  which you want to delete")
        to_del = int(input("enter -"))
        self.tasks.pop(to_del)

    def track(self):
        for data_fetch in self.tasks:
            print(data_fetch)



def main():
    while True:
        user_input = input("To-Do List : - \n 1.Create Tasks \n 2.Update Tasks \n 3.Track Tasks \n4.To Quit \nEnter -")
        if user_input == "1":
            todo.self.create()
        elif user_input == "2":
            todo.self.update()
        elif user_input =="3":
            todo.self.track()
        elif user_input =="4":
            print("Exitting")
            quit()
        else:
            print("invalid Selection")

if __name__ ==" __main__":
    main()
    
    