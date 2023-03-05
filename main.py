# -*- coding: utf-8 -*-
import json
from lib.checker import check_token, getint
import os

os.system("cls")
try:
    os.mkdir("export")
except:
    pass
print("\n\033[91m ██▓███  ▓█████  █     █░███▄    █  ██▓▓█████    ▄▄▄█████▓ ██ ▄█▀ ███▄    █ \n▓██░  ██▒▓█   ▀ ▓█░ █ ░█░██ ▀█   █ ▓██▒▓█   ▀    ▓  ██▒ ▓▒ ██▄█▒  ██ ▀█   █ \n▓██░ ██▓▒▒███   ▒█░ █ ░█▓██  ▀█ ██▒▒██▒▒███      ▒ ▓██░ ▒░▓███▄░ ▓██  ▀█ ██▒\n▒██▄█▓▒ ▒▒▓█  ▄ ░█░ █ ░█▓██▒  ▐▌██▒░██░▒▓█  ▄    ░ ▓██▓ ░ ▓██ █▄ ▓██▒  ▐▌██▒\n▒██▒ ░  ░░▒████▒░░██▒██▓▒██░   ▓██░░██░░▒████▒     ▒██▒ ░ ▒██▒ █▄▒██░   ▓██░\n▒▓▒░ ░  ░░░ ▒░ ░░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░▓  ░░ ▒░ ░     ▒ ░░   ▒ ▒▒ ▓▒░ ▒░   ▒ ▒ \n░▒ ░      ░ ░  ░  ▒ ░ ░ ░ ░░   ░ ▒░ ▒ ░ ░ ░  ░       ░    ░ ░▒ ▒░░ ░░   ░ ▒░\n░░          ░     ░   ░    ░   ░ ░  ▒ ░   ░        ░      ░ ░░ ░    ░   ░ ░ \n            ░  ░    ░            ░  ░     ░  ░            ░  ░            ░ \n                                                                            \033[0m")

x = input("Do you want to check token? (y/n) : ")

if x == "n" or x == "y" or x == "N" or x == "Y":
    print("\n")
else:
    print("Invalid choice. Please select y or n.")
    exit

tkns = 0

def checking():
    global tkns
    with open("config.json") as f:
        config = json.load(f)
        token_key = config["token_key"]
        json_file = config["json_file"]
        print("Config loaded!")

    with open(json_file) as f:
        data = json.load(f)
        print("Grabbed tokens!")

    tokens = []
    for key in data.keys():
        if token_key in data[key]:
                tkns += 1
                tokens.append(str(data[key][token_key]))
    print("Creating file!")

    with open("export/tokens.txt", "w") as f:
        f.write("\n".join(tokens))
        print(f"Done! You have {tkns} tokens!")

    if (x == "y" or x == "Y"):
        print("\nChecking tokens!")
        with open('export/tokens.txt', 'r') as f:
                tokens = f.read().splitlines()
        for token in tokens:
                check_token(token)
    os.system("cls")
    print("\n\033[91m ██▓███  ▓█████  █     █░███▄    █  ██▓▓█████    ▄▄▄█████▓ ██ ▄█▀ ███▄    █ \n▓██░  ██▒▓█   ▀ ▓█░ █ ░█░██ ▀█   █ ▓██▒▓█   ▀    ▓  ██▒ ▓▒ ██▄█▒  ██ ▀█   █ \n▓██░ ██▓▒▒███   ▒█░ █ ░█▓██  ▀█ ██▒▒██▒▒███      ▒ ▓██░ ▒░▓███▄░ ▓██  ▀█ ██▒\n▒██▄█▓▒ ▒▒▓█  ▄ ░█░ █ ░█▓██▒  ▐▌██▒░██░▒▓█  ▄    ░ ▓██▓ ░ ▓██ █▄ ▓██▒  ▐▌██▒\n▒██▒ ░  ░░▒████▒░░██▒██▓▒██░   ▓██░░██░░▒████▒     ▒██▒ ░ ▒██▒ █▄▒██░   ▓██░\n▒▓▒░ ░  ░░░ ▒░ ░░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░▓  ░░ ▒░ ░     ▒ ░░   ▒ ▒▒ ▓▒░ ▒░   ▒ ▒ \n░▒ ░      ░ ░  ░  ▒ ░ ░ ░ ░░   ░ ▒░ ▒ ░ ░ ░  ░       ░    ░ ░▒ ▒░░ ░░   ░ ▒░\n░░          ░     ░   ░    ░   ░ ░  ▒ ░   ░        ░      ░ ░░ ░    ░   ░ ░ \n            ░  ░    ░            ░  ░     ░  ░            ░  ░            ░ \n                                                                            \033[0m\n\nDo you want to check token? (y/n) : y\n\n\nConfig loaded!\nGrabbed tokens!\nCreating file!\nDone! You have 45 tokens!\n\nChecking tokens!")
    print(f"Status : {getint(1)} - valid | {getint(2)} - invalid | {getint(3)} - total")

checking()
