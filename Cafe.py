import asyncio,aiohttp
from aiogram import Bot, Dispatcher, types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = '6005870475:AAEHpN7PP1M16PMZwWzdiJHZAJ2pED_0UUE' 

loop = asyncio.get_event_loop()

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum Cafe botimizga hush kelibsiz:")
    photo = open('wot.jpg', 'rb')
    await message.answer_photo(photo, caption="caption")
    
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
