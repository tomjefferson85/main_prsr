import requests
import vk_api
import re
import time
import telebot
import datetime as dt
from telebot import types
import sys
import os

# ------------------login telebot--------------------------
bot = telebot.TeleBot('1762909475:AAHmEHQDIZLoIO688Gx2YM9DVWf3mt6XVtI')
chanel_name = '@ugar_non_stop'
token = '1762909475:AAHmEHQDIZLoIO688Gx2YM9DVWf3mt6XVtI'
myID = '@test_my_shit'
# ----------------login vk----------------------------
vk_session = vk_api.VkApi('+79647918149', 'solomon00001111')
vk_session.auth()
vk = vk_session.get_api()

UcTo4Huku = ["leprum", "da_side", "onlyorly", "mudakoff",
             "borsch", "iface", "stockmem", "medieval_or",
             "zloyzayacgif", "peregovorov", "fact", "ifun",
             "humour.page", "memes_bot", "txaxax", "fckbrain",
             "agil1_vk", "fucking_humor", "nice_student", "bot_maxim",
             "e_goist", "lifeontv", "stlbn", "a_zhe", "science_technology",
             "oxaxa", "sci", "topds", "oryslenti", "c.umor", "humor_schrodinger",
             "paper.comics"]


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
    teleprint("------====Ugar_bot ENABLE====------\n" + "Групп для парсинга в базе:", len(UcTo4Huku), "\n--Поиск контента запущен--")
    nomer_UcTo4Huka = 0
    nomer_faula = 1
    f_folder = r'C:\Users\user\Desktop\Python\My_bots\RememberMemes'
    sravnu_1 = []
    sravnu_11 = []
    while nomer_faula <= 32:
        main_folder = f_folder + str("\\" + str(nomer_faula)) + ".txt"
        # ______load all files______
        with open(main_folder, 'r+') as f_news:
            sravnu_11.append(f_news.read())
        # ______clear all files______
        # with open(main_folder, 'w') as f_news:
        # f_news.write('0')
        nomer_faula += 1

    vk_chanel = []


    # FINDER--------------------------------------------------------------

    def finder():
        '''
        global vk_chanel, attachment
        post = vk.wall.get(domain=vk_chanel[0], count=2)['items'][1]
        text_id = post['text']
        # -------------сплит текст на сссылки Y - норм рамер для фото
        text_resplit = re.split('"', str(post))
        fst_progon = ' '.join(text_resplit)
        all_photo_typeY = re.findall(r'https://sun\w*\S*\S\s\S*type\S*\s\Sx', fst_progon)
        scd_progon = ' '.join(all_photo_typeY)
        finish_url = re.findall(r'\b\w*https://sun\w*\S*\b', scd_progon)
        # ----------подсчет найденных фото
        len_finish_url = len(finish_url)
        # -----------проверка на кол-во вложенных фото
        time.sleep(0.8)

        images = []
        count_media = 0
        img = "img_" + str(count_media)
        media = []

        # !!!!!!!!------- цикл добавления информации в картинки и в медиа не работает
        while count_media < len_finish_url:
            images.append(finish_url[count_media])
            media.append(types.InputMediaPhoto(img))
            count_media += 1

        teleprint(images, "\n",media[0])
        # !!!!!!!!------- полуена вся инфа но отправлять ее не хочет
        bot.send_media_group(chanel_name, media)
        time.sleep(20)
        print(finish_url)

        '''
        global vk_chanel, attachment
        post = vk.wall.get(domain=vk_chanel[0], count=2)['items'][1]
        text_id = post['text']
        ad_blocker = re.findall(r'/', text_id)
        if len(ad_blocker) > 0:
            teleprint('\r' "\n" + "Обаружена реклама" + str(vk_chanel) + "\n")
        else:
            # -------------сплит текст на сссылки Y - норм рамер для фото
            text_resplit = re.split('"', str(post))
            fst_progon = ' '.join(text_resplit)
            all_photo_typeY = re.findall(r'https://sun\w*\S*\S\s\S*type\S*\s\Sx', fst_progon)
            scd_progon = ' '.join(all_photo_typeY)
            finish_url = re.findall(r'\b\w*https://sun\w*\S*\b', scd_progon)
            # ----------подсчет найденных фото
            len_finish_url = len(finish_url)
            # -----------проверка на кол-во вложенных фото
            time.sleep(0.8)

            if len_finish_url == 1:
                img_1 = finish_url[0]
                media = [types.InputMediaPhoto(img_1, caption=text_id)]
                bot.send_media_group(chanel_name, media)
                time.sleep(2)
            if len_finish_url == 2:
                img_1 = finish_url[0]
                img_2 = finish_url[1]
                media = [types.InputMediaPhoto(img_1, caption=text_id), types.InputMediaPhoto(img_2)]
                bot.send_media_group(chanel_name, media)
                time.sleep(2)
            if len_finish_url == 3:
                img_1 = finish_url[0]
                img_2 = finish_url[1]
                img_3 = finish_url[2]
                media = [types.InputMediaPhoto(img_1, caption=text_id), types.InputMediaPhoto(img_2),
                         types.InputMediaPhoto(img_3)]
                bot.send_media_group(chanel_name, media)
                time.sleep(2)
            if len_finish_url == 4:
                img_1 = finish_url[0]
                img_2 = finish_url[1]
                img_3 = finish_url[2]
                img_4 = finish_url[3]
                media = [types.InputMediaPhoto(img_1, caption=text_id), types.InputMediaPhoto(img_2),
                         types.InputMediaPhoto(img_3), types.InputMediaPhoto(img_4)]
                bot.send_media_group(chanel_name, media)
                time.sleep(2)
            if len_finish_url == 5:
                img_1 = finish_url[0]
                img_2 = finish_url[1]
                img_3 = finish_url[2]
                img_4 = finish_url[3]
                img_5 = finish_url[4]
                media = [types.InputMediaPhoto(img_1, caption=text_id), types.InputMediaPhoto(img_2),
                         types.InputMediaPhoto(img_3), types.InputMediaPhoto(img_4),
                         types.InputMediaPhoto(img_5)]
                bot.send_media_group(chanel_name, media)
                time.sleep(2)
            if len_finish_url == 6:
                img_1 = finish_url[0]
                img_2 = finish_url[1]
                img_3 = finish_url[2]
                img_4 = finish_url[3]
                img_5 = finish_url[4]
                img_6 = finish_url[5]
                media = [types.InputMediaPhoto(img_1, caption=text_id), types.InputMediaPhoto(img_2),
                         types.InputMediaPhoto(img_3), types.InputMediaPhoto(img_4),
                         types.InputMediaPhoto(img_5), types.InputMediaPhoto(img_6)]
                bot.send_media_group(chanel_name, media)
                time.sleep(2)


    # CHANELS-------------------------------------------------------------------------------------------------
    nomer_faula2 = 1


    def chanel_1():
        global nomer_UcTo4Huka, nomer_faula2

        vk_chanel.clear()
        vk_chanel.append(UcTo4Huku[nomer_UcTo4Huka])

        post = vk.wall.get(domain=vk_chanel[0], count=2)['items'][1]
        owner_id = post['owner_id']
        media_id = post['id']
        attachment = f'wall{owner_id}_{media_id}'
        sravnu_1.clear()
        sravnu_1.append(attachment)

        if sravnu_1[0] != sravnu_11[nomer_UcTo4Huka]:
            # print(attachment)
            msg = vk_chanel[0], sravnu_1[0] != sravnu_11[nomer_UcTo4Huka]
            teleprint('\r'"\n" + str(msg) + "\n")
            # print(sravnu_1, sravnu_11)
            # -----------сохранение
            main_folder = f_folder + str("\\" + str(nomer_faula2)) + ".txt"
            with open(main_folder, 'w') as f_news:
                # print(attachment, nomer_faula2)
                f_news.write(attachment)

            # -----------функция поиска контента на vk_chanel

            finder()
            if nomer_UcTo4Huka < 31:
                # print(nomer_UcTo4Huka, nomer_faula2)
                nomer_UcTo4Huka += 1
                nomer_faula2 += 1
                time.sleep(1)
                chanel_1()

        else:
            if nomer_UcTo4Huka < 31:
                msg = vk_chanel[0], sravnu_1[0] != sravnu_11[nomer_UcTo4Huka], "Пройдено " + str(
                    nomer_faula2) + " из " + str(len(UcTo4Huku))
                sys.stdout.write('\r' + str(msg))
                # print(nomer_UcTo4Huka, nomer_faula2)
                nomer_UcTo4Huka += 1
                nomer_faula2 += 1
                time.sleep(1)
                chanel_1()


    # --WAIT Function-----------------------------------------------------------------
    timeview = 0


    def w_function():
        w_time = 5
        global timeview
        if timeview >= w_time:
            chanel_1()
        else:
            timeview += 1
            wait_time = w_time - timeview
            sys.stdout.write('\r' + "Новый поиск через: " + str(wait_time) + " сек...")
            time.sleep(1)
            w_function()


    w_function()
# -----------------------------------------------------------------
except requests.ConnectionError:
    os.system('cls')
    print("Нет ебучего интернета [Угар]")

    time.sleep(10)


except requests.RequestException:
    os.system('cls')
    print('alarm, is disaster Угар')

    time.sleep(10)


except TimeoutError:
    os.system('cls')
    print("Connect Error [Угар]")

    time.sleep(10)


except Exception:
    os.system('cls')
    print("Какая то ошибка [Угар]")

    time.sleep(10)

# -!!!!!!!!!!!!----------добавить подддержку до 8ми фото и подготовить вывод для ТГ !!!!!!!!!!
