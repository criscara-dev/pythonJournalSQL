from db import *
menu = """Please select one of the following options:
1. add new entry for today
2. view entries
3. exit

Your selection: """

welcome = "Welcome to the programming diary!"


def prompt_new_entry():
    entry_content = input("What have you learnt today?")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry[1]} \n {entry[0]}\n\n")


# print(welcome)
create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    # elif user_input == "4":
    #     delete_table()
    else:
        print("Please try again")
