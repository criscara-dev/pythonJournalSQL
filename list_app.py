# database.py

entries = []


def add_entry(entry_content, entry_date):
    entries.append({"content": entry_content, "date": entry_date})


def get_entries():
    return entries


# entry point for list_app

menu = """Please select one of the following options:
1. add new entry for today
2. view entries
3. exit

Your selection: """

welcome = "Welcome to the programming diary!"
print(welcome)


while (user_input := input(menu)) != "3":
    if user_input == "1":
        add_entry(input("What have you learned today? "), input("Enter the date "))
    elif user_input == "2":
        entries = get_entries()
        for entry in entries:
            print(f"{entry['date']}\n{entry['content']}\n\n")
    else:
        print("Please try again")