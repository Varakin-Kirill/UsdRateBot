import logging
import asyncio
from aiogram import Bot, Dispatcher, Router
import main_handler
import os
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)

load_dotenv()

dp = Dispatcher()
bot = Bot(token=os.environ.get("BOT_TOKEN"))


async def main():
    dp.include_router(main_handler.router)
    await dp.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    asyncio.run(main())
