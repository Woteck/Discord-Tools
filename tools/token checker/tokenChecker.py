import requests

def checkToken(token, bot=False, proxy=None):
    """
    Checks a Discord token.
    <params>
    token : string
    bot   : bool    default = False
    proxy : string

    <returns>
    True if token is valid (code 200 from Discord) else False
    """
    DISCORD_URL = "https://discordapp.com/api/v6/users/@me/library"
    if proxy is not None:
        res = requests.get(DISCORD_URL, headers={'authorization':str(token)}, proxy={'https': str(proxy)})
    else:
        res = requests.get(DISCORD_URL, headers={'authorization':str(token)})
    return True if res.status_code is 200 else False

if __name__ == '__main__':

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
            if status:
                print(f'{Fore.GREEN + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {token}', Fore.WHITE + Style.NORMAL)
                validTokens_file.write(token + "\n")
            else:
                print(f'{Fore.RED + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {token}', Fore.WHITE + Style.NORMAL)
                invalidTokens_file.write(token + "\n")
    print('Done.')
    input()