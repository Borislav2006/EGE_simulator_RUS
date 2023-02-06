from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

# --- Кнопки главного меню ---

info_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_list = KeyboardButton("Тренироваться 🥸")

info_menu.add(btn_list)

# Виды викторины

quiz_menu_1 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_1 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_1")
btn_quiz_option_2_1 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_1")
btn_main_back = InlineKeyboardMarkup(text="🔙 Назад", callback_data="btn_main_back")

quiz_menu_1.insert(btn_quiz_option_1_1)
quiz_menu_1.insert(btn_quiz_option_2_1)
quiz_menu_1.insert(btn_main_back)

quiz_menu_2 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_2 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_2")
btn_quiz_option_2_2 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_2")

quiz_menu_2.insert(btn_quiz_option_1_2)
quiz_menu_2.insert(btn_quiz_option_2_2)
quiz_menu_2.insert(btn_main_back)

quiz_menu_3 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_3 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_3")
btn_quiz_option_2_3 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_3")

quiz_menu_3.insert(btn_quiz_option_1_3)
quiz_menu_3.insert(btn_quiz_option_2_3)
quiz_menu_3.insert(btn_main_back)

quiz_menu_4 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_4 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_4")
btn_quiz_option_2_4 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_4")

quiz_menu_4.insert(btn_quiz_option_1_4)
quiz_menu_4.insert(btn_quiz_option_2_4)
quiz_menu_4.insert(btn_main_back)

quiz_menu_5 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_5 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_5")
btn_quiz_option_2_5 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_5")

quiz_menu_5.insert(btn_quiz_option_1_5)
quiz_menu_5.insert(btn_quiz_option_2_5)
quiz_menu_5.insert(btn_main_back)

quiz_menu_6 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_6 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_6")
btn_quiz_option_2_6 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_6")

quiz_menu_6.insert(btn_quiz_option_1_6)
quiz_menu_6.insert(btn_quiz_option_2_6)
quiz_menu_6.insert(btn_main_back)

quiz_menu_7 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_7 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_7")
btn_quiz_option_2_7 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_7")

quiz_menu_7.insert(btn_quiz_option_1_7)
quiz_menu_7.insert(btn_quiz_option_2_7)
quiz_menu_7.insert(btn_main_back)

quiz_menu_8 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_8 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_8")
btn_quiz_option_2_8 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_8")

quiz_menu_8.insert(btn_quiz_option_1_8)
quiz_menu_8.insert(btn_quiz_option_2_8)
quiz_menu_8.insert(btn_main_back)

quiz_menu_9 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_9 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_9")
btn_quiz_option_2_9 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_9")

quiz_menu_9.insert(btn_quiz_option_1_9)
quiz_menu_9.insert(btn_quiz_option_2_9)
quiz_menu_9.insert(btn_main_back)

quiz_menu_10 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_10 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_10")
btn_quiz_option_2_10 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_10")

quiz_menu_10.insert(btn_quiz_option_1_10)
quiz_menu_10.insert(btn_quiz_option_2_10)
quiz_menu_10.insert(btn_main_back)

quiz_menu_11 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_11 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_11")
btn_quiz_option_2_11 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_11")

quiz_menu_11.insert(btn_quiz_option_1_11)
quiz_menu_11.insert(btn_quiz_option_2_11)
quiz_menu_11.insert(btn_main_back)

quiz_menu_12 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_12 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_12")
btn_quiz_option_2_12 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_12")

quiz_menu_12.insert(btn_quiz_option_1_12)
quiz_menu_12.insert(btn_quiz_option_2_12)
quiz_menu_12.insert(btn_main_back)

quiz_menu_13 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_13 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_13")
btn_quiz_option_2_13 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_13")

quiz_menu_13.insert(btn_quiz_option_1_13)
quiz_menu_13.insert(btn_quiz_option_2_13)
quiz_menu_13.insert(btn_main_back)

quiz_menu_14 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_14 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_14")
btn_quiz_option_2_14 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_14")

quiz_menu_14.insert(btn_quiz_option_1_14)
quiz_menu_14.insert(btn_quiz_option_2_14)
quiz_menu_14.insert(btn_main_back)

quiz_menu_15 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_15 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_15")
btn_quiz_option_2_15 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_15")

quiz_menu_15.insert(btn_quiz_option_1_15)
quiz_menu_15.insert(btn_quiz_option_2_15)
quiz_menu_15.insert(btn_main_back)

quiz_menu_16 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_16 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_16")
btn_quiz_option_2_16 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_16")

quiz_menu_16.insert(btn_quiz_option_1_16)
quiz_menu_16.insert(btn_quiz_option_2_16)
quiz_menu_16.insert(btn_main_back)

quiz_menu_17 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_17 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_17")
btn_quiz_option_2_17 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_17")

quiz_menu_17.insert(btn_quiz_option_1_17)
quiz_menu_17.insert(btn_quiz_option_2_17)
quiz_menu_17.insert(btn_main_back)

quiz_menu_18 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_18 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_18")
btn_quiz_option_2_18 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_18")

quiz_menu_18.insert(btn_quiz_option_1_18)
quiz_menu_18.insert(btn_quiz_option_2_18)
quiz_menu_18.insert(btn_main_back)

quiz_menu_19 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_19 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_19")
btn_quiz_option_2_19 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_19")

quiz_menu_19.insert(btn_quiz_option_1_19)
quiz_menu_19.insert(btn_quiz_option_2_19)
quiz_menu_19.insert(btn_main_back)

quiz_menu_20 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_20 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_20")
btn_quiz_option_2_20 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_20")

