from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # scroll to element
import platform # определение платформы
import traceback
from time import sleep
import time
from datetime import datetime
import os
import random
# from urllib.request import urlopen
import pickle # печеньки
import csv

def driver_start(device=None, proxy=None, useragent=None):
    
    if device == None:
        device = 'iPhone X'
    
    d = { # user agents
        'iPhone X' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
        'Pixel 2' : 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Galaxy S5' : 'ozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0',
        }

    if ((platform.platform())[:5]) == "Linux":
        dr = "/Linux/chromedriver"
    elif ((platform.platform())[:7]) == "Windows":
        dr = "\\Windows\\chromedriver.exe"
    elif ((platform.platform())[:5]) == "macOS":
        dr = "/MacOS/chromedriver"
    

    mobile_emulation = { "deviceName": device} # type your device from list
    opts = Options()
    opts.add_experimental_option("mobileEmulation", mobile_emulation)

    opts.add_argument(d[device]) # user agent
    opts.add_argument("accept=*/*")

    driver = webdriver.Chrome(chrome_options=opts, executable_path=r"driver" + dr)
    driver.set_window_size(1000, 1078)
    driver.set_window_position(0, 0)

    return driver

def sleepr(min=2, max=6):
    if min <= 0:
        min = 1
    sleep(random.uniform(min,max))

def authorization(driver):
        
    my_login = read_file('login.txt')
    driver.get('https://www.instagram.com/accounts/login/')
    sleepr()
    # try:
    #     pass
        # #Забираем куки из файла
        # cookies = pickle.load(open("cookies.pkl", "rb"))
        # for cookie in cookies:
        #     if 'expiry' in cookie:
        #         del cookie['expiry']
        #     driver.driver.add_cookie(cookie)
        # print("Cookies have been read")

    # except: # куки не найдены или возникла иная ошибка
    print("No cookies found")
    el = driver.element_by_name('username')
    el.send_keys(my_login[0])
    el = driver.element_by_name('password')
    el.send_keys(my_login[1])
    sleepr()

    el = driver.element_by_xpath('//button[@type="submit"]')
    
    # ! Предупреждение от 06.06.21: Инстаграм теперь предлагает устновить их приложение, нужно учитывать это окно
    # ! Внести правки!
    
    if el != None: # ? иногда срабатывает автоматический вход без нажатия кнопки отправки формы?
        el.click()

        print("Login to your account")
        sleepr(min=6, max=10)
        #Код из СМС
        # В случае подтверждения через СМС
        if driver.driver.current_url != "https://www.instagram.com/":
            pass
            # print('Enter your code from SMS')
        while (driver.driver.current_url != "https://www.instagram.com/") and (
            driver.driver.current_url != 'https://www.instagram.com/accounts/onetap/?next=%2F'):
            sleep(1)

        # # Создание Cookies
        # pickle.dump(driver.driver.get_cookies() , open("cookies.pkl","wb"))
        # print("Cookies has been created")

        # проверка, был ли вход
        if driver.element_by_xpath("//section/nav/div[2]/div/div") != None:
            print("Вход успешно выполнен")
        else:
            pass
            # print("Ошибка входа, проверьте правильность логина и пароля") 

    else:
        print("Login to your account")

def scroll_block(driver, pause_time, max_users, block=False):
    iteration = 0
    while (iteration*12+12) < max_users:
        print(f'Iteration: {iteration+1}, users: {(iteration+1)*12+12}')
        el = '//span[@aria-label="Load more comments"]'
        el = driver.element_by_xpath(el,2)
        if el == None:
            el = '//span[@aria-label="Загрузить больше комментариев"]' # ? is it?
            el = driver.element_by_xpath(el,1)
        if el == None:
            print('Not scrolling element')
            return None # then exit
        el = el.find_element_by_xpath('..')
        driver.driver.execute_script("arguments[0].scrollIntoView();", el)
        driver.driver.execute_script("arguments[0].click();", el)
        sleepr(pause_time-2, pause_time+2) 
        iteration += 1

        if iteration % 82 == 0:
            print('Pause')
            timer(60*random.randint(7,13))
            continue
        
        if iteration % 41 == 0:
            print('Pause...')
            timer(60*random.randint(1,2))
            continue
            
        if iteration % 10 == 0:
            print('Pause...')
            sleepr(7,10)
            continue

