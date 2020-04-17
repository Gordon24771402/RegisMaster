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

def os_mitmproxy():
    os.chdir('C:/Users/Hao Kang')
    os.system('mitmweb --mode upstream:127.0.0.1:7890 -s modify_response.py')


def refresh_completion(driver):
    driver.refresh()
    time.sleep(3)
    driver.refresh()


def main_program():
    os.chdir('C:/Users/Hao Kang/PycharmProjects/RegisMaster')
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    options.add_argument('--proxy-server=127.0.0.1:8080')
    driver = webdriver.Chrome(options=options)
    driver.get('https://collegereadiness.collegeboard.org/')

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
    time.sleep(5)

    driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
    time.sleep(5)

    try:
        register_another = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "actionRegisterAnother")))
        register_another.click()
        time.sleep(5)
    except:
        refresh_completion(driver)
        register_another = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "actionRegisterAnother")))
        register_another.click()
        time.sleep(5)

    try:
        authenticate_page = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "authenticatePage")))
        authenticate_page.click()
        time.sleep(5)
    except:
        refresh_completion(driver)
        authenticate_page = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "authenticatePage")))
        authenticate_page.click()
        time.sleep(5)

    try:
        register_continue001 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "continue")))
        register_continue001.click()
        time.sleep(5)
    except:
        refresh_completion(driver)
        register_continue001 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "continue")))
        register_continue001.click()
        time.sleep(5)

    try:
        update_later = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "updateLater")))
        update_later.click()
        time.sleep(5)
    except:
        refresh_completion(driver)
        update_later = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "updateLater")))
        update_later.click()
        time.sleep(5)

    try:
        agree_terms = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "agreeTerms")))
        agree_terms.click()
        time.sleep(5)
    except:
        refresh_completion(driver)
        agree_terms = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
            By.ID, "agreeTerms")))
        agree_terms.click()
        time.sleep(5)

    register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
        By.ID, "continue")))
    register_continue002.click()
    time.sleep(5)

    i = 0
    while i == 0:
        time.sleep(5)
        html = str(driver.execute_script("return document.documentElement.outerHTML"))
        if "There are no available registration dates for the current test year. Please check back later to register for future tests." in html:
            with open('LOG.txt', 'a') as LOG:
                LOG.write('\n' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "Future SAT NOT Available!")
        else:
            n = 1
            while n == 1:
                playsound("Alarm01.wav")

        time.sleep(600)
        driver.back()
        try:
            register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "continue")))
            register_continue002.click()
            time.sleep(5)
        except:
            refresh_completion(driver)
            register_continue002 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
                By.ID, "continue")))
            register_continue002.click()
            time.sleep(5)


thread_001 = threading.Thread(target=os_mitmproxy)
thread_002 = threading.Thread(target=main_program)
thread_001.start()
thread_002.start()
