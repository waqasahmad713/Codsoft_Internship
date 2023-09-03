class Todo:
    def __init__(self):
        self.task=[]
    def add_task(self,task):
        self.task.append(task)
    def remove_task(self,task):
        self.task.remove(task)
    def display_task(self):
        if self.tasks:
            print("Tasks")
            for index,task in enumerate(self.tasks,start=1):
                print(f"{index}.{task}")
        else:
            print("No tasks in list.")
todo=Todo()
while True:
    print("\n1. Add Task:")
    print("2.Remove Task.")
    print("3.Display Task.")
    print("4.Quit.")

    choice=input("Enter your choice:")
    if choice =='1':
        task=input("Enter the task:")
        todo.add_task(task)
    elif choice =='2':
        task=input("Enter the task to remove:")
        try:
            todo.remove_task(task)
            print(f"Task {task} removed :")
        except ValueError:
            print(f"Task {task} is not found:")
    elif choice =='3':
        todo.display_task()
    elif choice =='4':
        print("Good bye!")
        break

