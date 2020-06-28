from nitroGenerator import genNitroCode
from datetime import datetime
from colorama import Fore, Style, init
init()

count = int(input('How many codes do you want? \n >'))

CODES_FILE = 'nitro_codes.txt'
with open(CODES_FILE, 'a+') as f:
    for _ in range(count):
        code = genNitroCode()
        print(f'{Fore.BLUE + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {code}', Fore.WHITE + Style.NORMAL)
        f.write(code + '\n')
print('Done.')
input()