import os
# Import base modules

from LethalCompanyMM import modmanage
# Import my modules

os.system("title CharlesMD")  # Set Cmd title

cmds = [
        "help - List all commands.",
        "exit - Exit CharlesMD.",
        "lethalcompanymm - Launch the mod manager for Lethal Company.",
        ]
# List of commands and descriptions

while True:
    command = str(input("CharlesMD> "))
    match command.lower():  # Take input and run code according to the command
        case "help":
            for cmd in cmds:
                print(cmd)
        case "exit":
            break
        case "lethalcompanymm":
            modmanage()  # Run the Lethal Company mod manager
        case other:
            print("Command not recognised, try 'help'")
