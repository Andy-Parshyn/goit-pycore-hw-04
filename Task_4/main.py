def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

def change_contact(args, contacts):
    if not contacts:
        return 'There are no Contacts, please add one first'
    
    name, phone = args

    if name not in contacts:
        return f'There is no such contact {name}.'
    
    if contacts[name] == phone:
        return 'Please enter new phone number.'
    
    contacts[name] = phone
    return 'Contact updated.'
    
def show_phone(args, contacts):
    if not contacts:
        return 'There are no Contacts, please add one first'
    
    name = args[0]

    if name not in contacts:
        return f'There is no such contact {name}'
    
    return contacts.get(name)

def show_all(contacts: dict):
    result = ''
    if not contacts:
        return 'No contacts found!'
    
    for name, phone in contacts.items():
        result += f'{name} -> {phone}\n'
        
    return result
        

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
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

        elif command == "change":
            print(change_contact(args,contacts))

        elif command == "phone":
            print(show_phone(args,contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
