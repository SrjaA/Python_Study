# import csv
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# #
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
# drive = GoogleDrive(gauth)


import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Ждём завершения обеих задач (это должно занять
    # около 2 секунд.)
    await task2
    await task1

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())








def make_uchr(code: str):
    return chr(int(code.lstrip("U+").zfill(8), 16))
print(make_uchr("U+1F4DF"))
#chr(🔧)


# with open('files/heater_last.csv', 'r', newline='', encoding='utf-8') as file:
#     l=sum(1 for line in file)
#
# with open('files/heater_last.csv', 'r', newline='', encoding='utf-8') as file:
#     file_reader = csv.reader(file, delimiter=";")
#     count = 0  # Счетчик для подсчета количества строк и вывода заголовков столбцов
#     if l>1:
#         print(f'Новинки:')
#         for row in file_reader:
#
#             # Вывод строк
#             print(f'{row[0]} : {row[1]} : {row[3]} : {row[4]}')
#             count += 1
#     else:
#         print('sdf')