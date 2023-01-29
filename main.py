from aiogram import executor
from main_functions import *

# ms - экземпляр класса Message(), который работает с сообщениями: удалением, отправкой..
# db - экземпляр класса Database(), который работает с базой данных пользователей


@dp.message_handler(commands=['start'])  # Если встретится команда /start, то сработает наша функция
async def start(message: types.Message):
    if db.user_exists(message.from_user.id):  # FIXME -> ЭТУ СТРОЧКУ НУЖНО БУДЕТ УДАЛИТЬ, ОНА НУЖНА ДЛЯ ТОГО, ЧТОБЫ НЕ ВПУСКАТЬ ЛЮДЕЙ, ВРЕМЕННО!
        await ms.output_text(f'Здравствуйте, {message.from_user.first_name})\n{read_text_file("Information/Приветствие")}',
                             message, "info_menu")
        if not db.user_exists(message.from_user.id):  # Проверка на то, есть ли у нас пользователь в бд
            db.add_user(message.from_user.id)  # Если его нет, то добавляем


@dp.message_handler(content_types=['text'])
async def main_work(message: types.Message):
    if message.text == "Тренироваться 🥸":
        async def send_main_menu(report):
            await bot.send_photo(report.from_user.id, open("Information/USE_tasks_materials.png", mode="rb"),
                                 caption="<b>Выберите номер из ЕГЭ по русскому языку, который хотите потренировать:</b>",
                                 parse_mode="HTML", reply_markup=nav.main_menu)

        await send_main_menu(message)

        @dp.callback_query_handler(text='btn_number_1')
        async def number_1(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(1, osn_base, "quiz_menu")

            @dp.callback_query_handler(text='btn_quiz_option_1')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=1, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=1, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
