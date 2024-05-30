from loader import dp
from aiogram.types import Message
from aiogram.filters import Command


@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("Sizga qanday yordam kerak")

