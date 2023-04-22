class discussion():
    def add_discussion(self):
        with open('discussion.txt', 'a') as file:
            user_input = input("- ")
            file.write(user_input + '\n')
            
    def view_discussion(self):
        with open('discussion.txt', 'r') as file:        
             tasks = file.read()
        print(tasks)  
        
class extra():
    def add_extra(self):
        with open('extra.txt', 'a') as file:
            user_input = input("What about extra curricular:- ")
            file.write(user_input + '\n')
            print("New update added")
            
    def view_extra(self):
        with open('extra.txt', 'r') as file:        
             tasks = file.read()
        print(tasks)  
        
class Domain():
    def add_domainupdate(self):
        with open('update.txt', 'a') as file:
            user_input = input("What's new update:- ")
            file.write(user_input + '\n')
            print("New update added")
            
    def view_domainupdate(self):
        with open('update.txt', 'r') as file:        
             tasks = file.read()
        print(tasks)  
        
class other_tech():
    def add_othertech(self):
        with open('othertech.txt', 'a') as file:
            user_input = input("What's new update:- ")
            file.write(user_input + '\n')
        print("New update added")
            
    def view_othertech(self):
        with open('othertech.txt', 'r') as file:        
             tasks = file.read()
        print(tasks)           
                
class TeamA():
    def addtaskA(self):                           # Open the file in append mode
     with open('taskA.txt', 'a') as file:
        user_input = input("Enter task:- ")       # Get user input
        file.write(user_input + '\n')             # Append the user input to the file
     print("Task added")

    def viewtaskA(self):                          # Open the file in read mode
     with open('taskA.txt', 'r') as file:         # Read the contents of the file
        tasks = file.read()
     print(tasks)                                 # Display the contents of the file

class TeamB():
    def addtaskB(self):
     with open('taskB.txt', 'a') as file:
        user_input = input("Enter task:- ")
        file.write(user_input + '\n')
     print("Task added")

    def viewtaskB(self):
     with open('taskB.txt', 'r') as file:
        tasks = file.read()
     print(tasks)
     
class TeamC():
    def addtaskC(self):
     with open('taskC.txt', 'a') as file:
        user_input = input("Enter task:- ")
        file.write(user_input + '\n')
     print("Task added")

    def viewtaskC(self):
     with open('taskC.txt', 'r') as file:
        tasks = file.read()
     print(tasks)

def team():
    print("""A.(Ananya,Manas,Shantanu)\nB.(Shah,Yashraj,Ritika)\nC.(Mohit,Ashutosh,Shivanshu)\nD.Back""")
def task():
    print("""1.Add\n2.View\n3.Exit""") 
print("\n")     
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")       
print("                     Daily Record                      ")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
print("!!!!TO ADD ANYTHING FIRSTLY TYPE YOUR NAME to identify you!!!!\n")    
print("""Press_1) Task Updates\nPress_2) Domain Update\nPress_3) Other tech exp\nPress_4) Aceivements/Extra Curricular\nPress_5) Discussion\nPress_6) Exit""")
choice=int(input("Enter any of above no.:--"))
while True:
     if choice==1:
        team()
        teamno=input("Enter team:- ")
        if teamno=="A":
           task()
           taskno=int(input("Enter task no.:- "))
           while True:
                 if taskno==1:
                    a=TeamA()
                    a.addtaskA()                     
                 elif taskno==2:
                    a=TeamA()
                    a.viewtaskA()
                 elif taskno==3:
                     print("exited")
                     break   
                 else:
                     print("Wrong input")
                 break
             
        elif teamno=="B":
            task()
            taskno=int(input("Enter task no.:- "))
            while True:
                 if taskno==1:
                    a=TeamB()
                    a.addtaskB()                     
                 elif taskno==2:
                    a=TeamB()
                    a.viewtaskB()
                 elif taskno==3:
                     print("exited")
                     break   
                 else:
                     print("Wrong input")
                 break
                 
        elif teamno=="C":
            task()
            taskno=int(input("Enter task no.:- "))
            while True:
                 if taskno==1:
                    a=TeamC()
                    a.addtaskC()                     
                 elif taskno==2:
                    a=TeamC()
                    a.viewtaskC()
                 elif taskno==3:
                     print("exited")
                     break   
                 else:
                     print("Wrong input")
                 break
             
        elif teamno=="D":    
             break;
         
     elif choice==2:
        task()
        taskno=int(input("Enter task no.:- "))
        if taskno==1:
            b=Domain()
            b.add_domainupdate()
        elif taskno==2:
            b=Domain()
            b.view_domainupdate()
        elif taskno==3:
            print("exited")        
            break
        else:
            print("Wrong input")
        break    
     
     elif choice==3:
        task()
        taskno=int(input("Enter task no.:- "))
        if taskno==1:
            b=other_tech()
            b.add_othertech()
        elif taskno==2:
            b=other_tech()
            b.view_othertech()
        elif taskno==3:
            print("exited")        
            break
        else:
            print("Wrong input")
        break    
        
     elif choice==4:
        task()
        taskno=int(input("Enter task no.:- "))
        if taskno==1:
            b=extra()
            b.add_extra()
        elif taskno==2:
            b=extra()
            b.view_extra()
        elif taskno==3:
            print("exited")        
            break
        else:
            print("Wrong input")
        break    
        
     elif choice==5:
         while True:
              b=discussion()
              b.view_discussion()
              b.add_discussion()
     elif choice==6:
         print("Program Terminated!!")
     break        