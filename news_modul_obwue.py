import requests
from bs4 import BeautifulSoup
import telebot
import re
import datetime as dt
import time
from telebot import types
import sys
import os

bot = telebot.TeleBot('')
chanel_name = '@'
chanel_name1 = '@'
chanel_name2 = '@'
chanel_name3 = '@'
chanel_name4 = '@'
chanel_name5 = '@'
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


    teleprint("------====NEWS_Bot ENABLE====------\n")

    obwue = []
    obwue2 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\news.txt', 'r+') as f_news:
        obwue2.append(f_news.read())
        # time.sleep(1)

    sport = []
    sport2 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\sport.txt', 'r+') as f_news:
        sport2.append(f_news.read())
        # time.sleep(1)

    gryzb = []
    gryzb2 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\gryzb.txt', 'r+') as f_news:
        gryzb2.append(f_news.read())
        # time.sleep(1)

    naked = []
    naked2 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\naked.txt', 'r+') as f_news:
        naked2.append(f_news.read())
        # time.sleep(1)

    techno = []
    techno2 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\techno.txt', 'r+') as f_news:
        techno2.append(f_news.read())
        # time.sleep(1)

    Nauka = []
    Nauka2 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\nayka2.txt', 'r+') as f_news:
        Nauka2.append(f_news.read())
        # time.sleep(1)

    finanz = []
    finanz2 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\finanz.txt', 'r+') as f_news:
        finanz2.append(f_news.read())
        # time.sleep(1)

    KP = []
    KP2 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\KP.txt', 'r+') as f_news:
        KP2.append(f_news.read())
        # time.sleep(1)

    KP3 = []
    KP33 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\KP2.txt', 'r+') as f_news:
        KP33.append(f_news.read())
        # time.sleep(1)

    # ----------------------

    Ekspress = []
    Ekspress1 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\Ekspress.txt', 'r+') as f_news:
        Ekspress1.append(f_news.read())

    Auto = []
    Auto1 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\Auto.txt', 'r+') as f_news:
        Auto1.append(f_news.read())
        # time.sleep(1)

    autonews = []
    autonews1 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\autonews.txt', 'r+') as f_news:
        autonews1.append(f_news.read())
        # time.sleep(1)

    kolesa = []
    kolesa1 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\kolesa.txt', 'r+') as f_news:
        kolesa1.append(f_news.read())
        # time.sleep(1)

    ProucwectBuya = []
    ProucwectBuya1 = []
    with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\ProucwectBuya.txt', 'r+') as f_news:
        ProucwectBuya1.append(f_news.read())


    def ObwueRia():
        global SportNews
        time.sleep(4)
        # ----------поиск ссылки----------------------

        web_0 = 'https://ria.ru/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='lenta__item', limit=2)
        href_split = re.split('"', str(href[0]))
        myString = ' '.join(href_split)
        main_href = re.findall(r'\b\w*https://\w*\S*\b', myString)
        # ----------поиск главного заголовка----------------------
        title = soup.find_all(class_='lenta__item-text', limit=1)
        l = ''
        for tag in title:
            l = str(" ".join(tag.text.split()))
            # print(l)
        j = ("*" + l + "*" + '\n\n')  # главный заголовок-----------

        obwue.clear()
        obwue.append(main_href[0])

        if obwue != obwue2:
            # ----------выуживание инфы из сслыки----------------------
            teleprint('\r' + "Ria Main:" + str(obwue != obwue2) + "\n")
            # ----------берем текст------------------
            try:
                l = ''
                web_1 = main_href[0]
                rs_0 = requests.get(web_1)
                soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
                main_text = soup.find_all('div', itemprop="articleBody")
                for tag in main_text:
                    l = (str(" ".join(tag.text.split())))  # убираем теги из l
                href_split_text = re.split('\—', str(l), maxsplit=1)
                href_split_text2 = re.split('\. ', str(href_split_text), maxsplit=1)
                limit_text = href_split_text2[1][0:300]
                finish_text = "_" + limit_text + "_" + "...\n\n"  # Конечный текст -----------
                # ----------берем первое фото------------------
                main_photo = soup.find_all("div", src="")
                href_split = re.split('"', str(main_photo))
                myString = ' '.join(href_split)
                main_photo2 = re.findall(r'\b\w*https://cdn21\w*\S*\b',
                                         myString)  # Ссылки с картинками -----------
                with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\news.txt',
                          'w') as f_news:
                    obwue2.clear()
                    f_news.write(main_href[0])

                obwue2.append(main_href[0])
                img_1 = main_photo2[4]
                z = '(' + main_href[0] + ')'
                url = '[' + 'Читать полностью...' + ']'
                media = [
                    types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown')]
                bot.send_media_group(chanel_name, media)
                time.sleep(4)
                SportNews()
            except IndexError:
                teleprint('\r' "Ria Main Index Error:")
                SportNews()

        else:
            teleprint('\r' + "\n" + "Ria Main:" + str(obwue != obwue2))
            time.sleep(4)
            SportNews()


    def SportNews():
        time.sleep(1)
        # ----------href----------------------
        web_0 = 'https://rsport.ria.ru/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='lenta__item', limit=2)
        href_split = re.split('"', str(href[0]))
        myString = ' '.join(href_split)
        main_href = re.findall(r'\b\w*https://\w*\S*\b', myString)
        # ----------title----------------------
        title = soup.find_all(class_='lenta__item-text', limit=1)
        title_split = re.split('"', str(title))
        myString = ''.join(title_split[2])
        m_split2 = re.split('>', str(myString))

        myString1 = ''.join(m_split2[1])
        m_split3 = re.split('<', str(myString1))
        j = (m_split3[0] + '\n\n')

        sport.clear()
        sport.append(main_href[0])
        if sport != sport2:
            teleprint('\r' + "SPORT:" + str(sport != sport2) + "\n")
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\sport.txt', 'w') as f_news:
                sport2.clear()
                f_news.write(main_href[0])

            sport2.append(main_href[0])
            z = '(' + main_href[0] + ')'
            bot.send_message(chanel_name2, j + '[Источник:]' + z, parse_mode='Markdown')
            # bot.send_message(chanel_name2, j)
            Gryazb0()
            time.sleep(4)
        else:
            teleprint('\r' + "SPORT:" + str(sport != sport2))
            Gryazb0()
            time.sleep(4)


    def Gryazb0():
        # ----------href----------------------
        web_0 = 'https://www.starhit.ru'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='news news_previews news_list', limit=2)
        href_split = re.split('"', str(href[0]))
        hr = web_0 + href_split[5]
        # print(hr)
        # -----------------------------------------href_split[5] сcылка главная
        # ----------поиск главного заголовка----------------------
        l = []
        for tag in href:
            l.append(str(" ".join(tag.text.split())))
        j = ("*" + href_split[9] + "*" + '\n\n')

        gryzb.clear()
        gryzb.append(href_split[5])
        if gryzb != gryzb2:
            teleprint('\r' + "Грязь:" + str(gryzb != gryzb2) + "\n")
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\gryzb.txt', 'w') as f_news:
                gryzb2.clear()
                f_news.write(href_split[5])

            gryzb2.append(href_split[5])
            rs_0 = requests.get(hr)
            soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
            main_text = soup.find_all("p")
            l = []
            main_text_to_Chat = ""
            for tag in main_text:
                l.append(str(" ".join(tag.text.split())))
            if len(l) >= 3:
                main_text_to_Chat = l[0] + "\n\n" + l[1]
            if len(l) <= 2:
                main_text_to_Chat = l[0]
            finish_text = "_" + main_text_to_Chat + "_" + "\n\n"  # Конечный текст -----------
            # ----------берем первое фото------------------
            main_photo = soup.find_all(class_="figure__pic")
            href_split = re.split('"', str(main_photo))
            myString = ' '.join(href_split)
            main_photo2 = re.findall(r'\b\w*https://n1s\w*\S*\b', myString)  # Ссылки с картинками -----------
            # print(len(main_photo2))

            if len(main_photo2) <= 4:
                z = '(' + hr + ')'
                url = '[' + "Читать полностью..." + ']'
                img_1 = main_photo2[0]
                media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown')]
                bot.send_media_group(chanel_name4, media)
            elif len(main_photo2) >= 6:
                z = '(' + hr + ')'
                url = '[' + "Читать полностью..." + ']'
                img_1 = main_photo2[0]
                img_2 = main_photo2[2]
                img_3 = main_photo2[4]
                media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown'),
                         types.InputMediaPhoto(img_2),
                         types.InputMediaPhoto(img_3)]
                bot.send_media_group(chanel_name4, media)
            time.sleep(4)
            nakednews()
        else:
            teleprint('\r' + "Грязь:" + str(gryzb != gryzb2))
            time.sleep(4)
            nakednews()


    def nakednews():
        # ----------href----------------------
        web_0 = 'https://naked-science.ru/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all('h3', limit=2)
        href_split = re.split('"', str(href[0]))

        # ----------title----------------------
        title = soup.find_all('h3', limit=2)
        title_split = re.split('"', str(title[0]))
        myString = ''.join(title_split[4])
        m_split2 = re.split('>', str(myString))
        myString1 = ''.join(m_split2[1])
        m_split3 = re.split('<', str(myString1))

        # print(m_split3[0])
        # print(href_split[3])

        naked.clear()
        naked.append(href_split[3])

        if naked != naked2:
            teleprint('\r' + "Naked-science:" + str(naked != naked2) + "\n")

            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\naked.txt', 'w') as f_news:
                naked2.clear()
                f_news.write(href_split[3])

            naked2.append(href_split[3])
            j = (m_split3[0] + '\n\n')
            z = '(' + href_split[3] + ')'
            bot.send_message(chanel_name1, j + '[Источник:]' + z, parse_mode='Markdown')
            # bot.send_message(chanel_name1, m_split3[0] + '\n\n' + href_split[3])
            time.sleep(4)
            techno1()
        else:
            teleprint('\r' + "Naked-science: " + str(naked != naked2))
            time.sleep(4)
            techno1()


    def techno1():
        # ----------href----------------------
        web_0 = 'https://www.techcult.ru/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='pad pad1', limit=2)[0]
        href_split = re.split('"', str(href))
        # ----------title----------------------
        title = soup.find_all('h2', limit=2)[1]
        myString = ''.join(title)
        m_split2 = re.split('>', str(myString))
        myString1 = ''.join(m_split2[0])
        m_split3 = re.split('<', str(myString1))

        techno.clear()
        techno.append(href_split[3])
        if techno != techno2:
            teleprint('\r' + "Techno: " + str(techno != techno2) + "\n")

            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\techno.txt', 'w') as f_news:
                techno2.clear()
                f_news.write(href_split[3])

            techno2.append(href_split[3])
            j = (m_split3[0] + '\n\n')
            z = '(' + href_split[3] + ')'
            bot.send_message(chanel_name1, j + '[Источник:]' + z, parse_mode='Markdown')
            # bot.send_message(chanel_name1, m_split3[0] + '\n\n' + href_split[3])
            time.sleep(4)
            Nauka_novoctu()
        else:
            teleprint('\r' + "Techno: " + str(techno != techno2))
            time.sleep(4)
            Nauka_novoctu()


    def Nauka_novoctu():
        web_0 = 'https://lenta.ru/rubrics/science'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='titles', limit=2)[1]
        href_split = re.split('"', str(href))  # ---------href_split[3] сcылка главная

        # ----------поиск главного заголовка----------------------
        web_1 = 'https://lenta.ru' + href_split[3]
        rs_1 = requests.get(web_1)
        soup1 = BeautifulSoup(rs_1.content.decode('utf-8'), 'html.parser')
        title = soup1.find_all('title')
        l = []
        for tag in title:
            m = (str(" ".join(tag.text.split())))
            title_split = re.split(':', str(m))  # убираем теги из l
            l.append(title_split[0])
        j = ("*" + l[0] + "*" + '\n\n')  # MAIN TITLE

        Nauka.clear()
        Nauka.append(href_split[3])

        if Nauka != Nauka2:
            teleprint('\r' + "Lenta Nayka: " + str(Nauka != Nauka2) + "\n")
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\nayka2.txt', 'w') as f_news:
                Nauka2.clear()
                f_news.write(href_split[3])
            Nauka2.append(href_split[3])
            # ----------поиск текста новости----------------------
            main_text = soup1.find_all("div", class_="b-text clearfix js-topic__text")
            for tag in main_text:
                l = (str(" ".join(tag.text.split())))
                main_text_split = re.split('Материалы', str(l))
                finish_text = "_" + main_text_split[0] + "_" + "\n\n"

                # ----------берем первое фото------------------

                main_photo = soup1.find_all(class_="g-picture")
                main_photo_split = re.split('"', str(main_photo))
                myString = ' '.join(main_photo_split)
                main_photo = re.findall(r'\b\w*https://\w*\S*\b', myString)
                # ----------Готовим сообщение в телегу------------------
                img_1 = main_photo[0]
                z = '(' + web_1 + ')'
                url = '[' + "Читать полностью..." + ']'
                media = [types.InputMediaPhoto(img_1, caption=j + finish_text[0:300] + "..." + url + z,
                                               parse_mode='Markdown')]
                bot.send_media_group(chanel_name1, media)
                finanz_0()

        else:
            teleprint('\r' + "Lenta Nayka: " + str(Nauka != Nauka2))
            time.sleep(4)
            finanz_0()


    def finanz_0():
        # try:
        # ----------title----------------------
        web_0 = 'https://www.finanz.ru/novosti'
        web_1 = 'https://www.finanz.ru/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        title = soup.find_all('tbody', limit=2)
        new = []  # список для перебора ссылок
        for a in soup.find_all('tbody', href=True):  # ищем ссылки
            new.append(a['href'])
        title_split = re.split('"', str(title))

        myString = ' '.join(title_split)
        main_href = re.findall(r'\b\w*novosti\w*\S*\b', myString)

        zcv = web_1 + main_href[0]
        web_2 = zcv

        rs_0 = requests.get(web_2)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all('title', limit=3)
        href_split = re.split('"', str(href[0]))
        myString = ''.join(href_split[0])
        m_split2 = re.split('>', str(myString))
        myString1 = ''.join(m_split2[1])
        m_split3 = re.split('\|', str(myString1))

        finanz.clear()
        finanz.append(main_href[0])
        if finanz != finanz2:
            teleprint('\r' + "Finans: " + str(finanz != finanz2) + "\n")
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\finanz.txt', 'w') as f_news:
                finanz2.clear()
                f_news.write(main_href[0])
            finanz2.append(main_href[0])
            j = (m_split3[0] + '\n\n')
            z = '(' + zcv + ')'
            bot.send_message(chanel_name3, j + '[Источник:]' + z, parse_mode='Markdown')
            # bot.send_message(chanel_name3, m_split3[0] + '\n\n' + zcv)
            time.sleep(3)
            KP0()
        else:
            teleprint('\r' + "Finans: " + str(finanz != finanz2))
            time.sleep(3)
            KP0()


    def KP0():
        web_0 = 'https://www.kp.ru/stars/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='styled__TitleLink-sc-1tputnk-2 dxYRLK', limit=1)
        href_split = re.split('"', str(href[0]))
        # print(href_split[3])
        # -----------------------------------------href_split[3] сcылка главная

        # ----------поиск главного заголовка----------------------
        l = []
        for tag in href:
            l.append(str(" ".join(tag.text.split())))
            # print(l)
        j = ("*" + l[0] + "*" + '\n\n')  # главный заголовок-----------

        KP.clear()
        KP.append(href_split[3])

        if KP != KP2:
            teleprint('\r' + "KP STARS: " + str(KP != KP2) + "\n")

            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\KP.txt', 'w') as f_news:
                KP2.clear()
                f_news.write(href_split[3])

            KP2.append(href_split[3])
            # ----------берем текст------------------
            web_1 = 'https://www.kp.ru' + href_split[3]
            # print(web_1)
            rs_0 = requests.get(web_1)
            soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
            main_text = soup.find_all(class_="styled__Paragraph-sc-1wayp1z-16 iegLIC", limit=3)
            h = ""
            for tag in main_text:
                h = (str(" ".join(tag.text.split())))

            finish_text = "_" + h + "_" + "\n\n"  # Конечный текст -----------
            # ----------берем первое фото------------------
            main_photo = soup.find_all(class_="styled__Content-sc-14f2vgk-1 juRDLB")
            href_split = re.split('"', str(main_photo))
            myString = ' '.join(href_split)
            main_photo2 = re.findall(r'\b\w*https://s1\w*\S*\b', myString)  # Ссылки с картинками -----------
            z = '(' + web_1 + ')'
            url = '[' + "Читать полностью..." + ']'
            if len(main_photo2) <= 6:
                img_1 = main_photo2[0]
                media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown')]
                bot.send_media_group(chanel_name4, media)
            if len(main_photo2) == 7:
                img_1 = main_photo2[0]
                img_2 = main_photo2[-1]
                media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown'),
                         types.InputMediaPhoto(img_2)]
                bot.send_media_group(chanel_name4, media)

            if len(main_photo2) == 8:
                img_1 = main_photo2[0]
                img_2 = main_photo2[-1]
                img_3 = main_photo2[-2]
                media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown'),
                         types.InputMediaPhoto(img_2), types.InputMediaPhoto(img_3)]
                bot.send_media_group(chanel_name4, media)

            if len(main_photo2) >= 9:
                img_1 = main_photo2[0]
                img_2 = main_photo2[-1]
                img_3 = main_photo2[-2]
                img_4 = main_photo2[-3]
                media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown'),
                         types.InputMediaPhoto(img_2), types.InputMediaPhoto(img_3),
                         types.InputMediaPhoto(img_4)]
                bot.send_media_group(chanel_name4, media)
            time.sleep(4)
            KP1()
        else:
            teleprint('\r' + "KP STARS: " + str(KP != KP2))
            time.sleep(4)
            KP1()


    def KP1():
        # ----------поиск ссылки----------------------

        web_0 = 'https://www.kp.ru/online/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='styled__TitleLink-sc-1tputnk-2 lgPKnJ', limit=1)
        href_split = re.split('"', str(href[0]))
        # print(href_split)

        # -----------------------------------------href_split[3] сcылка главная

        # ----------поиск главного заголовка----------------------
        l = []
        for tag in href:
            l.append(str(" ".join(tag.text.split())))
        j = ("*" + l[0] + "*" + '\n\n')  # главный заголовок-----------

        KP3.clear()
        KP3.append(href_split[3])
        print(KP3,KP33)
        if KP3 != KP33:

            teleprint('\r' + "KP WORLD: " + str(KP3 != KP33) + "\n")
            # ----------Сохраняем данные------------------
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\KP2.txt', 'w') as f_news:
                KP33.clear()
                f_news.write(href_split[3])

            KP33.append(href_split[3])

            # ----------берем текст------------------
            web_1 = 'https://www.kp.ru' + href_split[3]
            # print(web_1)
            rs_0 = requests.get(web_1)
            soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
            main_text = soup.find_all(class_="styled__Paragraph-sc-1wayp1z-16 iegLIC", limit=3)
            h = ""
            for tag in main_text:
                h = (str(" ".join(tag.text.split())))

            finish_text = "_" + h + "_" + "\n\n"  # Конечный текст -----------
            # ----------берем первое фото------------------
            main_photo = soup.find_all()
            href_split = re.split('"', str(main_photo))
            myString = ' '.join(href_split)
            main_photo2 = re.findall(r'\b\S*\w*wr-\w*\S*\b', myString)  # Ссылки с картинками -----------
            # print(len(main_photo2))
            if len(main_photo2) == 0:
                main_photo3 = re.findall(r'\b\w*https://s1\w*\S*\b', myString)  # Ссылки с картинками -----------
                img_1 = main_photo3[2]
            else:
                img_1 = main_photo2[2]

            z = '(' + web_1 + ')'
            url = '[' + "Читать полностью..." + ']'
            media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown')]
            bot.send_media_group(chanel_name, media)
            time.sleep(4)
            Ekspress0()


        else:
            teleprint('\r' + "KP WORLD: " + str(KP3 != KP33))
            time.sleep(4)
            Ekspress0()


    def Ekspress0():
        # ----------href----------------------
        web_0 = 'https://www.eg.ru/news/'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='main2019_footer-collection-item-title', limit=1)
        href_split = re.split('"', str(href[0]))
        # print(href_split[3])
        l = []
        for tag in href:
            l.append(str(" ".join(tag.text.split())))
            # print(l[0])

        Ekspress.clear()
        Ekspress.append(href_split[3])

        if Ekspress != Ekspress1:
            teleprint('\r' + "Eksress News: " + str(Ekspress != Ekspress1) + "\n")

            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\Ekspress.txt', 'w') as f_news:
                Ekspress1.clear()
                f_news.write(href_split[3])

            Ekspress1.append(href_split[3])
            z = '(' + href_split[3] + ')'
            bot.send_message(chanel_name4, l[0] + '\n\n' + '[Источник:]' + z, parse_mode='Markdown')
            # bot.send_message(chanel_name4, j)
            time.sleep(4)
            Auto0()

        else:
            teleprint('\r' + "Express News: " + str(Ekspress != Ekspress1))
            time.sleep(4)
            Auto0()


    def Auto0():
        # ----------href----------------------
        web_0 = 'https://iz.ru/rubric/auto'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='node__cart__item__inside', limit=1)
        href_split = re.split('"', str(href[0]))
        Title = soup.find_all(class_='node__cart__item__inside__info__title small-title-style1', limit=1)
        Title2 = soup.find_all(class_='node__cart__item__inside__info__description text-style1', limit=1)
        l = []
        for tag in Title:
            l.append(str(" ".join(tag.text.split())))
        l2 = []
        for tag in Title2:
            l2.append(str(" ".join(tag.text.split())))
        web_1 = "https://iz.ru" + href_split[3]
        rs_1 = requests.get(web_1)
        soup1 = BeautifulSoup(rs_1.content.decode('utf-8'), 'html.parser')
        href2 = soup1.find_all(itemprop="articleBody", limit=1)
        href3 = soup1.find_all("meta")
        href_split = re.split('"', str(href3))
        myString = ' '.join(href_split)
        main_photo2 = re.findall(r'\b\w*https://cdn.iz.ru\w*\S*\b', myString)
        for tag in href2:
            l.append(str(" ".join(tag.text.split())))
        l3 = l[1]
        # print(main_photo2[0] + l[0], "\n" + l3[0:300] + "...")
        j = ("*" + l[0] + "*" + '\n\n')

        finish_text = ("_" + l3[0:300] + "..." + "_" + '\n\n')

        Auto.clear()
        Auto.append(web_1)

        if Auto != Auto1:
            teleprint('\r' + "Izvestia AutoNews: " + str(Auto != Auto1) + "\n")
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\Auto.txt', 'w') as f_news:
                Auto1.clear()
                f_news.write(web_1)
            img_1 = main_photo2[0]
            Auto1.append(web_1)
            z = '(' + web_1 + ')'
            url = '[' + "Читать полностью..." + ']'
            media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown')]
            bot.send_media_group(chanel_name5, media)
            time.sleep(4)
            autonews0()

        else:
            teleprint('\r' + "Izvestia AutoNews: " + str(Auto != Auto1))
            time.sleep(4)
            autonews0()


    def autonews0():
        # ----------href----------------------
        web_0 = 'https://www.autonews.ru/tags/?tag=Новости'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='item-big__link', limit=1)
        href_split = re.split('"', str(href[0]))

        autonews.clear()
        autonews.append(href_split[3])

        if autonews != autonews1:
            teleprint('\r' + "AutoNews.ru : " + str(autonews != autonews1) + "\n")
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\autonews.txt', 'w') as f_news:
                autonews1.clear()
                f_news.write(href_split[3])

            web_1 = href_split[3]
            rs_1 = requests.get(web_1)
            soup1 = BeautifulSoup(rs_1.content.decode('utf-8'), 'html.parser')

            href4 = soup1.find_all(class_='article__header__anons', limit=1)
            href2 = soup1.find_all(class_='js-slide-title', limit=1)
            href3 = soup1.find_all(class_='article__main-image__image', limit=1)
            href_split = re.split('"', str(href3))
            myString = ' '.join(href_split)
            main_photo2 = re.findall(r'\b\w*https://s0.rbk.ru/\w*\S*\b', myString)

            l = []
            l2 = []
            for tag in href4:
                l.append(str(" ".join(tag.text.split())))
            for tag in href2:
                l2.append(str(" ".join(tag.text.split())))
            xc = l[0]
            j = ("*" + l2[0] + "*" + '\n\n')

            finish_text = ("_" + xc[0:300] + "..." + "_" + '\n\n')

            if len(main_photo2) == 0:
                img_1 = "https://www.corigine.com/wp-content/uploads/2017/10/newsb-2.jpg"
            else:
                img_1 = main_photo2[0]
            z = '(' + web_1 + ')'

            url = '[' + "Читать полностью..." + ']'
            media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown')]
            bot.send_media_group(chanel_name5, media)
            autonews1.append(href_split[3])

            time.sleep(4)
            kolesa0()


        else:
            teleprint('\r' + "AutoNews.ru : " + str(autonews != autonews1))
            time.sleep(4)
            kolesa0()


    def kolesa0():
        # ----------href----------------------
        web_0 = 'https://www.kolesa.ru/news'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='post-list-item', limit=2)[1]
        title = soup.find_all(class_='post-name', limit=2)[1]
        title2 = soup.find_all(class_='post-lead', limit=2)[1]
        href_split = re.split('"', str(href))
        # -------------------------------------
        web_1 = href_split[3]
        rs_1 = requests.get(web_1)
        soup1 = BeautifulSoup(rs_1.content.decode('utf-8'), 'html.parser')
        foto = soup1.find_all(class_='post-image', limit=2)[1]
        href_split = re.split('"', str(foto))
        myString = ' '.join(href_split)
        main_photo2 = re.findall(r'\b\w*https://kolesa-upload\w*\S*\b', myString)
        img_1 = main_photo2[1]

        # -------------------------------------
        title_split = re.split('"', str(title))
        myString = ''.join(title_split[2])
        m_split2 = re.split('>', str(myString))
        myString1 = ''.join(m_split2[1])
        m_split3 = re.split('<', str(myString1))
        # -------------------------------------
        title2_split = re.split('"', str(title2))
        myString0 = ''.join(title2_split[2])
        m_split20 = re.split('>', str(myString0))
        myString10 = ''.join(m_split20[1])
        m_split30 = re.split('<', str(myString10))
        # -------------------------------------
        kolesa.clear()
        kolesa.append(href_split[3])
        if kolesa != kolesa1:
            teleprint('\r' + "Kolesa.ru : " + str(kolesa != kolesa1) + "\n")

            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\kolesa.txt', 'w') as f_news:
                kolesa1.clear()
                f_news.write(href_split[3])

            kolesa1.append(href_split[3])
            j = ("*" + m_split3[0] + "*" + '\n\n')

            finish_text = ("_" + m_split30[0] + "_" + '\n\n')
            z = '(' + web_1 + ')'

            url = '[' + "Читать полностью..." + ']'
            media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown')]
            bot.send_media_group(chanel_name5, media)

            time.sleep(4)
            ProucwectBuya0()


        else:
            teleprint('\r' + "Kolesa.ru : " + str(kolesa != kolesa1))
            time.sleep(4)
            ProucwectBuya0()


    def ProucwectBuya0():
        # ----------поиск ссылки----------------------
        web_0 = 'https://ren.tv/news/kriminal'
        rs_0 = requests.get(web_0)
        soup = BeautifulSoup(rs_0.content.decode('utf-8'), 'html.parser')
        href = soup.find_all(class_='news__frame__link', limit=1)
        href_split = re.split('"', str(href[0]))  # ---------------------------- href_split[3] ссылка

        # -------------------------------------
        ProucwectBuya.clear()
        ProucwectBuya.append(href_split[3])

        if ProucwectBuya != ProucwectBuya1:
            teleprint('\r' + "REN TV criminal : " + str(ProucwectBuya != ProucwectBuya1) + "\n")
            # -------Сохранение ссылки ------------
            with open(r'C:\Users\user\Desktop\Python\My_bots\RememberNews\ProucwectBuya.txt', 'w') as f_news:
                ProucwectBuya1.clear()
                f_news.write(href_split[3])
            ProucwectBuya1.append(href_split[3])

            # ----------текст основной----------------------
            web_1 = 'https://ren.tv' + href_split[3]
            rs_1 = requests.get(web_1)
            soup1 = BeautifulSoup(rs_1.content.decode('utf-8'), 'html.parser')
            main_text = soup1.find_all(property="twitter:description")
            text_split = re.split("'", str(main_text))
            finish = text_split[1][0:100]  # ----------------------------------- finish текст основной
            finish_text = "_" + finish + "_" + "...\n\n"
            # ----------Заголовок----------------------
            title = soup1.find_all("title", limit=2)
            j = ''
            for tag in title:
                l = str(" ".join(tag.text.split()))
                title_split = re.split(" \|", str(l))
                title_split1 = re.split("'", str(title_split[0]))
                j = ("*" + title_split1[
                    0] + "*" + '\n\n')  # ----------------------------------- TITLE текст основной
            # ---------отправка---------------
            img_1 = "https://cdn.ren.tv/cache/1200x630/media/img/d9/dc/d9dc4da6818f19461ddf3839c8fc41111670db02.png"
            z = '(' + web_1 + ')'
            url = '[' + 'Читать полностью...' + ']'
            media = [types.InputMediaPhoto(img_1, caption=j + finish_text + url + z, parse_mode='Markdown')]
            bot.send_media_group(chanel_name4, media)
            time.sleep(2)





        else:
            teleprint('\r' + "REN TV criminal : " + str(ProucwectBuya != ProucwectBuya1) + "\n")
            time.sleep(2)


    ObwueRia()



except requests.ConnectionError:
    os.system('cls')
    print("Пропал ебучий Интернет когда искал новость [Новости]")

    time.sleep(10)



except requests.RequestException:
    os.system('cls')
    print('alarm, is disaster happen')

    time.sleep(10)


except IndexError:
    os.system('cls')
    print('Ошибка индекса')

    time.sleep(10)


except TimeoutError:
    os.system('cls')
    print("Connect Error [Новости]")

    time.sleep(10)


except Exception:
    os.system('cls')
    print("Какая то ошибка [Новости]")
    time.sleep(10)

# ---------NEWS_BOT

