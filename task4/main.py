from constants import *
from handlers import *


def parse_input(user_input: str):
    try:
        cmd, *args = user_input.split()
    except ValueError:
        return INVALID_COMMAND
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def main():
    contacts = {}
    print(BANNER)
    print(GREETING)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "help":
            print(HELP)
        else:
            print(INVALID_COMMAND)

if __name__ == "__main__":
    main()