quiz_menu_20.insert(btn_quiz_option_1_20)
quiz_menu_20.insert(btn_quiz_option_2_20)
quiz_menu_20.insert(btn_main_back)

quiz_menu_21 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_21 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_21")
btn_quiz_option_2_21 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_21")

quiz_menu_21.insert(btn_quiz_option_1_21)
quiz_menu_21.insert(btn_quiz_option_2_21)
quiz_menu_21.insert(btn_main_back)

quiz_menu_22 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_22 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_22")
btn_quiz_option_2_22 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_22")

quiz_menu_22.insert(btn_quiz_option_1_22)
quiz_menu_22.insert(btn_quiz_option_2_22)
quiz_menu_22.insert(btn_main_back)

quiz_menu_23 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_23 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_23")
btn_quiz_option_2_23 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_23")

quiz_menu_23.insert(btn_quiz_option_1_23)
quiz_menu_23.insert(btn_quiz_option_2_23)
quiz_menu_23.insert(btn_main_back)

quiz_menu_24 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_24 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_24")
btn_quiz_option_2_24 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_24")

quiz_menu_24.insert(btn_quiz_option_1_24)
quiz_menu_24.insert(btn_quiz_option_2_24)
quiz_menu_24.insert(btn_main_back)

quiz_menu_25 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_25 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_25")
btn_quiz_option_2_25 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_25")

quiz_menu_25.insert(btn_quiz_option_1_23)
quiz_menu_25.insert(btn_quiz_option_2_23)
quiz_menu_25.insert(btn_main_back)

quiz_menu_26 = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1_26 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1_26")
btn_quiz_option_2_26 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2_26")

quiz_menu_26.insert(btn_quiz_option_1_24)
quiz_menu_26.insert(btn_quiz_option_2_24)
quiz_menu_26.insert(btn_main_back)

# --- Задачи и их описание ---

main_menu = InlineKeyboardMarkup(row_width=7)

btn_number_1 = InlineKeyboardMarkup(text="№1", callback_data="btn_number_1")
btn_number_2 = InlineKeyboardMarkup(text="№2", callback_data="btn_number_2")
btn_number_3 = InlineKeyboardMarkup(text="№3", callback_data="btn_number_3")
btn_number_4 = InlineKeyboardMarkup(text="№4", callback_data="btn_number_4")
btn_number_5 = InlineKeyboardMarkup(text="№5", callback_data="btn_number_5")
btn_number_6 = InlineKeyboardMarkup(text="№6", callback_data="btn_number_6")
btn_number_7 = InlineKeyboardMarkup(text="№7", callback_data="btn_number_7")
btn_number_8 = InlineKeyboardMarkup(text="№8", callback_data="btn_number_8")
btn_number_9 = InlineKeyboardMarkup(text="№9", callback_data="btn_number_9")
btn_number_10 = InlineKeyboardMarkup(text="№10", callback_data="btn_number_10")
btn_number_11 = InlineKeyboardMarkup(text="№11", callback_data="btn_number_11")
btn_number_12 = InlineKeyboardMarkup(text="№12", callback_data="btn_number_12")
btn_number_13 = InlineKeyboardMarkup(text="№13", callback_data="btn_number_13")
btn_number_14 = InlineKeyboardMarkup(text="№14", callback_data="btn_number_14")
btn_number_15 = InlineKeyboardMarkup(text="№15", callback_data="btn_number_15")
btn_number_16 = InlineKeyboardMarkup(text="№16", callback_data="btn_number_16")
btn_number_17 = InlineKeyboardMarkup(text="№17", callback_data="btn_number_17")
btn_number_18 = InlineKeyboardMarkup(text="№18", callback_data="btn_number_18")
btn_number_19 = InlineKeyboardMarkup(text="№19", callback_data="btn_number_19")
btn_number_20 = InlineKeyboardMarkup(text="№20", callback_data="btn_number_20")
btn_number_21 = InlineKeyboardMarkup(text="№21", callback_data="btn_number_21")
btn_number_22 = InlineKeyboardMarkup(text="№22", callback_data="btn_number_22")
btn_number_23 = InlineKeyboardMarkup(text="№23", callback_data="btn_number_23")
btn_number_24 = InlineKeyboardMarkup(text="№24", callback_data="btn_number_24")
btn_number_25 = InlineKeyboardMarkup(text="№25", callback_data="btn_number_25")
btn_number_26 = InlineKeyboardMarkup(text="№26", callback_data="btn_number_26")

main_menu.insert(btn_number_1)
main_menu.insert(btn_number_2)
main_menu.insert(btn_number_3)
main_menu.insert(btn_number_4)
main_menu.insert(btn_number_5)
main_menu.insert(btn_number_6)
main_menu.insert(btn_number_7)
main_menu.insert(btn_number_8)
main_menu.insert(btn_number_9)
main_menu.insert(btn_number_10)
main_menu.insert(btn_number_11)
main_menu.insert(btn_number_12)
main_menu.insert(btn_number_13)
main_menu.insert(btn_number_14)
main_menu.insert(btn_number_15)
main_menu.insert(btn_number_16)
main_menu.insert(btn_number_17)
main_menu.insert(btn_number_18)
main_menu.insert(btn_number_19)
main_menu.insert(btn_number_20)
main_menu.insert(btn_number_21)
main_menu.insert(btn_number_22)
main_menu.insert(btn_number_23)
main_menu.insert(btn_number_24)
main_menu.insert(btn_number_25)
main_menu.insert(btn_number_26)
