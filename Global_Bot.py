import time, sys, os, subprocess
# Функция эффекта печатной машинки
def teleprint(*args, delay=0.03, str_join=' '):
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        if i == n:
            char = f'{char}\n'
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
# Функция эффекта печатной машинки
def teleprint2(*args, delay=0.02, str_join=' '):
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        if i == n:
            char = f'{char}'
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
# Приветствие-----------------------------------------------------
begin_msg = "--\nMain_Parser_Bot ENABLE..."
creator = "\nCreator:Tom Jefferson"
version = "\nVersion 2.03\n--"
teleprint(begin_msg, creator, version)
# Настройка времени-----------------------------------------------------
time_main = 0    #! Переменная к которой плюсуется секунда
x_time = 240      #! Время ожидания нового прогона
crash_time = 120 #! Максимальное время отведенное на прогон одного модуля (Контроль зависания)
# Скрипт прогона модулей-----------------------------------------------------
while True:
    try:
        def main_def():
            print("\n")
            global time_main
            # Угар бот вызов сабпроцеccа
            def vk_modul_ugar():
                try:
                    subprocess.call(
                        ["python", r"C:\Users\user\Desktop\Python\My_bots\Modul bots\vk_modul_ugar.py", "-i",
                         "10", "-l",
                         "2"], timeout=crash_time)
                    time.sleep(5)
                    print("\n")
                    news_modul_obwue()
                except:
                    print("Время вышло, завис модуль Ugar")
                    news_modul_obwue()
            # Бот новостей вызов сабпроцеccа
            def news_modul_obwue():
                try:
                    subprocess.call(
                        ["python", r"C:\Users\user\Desktop\Python\My_bots\Modul bots\news_modul_obwue.py", "-i",
                         "10", "-l",
                         "2"], timeout=crash_time)
                    time.sleep(5)
                    print("\n")
                    insta_modul()
                except:
                    print("Время вышло, завис модуль NEWS")
                    insta_modul()
            # Инста бот вызов сабпроцеccа
            def insta_modul():
                try:
                    subprocess.call(
                        ["python", r"C:\Users\user\Desktop\Python\My_bots\Modul bots\insta_modul.py", "-i",
                         "10", "-l",
                         "2"], timeout=crash_time)
                    time.sleep(5)
                    print("\n")
                except:
                    print("Время вышло, завис модуль INSTA")
                    pass

            vk_modul_ugar()



            time.sleep(5)
            time_main = 0


# Скрипт ожидания выполнения условия-----------------------------------------------------
        def wait():
            global time_main
            if time_main >= x_time:
                main_def()
                time_main = 0
            else:
                time_main += 1
            t_time_option = ' ' + str(x_time - time_main)
            sys.stdout.write('\r' + "Следующий прогон контента через:")
            teleprint2(t_time_option)
            time.sleep(1)
            wait()


        wait()
    except Exception:
        continue
#-----------------------------------------------------
