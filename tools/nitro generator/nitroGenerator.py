import string, random

def genNitroCode(isclassic=False):
    """
    Generate a Discord nitro code.
    <params>
    isclassic : bool  default=False

    <returns>
    return a type code.
    """
    if isclassic is False:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    else:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=24))

if __name__ == '__main__':
    
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