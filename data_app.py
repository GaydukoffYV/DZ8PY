import datetime

def data_entry():
    # Функция приглашает пользователя внести данных учеников и сохранить их в файл
    print('Журнал заполнения\n')
    name = input('Введите имя ученика: ')
    family = input('Введите фамилию ученика: ')
    while True: #запускает проверку правильной даты
        try:
            birthdate = input('Введите дату рождения ученика в форме ДД.ММ.ГГГГ: ')
            if datetime.datetime.strptime(birthdate, '%d.%m.%Y'):
                break
            else:
                print("Неправильный формат данных, должен быть ДД.ММ.ГГГГ")
        except:
            print("Ошибка - это не дата")
    classroom = input('Введите класс ученика: ')
    achievement = input('Введите успеваемость ученика: ')
#     while True: # должно запускать проверку правильности ввода успеваемости
#         try:
            
#             if strptime(birthdate, 'отличник', 'хорошист', 'троичник', 'неуспевающий'):
#                 break
#             else:
#                 print("Неправильное значение, может быть: 'отличник', 'хорошист', 'троичник', 'неуспевающий'")
#         except:
#             print("Ошибка - повторите ввод")
    print(f'Вы ввели данные: {name} {family} {birthdate} {classroom} {achievement}\n')
# print(len(open('student_info.json').readlines()))

    stud_card = {
        'ID': [len(open('student_info.json').readlines())],
        'Имя' : [name],
        'Фамилия': [family],
        'Дата рождения' : [birthdate],
        'Класс' :[classroom],
        'Успеваемость' : [achievement]
        }
    with open('student_info.json', 'a') as data:
        data.write(f'{stud_card}\n')
#     print(f'Вы ввели данные: {stud_card}\n' )
    data.close()
data_entry()