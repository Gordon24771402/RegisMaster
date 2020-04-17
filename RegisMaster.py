import threading
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from playsound import playsound
import time
import random


def os_mitmproxy():
    os.chdir('C:/Users/Hao Kang')
    os.system('mitmdump --mode upstream:127.0.0.1:7890 -s modify_response.py')


def refresh_completion(driver):
    driver.refresh()
    time.sleep(random.randint(3, 10))
    driver.refresh()


def try_again(driver):
    html = str(driver.execute_script("return document.documentElement.outerHTML"))
    if "We are unable to process your request due to a system error." and "Please try again later." in html:
        refresh_completion(driver)
        again = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div/div[1]/div[1]/div/div/ul/li/a")))
        again.click()
        time.sleep(random.randint(5, 15))

        try:
            register_another = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "actionRegisterAnother")))
            register_another.click()
            time.sleep(random.randint(5, 15))
        except:
            try:
                refresh_completion(driver)
                register_another = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "actionRegisterAnother")))
                register_another.click()
                time.sleep(random.randint(5, 15))
            except:
                try_again(driver)

        try:
            authenticate_page = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "authenticatePage")))
            authenticate_page.click()
            time.sleep(random.randint(5, 15))
        except:
            try:
                refresh_completion(driver)
                authenticate_page = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "authenticatePage")))
                authenticate_page.click()
                time.sleep(random.randint(5, 15))
            except:
                try_again(driver)

        try:
            register_continue001 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "continue")))
            register_continue001.click()
            time.sleep(random.randint(5, 15))
        except:
            try:
                refresh_completion(driver)
                register_continue001 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "continue")))
                register_continue001.click()
                time.sleep(random.randint(5, 15))
            except:
                try_again(driver)

        try:
            update_later = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "updateLater")))
            update_later.click()
            time.sleep(random.randint(5, 15))
        except:
            try:
                refresh_completion(driver)
                update_later = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "updateLater")))
                update_later.click()
                time.sleep(random.randint(5, 15))
            except:
                try_again(driver)

        try:
            agree_terms = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "agreeTerms")))
            agree_terms.click()
            time.sleep(random.randint(5, 15))
        except:
            try:
                refresh_completion(driver)
                agree_terms = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "agreeTerms")))
                agree_terms.click()
                time.sleep(random.randint(5, 15))
            except:
                try_again(driver)

        register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "continue")))
        register_continue002.click()
        time.sleep(random.randint(5, 15))

        while True:
            time.sleep(random.randint(5, 15))
            html = str(driver.execute_script("return document.documentElement.outerHTML"))
            if "There are no available registration dates for the current test year. Please check back later to register for future tests." in html:
                with open('LOG.txt', 'a') as LOG:
                    LOG.write('\n' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "Future SAT NOT Available!")
            else:
                n = 1
                while n == 1:
                    playsound("Alarm01.wav")

            time.sleep(random.randint(600, 850))
            driver.back()
            time.sleep(random.randint(5, 15))
            try:
                register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "continue")))
                register_continue002.click()
                time.sleep(random.randint(5, 15))
            except:
                try:
                    refresh_completion(driver)
                    register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                        By.ID, "continue")))
                    register_continue002.click()
                    time.sleep(random.randint(5, 15))
                except:
                    try_again(driver)


