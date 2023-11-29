import os
import shutil
# Import modules

mod_dir = "S:/SteamLibrary/steamapps/common/Lethal Company/"
mod_inactive_dir = "S:/SteamLibrary/steamapps/common/Lethal Company/BepInExPack/"
# Set Paths of the Lethal Company folder and where the mods are stored when not in use

cmds = [
    "help - List all commands.",
    "exit - Exit LethalCompanyMM.",
    "enable - Enable Lethal Company Mods.",
    "disable - Disable Lethal Company Mods."
    ]
# List of Commands and descriptions


def modmanage():
    """
    Modmanage is a function that takes a command and either enables or disables mods in a Lethal Company installation if for
    whatever reason someone doesn't want to use any big mod manager.
    """
    while True:
        command = str(input("CharlesMD/LethalCompanyMM> "))
        match command.lower():  # Take input and run code according to the command
            case "help":
                for cmd in cmds:
                    print(cmd)
            case "exit":
                break
            case "enable":
                try:  # If the mods are in the storage folder then they are moved into use 
                    shutil.move(mod_inactive_dir + "BepInEx", mod_dir)
                    shutil.move(mod_inactive_dir + "doorstop_config.ini", mod_dir)
                    shutil.move(mod_inactive_dir + "winhttp.dll", mod_dir)
                    print("Lethal Company mods enabled.")
                except:
                    print("ERROR: Either mods are already enabled or Paths are incorrectly set.")
            case "disable":
                try:  # If the mods are in the Lethal Company folder they are moved into storage
                    shutil.move(mod_dir + "BepInEx", mod_inactive_dir)
                    shutil.move(mod_dir + "doorstop_config.ini", mod_inactive_dir)
                    shutil.move(mod_dir + "winhttp.dll", mod_inactive_dir)
                    print("Lethal Company mods disabled.")
                except:
                    print("ERROR: Either mods are already disabled or Paths are incorrectly set.")
            case other:
                print("Command not recognised, try 'help'")
            
