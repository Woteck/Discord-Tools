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