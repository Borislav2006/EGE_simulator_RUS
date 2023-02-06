import sqlite3


class Database:
    """ Класс для работы с базой данных """

    def __init__(self, db_file):  # db_file - переменная, по которой определяется название нашей бд
        self.connection = sqlite3.connect(db_file)  # подключение к бд
        self.cursor = self.connection.cursor()  # нужен для запросов в бд

    def add_user(self, human_id):
        """ Метод для добавления нового пользователя в бд """
        with self.connection:
            self.cursor.execute("INSERT INTO `users` (`human_id`) VALUES (?)", (human_id,))
            self.connection.commit()
            #  execute - метод для выполнения одного выражения SQL
            #  executemany - метод позволяет выполнить одно выражение SQL для последовательности параметров (или для итератора)
            #  executescript - метод позволяет выполнить несколько выражений SQL за один раз

    def user_exists(self, human_id):
        """ Метод для проверки на то, есть ли у нас в бд пользователь. Если да -> True, иначе -> False """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `human_id` = ?", (human_id,)).fetchall()
            return bool(len(result))

    def set_list_of_unsolved_quizzes(self, human_id, task_number, list_of_quizzes):
        """ Добавление списка, состоящего из номеров викторин, неверно решенных викторин, в бд """
        with self.connection:
            self.cursor.execute(f"UPDATE `users` SET `task_{task_number}` = ? WHERE `human_id` = ?", (list_of_quizzes, human_id,))
            self.connection.commit()

    def get_list_of_unsolved_quizzes(self, human_id, task_number):
        """ Получение списка, состоящего из номеров, неверно решенных викторин, из бд """
        with self.connection:
            result = self.cursor.execute(f"SELECT `task_{task_number}` FROM `users` WHERE `human_id` = ?", (human_id,)).fetchall()
            for row in result:
                check_sub = row[0]
            return check_sub

    def set_random_quiz(self, human_id, quiz):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `random_quiz` = ? WHERE `human_id` = ?", (quiz, human_id,))
            self.connection.commit()

    def get_random_quiz(self, human_id):
        with self.connection:
            result = self.cursor.execute("SELECT `random_quiz` FROM `users` WHERE `human_id` = ?", (human_id,)).fetchall()
            for row in result:
                check_sub = row[0]
            return check_sub

    def set_index_correct_answer_to_the_quiz(self, human_id, index_correct_answer):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `index_correct_answer` = ? WHERE `human_id` = ?", (index_correct_answer, human_id,))
            self.connection.commit()

    def get_index_correct_answer_to_the_quiz(self, human_id):
        with self.connection:
            result = self.cursor.execute("SELECT `index_correct_answer` FROM `users` WHERE `human_id` = ?", (human_id,)).fetchall()
            for row in result:
                check_sub = row[0]
            return check_sub

    def set_task_history(self, human_id, task_history):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `task_history` = ? WHERE `human_id` = ?", (task_history, human_id,))
            self.connection.commit()

    def get_task_history(self, human_id):
        with self.connection:
            result = self.cursor.execute("SELECT `task_history` FROM `users` WHERE `human_id` = ?", (human_id,)).fetchall()
            for row in result:
                check_sub = row[0]
            return check_sub
