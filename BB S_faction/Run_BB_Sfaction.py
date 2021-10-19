# ---------------BirjaBot S_faction

import requests, telebot, re, time, sys, os, glob, pyautogui, subprocess, webbrowser, setproctitle
import simpleaudio as sa
from bs4 import BeautifulSoup
from mss import mss
import datetime as dt
from telebot import types
files = glob.glob('C:\\Users\\user\\Desktop\\Python\\My_bots\\BirjaBotS_faction\\txt\\*')
for f in files:
    os.remove(f)
setproctitle.setproctitle('BB S_FACTION')
in_game_trend = []
Audio_on = []
in_game_trend_sleep = [0]
# BTCUSD имя
url = 'https://export.finam.ru/export9.out?market=520&em=484429&token=03AGdBq262xn2t6o5yg9JmHufTucBtBpq10aQZZBkdMCxlXtubwJ3eTa9uGdqTLDZvHCPZyb75hEWn-zHf-lN_rEQRGwxatnr6YscwwDiZECsnQ-oWXxjrOaWqghfE243trlcthbwsQcabj2mdgebOPSKZonBv1UW-BpkoWXthqb2FwI9gZ_WLAx-Gtn00vcq9yNOlqWaCY-EiPYVs6s4PwANMLz74VPWIwwhsIOs5XTIRZYWoppCKK3pylceKwrGAQvDCmKgoxhMp3u--rpLvczl4sFW0d-juWZHXWyMiW1tmO-z802Bqhw7yJOlHQv9aqx4YhxS8mr7oi7O65V5ZPoSzyHKErtk1INe5mfDGo0ZqQZEyBSYomEReAl9Qwy2fu1omU65r7qJeHOb2--fj_YyAbvHVLbfUTdBFtR0MaT9tGQpXFO7naAQXEVJsFImBHyYQcJBW6ylL&code=GDAX.BTC-USD&apply=0&df=20&mf=9&yf=2021&from=20.10.2021&dt=20&mt=9&yt=2021&to=20.10.2021&p=2&f=BTCUSD&e=.txt&cn=BTCUSD&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=4&at=1'
# DANTES_PEAK имя
url3 = 'https://export.finam.ru/export9.out?market=520&em=484429&token=03AGdBq24msi9xYSme1_Z-mFARC2xvviUqIIuYExvcHqCUz_gg42sOwPCqo04XUUnxrs8PfVYBsVj6mt6rA74dBVMuhzDEoIApOFf7x4TFXyyYPRUI8rFLhduNW5Dk0Z348StYySG1uGgAnaE4gp_idxCDS7DkRHPWngJhk_uYdaJEY8YTUTs6NtbKLhxdbomTfGa7BxOjj5DGVWZr5z-Gwx5W9f9UCCMF9G3del7Wvkog1hVonl2r5DmCuscztER-Ycp4j3q0QvPVy9TUPes0813GBv03QWjgN6HgI1WfTyLqGEa9oBx9Zs2ceHgX9j79DgiNwqUJZCOR3qux3bg0YuidoVfcV04WIo2h5n-QIuQzj6pnHzjha3xa-0fkYtxeWkVBYo7vy6pSzLu6hHZvH_tfEAgfg6N20mxPfFvMmqVeRR881g1yz6LbHtQlxN6abvIvWpvHVFqw&code=GDAX.BTC-USD&apply=0&df=20&mf=9&yf=2021&from=20.10.2021&dt=20&mt=9&yt=2021&to=20.10.2021&p=2&f=DANTES_PEAK&e=.txt&cn=GDAX.BTC-USD&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=5&at=1'
with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\audio.txt', 'r+',
          encoding="utf-8") as f_news:
    Audio_on.clear()
    Audio_on.append(f_news.read())
tsuga_count = 0

BET = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\BET.wav")
FIXMONEYPLUS = sa.WaveObject.from_wave_file(
    r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\FIXMONEYPLUS.wav")
LOSTMONEY = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\LOSTMONEY.wav")
RANO = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\RANO.wav")
SELL = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\SELL.wav")
Signal = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\Signal.wav")
SUGA = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\SUGA.wav")

HI = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\HI.wav")
set1sec = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\set1sek.wav")
set1secover = sa.WaveObject.from_wave_file(
    r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\set1secover.wav")
set5min = sa.WaveObject.from_wave_file(r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\set5min.wav")
set5minover = sa.WaveObject.from_wave_file(
    r"C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\set5minover.wav")

# os.system("taskkill /f /im  python.exe")
os.system("mode con cols=56 lines=17")
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

# НАЧАЛЬНАЯ НАСТРОЙКА ВЫСТАВЛЕНИЯ  ПРограммы на второй экран
pyautogui.keyDown("win")
time.sleep(0.4)
pyautogui.press("up")
time.sleep(0.4)
pyautogui.keyUp("win")
time.sleep(0.8)
pyautogui.moveTo(45, 13, 0.2)
pyautogui.mouseDown(button='left')
time.sleep(0.8)
pyautogui.moveTo(748, 520, 0.4)
pyautogui.mouseUp(button='left')


def start_progtamm():
    in_game_trend_sleep.insert(0, '0')
    print("Все. Поехали.")


start_progtamm()

cx = []

with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt', 'r+',
          encoding="utf-8") as f_news:
    cx.clear()
    cx.append(f_news.read())
obwuu_profit = int(cx[0])

wx = []

with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_win.txt', 'r+',
          encoding="utf-8") as f_news:
    wx.clear()
    wx.append(f_news.read())

count_win = int(wx[0])

lx = []
with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_lose.txt', 'r+',
          encoding="utf-8") as f_news:
    lx.clear()
    lx.append(f_news.read())

