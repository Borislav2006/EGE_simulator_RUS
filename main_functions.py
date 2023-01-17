import logging
import asyncio
import json
import jmespath
import markups as nav
from contextlib import suppress
from aiogram import Dispatcher, Bot, types
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound
from db import Database
from config import *
from other_functions import *
from random import choice

# Инициализируем бота
bot = Bot(token=BOT_TOKEN)  # Объект класса Bot
dp = Dispatcher(bot)  # Создали объект класса Dispatcher (нужен для хэндлеров)

# Включаем логирование, чтобы не пропустить важные сообщения красного цвета
logging.basicConfig(level=logging.INFO)

db = Database('database.db')

with open('tasks.json', encoding='utf-8') as json_file:
    WHOLE_THEORY = json.loads(json_file.read())  # Переменная, в которой хранится вся теория курса в формате JSON


class Message:
    """
     Класс работает с сообщениями:
     1) способен удалять сообщения
     2) способен печатать информацию, теорию, викторины и т.п. """

    answered_the_quiz = []

    def __init__(self):
        self.text_of_quiz_kind = read_text_file("Information\\text_of_quiz_kind")
        self.points_for_tasks = {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 3,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1,
            19: 1,
            20: 1,
            21: 1,
            22: 1,
            24: 1,
            25: 1,
            26: 1
        }

    @staticmethod
    async def delete_messages(message: types.Message, sleep_time: int = 0):
        """ Метод, способный удалять большие объекты: картинки, викторины и другое """
        await asyncio.sleep(sleep_time)  # Можно настроить время удаления
        with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
            await message.delete()

    @staticmethod
    async def del_last_message(human_id):
        """ Метод, удаляющий предыдущее сообщение """
        await bot.delete_message(human_id.from_user.id, human_id.message.message_id)

    async def del_output_text(self, text, human_id, menu=None):
        """ Метод, удаляющий предыдущее сообщение и печатающий текст с меню/без меню """
        await self.del_last_message(human_id)  # Удаляем предыдущее сообщение
        if menu is None:  # Если меню нет
            await bot.send_message(human_id.from_user.id, text, parse_mode="HTML")  # То выводим текст
        else:  # Иначе выводим текст с меню
            await bot.send_message(human_id.from_user.id, text, reply_markup=eval(f"nav.{menu}"), parse_mode="HTML")

    @staticmethod
    async def output_text(text, human_id, menu=None):
        """ Метод, печатающий текст с меню/без меню """
        if menu is None:  # Если меню нет
            await bot.send_message(human_id.from_user.id, text, parse_mode="HTML")  # То выводим текст
        else:  # Иначе выводим текст с меню
            await bot.send_message(human_id.from_user.id, text, reply_markup=eval(f"nav.{menu}"), parse_mode="HTML")

    async def output_of_quiz_kind(self, task_number, human_id, menu=None):
        """ Метод, печатающий виды викторины """
        await self.del_output_text(self.text_of_quiz_kind.format(task_number), human_id, menu)

    async def output_any_random_quiz(self, task_number, human_id, is_option_2=False, random_quiz=None):
        """ Метод, удаляющий предыдущее сообщение, печатающий любую рандомную викторину """
        if not is_option_2:
            await self.del_last_message(human_id)
            random_quiz = choice(jmespath.search(f"task_{task_number}.*", WHOLE_THEORY))
        db.set_task_number(human_id.from_user.id, task_number)
        db.set_random_quiz(human_id.from_user.id, json.dumps(random_quiz))
        if random_quiz["quiz_condition"]:
            photo_conditions = types.MediaGroup()
            photo_conditions.attach_photo(types.InputFile(random_quiz["quiz_condition"]))
            await bot.send_media_group(human_id.from_user.id, media=photo_conditions)
        if random_quiz["photo_of_answer_options"]:
            photo_of_answer_options = types.MediaGroup()
            photo_of_answer_options.attach_photo(types.InputFile(random_quiz["photo_of_answer_options"]))
            await bot.send_media_group(human_id.from_user.id, media=photo_of_answer_options)
        quiz_question = read_text_file(random_quiz["quiz_question"])
        await bot.send_poll(human_id.from_user.id,
                            quiz_question,
                            random_quiz["quiz_answer_options"],
                            correct_option_id=random_quiz["correct_answer_to_the_quiz"],
                            type='quiz',
                            is_anonymous=False)

        @dp.poll_answer_handler()
        async def handle_poll_answer(answer: types.PollAnswer):
            """ Функция для обработки рандомной викторины """
            rndm_quiz = json.loads(db.get_random_quiz(answer.user.id))
            number_task = db.get_task_number(human_id.from_user.id)
            json_list_of_quizzes = db.get_list_of_quizzes(answer.user.id, number_task)
            if not json_list_of_quizzes:
                list_of_quizzes = []
            else:
                list_of_quizzes = json.loads(json_list_of_quizzes)

            if answer.option_ids[0] != rndm_quiz["correct_answer_to_the_quiz"]:  # Если ответ неверный, то
                if rndm_quiz["quiz_number"] not in list_of_quizzes:
                    list_of_quizzes.append(rndm_quiz["quiz_number"])
                    await bot.send_message(answer.user.id,
                                           f"Ничего страшного! Теперь эта викторина занесена в раздел неверно решенных "
                                           f"викторин этого задания ЕГЭ. Потеряно баллов за неверно решенную викторину: {self.points_for_tasks[number_task]}")
                    db.set_list_of_quizzes(answer.user.id, number_task, json.dumps(list_of_quizzes))
                else:
                    await bot.send_message(answer.user.id,
                                           f"Ничего страшного! Потеряно баллов за неверно решенную викторину: {self.points_for_tasks[number_task]}")
            else:  # Если ответ пользователя верный, то
                if rndm_quiz["quiz_number"] in list_of_quizzes:
                    list_of_quizzes.remove(rndm_quiz["quiz_number"])
                    await bot.send_message(answer.user.id,
                                           f"Поздравляю! Теперь эта викторина убрана из раздела неверно решенных "
                                           f"викторин для этого задания ЕГЭ. Приобретено баллов за верно решенную "
                                           f"викторину: {self.points_for_tasks[number_task]}")
                    db.set_list_of_quizzes(answer.user.id, number_task, json.dumps(list_of_quizzes))
                else:
                    await bot.send_message(answer.user.id,
                                           f"Поздравляю! Вы верно решили викторину для этого задания ЕГЭ. Приобретено "
                                           f"баллов за верно решенную викторину: {self.points_for_tasks[number_task]}")

    async def output_random_unsolved_quiz(self, task_number, human_id):
        await self.del_last_message(human_id)
        json_list_of_quizzes = db.get_list_of_quizzes(human_id.from_user.id, task_number)
        if not json_list_of_quizzes or json_list_of_quizzes == "[]":
            await self.output_text("По этому заданию у Вас нет неверно решенных викторин!", human_id)
        else:
            list_of_quizzes = json.loads(json_list_of_quizzes)
            number_random_quiz = choice(list_of_quizzes)
            random_quiz = WHOLE_THEORY[f"task_{task_number}"][f"quiz_{number_random_quiz}"]
            await self.output_any_random_quiz(task_number, human_id, is_option_2=True, random_quiz=random_quiz)


ms = Message()  # Экземпляр класса Message

"""

<b> ... </b> - Жирный текст

<i> ... </i> - Курсивный текст

<u> ... </u> - Подчеркнутый текст

<del> ... </del> - Зачеркнутый текст

<code> ... </code> - моно-шрифт

&lt;html&gt;Вопрос&lt;/html&gt; -> <html>Вопрос</html> ->

<a href='https://www.python.org/'>здесь</a>    -> ссылка

Чтобы вставить HTML код в сообщение блога, чтобы он не интерпретировался 
как команды HTML, нужно все символы < заменить на &lt;, а символы > на &gt;

"""
