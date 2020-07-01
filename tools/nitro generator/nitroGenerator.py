import string, random

def genNitroCode(isclassic=False):
    """
    Generate a Discord nitro code.
    <params>
    isclassic : bool  default=False

    <returns>
    return a type code.
    """
    if isclassic:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    else:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=24))

if __name__ == '__main__':
    
    from datetime import datetime
    from colorama import Fore, Style, init

    init()

    code = str(input('Do you want the Nitro codes to be classic? y/n \n > '))
    code = True if code == 'y' else False

    count = int(input('How many codes do you want? \n > '))

    prefix = str(input('Do you want to add discord.gift prefix? y/n \n > '))
    prefix = 'discord.gift/' if prefix == 'y' else ''

    CODES_FILE = str(input('Do you want to custom the codes file? y/n \n > '))
    CODES_FILE = str(input('Enter file name (example.txt) \n > ')) if CODES_FILE == 'y' else 'nitro_codes.txt'

    with open(CODES_FILE, 'a+') as f:
        for _ in range(count):
            code = genNitroCode(code)
            print(f'{Fore.BLUE + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {code}', Fore.WHITE + Style.NORMAL)
            f.write(f'{prefix}{code}\n')
    print('Done.')
    input()