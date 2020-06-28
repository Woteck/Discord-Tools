from nitroChecker import checkNitro
from datetime import datetime
from colorama import Fore, Style, init
init()

userToken = str(input('Please, enter you user token to check the codes. \n >'))

VALID_CODES_FILE   = "valid_nitro_codes.txt"
INVALID_CODES_FILE = "invalid_nitro_codes.txt"
CODES_FILE         = "nitro_codes.txt"

validTokens_file   = open(VALID_CODES_FILE, 'a+')
invalidTokens_file = open(INVALID_CODES_FILE, 'a+')

with open(CODES_FILE , 'r') as codes_file:
    content = codes_file.readlines()
    codes = list(filter(None, list(map(lambda x: str.replace(x, "\n", ""), content)))) # removes shit lol

    for code in codes:
        status = checkNitro(code, userToken)
        if status is True:
            print(f'{Fore.GREEN + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {code}', Fore.WHITE + Style.NORMAL)
            validTokens_file.write(code + "\n")
        else:
            print(f'{Fore.RED + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {code}', Fore.WHITE + Style.NORMAL)
            invalidTokens_file.write(code + "\n")
print('Done.')
input()
