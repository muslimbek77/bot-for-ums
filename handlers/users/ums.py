from aiogram.types import Message, InlineQuery, InlineQueryResultArticle,InputLocationMessageContent,InlineQueryResultLocation,InputTextMessageContent
from loader import dp,db,ADMINS
from filters.admin import IsBotAdminFilter
from aiogram import F
from uuid import uuid4

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


@dp.inline_query()
async def inline_search(query: InlineQuery):
    results = []
    search_text = query.query.lower()

    if search_text.isdigit():
        # Search by ID if the query is a digit
        malumot = db.get_ums(search_text)
        if malumot:
            id, name, lat, lon, address, contact = malumot
            result_text = (
                f"ID: {id}\n"
                f"Name: {name}\n"
                f"Address: {address}\n"
                f"Contact: {contact}\n"
                # f"Latitude: {lat}\n"
                # f"Longitude: {lon}"
            )

            # Result as a text message
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title=f"{name} ma'lumotlari",
                    input_message_content=InputTextMessageContent(message_text=result_text),
                    description=f"{result_text}",
                )
            )

            # Result as a location message
            results.append(
                InlineQueryResultLocation(
                    id=str(uuid4()),
                    title=f"{name} Manzili",
                    latitude=float(lat),
                    longitude=float(lon),
                    input_message_content=InputLocationMessageContent(
                        latitude=float(lat),
                        longitude=float(lon),
                        # live_period=60  # Optional live period
                    ),
                    description=f"{result_text}",
                )
            )
    else:
        # Search by name if the query is not a digit
        malumot = db.get_ums_name(search_text)
        if malumot:
            id, name, lat, lon, address, contact = malumot
            result_text = (
                f"ID: {id}\n"
                f"Name: {name}\n"
                f"Address: {address}\n"
                f"Contact: {contact}\n"
                # f"Latitude: {lat}\n"
                # f"Longitude: {lon}"
            )

            # Result as a text message
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title=f"{name} ma'lumotlari",
                    input_message_content=InputTextMessageContent(message_text=result_text),
                    description=f"{result_text}",
                )
            )

            # Result as a location message
            results.append(
                InlineQueryResultLocation(
                    id=str(uuid4()),
                    title=f"{name} Manzili",
                    latitude=float(lat),
                    longitude=float(lon),
                    input_message_content=InputLocationMessageContent(
                        latitude=float(lat),
                        longitude=float(lon),
                        # live_period=60  # Optional live period
                    ),
                    description=f"{result_text}",
                )
            )

    # Return the results
    if results:
        await query.answer(results, cache_time=5)
    else:
        await query.answer([], switch_pm_text="Topilmadi", switch_pm_parameter="inline_no_results")