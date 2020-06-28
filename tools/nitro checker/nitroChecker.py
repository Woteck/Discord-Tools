import requests

def checkNitro(code, userToken):
    """
    Checks a Discord nitro code.
    <params>
    code        : string
    userToken   : string

    <returns>
    True if code is valid (code 200 from Discord) else False
    """
    URL = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem'
    result = requests.post(URL, headers={'authorization': userToken}).text
    if 'nitro' in result:
        return True
    else: 
        return False