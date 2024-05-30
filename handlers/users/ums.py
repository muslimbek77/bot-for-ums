from aiogram.types import Message
from loader import dp,db,ADMINS
from filters.admin import IsBotAdminFilter
from aiogram import F

@dp.message(F.text.isdigit(),IsBotAdminFilter(ADMINS))
async def get_nav_codes(message:Message):
    try:
        text = message.text
        malumot = db.get_ums(text)
        # print(malumot)
        id = malumot[0]
        name = malumot[1]
        lat = malumot[2]
        lon = malumot[3]
        address = malumot[4]
        contact = malumot[5]
        text = f"ID: {id}\nName: {name}\nAddress: {address}\nContact: {contact}\nLatitude: {lat}\nLongitude: {lon}"
        await message.answer(text=text)
        await message.answer_location(latitude=float(lat),longitude=float(lon))
    except:
        await message.answer(text="Malumot topilmadi")
@dp.message(F.text,IsBotAdminFilter(ADMINS))
async def get_nav_name(message:Message):
    try:
        text = message.text.lower()
        malumot = db.get_ums_name(text)
        # print(malumot)
        id = malumot[0]
        name = malumot[1]
        lat = malumot[2]
        lon = malumot[3]
        address = malumot[4]
        contact = malumot[5]
        text = f"ID: {id}\nName: {name}\nAddress: {address}\nContact: {contact}\nLatitude: {lat}\nLongitude: {lon}"
        await message.answer(text=text)
        await message.answer_location(latitude=float(lat),longitude=float(lon))
    except:
        await message.answer(text="Malumot topilmadi")
