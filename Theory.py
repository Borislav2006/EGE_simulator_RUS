import json
import jmespath
from pprint import pprint
from random import choice, shuffle
from trash import rubbish

Data = {
    "task_1": {
        "quiz_1": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_1.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_1",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Потому что", "Что", "Так как", "Но"],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None, 
            "quiz_note": None
        },
        "quiz_2": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_2.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_2",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Именно", "Разве", "Только", "Неужели"],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None, 
            "quiz_note": None
        },
        "quiz_3": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_3.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_3",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Но", "Потому что", "Когда", "Только"],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None, 
            "quiz_note": None
        },
        "quiz_4": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_4.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_4",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Ней", "Книге", "Него", "Которой"],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None, 
            "quiz_note": None
        },
        "quiz_5": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_5.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_5",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Такой", "Нашей", "Моей", "Их"],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None, 
            "quiz_note": None
        },
        "quiz_6": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_6.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_6",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Поэтому", "Конечно", "Думаю", "Полагаю"],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None, 
            "quiz_note": None
        },
        "quiz_7": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_7.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_7",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Как", "Не", "Это", "Просто"],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None, 
            "quiz_note": None
        },
        "quiz_8": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_8.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_8",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["Как раз", "Именно", "Точно", "Лишь"],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None, 
            "quiz_note": None
        },
        "quiz_9": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_9.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_9",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_10": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_10.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_10",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_11": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_11.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_11",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_12": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_12.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_12",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_13": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_13.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_13",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_14": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_14.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_14",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_15": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_15.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_15",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_16": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_16.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_16",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_17": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_17.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_17",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_18": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_18.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_18",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_19": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_19.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_19",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_20": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_20.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_20",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_21": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_21.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_21",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_22": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_22.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_22",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_23": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_23.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_23",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_24": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_24.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_24",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_25": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_25.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_25",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_26": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_26.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_26",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_27": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_27.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_27",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_28": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_28.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_28",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_29": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_29.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_29",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_30": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_30.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_30",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_31": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_31.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_31",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_32": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_32.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_32",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_33": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_33.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_33",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_34": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_34.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_34",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_35": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_35.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_35",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_36": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_36.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_36",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_37": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_37.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_37",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_38": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_38.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_38",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_39": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_39.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_39",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_40": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_40.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_40",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_41": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_41.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_41",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_42": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_42.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_42",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_43": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_43.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_43",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_44": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_44.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_44",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_45": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_45.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_45",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_46": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_46.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_46",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_47": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_47.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_47",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_48": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_48.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_48",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_49": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_49.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_49",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_50": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_50.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_50",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 1,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_51": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_51.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_51",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 2,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_52": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_52.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_52",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 3,
            "quiz_explanation": None,
            "quiz_note": None
        },
        "quiz_53": {
            "quiz_condition": "Tasks_materials\\conditions_of_quizzes\\task_1\\quiz_53.png",
            "quiz_question": "Tasks_materials\\questions_for_quizzes\\task_1\\quiz_53",
            "photo_of_answer_options": None,
            "quiz_answer_options": ["", "", "", ""],
            "correct_answer_to_the_quiz": 0,
            "quiz_explanation": None,
            "quiz_note": None
        }
    }
}


print(choice(jmespath.search("task_1.*", Data)))
