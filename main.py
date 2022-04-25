from aiogram import executor
from misc import dp,shutdown,startup

# Импорт Хендлеров
import handlers

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True)