from aiogram import executor
from main_functions import *

# ms - экземпляр класса Message(), который работает с сообщениями: удалением, отправкой..
# db - экземпляр класса Database(), который работает с базой данных пользователей


@dp.message_handler(commands=['start'])  # Если встретится команда /start, то сработает наша функция
async def start(message: types.Message):
    await ms.output_text(f'Здравствуйте, <b>{message.from_user.first_name}</b>!\n{read_text_file("Information/Приветствие")}',
                         message, "info_menu")
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)


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
            await ms.output_of_quiz_kind(1, osn_base, "quiz_menu_1")

            @dp.callback_query_handler(text='btn_quiz_option_1_1')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=1, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_1')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=1, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_2')
        async def number_2(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(2, osn_base, "quiz_menu_2")

            @dp.callback_query_handler(text='btn_quiz_option_1_2')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=2, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_2')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=2, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_3')
        async def number_3(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(3, osn_base, "quiz_menu_3")

            @dp.callback_query_handler(text='btn_quiz_option_1_3')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=3, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_3')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=3, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_4')
        async def number_4(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(4, osn_base, "quiz_menu_4")

            @dp.callback_query_handler(text='btn_quiz_option_1_4')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=4, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_4')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=4, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_5')
        async def number_5(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(5, osn_base, "quiz_menu_5")

            @dp.callback_query_handler(text='btn_quiz_option_1_5')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=5, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_5')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=5, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_6')
        async def number_6(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(6, osn_base, "quiz_menu_6")

            @dp.callback_query_handler(text='btn_quiz_option_1_6')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=6, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_6')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=6, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_7')
        async def number_7(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(7, osn_base, "quiz_menu_7")

            @dp.callback_query_handler(text='btn_quiz_option_1_7')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=7, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_7')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=7, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_8')
        async def number_8(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(8, osn_base, "quiz_menu_8")

            @dp.callback_query_handler(text='btn_quiz_option_1_8')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=8, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_8')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=8, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_9')
        async def number_9(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(9, osn_base, "quiz_menu_9")

            @dp.callback_query_handler(text='btn_quiz_option_1_9')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=9, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_9')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=9, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_10')
        async def number_10(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(10, osn_base, "quiz_menu_10")

            @dp.callback_query_handler(text='btn_quiz_option_1_10')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=10, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_10')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=10, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_11')
        async def number_11(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(11, osn_base, "quiz_menu_11")

            @dp.callback_query_handler(text='btn_quiz_option_1_11')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=11, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_11')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=11, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_12')
        async def number_12(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(12, osn_base, "quiz_menu_12")

            @dp.callback_query_handler(text='btn_quiz_option_1_12')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=12, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_12')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=12, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_13')
        async def number_13(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(13, osn_base, "quiz_menu_13")

            @dp.callback_query_handler(text='btn_quiz_option_1_13')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=13, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_13')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=13, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_14')
        async def number_14(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(14, osn_base, "quiz_menu_14")

            @dp.callback_query_handler(text='btn_quiz_option_1_14')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=14, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_14')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=14, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_15')
        async def number_15(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(15, osn_base, "quiz_menu")

            @dp.callback_query_handler(text='btn_quiz_option_1_15')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=15, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_15')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=15, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_16')
        async def number_16(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(16, osn_base, "quiz_menu_16")

            @dp.callback_query_handler(text='btn_quiz_option_1_16')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=16, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_16')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=16, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_17')
        async def number_17(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(17, osn_base, "quiz_menu_17")

            @dp.callback_query_handler(text='btn_quiz_option_1_17')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=17, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_17')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=17, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_18')
        async def number_18(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(18, osn_base, "quiz_menu_18")

            @dp.callback_query_handler(text='btn_quiz_option_1_18')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=18, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_18')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=18, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_19')
        async def number_19(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(19, osn_base, "quiz_menu_19")

            @dp.callback_query_handler(text='btn_quiz_option_1_19')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=19, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_19')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=19, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_20')
        async def number_20(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(20, osn_base, "quiz_menu_20")

            @dp.callback_query_handler(text='btn_quiz_option_1_20')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=20, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_20')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=20, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_21')
        async def number_21(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(21, osn_base, "quiz_menu_21")

            @dp.callback_query_handler(text='btn_quiz_option_1_21')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=21, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_21')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=21, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_22')
        async def number_22(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(22, osn_base, "quiz_menu_22")

            @dp.callback_query_handler(text='btn_quiz_option_1_22')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=22, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_22')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=22, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_23')
        async def number_23(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(23, osn_base, "quiz_menu_23")

            @dp.callback_query_handler(text='btn_quiz_option_1_23')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=23, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_23')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=23, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_24')
        async def number_24(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(24, osn_base, "quiz_menu_24")

            @dp.callback_query_handler(text='btn_quiz_option_1_24')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=24, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_24')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=24, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_25')
        async def number_25(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(25, osn_base, "quiz_menu_25")

            @dp.callback_query_handler(text='btn_quiz_option_1_25')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=25, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_25')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=25, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)

        @dp.callback_query_handler(text='btn_number_26')
        async def number_26(osn_base: types.CallbackQuery):
            await ms.output_of_quiz_kind(26, osn_base, "quiz_menu_26")

            @dp.callback_query_handler(text='btn_quiz_option_1_26')
            async def quiz_option_1(option_1: types.CallbackQuery):
                """ Первый вариант викторины """
                await ms.output_any_random_quiz(task_number=26, human_id=option_1)

            @dp.callback_query_handler(text='btn_quiz_option_2_26')
            async def quiz_option_2(option_2: types.CallbackQuery):
                """ Второй вариант викторины """
                await ms.output_random_unsolved_quiz(task_number=26, human_id=option_2)

            @dp.callback_query_handler(text='btn_main_back')
            async def back_main_menu(back: types.CallbackQuery):
                """ Функция, возвращающая меню базы """
                await ms.del_last_message(back)
                await send_main_menu(back)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
