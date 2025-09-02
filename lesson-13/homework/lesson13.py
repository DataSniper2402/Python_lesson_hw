# 1
from datetime import date

year = int(input('Tug‘ilgan yilingizni kiriting (YYYY): '))
month = int(input('Tug‘ilgan oyingizni kiriting (MM): '))
day = int(input('Tug‘ilgan kuningizni kiriting (DD): '))

tugilgan_sana = date(year, month, day)

bugun = date.today()

age = bugun.day - tugilgan_sana.year
if (bugun.month, bugun.day) < (tugilgan_sana.month, tugilgan_sana.day):
    yosh -= 1
print(f"Siz {age} yoshdasiz.")

# 2
from datetime import date

yil = int(input("Tug‘ilgan yilingizni kiriting (YYYY): "))
oy = int(input("Tug‘ilgan oyingizni kiriting (MM): "))
kun = int(input("Tug‘ilgan kuningizni kiriting (DD): "))

bugun = date.today()
tugilgan_sana = date(bugun.year, oy, kun)

if tugilgan_sana < bugun:
    tugilgan_sana = date(bugun.year + 1, oy, kun)

qolgan_kunlar = (tugilgan_sana - bugun).days
print(f"Keyingi tug‘ilgan kuningizgacha {qolgan_kunlar} kun qoldi.")
# 3

from datetime import datetime, timedelta

joriy = input("Joriy sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
soat = int(input("Uchrashuv davomiyligi (soat): "))
daqiqa = int(input("Uchrashuv davomiyligi (daqiqa): "))

boshlanish = datetime.strptime(joriy, "%Y-%m-%d %H:%M")
tugash = boshlanish + timedelta(hours=soat, minutes=daqiqa)

print(f"Uchrashuv tugash vaqti: {tugash}")

# 4

from datetime import datetime
import pytz

dt_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_tz = input("Hozirgi vaqt zonasi (masalan: Asia/Tashkent): ")
to_tz = input("Qaysi zonaga o‘tkazmoqchisiz (masalan: Europe/London): ")

naive = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
src_tz = pytz.timezone(from_tz)
dst_tz = pytz.timezone(to_tz)

local_dt = src_tz.localize(naive)
converted = local_dt.astimezone(dst_tz)

print("O‘zgartirilgan vaqt:", converted)


# 5

from datetime import datetime
import time

future_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
future = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    if now >= future:
        print("Vaqt tugadi!")
        break
    qolgan = future - now
    print("Qolgan vaqt:", qolgan, end="\r")
    time.sleep(1)
# 6
import re

email = input("Email manzilini kiriting: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Email manzili to‘g‘ri formatda.")
else:
    print("Noto‘g‘ri email formati.")


# 7
raqam = input("Telefon raqamini kiriting (faqat raqamlar): ")

if len(raqam) == 10:
    formatted = f"({raqam[0:3]}) {raqam[3:6]}-{raqam[6:]}"
    print("Formatlangan raqam:", formatted)
else:
    print("Xato: 10 xonali raqam kiriting.")
# 8

import re

parol = input("Parol kiriting: ")

if (len(parol) >= 8 and
    re.search(r'[A-Z]', parol) and
    re.search(r'[a-z]', parol) and
    re.search(r'[0-9]', parol)):
    print("Parol kuchli.")
else:
    print("Parol kuchsiz. (kamida 8 belgidan iborat bo‘lishi va har xil turdagi belgilar bo‘lishi kerak).")
# 9

matn = "Python dasturlash tili juda mashhur. Python oson va kuchli til."
soz = input("Qidiriladigan so‘zni kiriting: ")

joylar = []
boshi = 0
while True:
    idx = matn.find(soz, boshi)
    if idx == -1:
        break
    joylar.append(idx)
    boshi = idx + 1

if joylar:
    print(f"'{soz}' so‘zi {len(joylar)} marta uchradi. Indekslar: {joylar}")
else:
    print(f"'{soz}' so‘zi topilmadi.")
# 10

import re

matn = input("Matn kiriting: ")
pattern = r'\b\d{4}-\d{2}-\d{2}\b' 
sana_list = re.findall(pattern, matn)

if sana_list:
    print("Topilgan sanalar:", sana_list)
else:
    print("Matnda sana topilmadi.")