def scroll_page(driver, pause_time, max_users):
    last_height = driver.driver.execute_script("return document.body.scrollHeight") # Get scroll height
    i = 0 # iteration count
    number_stop = 0 # num of not load page
    num_users = 24 # start num
    
    while number_stop < 5:
        # Scroll down to bottom
        driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i += 1
        num_users += 12
        # Wait to load page
        sleepr(pause_time-2,pause_time+2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.driver.execute_script("return document.body.scrollHeight")
        print(f'Iteration: {i}, users: ~{num_users}, height:', new_height)

        if new_height == last_height:
            number_stop += 1
            num_users -= 12
        elif number_stop != 0:
            number_stop = 0

        last_height = new_height

        if num_users >= max_users:
            print('The maximum number of users has been reached')
            break

        if i % 82 == 0:
            print('Pause')
            timer(60*random.randint(7,13))
            continue
        
        if i % 41 == 0:
            print('Pause...')
            timer(60*random.randint(1,2))
            continue
            
        if i % 10 == 0:
            print('Pause...')
            sleepr(7,10)
            continue

# def hour_waiting(start_time, current_num, max_num_in_hour):
#     if ((time.time() - start_time) <= 60*60) and (current_num >= max_num_in_hour):
#         print("\nLimit of users per hour reached:", max_num_in_hour)
#         now = datetime.now()
#         if (now.minute / 10) <= 0:
#             str_ = "Time: " + str(now.hour) + ":0" + str(now.minute)
#         else:
#             str_ = "Time: " + str(now.hour) + ":" + str(now.minute)
#         print(str_)
#         timer(1) # ! test mod
#         # timer(60*60 - (time.time() - start_time))
#         current_num = 0
#         start_time = time.time()
#         return None
#     # zero hour
#     if ((time.time() - start_time) >= 60*60):
#         start_time = time.time()
#         return start_time # return new start_time value
#     return None

def timer(seconds):
    if (seconds/60) <= 1:
        print("Wait", int(seconds), "sec.")
        sleep(seconds + random.uniform(0,1))
    else:
        minutes = seconds/60
        seconds = seconds%60
        print("Wait", int(minutes), "min.")
        count = 0
        while int(minutes) > count: # add -1
            count += 1
            print(count, "out of", int(minutes), "min.")
            sleep(60)
        sleep(seconds + random.uniform(0,1))
        print("Works on")

# colors for console
class Terminal():
    __HEADER = '\033[95m'
    __OKBLUE = '\033[94m'
    __OKCYAN = '\033[96m'
    __OKGREEN = '\033[92m'
    __WARNING = '\033[93m'
    __FAIL = '\033[91m'
    __BOLD = '\033[1m'
    __UNDERLINE = '\033[4m'
    __ENDC = '\033[0m'

    def warning(self, string):
        print(f'{self.__FAIL}' + string + f'{self.__ENDC}')
    def ok(self, string):
        print(f'{self.__OKGREEN}' + string + f'{self.__ENDC}')

    def print_except(self):
        print(f'{self.__WARNING}"\nERROR!"' + traceback.format_exc() + f'{self.__ENDC}')


def replace_path(file_path):
    if ((platform.platform())[:7]) == "Windows":
        file_path = file_path.replace('/', '\\')

    return file_path

def read_file(file_path):
    file_path = replace_path(file_path)
    with open(file_path, 'r', encoding="utf-8", errors='ignore') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def write_file(file_path, lines, mod='a'):
    file_path = replace_path(file_path)
    with open(file_path, mod, encoding="utf-8", errors='ignore') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
