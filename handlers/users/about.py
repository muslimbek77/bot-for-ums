from loader import dp
from aiogram.types import Message
from aiogram.filters import Command


@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Sifat 2024")

