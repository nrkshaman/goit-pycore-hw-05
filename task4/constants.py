from colorama import Fore


BANNER = """
   _                                       
  /   _  ._  _|_  _.  _ _|_  _   |_   _ _|_ 
  \\_ (_) | |  |_ (_| (_  |_ _>   |_) (_) |_ 
"""
GREETING = """Hi! I am your bot-helper! I will help you to manage your contacts list.
Enter `help` for more information"""
HELP = """hello                        : responds "How can I help you?" in console
add [username] [phone]       : saves new contact
change [username] [phone]    : updates existing phone number
phone [username]             : prints phone number for username
all                          : prints all saved contacts
close, exit                  : prints "Good bye!" and finishes bot
help                         : prints this help"""
USE_HELP = "Use 'help' for more information"
INFO = Fore.GREEN + "[INFO]" + Fore.RESET
ERROR = Fore.RED + "[ERROR]" + Fore.RESET
INVALID_COMMAND = ERROR + " Invalid command. " + USE_HELP
NOT_EXISTS = ERROR + " Contact does not exists"
UNKNOWN = ERROR + " Unknow error happend. Please try again. " + USE_HELP
