import requests

def webhookSend(url, name, **kwargs):
    message = kwargs.get('message')
    if message is not None:
        payload = {'content': str(message), 'username': str(name)}
    else:
        payload = kwargs.get('payload')
    status = requests.post(url, json=payload).status_code
    return True if status == 204 else False

if __name__ == '__main__':

    from time import sleep
    from datetime import datetime
    from colorama import init, Fore, Style
    init()

    webhook_url = str(input("Webhook URL: \n > "))
    name        = str(input("Webhook name: \n > "))
    count       = int(input("Message count: \n > "))

    choice = str(input('Do you want to use a custom embed file? y/n (example: https://discohook.org/ ) \n > '))
    if choice == 'y':
        payload_file = str(input('Enter file name (example.json) \n > '))
        import json
        with open(payload_file, 'r') as content:
            payload = json.load(content)
            message = None
    else: 
        message = str(input('Message: \n > '))
        payload = None

    for _ in range(count):
        try:
            status = webhookSend(url=webhook_url, name=name, message=message, payload=payload)
            if status:
                print(f'{Fore.GREEN + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Message sent successfully.', Fore.WHITE + Style.NORMAL)
            else:
                print(f'{Fore.RED + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] An error occured !', Fore.WHITE + Style.NORMAL)
        except requests.exceptions.MissingSchema:
            print(f'{Fore.RED + Style.BRIGHT}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] This webhook doesn\'t exist !', Fore.WHITE + Style.NORMAL)
            break
        finally:
            sleep(0.5)