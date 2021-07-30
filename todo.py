#!/usr/bin/env python3
import sys
from datetime import date
import os

def main():
    if len(sys.argv) == 1 or sys.argv[1] == "help":
        helpTextBlock = """\
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
"""
        sys.stdout.buffer.write(helpTextBlock.encode('UTF-8'))
        return
    if  sys.argv[1] == "report" and len(sys.argv)== 2:
        displayReport()
    if sys.argv[1] == "add":
        if len(sys.argv) == 3:
            addTodo(sys.argv[2])
            return
        else:
            print("Error: Missing todo string. Nothing added!")
    if sys.argv[1] == "ls" and len(sys.argv) == 2:
        listTodo()
        return
    if sys.argv[1] == "del":
        if len(sys.argv) == 3:
            deleteTodo(sys.argv[2])
            return
        else:
            print("Error: Missing NUMBER for deleting todo.")
            return
    if sys.argv[1] == "done":
        if len(sys.argv) == 3:
            markAsDone(sys.argv[2])
            return
        else:
            print("Error: Missing NUMBER for marking todo as done.")    #####
            return
def addTodo(todo):
    todoFile = open("todo.txt", 'a')
    if os.stat("todo.txt").st_size == 0:
        todoFile.writelines([todo])
    else:
        todoFile.writelines(["\n"+todo])
    todoFile.close()
    print("Added todo: \""+todo+"\"")

def listTodo():
    todoFile = open("todo.txt", 'a')
    todoFile.close()
    todoFile = open("todo.txt", 'r')
    todoList = todoFile.readlines()
    if len(todoList) == 0:
        print("There are no pending todos!")
        return
    todoFile.close()
    todoList.reverse()
    todoNo = len(todoList)
    for todo in todoList:
        if todoNo == len(todoList):
            string = "["+str(todoNo)+"] "+todo+'\n'
        else:
            string = "["+str(todoNo)+"] "+todo
        sys.stdout.buffer.write(string.encode('UTF-8'))
        todoNo-=1

def displayReport():
    todoFile = open("todo.txt", 'r')
    doneFile = open("done.txt", 'r')
    pendingTodo = len(todoFile.readlines())
    completedTodo = len(doneFile.readlines())
    today = date.today()
    todoFile.close()
    doneFile.close()
    print(str(today.year)+'-'+str(today.month)+'-'+str(today.day)+" Pending : "+str(pendingTodo)+" Completed : "+str(completedTodo))
    return
def displayHelp():
    helpTextBlock = """\
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
"""
    sys.stdout.buffer.write(helpTextBlock.encode('UTF-8'))
    return
def deleteTodo(todoNo):
    todoFile = open("todo.txt", 'r')
    todoList = todoFile.readlines()
    todoFile.close()
    reversedList = todoList.copy()
    reversedList.reverse()
    delIndex = len(todoList)-int(todoNo)
    if len(todoList)==0 or int(todoNo)>len(todoList) or int(todoNo)<=0:
        print("Error: todo #"+todoNo+" does not exist. Nothing deleted.")
        return
    toDelete = reversedList[delIndex]
    todoFile = open("todo.txt", 'w')
    for todo in todoList:
        if todo.strip('\n') != toDelete.strip('\n'):
            todoFile.write(todo)
    todoFile.close()
    print("Deleted todo #"+todoNo)

def markAsDone(todoNo):
    todoFile = open("todo.txt", 'r')
    todoList = todoFile.readlines()
    if len(todoList)==0 or int(todoNo)>len(todoList) or int(todoNo)<=0:
        print("Error: todo #"+todoNo+" does not exist.")
        return
    reversedList = todoList.copy()
    reversedList.reverse()
    selectedIndex = len(todoList)-int(todoNo)
    selectedTodo = reversedList[selectedIndex]
    todoFile.close()
    todoFile = open("todo.txt", 'w')
    for todo in todoList:
        if todo.strip('\n') != selectedTodo.strip('\n'):
            todoFile.write(todo)
    todoFile.close()
    doneFile = open("done.txt", 'a')
    today = date.today()
    
    if os.stat("done.txt").st_size == 0:
        doneFile.writelines(["x "+str(today.year)+'-'+str(today.month)+'-'+str(today.day)+' '+selectedTodo.strip('\n')])
    else:
        doneFile.writelines(["\n"+"x "+str(today.year)+'-'+str(today.month)+'-'+str(today.day)+' '+selectedTodo.strip('\n')])
    doneFile.close()
    print("Marked todo #"+str(todoNo)+" as done.")


if __name__ == "__main__":
    main()
