# telegram_reader.py

from telethon import TelegramClient
import telethon.sync
import asyncio

async def main():
    for char in 'hello world':
        print(char, end='', flush=True)
        await asyncio.sleep(0.2)

asyncio.run(main())