# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DFerenczy,5.10.2020,Added code to complete assignment 5 - Maintained date format of block
# DFerenczy,5.10.2020,Updated strMenu variable to contain Menu text
# DFerenczy,5.10.2020,Added Processing code using objFile, strData, dicRow and lstTable variables
# DFerenczy,5.10.2020,Added Input / Output code
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """ # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
txtFile = open(objFile, "r")
for row in txtFile:
    strData = row.split(",")
    dicRow = {"Task":strData[0],"Priority":strData[1].strip()}
    lstTable.append(dicRow)
txtFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a Task to Add: ")
        strPriority = input("Enter a Priority to Add: ")
        dicRow = {"Task":strTask, "Priority":strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemoveTask = input("Enter a Task to Remove: ")
        for row in lstTable:
            strTask = row.get("Task")
            if strRemoveTask == strTask:
                strPriority = row.get("Priority")
                dicRow = {"Task":strTask, "Priority":strPriority}
                lstTable.remove(dicRow)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        txtFile = open(objFile, "w")
        for row in lstTable:
            strTask = row.get("Task")
            strPriority = row.get("Priority")
            dicRow = f'{strTask},{strPriority}\n'
            txtFile.write(dicRow)
        txtFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
