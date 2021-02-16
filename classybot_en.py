from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pynput.keyboard import Key, Controller
from datetime import datetime
from datetime import date
import calendar 
import pandas as pd
import random
import webbrowser
import pyautogui
from selenium.webdriver.common.by import By
import schedule
from selenium.webdriver.common.keys import Keys
import os




keyboard = Controller()
chat_responses = ['Bom Dia,Boa Tarde']
schedule = pd.read_csv('schedule.csv')





def findDate():
    born = date.today().weekday()
    return (calendar.day_name[born])


def findTime():
    now = datetime.now().time()
    return (findDate(),now.hour,now.minute)








def find_comment(link, hour):
   

    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\Nuno Miguel\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--profile-directory=Profile 1")
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=options)
    driver.get(link)
    time.sleep(10)
    coment=driver.find_element_by_xpath('//*[@id=":1.t"]')
    coment.click
    time.sleep(1)
    if hour <= 12:
        coment.send_keys("Good Morning")
    elif hour > 12:
        coment.send_keys("Good Afternoon")
    time.sleep(2)
    coment.send_keys(Keys.TAB, Keys.ENTER)


def kill_chrome():
   os.system('cmd /c "TASKKILL /f  /IM  CHROME.EXE"')

    


def lookup_schedule():
    current_time = findTime()
    row_count = len(schedule.index)
    print("CURRENT TIME:",current_time)
    for i in range(row_count):
        current_row = schedule.iloc[i]
        subject = current_row['SUBJECT']
        link = current_row['LINK']
        hour = current_row['Hour']
        minute = current_row['Minute']
        day = current_row['DAY OF WEEK']
        look_up = (day,hour,minute)
        print("LOOKUP RESULT:",look_up)
        print("Web Link for",subject,":" ,link)
        if current_time == look_up:
            print("EXECUTING")
            kill_chrome()
            time.sleep(4)
            find_comment(link, hour)
    print('\n')

    


def background_process():
    lookup_schedule()
    time.sleep(40)

while True: background_process()






 



