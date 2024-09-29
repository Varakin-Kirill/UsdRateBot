from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from get_usd_exchange_rate import get_usd_exchange_rate


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Добрый день. Как вас зовут?")


@router.message()
async def get_name_handler(message: Message):
    if get_usd_exchange_rate != None:
        await message.answer(
            f"Рад знакомству, {message.text}! Курс доллара сегодня {get_usd_exchange_rate()}р"
        )
    else:
        await message.answer(
            f"Рад знакомству, {message.text}! Курс доллара на сегодня неизвестен"
        )
