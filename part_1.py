
# Student ID: 20200688

#Part 1
allowedlist = [0,20,40,60,80,100,120] #List of inputs that are allowed
progress = 0  #Progress, initializing the Count
mod_ret = 0 #Module Retriever, initializing the Count
mod_tra = 0 #Module Trailer, initializing the Count
exclude = 0 #Exclude, initializing the Count
result = []
count = 0

def Inputs():
    global Pass, Defer, Fail #https://www.w3schools.com/python/python_variables_global.asp
    while True:
        try:
            Pass = int(input('Please enter your credits at pass: '))
        except ValueError:
            print('ERROR!- A Integer should be required!')
            continue
        if Pass not in allowedlist:
            print('Out of range!')
        else:
            break
    while True:
        try:
            Defer = int(input('Please enter your credit at defer:  '))
        except ValueError:
            print('ERROR!- A Integer should be required!')
            continue
        if Defer not in allowedlist:
            print('Out of range!')
        else:
            break
    while True:
        try:
            Fail = int(input('Please enter your credit at fail: '))
        except ValueError:
            print('ERROR!- A Integer should be required!')
            continue
        if Fail not in allowedlist:
            print('Out of range!')
        else:
            break

def Progression():
    global result
    global Pass,Defer,Fail #https://www.w3schools.com/python/python_variables_global.asp
    global progress, mod_ret, mod_tra, exclude       
    Total = Pass + Defer + Fail
    if Total == 120:
        if Pass == 120:
            print('Progress')
            progress += 1
            result.append('Progress')
            result.append(Pass)
            result.append(Defer)
            result.append(Fail)

        elif (Defer + Fail) == 20 and Pass == 100:
            print('Progress (Module Trailer)')
            mod_tra += 1
            result.append('Trailer')
            result.append(Pass)
            result.append(Defer)
            result.append(Fail)

        elif (Fail >= 80) and (Fail > Defer) and (Pass <= 40):
            print('Exclude')
            exclude += 1
            result.append('Exclude')
            result.append(Pass)
            result.append(Defer)
            result.append(Fail)
        
        elif (Pass < 100):
            print('Do not progress (Module Retriever)')
            mod_ret += 1
            result.append('Retriever')
            result.append(Pass)
            result.append(Defer)
            result.append(Fail)
   


        elif (Pass + Defer + Fail) != 120:
            print('Incorrect Total!')

        else:
            print('Out of range!')
    else:
        print('Incorrect Total!')        


def outcome():
    choice = None
    while True:
        choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        
        if choice == 'y':
            print('')
            Inputs()
            print('')    
            Progression()
            print('')        
        elif choice == 'q':
            print(70*'-')
            print('')
            print('Horizontal Histogram')
            Horizontal_His(count)
            print('')
            print(70*'-')                      
            print('')            
            break
        else:
            print('Wrong input!')


def Horizontal_His(count):   
    print('Progress',progress,':',progress*'*')
    print('Module Retriever',mod_ret,':',mod_ret*'*')
    print('Module Trailer',mod_tra,':',mod_tra*'*')
    print('Exclude',exclude,':',exclude*'*')
    total = progress + mod_ret + mod_tra + exclude
    print('Outcomes in total. = ',total)


option = 0
options = [1, 2] #List for initial menu choices2
while option not in options:
    try:
        print("For students press 1\nFor teachers press 2")
        option = int(input('Please enter the option 1 or 2: '))
        if option == 1:
            print('')
            Inputs()
            print('')
            Progression()
    
        if option == 2:
            print('')
            Inputs()
            print('')
            Progression()
            print('')
            outcome()
    except ValueError:
        print('Invalid Input!')


