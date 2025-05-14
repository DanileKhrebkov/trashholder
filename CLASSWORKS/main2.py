import asyncio
import time
async def fetch_data():
    print("Начинает загружать данные...")
    await asyncio.sleep(5)
    print("Данные загружены")
    return "результат"

async def convert_data():
    print(f'Начинает обработку данных')
    await asyncio.sleep(2)
    print("Данные обработаны")

ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(fetch_data()),
    ioloop.create_task(convert_data())
    ]
tasks_for_wait = asyncio.wait(tasks)
ioloop.run_until_complete(tasks_for_wait)
ioloop.close(  )