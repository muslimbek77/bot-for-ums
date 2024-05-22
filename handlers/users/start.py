# from aiogram.types import Message
# from loader import dp,db
# from aiogram.filters import CommandStart


# @dp.message(CommandStart())
# async def start_command(message:Message):
#     full_name = message.from_user.full_name
#     telegram_id = message.from_user.id
#     try:
#         db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
#         await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz")
#     except:
#         await message.answer(text="Assalomu alaykum")

navoi_region = {
    "Kanimex District": [
        "Navruz MFY",
        "Istikbol MFY",
        "Zaafarabod MFY",
        "Sargal MFY",
        "Yangigazgan MFY",
        "Mamikchi MFY",
        "RU-5, GTR-1 Factory",
        "Daaugiztau MFY",
        "Daaugiztau Quarry",
        "Birlik MFY"
    ],
    "Karmana District": [
        "Shibzon MFY",
        "Vark MFY",
        "Uyrat MFY",
        "Dekhkan MFY",
        "Azamat MFY",
        "Kurgonchi MFY",
        "Argun MFY",
        "Sirdoba MFY",
        "Kalovot MFY",
        "Urtakurgon MFY",
        "Farhod MFY",
        "Urtakurgon MFY",
        "Dustlik MFY",
        "Malik MFY",
        "Uchtut MFY",
        "Bogishamol MFY",
        "Uzbekistan MFY",
        "Navruz MFY",
        "Kahramon MFY",
        "Aironchi MFY",
        "Narpay MFY",
        "Degaron MFY",
        "Kumushkon MFY",
        "Yanhi Arik MFY"
    ],
    "Kiziltepa District": [
        "Humo MFY",
        "Ziyokor MFY",
        "Gamkhur MFY",
        "Nurafshon MFY",
        "Azizabod MFY",
        "Mehnatobod MFY",
        "Khuzhakurgon MFY",
        "Gardiyon MFY",
        "Goyibon MFY",
        "Hushbidin MFY",
        "Kulolon MFY",
        "Varozun MFY",
        "Kiziltepa MFY",
        "Qalayi Azizom MFY",
        "Oxoch MFY",
        "Gumbaz MFY",
        "Vangazi MFY",
        "Sheikhon MFY"
    ],
    "Hatirchi District": [
        "Bogchakalon MFY",
        "Kuragonchi MFY",
        "Mirishkor MFY",
        "Mustaqillik MFY",
        "Tamabahron MFY",
        "Parakhun MFY",
        "Mirishkor MFY",
        "A. Pulatov MFY",
        "Chilash MFY",
        "Tasmachi MFY",
        "Sh. Rashidov MFY",
        "Tortuvli MFY",
        "Zarafshon MFY",
        "Uyshun MFY",
        "Mergan MFY",
        "Mustaqillik MFY",
        "Yangirabod MFY",
        "Duslik MFY",
        "Bachashijar MFY",
        "Navruz MFY",
        "Mustaqillik MFY",
        "Zafarabad MFY",
        "Yanhi MFY"
    ],
    "Navbakhor District": [
        "Hashman MFY",
        "Guliston MFY",
        "Yangiobod MFY",
        "Oltin MFY",
        "Halovat tepa MFY",
        "Saroy MFY",
        "Gushbog tepa MFY",
        "Karvon MFY",
        "Keskan terak MFY",
        "Ijand MFY",
        "Arab Saroy MFY",
        "Vomitan MFY",
        "Beshobod MFY",
        "Pahtakor MFY",
        "Nabkhor MFY",
        "Olchin MFY",
        "Pahtakor MFY",
        "Uzbekistan MFY"
    ],
    "Nurata District": [
        "A. Navoi MFY",
        "Ibn Sina MFY",
        "Dehibaland MFY",
        "Choya MFY",
        "Jarama MFY",
        "A. Temur MFY",
        "Nurfah MFY",
        "Yangi Turmush MFY",
        "Kadok MFY"
    ],
    "Uchkuduk District": [
        "Kokpatas Quarry",
        "Mustaqillik MFY",
        "Kuntay MFY",
        "GMZ-3 Factory",
        "Yolchilar MFY",
        "Dostlik MFY"
    ],
    "Gazgan City": [
        "Guliston MFY",
        "Marmarabot MFY"
    ],
    "Navoiy City": [
        "Ishonch MFY",
        "Yangioobod MFY",
        "Orzu MFY",
        "Istiklol MFY",
        "Guliston MFY",
        "Bunyodkor MFY",
        "Uzbekistan MFY",
        "Sarafshon MFY",
        "Humon MFY",
        "Navoi Azot",
        "Honcharbog MFY",
        "UZMFY",
        "Electrohim Factory",
        "Galaba MFY",
        "Matornat MFY",
        "Memar MFY",
        "Tinchlik MFY",
        "YPM",
        "Bunyodkor MFY",
        "Altin Vadi MFY",
        "Kimyogar MFY"
    ],
    "Zarafshan City": [
        "Kurovchi MFY",
        "Muruntao MFY",
        "Yoshik MFY",
        "Bakhri MFY",
        "Yulduz MFY",
        "Yangi Zarafshan MFY"
    ]
}

# Example usage
for district, neighborhoods in navoi_region.items():
    print(f"{district}:")
    for neighborhood in neighborhoods:
        print(f"  - {neighborhood}")

