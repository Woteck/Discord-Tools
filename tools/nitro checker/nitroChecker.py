import requests

def checkNitro(code, token, proxy=None, timeout=5):
    """
    Checks a Discord nitro code.
    <params>
    code        : string - discord code
    token       : string - discord user token
    proxy       : string - valid proxy (obvious)
    timeout     : int    - timeout (in seconds)

    <returns>
    True if code is valid (code 200 from Discord) else False
    """
    URL = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem'
    if proxy is not None:
        proxy_dict = {"http" : proxy, "https" : proxy}
        result = requests.post(URL, headers={'authorization': token}, proxies=proxy_dict, timeout=timeout)
    else:
        result = requests.post(URL, headers={'authorization': token})

    if 'nitro' in result.text:
        return True
    else: 
        return False


if __name__ == '__main__':

    from random import choice
    from datetime import datetime
    from colorama import Fore, Style, init

    init()

    userToken = str(input('Please, enter you user token to check the codes. \n > '))

    VALID_CODES_FILE   = "valid_nitro_codes.txt"
    INVALID_CODES_FILE = "invalid_nitro_codes.txt"

    CODES_FILE = str(input('Do you want to use a custom codes file? (by default \'nitro_codes.txt\') y/n \n > '))
    CODES_FILE = str(input('Enter file name (example.txt) \n > ')) if CODES_FILE == 'y' else 'nitro_codes.txt'

    proxySup = str(input('Do you want to use proxy? y/n \n > '))
    proxySup = str(input('Enter file name (example.txt) \n > ')) if proxySup == 'y' else False

    proxy_list = None
    if proxySup is not False:
        proxy_list = list(open(proxySup, 'r').readlines())
        proxy_list = list(filter(None, list(map(lambda x: str.replace(x, "\n", ""), proxy_list)))) # removes shit lol

    validTokens_file   = open(VALID_CODES_FILE, 'a+')
    invalidTokens_file = open(INVALID_CODES_FILE, 'a+')

    with open(CODES_FILE , 'r') as codes_file:
        codes = codes_file.readlines()
        codes = list(filter(None, list(map(lambda x: str.replace(x, "\n", ""), codes)))) # removes shit lol

        for code in codes:
            if proxy_list is not None:
                proxy = choice(proxy_list)
                print(f'{Fore.BLUE + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Using proxy {proxy}', Fore.WHITE + Style.NORMAL)
            else:
                proxy = None

            try:
                status = checkNitro(code=code, token=userToken, proxy=proxy)
            except:
                continue

            if status:
                print(f'{Fore.GREEN + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {code}', Fore.WHITE + Style.NORMAL)
                validTokens_file.write(code + "\n")
            else:
                print(f'{Fore.RED + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {code}', Fore.WHITE + Style.NORMAL)
                invalidTokens_file.write(code + "\n")
    print('Done.')
    input()