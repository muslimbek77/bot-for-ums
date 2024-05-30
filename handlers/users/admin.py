from loader import bot,db,dp,CHANNELS,ADMINS
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message,InlineKeyboardButton
from aiogram.filters import Command
from filters.admin import IsBotAdminFilter
from states.reklama import UMS, Adverts
from aiogram.fsm.context import FSMContext #new
from keyboard_buttons import admin_keyboard
import time 
from aiogram import F


# @dp.message(IsCheckSubChannels())
# async def kanalga_obuna(message:Message):
#     text = ""
#     inline_channel = InlineKeyboardBuilder()
#     for index,channel in enumerate(CHANNELS):
#         ChatInviteLink = await bot.create_chat_invite_link(channel)
#         inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal",url=ChatInviteLink.invite_link))
#     inline_channel.adjust(1,repeat=True)
#     button = inline_channel.as_markup()
#     await message.answer(f"{text} kanallarga azo bo'ling",reply_markup=button)



def dms_to_decimal(dms_str):#41°15'34"N 64°35'02"E
  try:
    degrees, minutes_seconds = dms_str.split("°")
    degrees = float(degrees)
    minutes, seconds_str = minutes_seconds.split("'")
    minutes = float(minutes)
    # Replace comma with decimal point and remove trailing quotation mark
    seconds = float(seconds_str.replace(',', '.').replace('"', ''))
    return float(degrees) + (float(minutes) / 60) + (seconds / 3600)
  except ValueError:
    # Handle invalid DMS format
    return None

@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)


@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

@dp.message(F.text=="Bazani o'zgartirish",IsBotAdminFilter(ADMINS))
async def edit_db(message:Message,state:FSMContext):
    await state.set_state(UMS.ums)
    await message.answer(text="O'zgartirmoqchi bo'lgan baza id sini kiriting")

@dp.message(F.text,UMS.ums)
async def edit_db_id(message:Message,state:FSMContext):
    id = message.text
    await state.update_data(id=id)
    await state.set_state(UMS.location)
    await message.answer(text="O'zgartirmoqchi bo'lgan baza locatsiyasini kiriting")

@dp.message(F.text,UMS.location)
async def edit_db_loc(message:Message,state:FSMContext):
    # try:
        lat,long = message.text.split() #40°16'26"N 65°09'28"E
        lat = dms_to_decimal(lat[:-1])
        long = dms_to_decimal(long[:-1])
        data = await state.get_data()
        id = data.get("id")
        db.set_ums_location(id,lat,long)
        await message.answer(text="Baza o'zgartirildi")
    # except:
    #     await message.answer(text="Malumot topilmadi")
        await state.clear()

@dp.message(F.text=="Yangi bazaga qo'shish",IsBotAdminFilter(ADMINS))
async def add_db(message:Message):
    await message.answer(text="Yangi bazaga qo'shish")