from aiogram.types import Message
from loader import dp,db
from aiogram import F
nav_codes = [
    "NAV0020", "NAV0031", "NAV0032", "NAV0035", "NAV0037", "NAV0038", "NAV0039",
    "NAV0040", "NAV0041", "NAV0042", "NAV0043", "NAV0044", "NAV0047", "NAV0048",
    "NAV0049", "NAV0050", "NAV0051", "NAV0053", "NAV0054", "NAV0055", "NAV0056",
    "NAV0073", "NAV0130", "NAV0137", "NAV0156", "NAV0168", "NAV0268", "NAV1601",
    "NAV1602", "NAV1603", "NAV1604", "NAV1605", "NAV1606", "NAV1607", "NAV1608",
    "NAV1609", "NAV1610", "NAV1611", "NAV1612", "NAV1613", "NAV1614", "NAV1615",
    "NAV1616", "NAV1617", "NAV1618", "NAV1619", "NAV1620", "NAV1621", "NAV1622",
    "NAV1624", "NAV1625", "NAV1626", "NAV1627", "NAV1628", "NAV1629", "NAV1630",
    "NAV1631", "NAV1632", "NAV1633", "NAV1634", "NAV1635", "NAV1636", "NAV1637",
    "NAV1638", "NAV1639", "NAV1640", "NAV1641", "NAV1642", "NAV1643", "NAV1644",
    "NAV1645", "NAV1646", "NAV1647", "NAV1648", "NAV1649", "NAV1650", "NAV1651",
    "NAV1652", "NAV1653", "NAV1654", "NAV1655", "NAV1656", "NAV1657", "NAV1658",
    "NAV1659", "NAV1660", "NAV1661", "NAV1662", "NAV1663", "NAV1664", "NAV1666",
    "NAV1667", "NAV1668", "NAV1669", "NAV1670", "NAV1671", "NAV1672", "NAV1674",
    "NAV1675", "NAV1676", "NAV1677", "NAV1678", "NAV1679", "NAV1680", "NAV1681",
    "NAV1683", "NAV1684", "NAV1685", "NAV1686", "NAV1687", "NAV1688", "NAV1689",
    "NAV1690", "NAV1691", "NAV1692", "NAV1693", "NAV1694", "NAV1695", "NAV1698",
    "NAV1701", "NAV1702", "NAV1703", "NAV1704", "NAV1705", "NAV1706", "NAV1707",
    "NAV1708", "NAV1710", "NAV1711", "NAV1712", "NAV1713", "NAV1714", "NAV1715",
    "NAV1716", "NAV1717", "NAV1718", "NAV1719", "NAV1720", "NAV1721", "NAV1722",
    "NAV1723", "NAV1724", "NAV1725", "NAV1726", "NAV1727","NAV0", "NAV1730", "NAV1731",
    "NAV1732", "NAV1734", "NAV1736", "NAV1737", "NAV1738", "NAV1739", "NAV1740",
    "NAV1743", "NAV1744", "NAV1745", "NAV1746", "NAV1747", "NAV1751", "NAV1752",
    "NAV1754", "NAV1755", "NAV1756", "NAV1761", "NAV1766", "NAV1767", "NAV1771",
    "NAV1772", "NAV1773", "NAV1774", "NAV1775", "NAV1776", "NAV1780", "NAV1782",
    "NAV1783", "NAV1784", "NAV1785", "NAV1786", "NAV1787", "NAV1789", "NAV1790",
    "NAV1791"
]

@dp.message(F.text.in_(nav_codes))
async def get_nav_codes(message:Message):
    text = message.text
    malumot = db.get_ums(text)
    print(malumot)
    id = malumot[0]
    name = malumot[1]
    lat = malumot[2]
    lon = malumot[3]
    address = malumot[4]
    contact = malumot[5]
    text = f"ID: {id}\nName: {name}\nAddress: {address}\nContact: {contact}"
    await message.answer(text=text)
    await message.answer_location(latitude=float(lat),longitude=float(lon))