def main_program():
    os.chdir('C:/Users/Hao Kang/PycharmProjects/RegisMaster')
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    options.add_argument('--proxy-server=127.0.0.1:8080')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://collegereadiness.collegeboard.org/')
        time.sleep(random.randint(5, 15))
    except:
        refresh_completion(driver)
        driver.get('https://collegereadiness.collegeboard.org/')
        time.sleep(random.randint(5, 15))

    sign_in = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/a[1]")))
    sign_in.click()

    user_name = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.XPATH,
        "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[1]/input")))
    user_name.send_keys("USERNAME")

    password = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.XPATH,
        "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[2]/input")))
    password.send_keys("PASSWORD")

    submit = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/button")))
    submit.click()
    time.sleep(random.randint(5, 15))

    try:
        driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
        time.sleep(random.randint(5, 15))
    except:
        refresh_completion(driver)
        driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
        time.sleep(random.randint(5, 15))

    try:
        register_another = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "actionRegisterAnother")))
        register_another.click()
        time.sleep(random.randint(5, 15))
    except:
        try:
            refresh_completion(driver)
            register_another = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "actionRegisterAnother")))
            register_another.click()
            time.sleep(random.randint(5, 15))
        except:
            try_again(driver)

    try:
        authenticate_page = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "authenticatePage")))
        authenticate_page.click()
        time.sleep(random.randint(5, 15))
    except:
        try:
            refresh_completion(driver)
            authenticate_page = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "authenticatePage")))
            authenticate_page.click()
            time.sleep(random.randint(5, 15))
        except:
            try_again(driver)

    try:
        register_continue001 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "continue")))
        register_continue001.click()
        time.sleep(random.randint(5, 15))
    except:
        try:
            refresh_completion(driver)
            register_continue001 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "continue")))
            register_continue001.click()
            time.sleep(random.randint(5, 15))
        except:
            try_again(driver)

    try:
        update_later = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "updateLater")))
        update_later.click()
        time.sleep(random.randint(5, 15))
    except:
        try:
            refresh_completion(driver)
            update_later = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "updateLater")))
            update_later.click()
            time.sleep(random.randint(5, 15))
        except:
            try_again(driver)

    try:
        agree_terms = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "agreeTerms")))
        agree_terms.click()
        time.sleep(random.randint(5, 15))
    except:
        try:
            refresh_completion(driver)
            agree_terms = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "agreeTerms")))
            agree_terms.click()
            time.sleep(random.randint(5, 15))
        except:
            try_again(driver)

    register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.ID, "continue")))
    register_continue002.click()
    time.sleep(random.randint(5, 15))

    while True:
        time.sleep(random.randint(5, 15))
        html = str(driver.execute_script("return document.documentElement.outerHTML"))
        if "We’re sorry, you must accept the SAT Terms and Conditions before you can register for the SAT. Please accept the Terms and Conditions and click ‘Continue’ to proceed with your registration." in html:
            try:
                agree_terms = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "agreeTerms")))
                agree_terms.click()
                time.sleep(random.randint(5, 15))
            except:
                try:
                    refresh_completion(driver)
                    agree_terms = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                        By.ID, "agreeTerms")))
                    agree_terms.click()
                    time.sleep(random.randint(5, 15))
                except:
                    try_again(driver)
            try:
                register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "continue")))
                register_continue002.click()
                time.sleep(random.randint(5, 15))
            except:
                try:
                    refresh_completion(driver)
                    register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                        By.ID, "continue")))
                    register_continue002.click()
                    time.sleep(random.randint(5, 15))
                except:
                    try_again(driver)

        elif "There are no available registration dates for the current test year. Please check back later to register for future tests." in html:
            with open('LOG.txt', 'a') as LOG:
                LOG.write('\n' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "Future SAT NOT Available!")
        else:
            n = 1
            while n == 1:
                playsound("Alarm01.wav")

        time.sleep(random.randint(300, 350))
        driver.back()
        time.sleep(random.randint(5, 15))
        try:
            register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "continue")))
            register_continue002.click()
            time.sleep(random.randint(5, 15))
        except:
            try:
                refresh_completion(driver)
                register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                    By.ID, "continue")))
                register_continue002.click()
                time.sleep(random.randint(5, 15))
            except:
                try_again(driver)


thread_001 = threading.Thread(target=os_mitmproxy)
time.sleep(random.randint(3, 5))
thread_002 = threading.Thread(target=main_program)
thread_001.start()
thread_002.start()
