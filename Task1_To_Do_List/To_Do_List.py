to_do_list = []
while True:
    print("To Do List:")
    print("1)View Tasks")
    print("2)Add Task")
    print("3)Update Task")
    print("4)Delete Task")
    print("5)Exit")

    try:
        choice = int(input("Enter Your Choice:"))

    except ValueError:
        print("Enter Values only!(1-5)")
        continue
    n = len(to_do_list)


    #Display To do List
    if choice == 1:
        if n == 0:
            print("All Tasks Complete")
        else:
            print("Tasks To Complete:")
        
            for i in range(n):
             print(f"{i + 1}){to_do_list[i]}")


    #Add Task
    elif choice == 2:
        new_task = input("Enter Task:")
        to_do_list.append(new_task)
        print("Task Added Succesfully!")


    #Update Task
    elif choice == 3:
        if n != 0:
            try:
                position = int(input("Enter Position:"))
                if position <= n and position > 0:
                   updated_task = input("Enter Updated Task:")
                   to_do_list[position - 1] = updated_task
                   print("Task Updated Succesfully!")
                else:
                    print("Enter Valid Input!")
            except ValueError:
                print(f"Enter Correct Values(1 - {n})")
                continue
        
        else:
            print("No Tasks Present to Update!")
            
    #Delete Task
    elif choice == 4:
        if n != 0:
            try:
                task_number = int(input("Enter Task Number:"))

                if task_number <= n and task_number > 0 :
                    del to_do_list[task_number - 1]
                    print("Task Deleted Successfully!")
                else:
                    print("Enter Valid Input!")
            except ValueError:
                print(f"Enter Valid Input(1-{n})!")

        else:
            print("No Tasks Present to Delete!")
    #Exit
    elif choice == 5:
        print('Program Exited Successfully!')
        break
    else:
        print("Enter Valid input!")

