import re, requests, json, time, os, asyncio
from discord.ext import commands
from colorama import Fore, init

init()
data = {}

with open('token.json') as f:
    data = json.load(f)
token = data['token']
token_redeemer = data['token-redeemer'] if data['token-redeemer'] is not "" else token

os.system("clear")
print(chr(27) + "[2J")

bot = commands.Bot(command_prefix=".", self_bot=True)
ready = False

@bot.event
async def on_message(ctx):
    global ready

    if not ready:
        print(Fore.LIGHTCYAN_EX + 'Sniping Discord Nitro and Giveaway on ' + str(len(bot.guilds)) + ' Servers \n' + Fore.RESET)
        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
        print("[+] Bot is ready")
        ready = True

    def check(codes):
        for code in codes:

            start_time = time.time()
            result = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem', json={"channel_id": str(ctx.channel.id)}, headers={'authorization': token_redeemer}).text
            delay = (time.time() - start_time)

            print(Fore.LIGHTGREEN_EX + "[-] Snipped code: " + Fore.LIGHTRED_EX + code + Fore.RESET + " From " + ctx.author.name + "#" + ctx.author.discriminator + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)

            if 'This gift has been redeemed already.' in result:
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                print(Fore.LIGHTYELLOW_EX + "[-] Code has been already redeemed" + Fore.RESET, end='')

            elif 'nitro' in result:
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                print(Fore.GREEN + "[+] Code applied" + Fore.RESET, end='')

            elif 'Unknown Gift Code' in result:
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                print(Fore.LIGHTRED_EX + "[-] Invalid Code" + Fore.RESET, end=' ')

            print(" Delay:" + Fore.GREEN + " %.3fs" % delay + Fore.RESET)

    content = ctx.content
    if content is not None:
        # Idk the fuck I did there but iT woRKs LoL
        codes = re.findall(r"(?=(\b[A-Za-z0-9]{16}\b))|(?=(\b[A-Za-z0-9]{24}\b))",content)
        codes = list(map(lambda x: list(filter(None, x)),codes))
        codes = [item for sublist in codes for item in sublist]
        check(codes)

bot.run(token, bot=False)
