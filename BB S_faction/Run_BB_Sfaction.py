# ---------------BirjaBot S_faction
import os, subprocess, logging

os.system("mode con cols=56 lines=30")
subprocess.Popen(['python.exe', r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\open_start.py'])

import requests, telebot, re, time, sys, glob, pyautogui, webbrowser, setproctitle
import simpleaudio as sa
from bs4 import BeautifulSoup
import mss
import mss.tools
import datetime as dt
from telebot import types

while True:
    try:
        DANTES_PEAK = []

        setproctitle.setproctitle('BB S_FACTION')
        in_game_trend = []
        Audio_on = []
        in_game_trend_sleep = [0]
        # BTCUSD имя
        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\audio.txt', 'r+',
                  encoding="utf-8") as f_news:
            Audio_on.clear()
            Audio_on.append(f_news.read())
        tsuga_count = 0

        BET = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\BET.wav")
        FIXMONEYPLUS = sa.WaveObject.from_wave_file(
            r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\FIXMONEYPLUS.wav")
        LOSTMONEY = sa.WaveObject.from_wave_file(
            r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\LOSTMONEY.wav")
        RANO = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\RANO.wav")
        SELL = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\SELL.wav")
        Signal = sa.WaveObject.from_wave_file(
            r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\Signal.wav")
        SUGA = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\SUGA.wav")

        HI = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\HI.wav")
        set1sec = sa.WaveObject.from_wave_file(
            r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\set1sek.wav")
        set1secover = sa.WaveObject.from_wave_file(
            r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\set1secover.wav")
        set5min = sa.WaveObject.from_wave_file(
            r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\set5min.wav")
        set5minover = sa.WaveObject.from_wave_file(
            r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\set5minover.wav")

        # os.system("taskkill /f /im  python.exe")

        if int(Audio_on[0]) == 1:
            play_obj = HI.play()
        name_main = "Hi! My name is BB S_Faction\n"
        autor = "Tom Jefferson made me.\n"
        hi_world_massege = "!Начинаю первичную настройку...Пожалуйста подождите.."


        def teleprint(*args, delay=0.01, str_join=' '):
            text = str_join.join(str(x) for x in args)
            n = len(text)
            for i, char in enumerate(text, 1):
                if i == n:
                    char = f'{char}\n'
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)


        teleprint(name_main + autor + hi_world_massege)
        BB_tg_token = []
        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\BB_tg_token.txt', 'r+') as f_news:
            BB_tg_token.append(f_news.read())

        bot = telebot.TeleBot(BB_tg_token[0])
        chanel_name = '@test_my_shit'
        v = "Я готов к работе."
        bot.send_message(chanel_name, text=v)


        def start_progtamm():
            in_game_trend_sleep.insert(0, '0')


        start_progtamm()

        code_5min_show = []
        Xsec = []
        check_end = []  # последняя 5ти минутная проверка.
        vol_20_min = []
        while True:

            try:
                c = []
                statistics = []
                cost_now = [0]
                web_0 = 'https://www.finam.ru/quote/cryptocurrencies/btc-usd/'
                rs_0 = requests.get(web_0)
                soup = BeautifulSoup(rs_0.content, 'html.parser')
                href = soup.find_all(class_="PriceInformation__price--26G", limit=1)
                over_string2 = ""
                for tag in href:
                    statistics.append(str(" ".join(tag.text.split())))
                    href_split = re.split(' ', str(statistics[0]))
                    over_string2 = str(href_split[0] + href_split[1])[:5]
                    if len(statistics) == 1:

                        statistics.append(str(" ".join(tag.text.split())))

                    else:
                        pass

                now_cost_v = over_string2
                # now_cost_v = str(int(now_cost_v2) * 10)
                print("Цена BTC сейчас: ", now_cost_v)
                time.sleep(0.8)
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\profit.txt', 'w') as f_news:
                    f_news.write('0')
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Sell.txt', 'w') as f_news:
                    f_news.write(now_cost_v)


                def main_function():

                    # получить данный с тхт файла найти большое число и маленькое. опрделить тренд
                    # временнОго диапазона и исходя из полученных данных и сравнения других диапазонов времени, определить окончательный тренд
                    # и выбирать из этого действия. Если два раза проиграл ставку то останавливается. Если выйграл продолжает. Настроить парог допустимой
                    # ямы для отката.
                    last_cot = []  # цена сейчас
                    first_cot = []  # цена начала времени сравнения (5, 15, 60 минут)

                    # ---------- код piygui на скачивание файла
                    def choose_start():
                        global c

                        # x = int(input("Веедите интервал (5, 10, 15, 30 минут): "))           # просим интервал
                        c.append("1")
                        print("\nНачинаю анализ рынка. Ничего не трогайте.\n")
                        '''webbrowser.open(url)
                        time.sleep(2)
                        webbrowser.open(url2)
                        time.sleep(1.8)'''
                        # Вставляем каждый раз на первое значение в листе последние данные по приросту
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD5min.txt',
                                  'r+') as f_news:
                            DANTES_PEAK.append(f_news.readlines()[1])

                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Xsec.txt', 'r+') as f_news:
                        Xsec.append(f_news.read())

                    t_time = 0
                    time_change = []
                    good_signal_bet = []
                    EASY_0 = []

                    while t_time <= int(Xsec[0]):

                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\EASY_1.txt',
                                  'r+') as f_news:
                            good_signal_bet.clear()
                            good_signal_bet.append(f_news.read())
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\EASY_0.txt',
                                  'r+') as f_news:
                            EASY_0.clear()
                            EASY_0.append(f_news.read())
                        # проверяю есть ли изменения для выхода из цикла
                        time_change.clear()
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\emergency_change.txt',
                                  'r+') as f_news:
                            time_change.append(f_news.read())

                        if int(time_change[0]) == 0:
                            time.sleep(1)
                            sys.stdout.write('\r' + "Новый поиск через: " + str(int(Xsec[0]) - int(t_time)) + " сек...")
                            t_time += 1

                        elif int(time_change[0]) == 1:
                            print(
                                "\nОбнаружено принудительное пробуждение.\nНачинаю анализ для лучшего вхождения в рынок\n")
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\emergency_change.txt',
                                      'w') as f_news:
                                f_news.write("0")
                            break
                    Xsec.clear()
                    choose_start()

                    day_trend_list = []
                    day_trend_list_5min = []
                    day_trend_list2 = []  # промежуточный список
                    day_trend_list3 = []  # промежуточный список
                    day_trend_list4 = []  # хранение списка 4ех котировок в 5ти минутке

                    trend_day_count = 0
                    lst_count = 0  # --------------последнее начение курса--------------------
                    frs_count = 1  # ----------- значение на (6 * N)=30 мин назад, где N это выбранный диапазон

                    # min_5_download

                    def min_5_dowload():
                        global count_win, count_lose, obwuu_profit
                        # print("Поступил сигнал,проверяю на 3ти минутах.")
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Xsec.txt', 'w') as f_news:
                            f_news.write("5")
                        day_trend_list4.clear()
                        time.sleep(1.5)
                        trend_day_count = 0
                        lst_count5 = 1  # --------------последнее начение курса--------------------
                        frs_count5 = 2  # ----------- значение на (6 * N)=30 мин назад, где N это выбранный диапазон
                        try:
                            while trend_day_count <= 3:
                                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD5min.txt',
                                          'r+',
                                          encoding="utf-8") as f_news:
                                    last_cot.clear()
                                    last_cot.append(f_news.readlines()[lst_count5])
                                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD5min.txt',
                                          'r+',
                                          encoding="utf-8") as f_news:
                                    first_cot.clear()
                                    first_cot.append(f_news.readlines()[
                                                         frs_count5])  # <----- (-3 это 15 минут назад -6 это 30 мин назад и т.д если интервал 5 мин)

                                lst_count5 += 1
                                frs_count5 += 1
                                # print(lst_count, frs_count)
                                # -----l -> last-------f -> first----------------------
                                l = last_cot
                                l = [line.rstrip() for line in l]
                                f = first_cot
                                f = [line.rstrip() for line in f]

                                now_cost = str(l[0])
                                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_now.txt',
                                          'w') as f_news:
                                    f_news.write(now_cost)
                                # ---------------------
                                start_cost = str(f[0])
                                # запоинать цену которая выдала еденица и сравнивать последущие значения с ней, чтобы определить идет ли рост

                                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\EASY_0.txt', 'r+',
                                          encoding="utf-8") as f_news:
                                    EASY_0.clear()
                                    EASY_0.append(f_news.read())
                                if int(now_cost) > int(start_cost):  # ----------сравниваем

                                    j = int(now_cost) - int(start_cost)  # 1 - 5 = -4 \ 5 - 1 = 4

                                    # day_trend_list2.append(str(j) + time_cost)
                                    day_trend_list4.append(now_cost + "(+" + str(int(now_cost) - int(start_cost)) + ")")

                                    day_trend_list3.append(now_cost)
                                    # good_signal = int(good_signal_bet[0])

                                    # !!! на 5ти минутах и порог выше для '1'  !!!

                                    good_signal = int(EASY_0[0])
                                    if int(j) >= good_signal:

                                        day_trend_list_5min.append("1")
                                        # print(float(j), last_list_split2[0], first_list_split2[0])
                                        with open(
                                                r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_begin.txt',
                                                'w') as f_news:
                                            f_news.write(now_cost)
                                    else:
                                        day_trend_list_5min.append("2")

                                        day_trend_list3.append(now_cost)
                                # запоинать цену которая выдала еденица и сравнивать последущие значения с ней, чтобы определить идет ли рост

                                elif int(now_cost) <= int(start_cost):
                                    trend_day_count += 1
                                    day_trend_list4.append(now_cost + "(" + str(int(now_cost) - int(start_cost)) + ")")
                                    if int(int(now_cost) - int(start_cost)) <= int(EASY_0[0]):
                                        day_trend_list_5min.append("0")
                                    else:
                                        day_trend_list_5min.append("2")
                                    day_trend_list3.append(now_cost)
                                trend_day_count += 1

                        # min_5_dowload over
                        except FileNotFoundError:
                            print('Не смог найти фаил для анализа. Пауза 20 сек')
                            start_progtamm()

                    mainCODE = []

                    while trend_day_count <= 3:
                        open_try = 0

                        while open_try <= 5:
                            try:
                                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt',
                                          'r+',
                                          encoding="utf-8") as f_news:
                                    last_cot.clear()
                                    last_cot.append(f_news.readlines()[lst_count])
                                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt',
                                          'r+',
                                          encoding="utf-8") as f_news:
                                    first_cot.clear()
                                    first_cot.append(f_news.readlines()[frs_count])
                            except UnicodeDecodeError:
                                print('Не смог прочесть фаил на 1 минуту. Попытка:', open_try)
                                open_try += 1
                                time.sleep(2)
                                continue
                            break
                        if open_try >= 5:
                            print('Найти фаил 1"ой минуты не удалось. Перезагружаюсь')
                            time.sleep(3)
                            main_function()
                        # print("COUNT: ",trend_day_count)

                        lst_count += 1
                        frs_count += 1
                        # print(lst_count, frs_count)
                        # -----l -> last-------f -> first----------------------
                        l = last_cot
                        l = [line.rstrip() for line in l]
                        f = first_cot
                        f = [line.rstrip() for line in f]

                        now_cost = str(l[0])
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_now.txt',
                                  'w') as f_news:
                            f_news.write(now_cost)
                        # ---------------------
                        start_cost = str(f[0])
                        # print(now_cost, start_cost)
                        # Сравнение цены. Чтобы узнать идет ли плюс. Это для снятия ставки в случае 01 21 00
                        in_game_trend2 = str(int(now_cost) - int(start_cost))

                        if int(now_cost) > int(start_cost):  # ----------сравниваем

                            j = int(now_cost) - int(start_cost)  # 1 - 5 = -4 \ 5 - 1 = 4

                            # day_trend_list2.append(str(j) + time_cost)
                            if trend_day_count > 0:
                                day_trend_list2.append("(+" + str(int(now_cost) - int(start_cost)) + ")")
                            else:
                                day_trend_list2.append(now_cost + "(" + str(int(now_cost) - int(start_cost)) + ")")
                            day_trend_list3.append(now_cost)
                            good_signal = int(good_signal_bet[0])

                            # print(int(j), now_cost, start_cost)
                            # print(j)

                            if int(j) >= good_signal:

                                day_trend_list.append("1")
                                # print(float(j), last_list_split2[0], first_list_split2[0])
                                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_begin.txt',
                                          'w') as f_news:
                                    f_news.write(now_cost)
                            else:
                                day_trend_list.append("2")

                                day_trend_list3.append(now_cost)

                        # запоинать цену которая выдала еденица и сравнивать последущие значения с ней, чтобы определить идет ли рост

                        else:

                            if trend_day_count > 0:
                                day_trend_list2.append("(" + str(int(now_cost) - int(start_cost)) + ")")
                            else:
                                day_trend_list2.append(now_cost + "(" + str(int(now_cost) - int(start_cost)) + ")")

                            day_trend_list3.append(now_cost)
                            if int(int(now_cost) - int(start_cost)) <= int(EASY_0[0]):
                                day_trend_list.append("0")
                            else:
                                day_trend_list.append("2")
                            day_trend_list3.append(now_cost)
                        # VOL CHECKER BEGIN
                        if trend_day_count == 0:
                            # СУТЬ УЗНАТЬ СУММУ 20 ПОСЛЕДНИХ МИНУТ
                            now_5_min = []
                            before_5_min = []
                            time.sleep(1.5)
                            lst_5count = 0
                            frs_5count = 1
                            DP = []
                            check_5 = 0
                            while check_5 <= 3:
                                open_try = 0
                                while open_try <= 5:
                                    try:
                                        with open(
                                                r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD5min.txt',
                                                'r+',
                                                encoding="utf-8") as f_news:
                                            now_5_min.clear()
                                            now_5_min.append(f_news.readlines()[lst_5count])
                                        with open(
                                                r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD5min.txt',
                                                'r+',
                                                encoding="utf-8") as f_news:
                                            before_5_min.clear()
                                            before_5_min.append(f_news.readlines()[
                                                                    frs_5count])  # <----- (-3 это 15 минут назад -6 это 30 мин назад и т.д если интервал 5 мин)
                                    except UnicodeDecodeError:
                                        print('Не смог прочесть фаил на 5ти инутах. Попытка:', open_try)
                                        open_try += 1
                                        time.sleep(2)
                                        continue
                                    break
                                if open_try >= 5:
                                    print('Найти фаил 5минут не удалось. Перезагружаюсь')
                                    time.sleep(3)
                                    main_function()
                                lst_5count += 1
                                frs_5count += 1
                                # print(lst_count, frs_count)
                                # -----l -> last-------f -> first----------------------
                                l = now_5_min
                                l = [line.rstrip() for line in l]
                                f = before_5_min
                                f = [line.rstrip() for line in f]

                                min5_now_cost = str(l[0])  # ---------------------------Цена 1 (первые 5 знаков)
                                # ---------------------
                                min5_start_cost = str(f[0])

                                if check_5 == 1:
                                    with open(
                                            r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\keep_calm_bet.txt',
                                            'w') as f_news:
                                        f_news.write(str(min5_now_cost))
                                min5_PLUS_or_Minus = int(int(min5_now_cost) - int(min5_start_cost))
                                DP.append(min5_PLUS_or_Minus)
                                check_5 += 1

                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\vol_3min_check.txt',
                                      'w') as f_news:
                                f_news.write(str(DP))
                            DANTES_PEAK.clear()
                            DANTES_PEAK.append(DP[0])
                            DANTES_PEAK.append(DP[1])
                            DANTES_PEAK.append(DP[2])
                            DANTES_PEAK.append(DP[3])
                            vol_20_min.clear()
                            vol_20_min.append(int(int(DP[1]) + int(DP[2]) + int(DP[3])))

                            vol_show.append(DP[0])
                            vol_show.append(DP[1])
                            if int(DP[1]) >= 80:
                                check_end.clear()
                                check_end.append('1')
                            else:
                                check_end.clear()
                                check_end.append('0')

                            # vol cheker finish

                            with open(r'C:\\Users\\user\\Desktop\Python\My_bots\BirjaBotS_faction\in_game_trend.txt',
                                      'w') as f_news:
                                in_game_trend.insert(0, in_game_trend2)
                                f_news.write(str(in_game_trend2))

                        trend_day_count += 1
                    # VOL CHECKER OVER

                    saved_cost = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_begin.txt',
                              'r+') as f_news:
                        saved_cost.append(f_news.read())
                    os.system('cls')
                    global count_win, count_lose, obwuu_profit, tsuga_count, play_obj
                    # print(day_trend_list2)
                    print("-----------\nСейчас       -1min    -2min     -3min \n" + str(day_trend_list2))
                    print("Код: " + str(
                        str(day_trend_list[0] + str(day_trend_list[1])) + str(
                            str(day_trend_list[2] + str(day_trend_list[3])))))
                    # print('check_end:', check_end)
                    # , "(создать отдельную переменную для сохранения всех ставок)")
                    # teleprint("Сигналы закрытия ставки: функция запоминает ставку и послед цена вычитает разницу и показывает или прибыль или убыль")
                    trend_k = int(day_trend_list3[0]) - int(Byu_bet_len[0])

                    # ЛОГИКА ____
                    # TEST
                    min_5_dowload()
                  
                    code_5min_show.clear()
                    code_5min_show.append(day_trend_list_5min[0] + day_trend_list_5min[1])
                    info_5min = str(code_5min_show[0] + " " + str(DANTES_PEAK[0]))
                    with open(r'C:\\Users\\user\\Desktop\Python\My_bots\BirjaBotS_faction\while_code_man.txt',
                              'w') as f_news:
                        f_news.write(str(info_5min))
                    # TEST

                    FIRSTCODE = ["12", "11", "10"]
                    l3 = mainCODE
                    res = [x for x in FIRSTCODE + l3 if x not in FIRSTCODE or x not in l3]

                    # SLEEP 00 begin
                    DOWN_BET_CODE = ["00", "02", "01"]
                    l5 = mainCODE
                    res_down = [x for x in DOWN_BET_CODE + l5 if x not in DOWN_BET_CODE or x not in l5
                                ]
                    if len(res_down) == 2:

                        DOWN_BET_CODE2 = []
                        DOWN_BET_CODE2.clear()

                        DOWN_BET_CODE2.append(str(day_trend_list_5min[0]) + str(day_trend_list_5min[1]))
                        SECONDCODE_DOWN = ["02", "00", "01"]
                        l4 = DOWN_BET_CODE2
                        res2 = [x for x in SECONDCODE_DOWN + l4 if x not in SECONDCODE_DOWN or x not in l4]
                        os.system('cls')
                        if len(res2) >= 4:

                            pass
                            # print("\nПОКА НЕ ВРЕМЯ СТАВИТЬ В ШОРТ...\n")


                        elif len(res2) <= 3:
                            # "TO SHORT IF"
                            # ЕСЛИ в эти 5 минут цена больше чем -40
                            # ЕСЛИ МИНУТНАЯ ЦЕНА МЕНЬШЕ -10
                            # И МИНУТНАЯ ЦЕНА БОЛЬШЕ -80 И ЦЕНА 5МИН НАЗАД БОЛЬШЕ -220
                            # И ПРИРОСТ ЗА 20 МИН БОЛЬШЕ -300
                            if int(DANTES_PEAK[0]) > -40 and int(in_game_trend[0]) <= 20 and \
                                    int(in_game_trend[0]) >= -80 and int(vol_show[1]) >= -220 and int(
                                vol_20_min[0]) >= -300:
                                # ПРОВЕРКА НА СВЕЧУ ------------------------------------------------------
                                zero_count = [0]

                                def last_control():

                                    keep_calm_count = 0
                                    YES_NO = []

                                    # while keep_calm_count <= 1:

                                    play_obj = signal.play()
                                    subprocess.call(
                                        ["python",
                                         r"C:\\Users\\user\Desktop\Python\My_bots\BirjaBotS_faction\keep_calm_down.py",
                                         "-i",
                                         "10", "-l",
                                         "2"])
                                    # os.system('cls')
                                    keep_calm_count += 1
                                    with open(
                                            r'C:\\Users\\user\Desktop\Python\My_bots\BirjaBotS_faction\keep_calm.txt',
                                            'r+',
                                            encoding="utf-8") as f_news:
                                        YES_NO.clear()
                                        YES_NO.append(f_news.read())

                                    if int(YES_NO[0]) == 1:
                                        zero_count.insert(0, 3)

                                        # break

                                    # ------------------------Из ЦУГИ
                                    if int(YES_NO[0]) == 0:
                                        print('Свеча выросла выше прошлых 5 минут. Нахуй. Ставить не буду')
                                        bot.send_message(chanel_name,
                                                         text="Планировал ставку в ШОРТ. Но что то не сраслось")

                                    '''elif int(YES_NO[0]) == 0:
                                        print('Цена падает. Не ставлю, Мониторю')
                                        zero_count.insert(0, int(zero_count[0]) + 1 )
                                        print('Попытка: ', zero_count[0], 'из 2ух')'''

                                last_control()

                                # ПРОВЕРКА НА СВЕЧУ ----------------------------------------------------------------

                            if int(vol_20_min[0]) <= -300:
                                teleprint("\nМЫ НА ПИКЕ ПАДЕНИЯ. СТАВИТЬ НЕ БУДУ\n ")
                            elif int(in_game_trend[0]) >= 20:
                                teleprint("\nРЫНОК ЕЩЕ СЛАБ ДЛЯ УВЕРЕННОЙ СТАВКИ В ШОРТ . СТАВИТЬ НЕ БУДУ\n")
                            else:
                                print('\nНе подходящее условия на рынке для SHORT ставки\n')


                    else:
                        pass

                    if len(res) == 2:

                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Xsec.txt',
                                  'w') as f_news:
                            # print("Поехали, че то намечается, начинаю мониторить каждые 5 сек")
                            if int(Audio_on[0]) == 1:
                                play_obj = Signal.play()
                            f_news.write("5")

                        mainCODE2 = []
                        mainCODE2.clear()

                        mainCODE2.append(str(day_trend_list_5min[0]) + str(day_trend_list_5min[1]))
                        SECONDCODE = ["12", "11", "10"]
                        l4 = mainCODE2
                        res2 = [x for x in SECONDCODE + l4 if x not in SECONDCODE or x not in l4]
                        # os.system('cls')
                        if len(res2) >= 4:

                            # print("\nПОКА НЕ ВРЕМЯ СТАВИТЬ В ЛОНГ...\n")
                            pass

                        elif len(res2) <= 3:
                            # "TO LONG IF"
                            # ЕСЛИ в эти 5 минут цена  меньше чем 40
                            # ЕСЛИ ЦЕНА МИНУТНАЯ ЦЕНА БОЛЬШЕ 10
                            # И МИНУТНАЯ ЦЕНА МЕНЬШЕ 80 И ЦЕНА 5МИН НАЗАД МЕНЬШЕ 220
                            # И ПРИРОСТ ЗА 20 МИН МЕНЬШЕ 300
                            if int(DANTES_PEAK[0]) < 40 and int(in_game_trend[0]) >= -20 and \
                                    int(in_game_trend[0]) <= 80 and int(vol_show[1]) <= 220 and int(
                                vol_20_min[0]) <= 300:
                                zero_count = [0]

                                # ПРОВЕРКА НА СВЕЧУ ------------------------------------------------------
                                def last_control():

                                    keep_calm_count = 0
                                    YES_NO = []

                                    # while keep_calm_count <= 1:
                                    play_obj = signal.play()
                                    subprocess.call(
                                        ["python",
                                         r"C:\\Users\\user\Desktop\Python\My_bots\BirjaBotS_faction\keep_calm.py",
                                         "-i",
                                         "10", "-l",
                                         "2"])
                                    # os.system('cls')
                                    keep_calm_count += 1
                                    with open(
                                            r'C:\\Users\\user\Desktop\Python\My_bots\BirjaBotS_faction\keep_calm.txt',
                                            'r+',
                                            encoding="utf-8") as f_news:
                                        YES_NO.clear()
                                        YES_NO.append(f_news.read())

                                    if int(YES_NO[0]) == 1:
                                        zero_count.insert(0, 3)

                                        # break
                                    # ------------------------Из ЦУГИ
                                    if int(YES_NO[0]) == 0:
                                        print('Свеча упала ниже прошлых 5 минут. Нахуй. Ставить не буду')
                                        bot.send_message(chanel_name,
                                                         text="Планировал ставку ЛОНГ. Но что то не сраслось")

                                        # break

                                    '''elif int(YES_NO[0]) == 0:
                                        print('Цена падает. Не ставлю, Мониторю')
                                        zero_count.insert(0, int(zero_count[0]) + 1 )
                                        print('Попытка: ', zero_count[0], 'из 2ух')'''

                                    # bot.send_message(chanel_name, text="Цена падает. Не ставлю, Мониторю")

                                last_control()

                                # ПРОВЕРКА НА СВЕЧУ ----------------------------------------------------------------

                            if int(vol_20_min[0]) >= 300:
                                teleprint("\nМЫ НА ПИКЕ. СТАВИТЬ НЕ БУДУ\n ")
                            elif int(in_game_trend[0]) <= -20:
                                teleprint("\nРЫНОК ЕЩЕ СЛАБ ДЛЯ УВЕРЕННОЙ СТАВКИ D ЛОНГ . СТАВИТЬ НЕ БУДУ\n")
                            else:
                                print('\nНе подходящее условия на рынке для LONG ставки\n')


                    else:
                        pass
                    # print("КОД 5; " + str(code_5min_show[0]), '\n' + str(day_trend_list4))
                    print("КОД 5; " + str(code_5min_show[0]))

                    if trend_k > 0:
                        j = count_win + count_lose
                        teleprint("\n-----------\nВсего сделок: ", j, "\nВыиграно сделок: " + str(count_win))
                        print("Total Profit:", str(obwuu_profit), "$", "\n\nCostNow:", day_trend_list3[0], "( +",
                              trend_k,
                              ")\n-----------\n")

                    else:
                        j = count_win + count_lose
                        teleprint("\n-----------\nВсего сделок: ", j, "\nВыиграно сделок: " + str(count_win))
                        print("Total Profit:", str(obwuu_profit), "$", "\nCostNow:", day_trend_list3[0], "(", trend_k,
                              ")\n-----------\n")

                    print("ПРИРОСТ 1 МИН: " + str(in_game_trend[0]) + '\nПРИРОСТ 5 МИН:   ' + str(
                        vol_show) + "\nПРИРОСТ 20 МИН: " + str(vol_20_min[0]) + '\n-----------\n')
                    # удаление файлов в папке в цикле.

                    vol_show.clear()


                def start_bet():
                    # делает ставку на сайте
                    pass


                def start_cell():
                    # продает
                    pass


                vol_show = []

                while True:

                    now = dt.datetime.now()
                    '''def time_work():
                        w_time = 0
                        while not (now.hour >= 9 and now.hour < 19):

                            if now.hour >= 9 and now.hour < 19:
                                break
                            else:
                                os.system('cls')
                                print("Трейдинг недоступен.\nЧасы работы с 9 до 19ти")
                                sys.stdout.write('\r' + "Сверка времени через: " + str(20 - int(w_time)) + " сек...")
                                w_time += 1
                                time.sleep(1)
                                continue
                    time_work()'''

                    profit_load = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt', 'r+',
                              encoding="utf-8") as f_news:
                        profit_load.clear()
                        profit_load.append(f_news.read())
                    obwuu_profit = int(profit_load[0])

                    win_load = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_win.txt', 'r+',
                              encoding="utf-8") as f_news:
                        win_load.clear()
                        win_load.append(f_news.read())
                    count_win = int(win_load[0])

                    lose_load = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_lose.txt', 'r+',
                              encoding="utf-8") as f_news:
                        lose_load.clear()
                        lose_load.append(f_news.read())
                    count_lose = int(lose_load[0])
                    # Считывание настроек аудио
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\audio.txt',
                              'r+') as f_news:
                        Audio_on.clear()
                        Audio_on.append(f_news.read())

                    TSUGA_LIMIT = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\TSUGA_LIMIT.txt',
                              'r+') as f_news:
                        TSUGA_LIMIT.clear()
                        TSUGA_LIMIT.append(f_news.read())
                    profit_total = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\profit.txt', 'r+') as f_news:
                        profit_total.append(f_news.read())
                    Byu_bet_len = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Bet.txt', 'r+') as f_news:
                        Byu_bet_len.append(f_news.read())
                    Last_sell = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Sell.txt', 'r+') as f_news:
                        Last_sell.append(f_news.read())
                    in_game = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game.txt', 'r+') as f_news:
                        in_game.append(f_news.read())
                    stop_comand = []
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\stop_comand.txt',
                              'r+') as f_news:
                        stop_comand.append(f_news.read())
                    if int(stop_comand[0]) == 0:

                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game_trend.txt',
                                  'r+') as f_news:
                            in_game_trend.insert(0, str(f_news.read()))
                            if len(in_game_trend) >= 3:
                                in_game_trend.pop(-1)

                        main_function()
                    else:
                        os.system('cls')
                        print('\r Торговая сессия приостановлена...Жду команду для продолжения...', end='')
                        time.sleep(5)





            except FileNotFoundError:
                print("Нет файла в папках")
                # bot.send_message(chanel_name, text="FileNotFoundError / Reloading,,,")
                time.sleep(1)
                pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
                start_progtamm()
                time.sleep(10)
                continue

            except IndexError:

                print("Ошибка индекса")
                bot.send_message(chanel_name, text="Index Error / Reloading,,,")
                time.sleep(1)
                pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
                start_progtamm()
                time.sleep(10)
                continue

            except Exception as err:
                logging.error(err, exc_info=True)
                bot.send_message(chanel_name, text="Critical Error / Reloading,,,")
                print("\nCritical Error / Reloading,,,")
                time.sleep(1)
                pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
                start_progtamm()
                time.sleep(10)
                continue

    except requests.ConnectionError:
        print("Нет ебучего интернета / Reloading,,")
        # bot.send_message(chanel_name, text="Нет ебучего интернета / Reloading,,,")
        time.sleep(1)
        pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
        # start_progtamm()
        time.sleep(10)

        continue
    except TimeoutError:
        print("Connect Error / Reloading,,,")
        # bot.send_message(chanel_name, text="Connect Error / Reloading,,,")
        time.sleep(1)
        pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
        # start_progtamm()
        time.sleep(10)
        continue