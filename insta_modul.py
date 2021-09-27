import requests, telebot, re, time, os, sys, datetime as dt
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from telebot import types

insta_tg_token = []
with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\insta_tg_token.txt', 'r+') as f_news:
    insta_tg_token.append(f_news.read())

bot = telebot.TeleBot(insta_tg_token[0])

chanel_name = '@test_my_shit'
chanel_Test_my_shit_bot = '@Test_my_shit_bot'
chanel_name1 = '@ugar_non_stop'
chanel_name2 = '@news_non_stop_nayka'
chanel_name3 = '@gryazb_non_stop'
chanel_name4 = '@auto_non_stop'

# Импортируем типы из модуля, чтобы создавать кнопки
try:
    def teleprint(*args, delay=0.09, str_join=' '):
        text = str_join.join(str(x) for x in args)
        n = len(text)
        for i, char in enumerate(text, 1):
            if i == n:
                char = f'{char}\n'
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)


    in1 = []  # лист для сравнения полученных ссылок  scince0()
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\in1.txt', 'r') as f:
        in1.extend(f.read().splitlines())
        # print(in1)
    in2 = []  # лист для добавления показанных ссылок  scince0()
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\in2.txt', 'r') as f:
        in2.extend(f.read().splitlines())
        # print(in2)
    in3 = []  # лист для сравнения полученных ссылок  ugar0()
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\in3.txt', 'r') as f:
        in3.extend(f.read().splitlines())
        # print(in3)
    in4 = []  # лист для добавления показанных ссылок  ugar0()
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\in4.txt', 'r') as f:
        in4.extend(f.read().splitlines())

    # ------------------------------------ подсчет колва файлов в папках
    len_files = [0]
    len_files2 = [0]
    len_files3 = [0]
    len_files4 = [0]
    len_files5 = [0]
    # ------------------------------------ время и имя файла
    culture_time = []
    j = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\culture_time.txt', 'r+') as f_news:
        culture_time.append(f_news.read())
        # print('Загружен таймер Видео для канала культура: ', culture_time[0])
        mypath2 = r'C:\Users\user\Desktop\Python\dowload\culture_video'
        for i in listdir(mypath2):
            if isfile(joinpath(mypath2, i)):
                j.append(i)
    # ------------------------------------ время и имя файла
    culture_time2 = []
    h = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\culture_time2.txt', 'r+') as f_news:
        culture_time2.append(f_news.read())
        # print('Загружен таймер Фото для канала культура: ', culture_time2[0])
        mypath3 = r'C:\Users\user\Desktop\Python\dowload\culture_photo'
        for i in listdir(mypath3):
            if isfile(joinpath(mypath3, i)):
                h.append(i)
    # ------------------------------------ время и имя файла
    auto_time = []
    auto_name = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\auto_time.txt', 'r+') as f_news:
        auto_time.append(f_news.read())
        # print('Загружен таймер Фото для канала auto: ', auto_time[0])
        mypath4 = r'C:\Users\user\Desktop\Python\dowload\auto_photo'
        for i in listdir(mypath4):
            if isfile(joinpath(mypath4, i)):
                auto_name.append(i)
    # ------------------------------------ время и имя файла
    autoV_time = []
    autoV_name = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\autoV_time.txt', 'r+') as f_news:
        autoV_time.append(f_news.read())
        # print('Загружен таймер Видео для канала autoVideo : ', autoV_time[0])
        mypath5 = r'C:\Users\user\Desktop\Python\dowload\auto_video'
        for i in listdir(mypath5):
            if isfile(joinpath(mypath5, i)):
                autoV_name.append(i)
    # ------------------------------------ время и имя файла
    instatime = []
    k = []

    youtubetime = 0

    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\youtbTime.txt', 'r+') as f_news:
        youtubetime += int(f_news.read())
    youtubetime2 = 0
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\youtbTime2.txt', 'r+') as f_news:
        youtubetime += int(f_news.read())
        # print('YOUTUBEtime: ', youtubetime)
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\instatime.txt', 'r+') as f_news:
        instatime.append(f_news.read())
        # print('INSTAtime: ', instatime[0])
        mypath = r'C:\Users\user\Desktop\Python\dowload\new'
        for i in listdir(mypath):
            if isfile(joinpath(mypath, i)):
                k.append(i)

        # ------------------------------------
        # print(k)

    teleprint("------====INSTA_Bot ENABLE====------")

    control_time = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\4vidTime.txt', 'r') as f:
        control_time.extend(f.read().splitlines())

    def callback_worker1():

        path, dirs, files = next(os.walk(r'C:\Users\user\Desktop\Python\dowload\new'))
        file_count = len(files)
        global control_time
        now = dt.datetime.now()

        def content():
            global control_time
            x = 0
            video0 = open('C:\\Users\\user\\Desktop\\Python\\dowload\\new\\' + k[x], 'rb')
            video1 = open('C:\\Users\\user\\Desktop\\Python\\dowload\\new\\' + k[x + 1], 'rb')
            video2 = open('C:\\Users\\user\\Desktop\\Python\\dowload\\new\\' + k[x + 2], 'rb')
            video3 = open('C:\\Users\\user\\Desktop\\Python\\dowload\\new\\' + k[x + 3], 'rb')
            video4 = open('C:\\Users\\user\\Desktop\\Python\\dowload\\new\\' + k[x + 4], 'rb')

            bot.send_video(chanel_name1, video0)
            bot.send_video(chanel_name1, video1)
            bot.send_video(chanel_name1, video2)
            bot.send_video(chanel_name1, video3)
            bot.send_video(chanel_name1, video4)


            mydir = 'C:\\Users\\user\\Desktop\\Python\\dowload\\new'
            filelist0 = [f for f in os.listdir(mydir) if f.endswith(k[x])]
            filelist1 = [f for f in os.listdir(mydir) if f.endswith(k[x + 1])]
            filelist2 = [f for f in os.listdir(mydir) if f.endswith(k[x + 2])]
            filelist3 = [f for f in os.listdir(mydir) if f.endswith(k[x + 3])]
            filelist4 = [f for f in os.listdir(mydir) if f.endswith(k[x + 4])]

            video0.close()
            video1.close()
            video2.close()
            video3.close()
            video4.close()

            for f in filelist0:
                os.remove(os.path.join(mydir, f))
            for f in filelist1:
                os.remove(os.path.join(mydir, f))
            for f in filelist2:
                os.remove(os.path.join(mydir, f))
            for f in filelist3:
                os.remove(os.path.join(mydir, f))
            for f in filelist4:
                os.remove(os.path.join(mydir, f))


        if len(files) > 0 and int(now.hour) >= 12 and int(now.hour) < 15 and int(control_time[0]) == 0:
            content()
            control_time.clear()
            control_time.append(1)
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\4vidTime.txt',
                      'w+') as f_news:
                f_news.write(str(control_time[0]))
                scince0()

        elif len(files) > 0 and int(now.hour) >= 15 and int(now.hour) < 18 and int(control_time[0]) == 1:
            content()
            control_time.clear()
            control_time.append(2)
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\4vidTime.txt',
                      'w+') as f_news:
                f_news.write(str(control_time[0]))
                scince0()
        elif len(files) > 0 and int(now.hour) >= 18 and int(now.hour) < 21 and int(control_time[0]) == 2:
            content()
            control_time.clear()
            control_time.append(3)
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\4vidTime.txt',
                      'w+') as f_news:
                f_news.write(str(control_time[0]))
                scince0()


        elif len(files) > 0 and int(now.hour) >= 21 and int(now.hour) < 23 and int(control_time[0]) == 3:
            content()
            control_time.clear()
            control_time.append(0)
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\4vidTime.txt',
                      'w+') as f_news:
                f_news.write(str(control_time[0]))
                scince0()
        else:
            print("Время для выкладки видео в Угар по расписанию не подошло \nControl_time =", control_time[0],
                  "\nВидео в папке New:",len(files) )
            time.sleep(1.5)
            scince0()



    time_view = 7300


    def scince0():
        global youtubetime
        time.sleep(5)
        web_0 = 'https://www.youtube.com/results?search_query=%D0%BD%D0%B0%D1%83%D0%BA%D0%B0+%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81&sp=EgIYAw%253D%253D'
        web_1 = 'https://www.youtube.com/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        m = soup.find_all('script')
        m_split1 = re.split('"', str(m))
        myString = ' '.join(m_split1)
        # \b начинаем искать с букв \w* ищем буквы(* - много) \S(c символами) \b заканчиваем буквой
        match = re.findall(r'watch\Sv\S\w\w\S\w\w\w\w\w\w\w\w?', myString)
        in1.extend(match)
        with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\in1.txt', 'w') as f_news:
            f_news.write("\n".join(set(in1)))
        result = list(set(in1) ^ set(in2))

        youtubetime += 240
        with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\youtbTime.txt', 'w+') as f_news:
            f_news.write(str(youtubetime))

        if youtubetime >= time_view:

            z = '(' + web_1 + result[0] + ')'
            bot.send_message(chanel_name2, '[Опубликовано интересное видео]' + z, parse_mode='Markdown')
            teleprint('НАУКА ЮТУБ вывел: ', result[0])
            in2.append(result[0])
            youtubetime = 0
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\youtbTime.txt', 'w+') as f_news:
                f_news.write(str(youtubetime))

            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\in2.txt', 'w') as f_news:
                f_news.write("\n".join(in2))
            time.sleep(0.8)
            ugar0()
        else:
            # ('ссылок НАУКИ в 1 базе: ', len(set(in1)))
            # teleprint('ссылок НАУКИ в 2 базе: ', len(in2))
            teleprint('\r' + 'Scince sec: ' + str(time_view - youtubetime))
            time.sleep(1.5)
            ugar0()


    time_view2 = 7200


    def ugar0():
        global youtubetime2
        time.sleep(5)
        web_0 = 'https://www.youtube.com/results?search_query=%23coub&sp=CAASBAgCEAE%253D'
        web_1 = 'https://www.youtube.com/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        m = soup.find_all('script')
        m_split1 = re.split('"', str(m))
        myString = ' '.join(m_split1)
        # \b начинаем искать с букв \w* ищем буквы(* - много) \S(c символами) \b заканчиваем буквой
        match = re.findall(r'watch\Sv\S\w\w\S\w\w\w\w\w\w\w\w?', myString)
        in3.extend(match)
        with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\in3.txt', 'w') as f_news:
            f_news.write("\n".join(set(in3)))
        result = list(set(in3) ^ set(in4))
        youtubetime2 += 240
        with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\youtbTime.txt', 'w+') as f_news:
            f_news.write(str(youtubetime2))
        if len(result) > 0 and youtubetime2 >= time_view2:

            z = '(' + web_1 + result[0] + ')'
            bot.send_message(chanel_name1, '[Новая Сoub подборка! Все самое смешное в одном видео!]' + z,
                             parse_mode='Markdown')
            teleprint('УГАР вывел Coub: ', result[0])

            youtubetime2 = 0
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\youtbTime.txt', 'w+') as f_news:
                f_news.write(str(youtubetime2))
            in4.append(result[0])
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\in4.txt', 'w') as f_news:
                f_news.write("\n".join(in4))
            time.sleep(0.8)
            culture_video()
        else:
            # print(' - ссылок COUB в 1 базе: ', len(set(in3)))
            # print(' - ссылок COUB в 2 базе: ', len(in4))
            teleprint('Ugar Coub sec: ' + str(time_view2 - youtubetime2))
            time.sleep(1.5)
            culture_video()


    def culture_video():
        xc = 7200  # 7200 кажды два часа
        # td = dt.datetime.now()
        x = 0

        path, dirs, files = next(os.walk(r'C:\Users\user\Desktop\Python\dowload\culture_video'))
        file_count = len(files)
        len_files2.clear()
        len_files2.append(file_count)
        culture_time.insert(0, int(culture_time[0]) + 240)
        culture_time.pop(1)

        with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\culture_time.txt',
                  'w+') as f_news:
            f_news.write(str(culture_time[0]))
            # print("Новый таймер культуры ВИДЕО записан успешно", culture_time[0])

        if x <= len_files2[0] and int(culture_time[0]) >= xc:

            video = open('C:\\Users\\user\\Desktop\\Python\\dowload\\culture_video\\' + j[x], 'rb')
            bot.send_video(chanel_name3, video)
            # print(len_files2)
            # print(int(culture_time[0]))
            mydir = 'C:\\Users\\user\\Desktop\\Python\\dowload\\culture_video'
            filelist = [f for f in os.listdir(mydir) if f.endswith(j[x])]
            video.close()
            time.sleep(1)
            for f in filelist:
                os.remove(os.path.join(mydir, f))
                time.sleep(1)
                teleprint("\n" + 'culture_video отправил и удалил видео: ' + j[x])
                j.pop(0)
                culture_time.insert(0, 0)
                culture_time.pop(1)
                with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\culture_time.txt',
                          'w+') as f_news:
                    f_news.write(str(culture_time[0]))
                    # teleprint("время в конце успешного удаления Культура видео: ", culture_time[0], "файлов в папке: ", len_files2)
                    culture_photo()

                # bot.send_message(call.message.chat.id, "В папке " + str(len_files) + " видосов")

        else:
            # print("Время для Видео культуры не подошло")
            teleprint('Culture_video sec: ' + str(xc - int(culture_time[0])))
            time.sleep(1.5)
            culture_photo()


    def culture_photo():
        xc = 3600  # 14400 кажды два часа
        # td = dt.datetime.now()
        x = 0

        path, dirs, files = next(os.walk(r'C:\Users\user\Desktop\Python\dowload\culture_photo'))
        file_count = len(files)
        len_files3.clear()
        len_files3.append(file_count)
        culture_time2.insert(0, int(culture_time2[0]) + 240)
        culture_time2.pop(1)

        with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\culture_time2.txt',
                  'w+') as f_news:
            f_news.write(str(culture_time2[0]))
            # print("Новый таймер культуры ФОТО записан успешно", culture_time2[0])

        if x <= len_files3[0] and int(culture_time2[0]) >= xc:

            photo = open('C:\\Users\\user\\Desktop\\Python\\dowload\\culture_photo\\' + h[x], 'rb')
            media = [types.InputMediaPhoto(photo)]
            z = "Рубрика «Жизнь замечательных людей»"
            bot.send_media_group(chanel_name3, media)
            # bot.send_video(chanel_name3, video)
            # print("культура фото файлов: ", len_files3)
            # print("культура фото время", culture_time2[0])
            mydir = 'C:\\Users\\user\\Desktop\\Python\\dowload\\culture_photo'
            filelist = [f for f in os.listdir(mydir) if f.endswith(h[x])]
            photo.close()
            time.sleep(1)
            for f in filelist:
                os.remove(os.path.join(mydir, f))
                time.sleep(1)
                teleprint("\n" + 'culture_photo отправил и удалил культура фото: ' + h[x])
                h.pop(0)
                culture_time2.insert(0, 0)
                culture_time2.pop(1)
                with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\culture_time2.txt',
                          'w+') as f_news:
                    f_news.write(str(culture_time2[0]))
                    # print("время в конце успешного удаления Культура фото: ", culture_time2[0],
                    #    "файлов в папке: ", len_files3)
            auto_photo()

            # bot.send_message(call.message.chat.id, "В папке " + str(len_files) + " видосов")

        else:
            # print("Время для Фото культуры не подошло")
            teleprint('Culture_photo sec: ' + str(xc - int(culture_time2[0])))
            time.sleep(1.5)
            auto_photo()


    def auto_photo():
        xc = 3600  # 7200 кажды два часа
        x = 0

        path, dirs, files = next(os.walk(r'C:\Users\user\Desktop\Python\dowload\auto_photo'))
        file_count = len(files)
        len_files4.clear()
        len_files4.append(file_count)
        auto_time.insert(0, int(auto_time[0]) + 240)
        auto_time.pop(1)

        with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\auto_time.txt',
                  'w+') as f_news:
            f_news.write(str(auto_time[0]))
            # print("Новый таймер Авто фото записан успешно", auto_time[0])

        if x <= len_files4[0] and int(auto_time[0]) >= xc:

            photo = open('C:\\Users\\user\\Desktop\\Python\\dowload\\auto_photo\\' + auto_name[x], 'rb')
            media = [types.InputMediaPhoto(photo)]
            z = "Рубрика «Смотри какая...»"
            bot.send_media_group(chanel_name4, media)

            mydir = 'C:\\Users\\user\\Desktop\\Python\\dowload\\auto_photo'
            filelist = [f for f in os.listdir(mydir) if f.endswith(auto_name[x])]
            photo.close()
            time.sleep(1)
            for f in filelist:
                os.remove(os.path.join(mydir, f))
                time.sleep(1)
                teleprint("\n" + 'auto_photo отправил и удалил Авто фото: ' + auto_name[x])
                auto_name.pop(0)
                auto_time.insert(0, 0)
                auto_time.pop(1)
                with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\auto_time.txt',
                          'w+') as f_news:
                    f_news.write(str(auto_time[0]))
                    teleprint("время в конце успешного удаления Авто фото: ", auto_time[0], "файлов в папке: ",
                              len_files4)
                auto_video()

                # bot.send_message(call.message.chat.id, "В папке " + str(len_files) + " видосов")

        else:
            # print("Время для Фото Авто не подошло")
            teleprint('Auto_photo sec: ' + str(xc - int(auto_time[0])))
            time.sleep(1.5)
            auto_video()


    def auto_video():
        xc = 7200  # 7200 кажды два часа
        x = 0

        path, dirs, files = next(os.walk(r'C:\Users\user\Desktop\Python\dowload\auto_video'))
        file_count = len(files)
        len_files5.clear()
        len_files5.append(file_count)
        autoV_time.insert(0, int(autoV_time[0]) + 240)
        autoV_time.pop(1)

        with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\autoV_time.txt',
                  'w+') as f_news:
            f_news.write(str(autoV_time[0]))
            # print("Новый таймер культуры ВИДЕО записан успешно", autoV_time[0])

        if x <= len_files5[0] and int(autoV_time[0]) >= xc:

            video = open('C:\\Users\\user\\Desktop\\Python\\dowload\\auto_video\\' + autoV_name[x], 'rb')
            bot.send_video(chanel_name4, video)

            mydir = 'C:\\Users\\user\\Desktop\\Python\\dowload\\auto_video'
            filelist = [f for f in os.listdir(mydir) if f.endswith(autoV_name[x])]
            video.close()
            time.sleep(1)
            for f in filelist:
                os.remove(os.path.join(mydir, f))
                time.sleep(1)
                teleprint("\n" + 'auto_video отправил и удалил Авто video: ' + autoV_name[x])
                autoV_name.pop(0)
                autoV_time.insert(0, 0)
                autoV_time.pop(1)
                with open(r'C:\Users\user\Desktop\Python\My_bots\RememberMemes\autoV_time.txt',
                          'w+') as f_news:
                    f_news.write(str(autoV_time[0]))
                    teleprint("время в конце успешного удаления Авто video: ", autoV_time[0], "файлов в папке: ",
                              len_files5)
                waite_time = 0



        else:
            # print("Время для Video Авто не подошло")
            teleprint('Auto_video sec: ' + str(xc - int(autoV_time[0])))
            waite_time = 0


    callback_worker1()





except requests.ConnectionError:
    print("Нет ебучего интернета [Инста]")

    time.sleep(10)

except TimeoutError:
    print("Connect Error [Инста]")

    time.sleep(10)


except Exception:
    print("Какая то ошибка [Инста]")

    time.sleep(10)

# -----------Инста бот
