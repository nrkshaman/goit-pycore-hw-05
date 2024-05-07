from constants import *
from task4.decorators import input_error

@input_error
def add_contact(args:list[str], contacts:dict[str, str]) -> str:
    name, phone, = args
    #Enforce adding only *NEW* contacts
    if name in contacts:
        return ERROR + " Contact already exists."
    contacts[name] = phone
    return INFO + f" Contact {name} successfully added."

@input_error
def change_contact(args:list[str], contacts:dict[str, str]) -> str:
    name, phone, = args
    #Enforce changing only existing contacts
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return INFO + f" Contact {name} successfully changed."
    
@input_error
def phone_contact(args:list[str], contacts:dict[str, str]) -> str:
    name, = args
    return contacts[name]

def all_contact(contacts:dict[str, str]) -> str:
    if contacts:
        all = f"{'Name':<15}{'| Phone'}\n" + "-"*32 + "\n"
    else:
        all = INFO + " You do not have any contacts saved"
    for name in contacts:
        all += f"{name: <15}| {contacts[name]}\n"
    return all.strip()
