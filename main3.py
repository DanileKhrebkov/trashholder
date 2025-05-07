import asyncio
from dataclasses import dataclass
@dataclass
class FakeAPI:
    base_url:str

    async def get_data(self, endpoint):
        print("Запрос отправлен", self.base_url, endpoint)
        await asyncio.sleep(2)
        print(f"Ответ по API адресу {self.base_url}/{endpoint} получен")
        return f"Данные с {endpoint}"

async def main():
    api = FakeAPI("https://sample.ru/")
    data1 = await api.get_data("user/1")
    data2 = await api.get_data("post/1")
    print(data1)
    print(data2)

asyncio.run(main())