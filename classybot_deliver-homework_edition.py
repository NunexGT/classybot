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
import getpass




keyboard = Controller()
chat_responses = ['Bom Dia,Boa Tarde']
deliver_hw = pd.read_csv('deliver_hw.csv')







def findTime():
    today = date.today()
    now = datetime.now().time()
    d1 = today.strftime("%d/%m/%Y")
    return (d1,now.hour,now.minute)








def find_comment(link, current_user):
   

    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\"+current_user+"\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--profile-directory=Profile 1")
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=options)
    driver.get(link)
    time.sleep(10)
    homework=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[1]/div[2]/aside/div[1]/div[5]/div[3]/div')
    homework.click
    time.sleep(2)
    homework.send_keys(Keys.ENTER)
    time.sleep(2)
    homework_give=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[11]/div/div[2]/div[3]/div[2]')
    homework_give.click
    homework_give.send_keys(Keys.ENTER)



def kill_chrome():
   os.system('cmd /c "TASKKILL /f  /IM  CHROME.EXE"')

    


def lookup_schedule():
    current_time = findTime()
    row_count = len(deliver_hw.index)
    print("CURRENT TIME:",current_time)
    for i in range(row_count):
        current_row = deliver_hw.iloc[i]
        subject = current_row['Work_Name']
        link = current_row['LINK']
        hour = current_row['Hour']
        minute = current_row['Minute']
        date = current_row['DATE']
        current_user=getpass.getuser()
        look_up = (date,hour,minute)
        print("LOOKUP RESULT:",look_up)
        print("Web Link for",subject,":" ,link)
        if current_time == look_up:
            print("EXECUTING")
            kill_chrome()
            time.sleep(4)
            find_comment(link, current_user)
    print('\n')

    


def background_process():
    lookup_schedule()
    time.sleep(40)

while True: background_process()






 



