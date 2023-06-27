import os

from telethon import sync, events
from telethon import TelegramClient

api_id = 10074413
api_hash = 'ccb515905c0c4c581b99525e9ac15328'
akks = os.listdir('C:\\Users\\valer\\OneDrive\\Рабочий стол\\telethon\\akes')

def obr(func):
    print('start')
    func()
    print('end')
@obr
def main():
    for i in akks:
        session = "akes/" + i
        client = TelegramClient(session, api_id, api_hash)
        print(session)
        client.start()
        print(client.get_me().first_name)
        client.disconnect()

if __name__ == '__main__':
    main()