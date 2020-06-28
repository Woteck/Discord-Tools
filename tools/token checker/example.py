from tokenChecker import checkToken
from datetime import datetime
from colorama import Fore, Style, init
init()

VALID_TOKEN_FILE   = "valid_tokens.txt"
INVALID_TOKEN_FILE = "invalid_tokens.txt"
TOKEN_FILE         = "tokens.txt"

validTokens_file   = open(VALID_TOKEN_FILE, 'a+')
invalidTokens_file = open(INVALID_TOKEN_FILE, 'a+')

with open(TOKEN_FILE , 'r') as tokens_file:
    content = tokens_file.readlines()
    tokens = list(filter(None, list(map(lambda x: str.replace(x, "\n", ""), content)))) # removes shit lol

    for token in tokens:
        status = checkToken(token)
        if status is True:
            print(f'{Fore.GREEN + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {token}', Fore.WHITE + Style.NORMAL)
            validTokens_file.write(token + "\n")
        else:
            print(f'{Fore.RED + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {token}', Fore.WHITE + Style.NORMAL)
            invalidTokens_file.write(token + "\n")
print('Done.')
input()