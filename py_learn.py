while True:
    action = input("Type add / show / exit: ")

    match action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the completed item: "))
            todos.pop(number - 1)
        case "exit":
            break
print("Bye!")
