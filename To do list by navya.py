# making class of task
class Task:
    def __init__(self, name, description, priority, deadline, status):
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = status
# making class of to do list
class ToDoList:
    def __init__(self):
        self.tasks =[]
    #making function to add task
    def add_task(self, task):
        self.tasks.append(task)
    #making fucntion completing task
    def complete_task(self, task):
        for i in range(len(self.tasks)):
            if self.tasks[i].name == task:
                self.tasks[i].status = "Completed"
                break
    #making function to display tasks
    def display_tasks(self):
     for i in range(len(self.tasks)):
        print(self.tasks[i].name, self.tasks[i].description, self.tasks[i].priority, self.tasks[i].deadline, self.tasks[i].status)
                    
# making the main function to run the program
def main():
    #making the to do list
    to_do_list = ToDoList()
    while True:
        print("\n ---To Do list---")
        print('1. Add Task')
        print('2. Complete Task')
        print('3. Display Tasks')
        print('4. Exit')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter the name of the task: ")
            description = input("Enter the description of the task: ")
            priority =input("Enter the priority of the task: ")
            deadline = input("Enter the deadline of the task: ")
            status = "Pending"
            task = Task(name, description, priority, deadline, status)
            to_do_list.add_task(task)
        elif choice == 2:
            task = input("Enter the name of the task to complete: ")
            for i in range(len(to_do_list.tasks)):
                if to_do_list.tasks[i].name == task:
                    to_do_list.tasks[i].status = "Completed"
                    break
        elif choice==3:
            to_do_list.display_tasks()
        elif choice==4:
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()




    

