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
