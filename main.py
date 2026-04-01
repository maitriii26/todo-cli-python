tasks=[]

try:
    file=open("tasks.txt","r")
    lines=file.readlines()#gives list of lines

    for line in lines:
        tasks.append(line.strip())#removes \n
    file.close()
    
except FileNotFoundError:
    pass

def save_tasks():
    file=open("tasks.txt","w")
    for t in tasks:
        file.write(t+"\n")
    file.close()

while True:
    print("---------menu---------")
    print("1.add task")
    print("2.view task")
    print("3.delete task")
    print("4.exit")
    
    try:
        ch=int(input("Enter your choice:"))
    except:
        print("please enter a valid number!")
        continue

    match ch:
        case 1:
            task=input("Enter task:")
            tasks.append(task)
            save_tasks()
            print("task added successfully!\n")

        case 2:
            if not tasks:
                print("no tasks")
            else:
                for index,task in enumerate(tasks):
                    print(index+1,".",task)
        case 3:
            if not tasks:
                print("no tasks...")
            else:
                for index,task in enumerate(tasks):
                    print(index+1,".",task)
            
                try:
                    number = int(input("Enter task number to delete:"))
                except:
                    print("please enter a valid number!")
                    continue
                if 1<= number <= len(tasks):
                    tasks.pop(number-1)
                    save_tasks()
                    print("task deleted!\n")
                    for index,task in enumerate(tasks):
                        print(index+1,".",task)
                else:
                    print("invalid task number")

        case 4:
            print("exiting......")
            break

        case _:
            print("invalid choice please try again!")
        

