from telethon import TelegramClient

api_id = 21437070
api_hash = '536a8ec234fb30a183745dc45d43c4e3'

with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello!'))