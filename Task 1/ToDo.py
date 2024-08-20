


tasks=[]
def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully")

def listTask():
   if not tasks:
      print("There are no task currently in the list")
   else:
      print("Current Tasks:")
      for i,task in enumerate(tasks):
         print(f"Task #{i} . #{task}")

def deleteTask():
    listTask()
    try:
       taskToDelete = int(input('Enter the # to delete: '))
       if taskToDelete >=0 and taskToDelete < len(tasks):
         tasks.pop(taskToDelete)
         print(f"Task #{taskToDelete} deleted successfully")

       else:
          print(f"Task #{taskToDelete} was not found.")
    except:
          print("Invalid Input ")

if __name__=="__main__": 

 print("WELCOME TO THE TO-DO LIST 😊")  
while True:
    print("\n")
    print("Please select one of the following options:")
    print("==============================================")
    print("1.  Add a new task")
    print("2.  Delete a task")
    print("3.  List tasks")
    print("4.  Quit")

    choice = input ("Enter your choice: ")

    if(choice == "1"):
        addTask()
    elif(choice == "2"):
        deleteTask()
    elif(choice == "3"):
        listTask()
    elif(choice == "4"):
        break
    else:
     print("Invalid choice. Please try again !!!")
print("Thanks for Visiting 😊")

    
   
    
   