count_lose = int(lx[0])

Xsec = []

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
                v = "Я готов к работе."
                bot.send_message(chanel_name, text=v)
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
                files = glob.glob('C:\\Users\\user\\Desktop\\Python\\My_bots\\BirjaBotS_faction\\txt\\*')
                for f in files:
                    os.remove(f)
                # x = int(input("Веедите интервал (5, 10, 15, 30 минут): "))           # просим интервал
                c.append("1")
                print("\nНачинаю анализ рынка. Ничего не трогайте.\n")
                webbrowser.open(url)
                time.sleep(2)

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
                    print("\nОбнаружено принудительное пробуждение.\nНачинаю анализ для лучшего вхождения в рынок\n")
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
            lst_count = -1  # --------------последнее начение курса--------------------
            frs_count = -2  # ----------- значение на (6 * N)=30 мин назад, где N это выбранный диапазон

            # min_5_dowload

            def min_5_dowload():
                global count_win, count_lose, obwuu_profit
                print("Поступил сигнал,проверяю на 5ти минутах.")
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Xsec.txt', 'w') as f_news:
                    f_news.write("5")
                # day_trend_list4.clear()
                files = glob.glob('C:\\Users\\user\\Desktop\\Python\\My_bots\\BirjaBotS_faction\\txt\\*')
                for f in files:
                    os.remove(f)
                webbrowser.open(url)
                time.sleep(1.5)
                trend_day_count = 0
                lst_count = -2  # --------------последнее начение курса--------------------
                frs_count = -3  # ----------- значение на (6 * N)=30 мин назад, где N это выбранный диапазон
                try:
                    while trend_day_count <= 3:
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt', 'r+',
                                  encoding="utf-8") as f_news:
                            last_cot.clear()
                            last_cot.append(f_news.readlines()[lst_count])
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt', 'r+',
                                  encoding="utf-8") as f_news:
                            first_cot.clear()
                            first_cot.append(f_news.readlines()[
                                                 frs_count])  # <----- (-3 это 15 минут назад -6 это 30 мин назад и т.д если интервал 5 мин)

                        lst_count -= 1
                        frs_count -= 1
                        # print(lst_count, frs_count)
                        # -----l -> last-------f -> first----------------------
                        l = last_cot
                        l = [line.rstrip() for line in l]
                        f = first_cot
                        f = [line.rstrip() for line in f]

                        last_list_split = re.split(',', str(l[0]))  # отжим необходимых чисел
                        # time_cost = str(int(str(last_list_split[-2])[2:4]) - 1)
                        last_list_split2 = re.split("'", str(last_list_split[-1]))
                        first_list_split = re.split(',', str(f[0]))
                        # print(last_list_split,first_list_split)
                        first_list_split2 = re.split("'", str(first_list_split[-1]))

                        now_cost = str(last_list_split2[0])[:5]  # ---------------------------Цена 1 (первые 5 знаков)
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_now.txt',
                                  'w') as f_news:
                            f_news.write(now_cost)
                        # ---------------------
                        start_cost = str(first_list_split2[0])[
                                     :5]  # ----------------------------Цена 2 (первые 5 знаков)
                        # запоинать цену которая выдала еденица и сравнивать последущие значения с ней, чтобы определить идет ли рост

                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\EASY_0.txt', 'r+',
                                  encoding="utf-8") as f_news:
                            EASY_0.clear()
                            EASY_0.append(f_news.read())
                        if int(now_cost) > int(start_cost):  # ----------сравниваем
                            trend_day_count += 1
                            j = int(now_cost) - int(start_cost)  # 1 - 5 = -4 \ 5 - 1 = 4

                            # day_trend_list2.append(str(j) + time_cost)
                            day_trend_list4.append(now_cost + "(+" + str(int(now_cost) - int(start_cost)) + ")")

                            day_trend_list3.append(now_cost)
                            good_signal = int(good_signal_bet[0])

                            if int(j) >= good_signal:

                                day_trend_list_5min.append("1")
                                # print(float(j), last_list_split2[0], first_list_split2[0])
                                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_begin.txt',
                                          'w') as f_news:
                                    f_news.write(now_cost)
                            else:
                                day_trend_list_5min.append("2")

                                day_trend_list3.append(now_cost)
                        # запоинать цену которая выдала еденица и сравнивать последущие значения с ней, чтобы определить идет ли рост

                        elif int(now_cost) < int(start_cost):
                            trend_day_count += 1
                            day_trend_list4.append(now_cost + "(" + str(int(now_cost) - int(start_cost)) + ")")
                            if int(int(now_cost) - int(start_cost)) <= int(EASY_0[0]):
                                day_trend_list_5min.append("0")
                            else:
                                day_trend_list_5min.append("2")
                            day_trend_list3.append(now_cost)

                # min_5_dowload over
                except FileNotFoundError:
                    print('Не смог найти фаил для анализа. Пауза 20 сек')
                    start_progtamm()

            mainCODE = []

            def BET1():
                global count_win, count_lose, obwuu_profit

                callback_worker = []
                callback_worker.clear()
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\sell_now.txt', 'r+') as f_news:
                    callback_worker.append(f_news.read())
                if int(callback_worker[0]) == 1:
                    global count_win, count_lose, obwuu_profit
                    if int(in_game[0]) == 1:
                        bot.send_message(chanel_name, "Ставка снята")
                        Last_sell.append(day_trend_list3[0])
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Sell.txt', 'w') as f_news:
                            f_news.write(day_trend_list3[0])
                        kj = trend_k
                        if int(kj) > 0:
                            s = str("Фиксирую прибыль: +" + str(kj))
                            obwuu_profit += int(kj)
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt',
                                      'w') as f_news:
                                f_news.write(str(obwuu_profit))
                            count_win += 1
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_win.txt',
                                      'w') as f_news:
                                f_news.write(str(count_win))
                            print(s)
                            # "[ФИКС. ПРОФИТ][BTC][ЗАК.КУРС: " + str(day_trend_list3[0]) + "]"
                            telemsg = str("[ФИКС. ПРОФИТ]\n[BTC][ЗАК.КУРС: " + str(day_trend_list3[0]) + "]"
                                          + "\nИтоговая прибыль сделки: +" + str(
                                kj) + "\nСтавок в плюс сегодня: " + str(
                                count_win)
                                          + "\nСтавок в минус :" + str(count_lose) +
                                          "\nОбщий доход за сегодня :" + str(obwuu_profit) + "\nVOL: " + str(vol_show))
                            bot.send_message(chanel_name, text=telemsg)
                            with mss() as sct:
                                sct.shot()
                            photo = open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\monitor-1.png', 'rb')
                            bot.send_photo(chanel_name, photo)

                        else:
                            v = str("Заработать не получилось...Мы проебали: " + str(kj))
                            count_lose += 1
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_lose.txt',
                                      'w') as f_news:
                                f_news.write(str(count_lose))
                            obwuu_profit += int(kj)
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt',
                                      'w') as f_news:
                                f_news.write(str(obwuu_profit))
                            print(v)

                            telemsg = str("[Неудача]\n[BTC][ЗАК.КУРС: " + str(day_trend_list3[0]) + "]"
                                          + "\nУшли в минус: " + str(kj) + "\nСтавок в плюс сегодня: " + str(count_win)
                                          + "\nСтавок в минус: " + str(count_lose) +
                                          "\nОбщий доход за сегодня: " + str(obwuu_profit) + "\nVOL: " + str(vol_show))
                            bot.send_message(chanel_name, text=telemsg)
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\profit.txt', 'w') as f_news:
                            f_news.write(str(kj))
                        in_game.append("0")
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game.txt', 'w') as f_news:
                            f_news.write('0')
                        print("Снял ставку по сигналу трусливого человечка")
                if int(callback_worker[0]) == 1 and int(in_game[0]) == 0:
                    print("Сейчас я не в ставке, Фиксировать нечего...даун")
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\sell_now.txt', 'w') as f_news:
                    f_news.write("0")

                mainCODE.append(day_trend_list[0] + day_trend_list[1])
                if int(in_game[0]) == 0:
                    '''if int(day_trend_list[0]) == 2 and int(day_trend_list[1]) == 1:
                        print("П-1: -!СЛАБЫЙ Сигнал для ставки!- ЦЕНА:", day_trend_list3[0])'''



                    if int(day_trend_list[0]) == 1 and int(day_trend_list[1]) == 1:
                        print("П-1: -!СИЛЬНЫЙ Сигнал для ставки!- ЦЕНА:", day_trend_list3[0])


                    elif int(day_trend_list[0]) == 1 and int(day_trend_list[1]) == 2:
                        print("П-1: -!СРЕДНИЙ Сигнал для ставки!- ЦЕНА:", day_trend_list3[0])
                    else:
                        print('\nКод для продолжения не подходящий...\n')

                else:
                    if int(in_game[0]) == 1:
                        teleprint("Активные ставки: 1\n")
                    else:
                        teleprint("Активные ставки: 0\n")
                    pass

            while trend_day_count <= 3:
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt', 'r+',
                          encoding="utf-8") as f_news:
                    last_cot.clear()
                    last_cot.append(f_news.readlines()[lst_count])
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt', 'r+',
                          encoding="utf-8") as f_news:
                    first_cot.clear()
                    first_cot.append(f_news.readlines()[
                                         frs_count])  # <----- (-3 это 15 минут назад -6 это 30 мин назад и т.д если интервал 5 мин)

                lst_count -= 1
                frs_count -= 1
                # print(lst_count, frs_count)
                # -----l -> last-------f -> first----------------------
                l = last_cot
                l = [line.rstrip() for line in l]
                f = first_cot
                f = [line.rstrip() for line in f]

                last_list_split = re.split(',', str(l[0]))  # отжим необходимых чисел
                # time_cost = str(int(str(last_list_split[-2])[2:4]) - 1)
                last_list_split2 = re.split("'", str(last_list_split[-1]))
                first_list_split = re.split(',', str(f[0]))
                # print(last_list_split,first_list_split)
                first_list_split2 = re.split("'", str(first_list_split[-1]))

                now_cost = str(last_list_split2[0])[:5]  # ----------------------------------Цена 1 (первые 5 знаков)
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_now.txt', 'w') as f_news:
                    f_news.write(now_cost)
                # ---------------------
                start_cost = str(first_list_split2[0])[:5]  # ----------------------------------Цена 2 (первые 5 знаков)
                # print(now_cost, start_cost)
                # Сравнение цены. Чтобы узнать идет ли плюс. Это для снятия ставки в случае 01 21 00
                in_game_trend2 = str(int(now_cost) - int(start_cost))
                # Записать только первое значение

                '''limit_min_trend_up = 10
                limit_max_trend_up = 30         # ненужный на данный момент кусок кода.
                                                #Через две обновы удалить. а так же фаилы старее черм два дня
                limit_min_trend_dwn = -5
                limit_max_trend_dwn = -20'''

                if trend_day_count == 0:
                    # vol cheker begin
                    files = glob.glob('C:\\Users\\user\\Desktop\\Python\\My_bots\\BirjaBotS_faction\\txt\\*')
                    for f in files:
                        os.remove(f)
                    webbrowser.open(url)
                    time.sleep(1.5)
                    trend_day_count = 0
                    lst_count = -2  # --------------последнее начение курса--------------------
                    frs_count = -3  # ----------- значение на (6 * N)=30 мин назад, где N это выбранный диапазон
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt', 'r+',
                              encoding="utf-8") as f_news:
                        last_cot.clear()
                        last_cot.append(f_news.readlines()[lst_count])
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt', 'r+',
                              encoding="utf-8") as f_news:
                        first_cot.clear()
                        first_cot.append(f_news.readlines()[
                                             frs_count])  # <----- (-3 это 15 минут назад -6 это 30 мин назад и т.д если интервал 5 мин)

                    # print(lst_count, frs_count)
                    # -----l -> last-------f -> first----------------------
                    l = last_cot
                    l = [line.rstrip() for line in l]
                    f = first_cot
                    f = [line.rstrip() for line in f]

                    last_list_split = re.split(',', str(l[0]))  # отжим необходимых чисел
                    # time_cost = str(int(str(last_list_split[-2])[2:4]) - 1)
                    last_list_split2 = re.split("'", str(last_list_split[-1]))
                    first_list_split = re.split(',', str(f[0]))
                    # print(last_list_split,first_list_split)
                    first_list_split2 = re.split("'", str(first_list_split[-1]))

                    VOLnow_cost = str(last_list_split2[0])[
                               :5]  # ---------------------------Цена 1 (первые 5 знаков)
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_now.txt',
                              'w') as f_news:
                        f_news.write(now_cost)
                    # ---------------------
                    VOLstart_cost = str(first_list_split2[0])[
                                 :5]
                    VOL_PLUS_or_Minus = int(int(VOLnow_cost) - int(VOLstart_cost))

                    vol = DANTES_PEAK[-1]  # ----------------------------------Показатель VOL 3 минуты назад)
                    last_list_split3 = re.split(',', str(vol))  # отжим необходимых чисел
                    vol_dantes = 0
                    if VOL_PLUS_or_Minus > 0:
                        vol_dantes = int(last_list_split3[-1])
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\vol_3min_check.txt',
                                  'w') as f_news:
                            f_news.write(str(vol_dantes))
                    if VOL_PLUS_or_Minus < 0:
                        vol_dantes = int('-' + last_list_split3[-1])
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\vol_3min_check.txt',
                                  'w') as f_news:
                            f_news.write(str(vol_dantes))
                    DANTES_PEAK.clear()
                    DANTES_PEAK.append(vol_dantes)

                    vol_show.insert(0, vol_dantes)

                    # vol cheker finish

                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game_trend.txt',
                              'w') as f_news:
                        f_news.write(str(in_game_trend2))

                if int(now_cost) > int(start_cost):  # ----------сравниваем
                    trend_day_count += 1
                    j = int(now_cost) - int(start_cost)  # 1 - 5 = -4 \ 5 - 1 = 4

                    # day_trend_list2.append(str(j) + time_cost)
                    if trend_day_count > 1:
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

                elif int(now_cost) < int(start_cost):

                    if trend_day_count > 0:
                        day_trend_list2.append("(" + str(int(now_cost) - int(start_cost)) + ")")
                    else:
                        day_trend_list2.append(now_cost + "(" + str(int(now_cost) - int(start_cost)) + ")")
                    trend_day_count += 1
                    day_trend_list3.append(now_cost)
                    if int(int(now_cost) - int(start_cost)) <= int(EASY_0[0]):
                        day_trend_list.append("0")
                    else:
                        day_trend_list.append("2")
                    day_trend_list3.append(now_cost)

            saved_cost = []
            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_begin.txt', 'r+') as f_news:
                saved_cost.append(f_news.read())
            os.system('cls')
            global count_win, count_lose, obwuu_profit, tsuga_count, play_obj
            teleprint("-----------\nСейчас       -1min    -2min     -3min \n" + str(day_trend_list2))
            teleprint("Код: " + str(
                str(day_trend_list[0] + str(day_trend_list[1])) + str(str(day_trend_list[2] + str(day_trend_list[3])))))
            # , "(создать отдельную переменную для сохранения всех ставок)")
            # teleprint("Сигналы закрытия ставки: функция запоминает ставку и послед цена вычитает разницу и показывает или прибыль или убыль")
            trend_k = int(day_trend_list3[0]) - int(Byu_bet_len[0])

            # ЛОГИКА ____

            BET1()
            FIRSTCODE = ["12", "11"]
            l3 = mainCODE
            res = [x for x in FIRSTCODE + l3 if x not in FIRSTCODE or x not in l3]
            SLEEPCODE = ["00"]
            l5 = mainCODE
            res_sleep = [x for x in SLEEPCODE + l5 if x not in SLEEPCODE or x not in l5]
            # SLEEP 00 begin
            if len(res_sleep) == 0 and int(in_game[0]) == 0:
                #v = "Вхожу в режим ожидания скачка."
                #bot.send_message(chanel_name, text=v)
                while int(in_game_trend_sleep[0]) < 50:
                    try:
                        files = glob.glob('C:\\Users\\user\\Desktop\\Python\\My_bots\\BirjaBotS_faction\\txt\\*')
                        for f in files:
                            os.remove(f)
                        webbrowser.open(url)
                        time.sleep(3.8)

                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt', 'r+',
                                  encoding="utf-8") as f_news:
                            last_cot.clear()
                            last_cot.append(f_news.readlines()[-1])
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\BTCUSD.txt', 'r+',
                                  encoding="utf-8") as f_news:
                            first_cot.clear()
                            first_cot.append(f_news.readlines()[
                                                 -2])  # <----- (-3 это 15 минут назад -6 это 30 мин назад и т.д если интервал 5 мин)

                        # -----l -> last-------f -> first----------------------
                        l = last_cot
                        l = [line.rstrip() for line in l]
                        f = first_cot
                        f = [line.rstrip() for line in f]

                        last_list_split = re.split(',', str(l[0]))  # отжим необходимых чисел
                        # time_cost = str(int(str(last_list_split[-2])[2:4]) - 1)
                        last_list_split2 = re.split("'", str(last_list_split[-1]))
                        first_list_split = re.split(',', str(f[0]))
                        # print(last_list_split,first_list_split)
                        first_list_split2 = re.split("'", str(first_list_split[-1]))

                        now_cost = str(last_list_split2[0])[
                                   :5]  # ----------------------------------Цена 1 (первые 5 знаков)
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\trend_now.txt',
                                  'w') as f_news:
                            f_news.write(now_cost)
                        # ---------------------
                        start_cost = str(first_list_split2[0])[
                                     :5]  # ----------------------------------Цена 2 (первые 5 знаков)
                        # print(now_cost, start_cost)
                        # Сравнение цены. Чтобы узнать идет ли плюс. Это для снятия ставки в случае 01 21 00
                        in_game_trend_sleep.clear()
                        in_game_trend_sleep.append(str(int(now_cost) - int(start_cost)))
                        os.system('cls')
                        teleprint("Активность за последние 10 секунд:", in_game_trend_sleep[0])

                        teleprint("Слабая динамика... Тихий режим включен. Лимит на пробуждения +50")
                        time.sleep(10)
                    except FileNotFoundError:
                        print("Фаил не успел прогрузиться. пробую еще раз")
                        time.sleep(2)
                        continue

                in_game_trend_sleep.insert(0,'0')

                #tx = "Появилась активность. Выхожу из цикла ожидания."
                #bot.send_message(chanel_name, text=tx)

            # SLEEP 00 over

            # (неактуально, использован VOL для проверки на пик горы) проерка на снятие ставки и продолжение/ КОгда программа запущенна,
            # то в in_game_trend всего лишь один индекс будет, может приести к ошибке

            '''SELLCODE = ["67", "77", "66", "76"]
            l4 = in_game_trend
            res3 = [x for x in SELLCODE + l3 if x not in SELLCODE or x not in l3]
            print(res3, len(res3))'''

            def TSUGA():
                global count_win, obwuu_profit, tsuga_count, play_obj

                if int(trend_k) >= int(TSUGA_LIMIT[0]) and int(in_game[0]) == 1:
                    Last_sell.append(day_trend_list3[0])
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Sell.txt', 'w') as f_news:
                        f_news.write(day_trend_list3[0])
                    kj = trend_k
                    if int(Audio_on[0]) == 1:
                        play_obj = SUGA.play()
                    s = str("[ЦУГА на" + TSUGA_LIMIT[0] + "]" + "Фиксирую прибыль: +" + str(kj))
                    count_win += 1
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_win.txt',
                              'w') as f_news:
                        f_news.write(str(count_win))
                    obwuu_profit += int(kj)
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt', 'w') as f_news:
                        f_news.write(str(obwuu_profit))
                    print(s)
                    # "[ЦУГА=60][BTC][ЗАК.КУРС: " + str(day_trend_list3[0]) + "]"
                    telemsg = str("[ЦУГА=" + TSUGA_LIMIT[0] + "]\n[BTC][ЗАК.КУРС: " + str(day_trend_list3[0]) + "]"
                                  + "\nЗабрал +" + str(kj) + "\nСтавок в плюс сегодня: " + str(count_win)
                                  + "\nСтавок в минус: " + str(count_lose) +
                                  "\nОбщий доход за сегодня: " + str(obwuu_profit) + "\nVOL: " + str(vol_show))
                    bot.send_message(chanel_name, text=telemsg)
                    with mss() as sct:
                        sct.shot()
                    photo = open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\monitor-1.png', 'rb')
                    bot.send_photo(chanel_name, photo)

                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\profit.txt', 'w') as f_news:
                        f_news.write(str(kj))
                    in_game.append("0")
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game.txt', 'w') as f_news:
                        f_news.write('0')
                    print('Фуф отдохну пока от греха подальше пару минут')
                    time.sleep(120)
                elif int(in_game[0]) == 1:
                    print("ЦУГИ еще нет..")
                    tsuga_count += 1
                    print('                 ПОПЫТКИ ВЗЯТЬ ЦУГУ:', tsuga_count)

            TSUGA()
            if len(res) == 3 or tsuga_count == 3:
                if int(in_game[0]) == 1:
                    tsuga_count = 0 / int(tsuga_count)
                    print("Снимаю ставку")
                    Last_sell.append(day_trend_list3[0])
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Sell.txt', 'w') as f_news:
                        f_news.write(day_trend_list3[0])
                    kj = trend_k
                    if int(kj) > 0:
                        s = str("Фиксирую прибыль: +" + str(kj))
                        obwuu_profit += int(kj)
                        if int(Audio_on[0]) == 1:
                            play_obj = FIXMONEYPLUS.play()
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt',
                                  'w') as f_news:
                            f_news.write(str(obwuu_profit))
                        count_win += 1
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_win.txt',
                                  'w') as f_news:
                            f_news.write(str(count_win))
                        print(s)
                        # "[ФИКС. ПРОФИТ][BTC][ЗАК.КУРС: " + str(day_trend_list3[0]) + "]"
                        telemsg = str("[ФИКС. ПРОФИТ]\n[BTC][ЗАК.КУРС: " + str(day_trend_list3[0]) + "]"
                                      + "\nИтоговая прибыль сделки: +" + str(kj) + "\nСтавок в плюс сегодня: " + str(
                            count_win)
                                      + "\nСтавок в минус :" + str(count_lose) +
                                      "\nОбщий доход за сегодня :" + str(obwuu_profit) + "\nVOL: " + str(vol_show))
                        bot.send_message(chanel_name, text=telemsg)
                        with mss() as sct:
                            sct.shot()
                        photo = open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\monitor-1.png', 'rb')
                        bot.send_photo(chanel_name, photo)
                    else:
                        v = str("Заработать не получилось...Мы проебали: " + str(kj))
                        count_lose += 1
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_lose.txt',
                                  'w') as f_news:
                            f_news.write(str(count_lose))
                        obwuu_profit += int(kj)
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt',
                                  'w') as f_news:
                            f_news.write(str(obwuu_profit))
                        print(v)

                        telemsg = str("[Неудача]\n[BTC][ЗАК.КУРС: " + str(day_trend_list3[0]) + "]"
                                      + "\nУшли в минус: " + str(kj) + "\nСтавок в плюс сегодня: " + str(count_win)
                                      + "\nСтавок в минус: " + str(count_lose) +
                                      "\nОбщий доход за сегодня: " + str(obwuu_profit) + "\nVOL: " + str(vol_show))
                        if int(Audio_on[0]) == 1:
                            play_obj = LOSTMONEY.play()
                        bot.send_message(chanel_name, text=telemsg)
                        with mss() as sct:
                            sct.shot()
                        photo = open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\monitor-1.png', 'rb')
                        bot.send_photo(chanel_name, photo)

                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\profit.txt', 'w') as f_news:
                        f_news.write(str(kj))
                    in_game.append("0")
                    with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game.txt', 'w') as f_news:
                        f_news.write('0')

            elif len(res) == 1 and int(in_game[0]) == 0:

                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Xsec.txt',
                          'w') as f_news:
                    print("Поехали, че то намечается, начинаю мониторить каждые 5 сек")
                    if int(Audio_on[0]) == 1:
                        play_obj = Signal.play()
                    f_news.write("5")

                mainCODE2 = []
                mainCODE2.clear()

                min_5_dowload()

                show_code = day_trend_list_5min[0] + day_trend_list_5min[1] + day_trend_list_5min[2] + \
                            day_trend_list_5min[3]
                mainCODE2.append(str(day_trend_list_5min[0]) + str(day_trend_list_5min[1]))
                SECONDCODE = ["12", "11"]
                l4 = mainCODE2
                res2 = [x for x in SECONDCODE + l4 if x not in SECONDCODE or x not in l4]
                if len(res2) >= 3:

                    print("\nПока Тренд отрицательный...")
                    if int(in_game[0]) == 1:
                        Last_sell.append(day_trend_list3[0])
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Sell.txt',
                                  'w') as f_news:
                            f_news.write(day_trend_list3[0])
                        kj = trend_k
                        if int(kj) > 0:
                            s1 = "\n\nСНИМАЮ СДЕЛКУ. ЦЕНА: " + str(day_trend_list3[0])
                            s = str("Фиксирую прибыль: +" + str(kj) + "\n\n")
                            obwuu_profit += int(kj)
                            if int(Audio_on[0]) == 1:
                                play_obj = FIXMONEYPLUS.play()
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt',
                                      'w') as f_news:
                                f_news.write(str(obwuu_profit))
                            count_win += 1
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_win.txt',
                                      'w') as f_news:
                                f_news.write(str(count_win))
                            print(s + s1)
                            bot.send_message(chanel_name, text=s)
                        else:
                            s1 = "СНИМАЮ СДЕЛКУ. ЦЕНА: " + str(day_trend_list3[0])
                            v = str("\nЗаработать не получилось...Мы проебали: " + str(kj))
                            if int(Audio_on[0]) == 1:
                                play_obj = LOSTMONEY.play()
                            count_lose += 1
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\count_lose.txt',
                                      'w') as f_news:
                                f_news.write(str(count_lose))
                            obwuu_profit += int(kj)
                            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\day_profit.txt',
                                      'w') as f_news:
                                f_news.write(str(obwuu_profit))
                            print(v)
                            bot.send_message(chanel_name, text=s1 + v)
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\profit.txt',
                                  'w') as f_news:
                            f_news.write(str(kj))
                        in_game.append("0")
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game.txt',
                                  'w') as f_news:
                            f_news.write('0')
                    else:
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Xsec.txt',
                                  'w') as f_news:
                            if int(Audio_on[0]) == 1:
                                play_obj = RANO.play()
                            print("Поэтому подождем пока..секунд 5..может что измениться")
                            f_news.write("5")

                elif len(res2) <= 2:

                    if int(in_game[0]) == 0 and int(DANTES_PEAK[-1]) >= 1 and int(
                            DANTES_PEAK[0]) < 4:  # сделать ставку!!!
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\Bet.txt',
                                  'w') as f_news:
                            f_news.write(day_trend_list3[0])
                        v = "[СТАВЛЮ В РОСТ]\n[BTC][ТЕК.КУРС: " + str(day_trend_list3[0]) + "] + '\nVOL: " + str(
                            vol_show)
                        print(str("\nУСПЕШНО! --- СТАВКА ОДОБРЕНА ---- ЦЕНА: " + str(day_trend_list3[0]) + '\n'))
                        bot.send_message(chanel_name, text=v)
                        if int(Audio_on[0]) == 1:
                            play_obj = BET.play()
                        with mss() as sct:
                            sct.shot()
                        photo = open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\monitor-1.png', 'rb')
                        bot.send_photo(chanel_name, photo)
                        in_game.append("1")
                        with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game.txt',
                                  'w') as f_news:
                            f_news.write('1')
                        Byu_bet_len.append(day_trend_list3[0])

                    if int(in_game[0]) == 1:
                        print("\nЕсть активная сделка\n")
                    if int(DANTES_PEAK[0]) > 4:
                        print("\nМЫ НА ПИКЕ. ПОВТОРНО СТАВИТЬ НЕ БУДУ\n ")
                    elif int(DANTES_PEAK[0]) == 0:
                        print("\nМАЛАЯ ВОЛОНТИЛЬНОСТЬ НА РЫНКЕ. СТАВИТЬ НЕ БУДУ\n")

                teleprint("Сейчас     3м. назад     6м. назад    9.м назад \n" + str(day_trend_list4))
                teleprint("КОД 5 минут: " + str(show_code))

            else:
                pass

            if trend_k > 0:
                j = count_win + count_lose
                teleprint("Всего сделок: ", j, "\nВыиграно сделок: " + str(count_win))
                print("Total Profit:", str(obwuu_profit), "\n\nCostNow:", day_trend_list3[0], "( +", trend_k, ")")

            else:
                j = count_win + count_lose
                teleprint("-----------\nВсего сделок: ", j, "\nВыиграно сделок: " + str(count_win))
                print("Total Profit:", str(obwuu_profit), "\nCostNow:", day_trend_list3[0], "(", trend_k,
                      ")\n-----------")

            print("Активность рынка:\n   " + str(in_game_trend) +'      VOL:'  , vol_show)
            # удаление файлов в папке в цикле.
            if len(vol_show) >=1:
                vol_show.pop(-1)
            files = glob.glob('C:\\Users\\user\\Desktop\\Python\\My_bots\\BirjaBotS_faction\\txt\\*')
            for f in files:
                os.remove(f)

            # Чтобы определить куда идет тренд сечас нужно смотреть на первые 4е индекса. Если все 4е положительные, то 4е часа идет положительный тренд
            # (при условии, что диапазон 5 мин) Каждое начение индекса - это сравнение за 30 минут
            # Строить сратегию из последних 4ех чисел (0, 1, 1, 0) - проверка на положительные числа if x > 0 = .append "1"
            # Сравнить значения временных диапазонов для выбора оптимальной временного отрезка для ставки
            # 5 мин = (1, 1, 1, 0) - значит тренд вверх идет \ 15 мин (1.0.0.0) \ 60 минут (0.0.0.0) - индикатор начала тренда
            # 5 мин = (0, 0, 1, 1) - значит тренд вниз идет \ 15 мин (0.1.1.1) \ 60 минут (0.1.1.0) - индикатор падения тренда
            # на этом тех анализ заканчивается
            # дальше идет анализ новостей в поддержку ставки. Если последняя новость плохая, то это "0" в поддержку
            # В общем еще одна проверка и лист (0,1,1) -> подтверждающая ставка \ (0, 1, 0) -> всегда нет
            #
            #
            # input()


        def start_bet():
            # делает ставку на сайте
            pass


        def start_cell():
            # продает
            pass


        vol_show = []
        while True:
            # Считывание настроек аудио
            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\audio\audio.txt', 'r+') as f_news:
                Audio_on.clear()
                Audio_on.append(f_news.read())

            TSUGA_LIMIT = []
            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\TSUGA_LIMIT.txt', 'r+') as f_news:
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
            with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\stop_comand.txt', 'r+') as f_news:
                stop_comand.append(f_news.read())
            if int(stop_comand[0]) == 0:
                webbrowser.open(url3)
                time.sleep(1.8)
                # Вставляем каждый раз на первое значение в листе последние данные по приросту
                DANTES_PEAK = []
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\txt\DANTES_PEAK.txt',
                          'r+') as f_news:
                    DANTES_PEAK.append(f_news.readlines()[-3])
                with open(r'C:\Users\user\Desktop\Python\My_bots\BirjaBotS_faction\in_game_trend.txt', 'r+') as f_news:
                    in_game_trend.insert(0, str(f_news.read()))
                    if len(in_game_trend) >= 3:
                        in_game_trend.pop(-1)
                main_function()
            else:
                os.system('cls')
                print('\r Торговая сессия приостановлена...Жду команду для продолжения...', end='')
                time.sleep(5)

    except requests.ConnectionError:
        print("Нет ебучего интернета / Reloading,,")
        bot.send_message(chanel_name, text="Нет ебучего интернета / Reloading,,,")
        time.sleep(1)
        pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
        start_progtamm()
        time.sleep(10)

        continue
    except TimeoutError:
        print("Connect Error / Reloading,,,")
        bot.send_message(chanel_name, text="Connect Error / Reloading,,,")
        time.sleep(1)
        pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
        start_progtamm()
        time.sleep(10)
        continue
    except FileNotFoundError:
        print("Нет файла в папках")
        bot.send_message(chanel_name, text="Connect Error / Reloading,,,")
        time.sleep(1)
        pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
        start_progtamm()
        time.sleep(10)
        continue

    except Exception:
        bot.send_message(chanel_name, text="Critical Error / Reloading,,,")
        print("Critical Error / Reloading,,,")
        time.sleep(1)
        pyautogui.click(x=356, y=521, clicks=2, interval=0.8)
        start_progtamm()
        time.sleep(10)
        continue
