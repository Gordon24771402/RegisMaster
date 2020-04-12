# Selenium Version =====================================================================================================
from selenium import webdriver
import time
from playsound import playsound
import schedule
import os
import logging

logging.basicConfig(filename='LOG.log', level=10, format='%(asctime)s: %(levelname)s, %(message)s')


def browser_maximize(driver):
    driver.maximize_window()


def collegeboard_website(driver):
    driver.get("https://collegereadiness.collegeboard.org/")


# noinspection PyBroadException
def collegeboard_log_in001(driver):
    try:
        sign_in = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/a[1]/span[1]")
        sign_in.click()
        logging.debug("XPath: collegeboard_log_in001")
    except:
        try:
            sign_in = driver.find_element_by_id("cb-atlas-header-1")
            sign_in.clcik()
            logging.debug("ID: collegeboard_log_in001")
        except:
            try:
                os.system('ipconfig/release')
                time.sleep(30)
                os.system('ipconfig/renew')
                time.sleep(30)
                driver.refresh()
                time.sleep(5)
                sign_in = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/a[1]/span[1]")
                sign_in.click()
                logging.debug("Refresh & XPath: collegeboard_log_in001")
            except:
                os.system('ipconfig/release')
                time.sleep(30)
                os.system('ipconfig/renew')
                time.sleep(30)
                driver.refresh()
                time.sleep(5)
                sign_in = driver.find_element_by_id("cb-atlas-header-1")
                sign_in.clcik()
                logging.debug("Refresh & ID: collegeboard_log_in001")


# noinspection PyBroadException
def collegeboard_log_in002(driver):
    try:
        user_name = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[1]/input")
        user_name.send_keys("USERNAME")
        logging.debug("XPath: collegeboard_log_in002")
    except:
        try:
            user_name = driver.find_element_by_id("userName")
            user_name.send_keys("USERNAME")
            logging.debug("ID: collegeboard_log_in002")
        except:
            try:
                os.system('ipconfig/release')
                time.sleep(30)
                os.system('ipconfig/renew')
                time.sleep(30)
                driver.refresh()
                time.sleep(5)
                user_name = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[1]/input")
                user_name.send_keys("USERNAME")
                logging.debug("Refresh & XPath: collegeboard_log_in002")
            except:
                os.system('ipconfig/release')
                time.sleep(30)
                os.system('ipconfig/renew')
                time.sleep(30)
                driver.refresh()
                time.sleep(5)
                user_name = driver.find_element_by_id("userName")
                user_name.send_keys("USERNAME")
                logging.debug("Refresh & ID: collegeboard_log_in002")


# noinspection PyBroadException
def collegeboard_log_in003(driver):
    try:
        password = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[2]/input")
        password.send_keys("PASSWORD")
        logging.debug("XPath: collegeboard_log_in003")
    except:
        try:
            password = driver.find_element_by_id("password")
            password.send_keys("PASSWORD")
            logging.debug("ID: collegeboard_log_in003")
        except:
            try:
                os.system('ipconfig/release')
                time.sleep(30)
                os.system('ipconfig/renew')
                time.sleep(30)
                driver.refresh()
                time.sleep(5)
                password = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[2]/input")
                password.send_keys("PASSWORD")
                logging.debug("Refresh & XPath: collegeboard_log_in003")
            except:
                os.system('ipconfig/release')
                time.sleep(30)
                os.system('ipconfig/renew')
                time.sleep(30)
                driver.refresh()
                time.sleep(5)
                password = driver.find_element_by_id("password")
                password.send_keys("PASSWORD")
                logging.debug("Refresh & ID: collegeboard_log_in003")


# noinspection PyBroadException
def collegeboard_log_in004(driver):
    try:
        submit = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/button")
        submit.click()
        logging.debug("XPath: collegeboard_log_in004")
    except:
        try:
            submit = driver.find_element_by_id("cb-atlas-identity-2")
            submit.click()
            logging.debug("ID: collegeboard_log_in004")
        except:
            try:
                os.system('ipconfig/release')
                time.sleep(30)
                os.system('ipconfig/renew')
                time.sleep(30)
                driver.refresh()
                time.sleep(5)
                submit = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/button")
                submit.click()
                logging.debug("Refresh & XPath: collegeboard_log_in004")
            except:
                os.system('ipconfig/release')
                time.sleep(30)
                os.system('ipconfig/renew')
                time.sleep(30)
                driver.refresh()
                time.sleep(5)
                submit = driver.find_element_by_id("cb-atlas-identity-2")
                submit.click()
                logging.debug("Refresh & ID: collegeboard_log_in004")


# noinspection PyBroadException
def collegeboard_sat_home(driver):
    try:
        driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
        logging.debug("Get: collegeboard_sat_home")
    except:
        os.system('ipconfig/release')
        time.sleep(30)
        os.system('ipconfig/renew')
        time.sleep(30)
        driver.refresh()
        time.sleep(5)
        driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
        logging.debug("Refresh & Get: collegeboard_sat_home")


# noinspection PyBroadException
def sat_register_another(driver):
    try:
        register_another = driver.find_element_by_xpath(
            "/html/body/div[11]/div/div/div/div/div/div[2]/button")
        register_another.click()
        logging.debug("Xpath: sat_register_another")
    except:
        register_another = driver.find_element_by_id("actionRegisterAnother")
        register_another.click()
        logging.debug("ID: sat_register_another")
        try:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            register_another = driver.find_element_by_xpath(
                "/html/body/div[11]/div/div/div/div/div/div[2]/button")
            register_another.click()
            logging.debug("Refresh & Xpath: sat_register_another")
        except:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            register_another = driver.find_element_by_id("actionRegisterAnother")
            register_another.click()
            logging.debug("Refresh & ID: sat_register_another")
            try:
                sat_register_another(driver)
            except:
                sat_register_another(driver)


# noinspection PyBroadException
def sat_authenticate_page(driver):
    try:
        authenticate_page = driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/footer/button")
        authenticate_page.click()
        logging.debug("Xpath: sat_authenticate_page")
    except:
        authenticate_page = driver.find_element_by_id("authenticatePage")
        authenticate_page.click()
        logging.debug("ID: sat_authenticate_page")
        try:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            authenticate_page = driver.find_element_by_xpath(
                "/html/body/div[4]/div/div/div/footer/button")
            authenticate_page.click()
            logging.debug("Refresh & Xpath: sat_authenticate_page")
        except:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            authenticate_page = driver.find_element_by_id("authenticatePage")
            authenticate_page.click()
            logging.debug("Refresh & ID: sat_authenticate_page")


# noinspection PyBroadException
def sat_register_continue001(driver):
    try:
        register_continue001 = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div/main/form/div[6]/div/input[2]")
        register_continue001.click()
        logging.debug("Xpath: sat_register_continue001")
    except:
        register_continue001 = driver.find_element_by_id("continue")
        register_continue001.click()
        logging.debug("ID: sat_register_continue001")
        try:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            register_continue001 = driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div/main/form/div[6]/div/input[2]")
            register_continue001.click()
            logging.debug("Refresh & Xpath: sat_register_continue001")
        except:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            register_continue001 = driver.find_element_by_id("continue")
            register_continue001.click()
            logging.debug("Refresh & ID: sat_register_continue001")


# noinspection PyBroadException
def sat_update_later(driver):
    try:
        update_later = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div/main/form/div[6]/div/button[2]")
        update_later.click()
        logging.debug("Xpath: sat_update_later")
    except:
        update_later = driver.find_element_by_id("updateLater")
        update_later.click()
        logging.debug("ID: sat_update_later")
        try:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            update_later = driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div/main/form/div[6]/div/button[2]")
            update_later.click()
            logging.debug("Refresh & Xpath: sat_update_later")
        except:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            update_later = driver.find_element_by_id("updateLater")
            update_later.click()
            logging.debug("Refresh & ID: sat_update_later")


# noinspection PyBroadException
def sat_agree_terms(driver):
    try:
        agree_terms = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[1]/main/form/fieldset/div/label/input")
        agree_terms.click()
        logging.debug("Xpath: sat_agree_terms")
    except:
        agree_terms = driver.find_element_by_id("agreeTerms")
        agree_terms.click()
        logging.debug("ID: sat_agree_terms")
        try:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            agree_terms = driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div[1]/main/form/fieldset/div/label/input")
            agree_terms.click()
            logging.debug("Refresh & Xpath: sat_agree_terms")
        except:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            agree_terms = driver.find_element_by_id("agreeTerms")
            agree_terms.click()
            logging.debug("Refresh & ID: sat_agree_terms")


# noinspection PyBroadException
def sat_register_continue002(driver):
    try:
        register_continue002 = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[2]/div/input[2]")
        register_continue002.click()
        logging.debug("Xpath: sat_register_continue002")
    except:
        register_continue002 = driver.find_element_by_id("continue")
        register_continue002.click()
        logging.debug("ID: sat_register_continue002")
        try:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            register_continue002 = driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div[2]/div/input[2]")
            register_continue002.click()
            logging.debug("Refresh & Xpath: sat_register_continue002")
        except:
            os.system('ipconfig/release')
            time.sleep(30)
            os.system('ipconfig/renew')
            time.sleep(30)
            driver.refresh()
            time.sleep(5)
            register_continue002 = driver.find_element_by_id("continue")
            register_continue002.click()
            logging.debug("Refresh & ID: sat_register_continue002")


def browser_close(driver):
    driver.close()


# noinspection PyBroadException
def sat_main(driver):
    browser_maximize(driver)
    collegeboard_website(driver)
    time.sleep(1)
    collegeboard_log_in001(driver)
    time.sleep(5)
    collegeboard_log_in002(driver)
    time.sleep(1)
    collegeboard_log_in003(driver)
    time.sleep(1)
    collegeboard_log_in004(driver)
    time.sleep(5)
    collegeboard_sat_home(driver)
    time.sleep(5)
    sat_register_another(driver)
    time.sleep(5)
    sat_authenticate_page(driver)
    time.sleep(5)
    sat_register_continue001(driver)
    time.sleep(5)
    sat_update_later(driver)
    time.sleep(5)
    sat_agree_terms(driver)
    time.sleep(5)
    sat_register_continue002(driver)
    time.sleep(5)
    browser_close(driver)


def sat_schedule():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    sat_main(driver)
    html = str(driver.execute_script("return document.documentElement.outerHTML"))
    if "There are no available registration dates for the current test year. Please check back later to register for " \
       "future tests." in html:
        browser_close(driver)
        print("Future SAT Registration Not Available!")
    else:
        n = 1
        while n == 1:
            playsound("Alarm01.wav")


print("Program Will Run Automatically!")
schedule.every().day.at("23:00").do(sat_schedule)
schedule.every().day.at("00:00").do(sat_schedule)
schedule.every().day.at("01:00").do(sat_schedule)
schedule.every().day.at("03:30").do(sat_schedule)
schedule.every().day.at("04:30").do(sat_schedule)
schedule.every().day.at("05:00").do(sat_schedule)

while True:
    schedule.run_pending()
    time.sleep(1)


# Pynput Version =======================================================================================================
import win32api
import win32con
import win32clipboard
from pynput.keyboard import Key, Controller as KeyboardController
import time
from pynput.mouse import Button, Controller as MouseController
from playsound import playsound
import schedule

keyboard = KeyboardController()
mouse = MouseController()
x_resolution = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
y_resolution = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
x_conversion_factor = round(x_resolution / 1600, 4)
y_conversion_factor = round(y_resolution / 900, 4)


def sat_main_cracker():
    # Chrome Open
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(1.5)
    for characters in "Google Chrome":
        keyboard.press(characters)
        keyboard.release(characters)
    time.sleep(1.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1.5)

    # Enter Collegeboard Address
    time.sleep(1.5)
    mouse.position = (round(300 * x_conversion_factor, 4), round(50 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    for characters in "https://collegereadiness.collegeboard.org/":
        keyboard.press(characters)
        keyboard.release(characters)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)

    # Enter UserName & Password
    mouse.position = (round(1060 * x_conversion_factor, 4), round(130 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    mouse.position = (round(570 * x_conversion_factor, 4), round(365 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    for characters in "USERNAME":
        keyboard.press(characters)
        keyboard.release(characters)
    time.sleep(1.5)
    mouse.position = (round(1400 * x_conversion_factor, 4), round(400 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    mouse.position = (round(570 * x_conversion_factor, 4), round(455 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    for characters in "PASSWORD":
        keyboard.press(characters)
        keyboard.release(characters)
    time.sleep(1.5)
    mouse.position = (round(1400 * x_conversion_factor, 4), round(400 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    mouse.position = (round(490 * x_conversion_factor, 4), round(575 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(5)

    # Go To My_SAT
    mouse.position = (round(1060 * x_conversion_factor, 4), round(130 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    mouse.position = (round(490 * x_conversion_factor, 4), round(300 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(5)

    # Register for the SAT
    mouse.position = (round(1130 * x_conversion_factor, 4), round(290 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    mouse.position = (round(1135 * x_conversion_factor, 4), round(430 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(5)
    mouse.scroll(round(16000 * x_conversion_factor, 4), round(-9000 * y_conversion_factor, 4))
    time.sleep(1.5)
    mouse.position = (round(1200 * x_conversion_factor, 4), round(860 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(5)
    mouse.scroll(round(16000 * x_conversion_factor, 4), round(-9000 * y_conversion_factor, 4))
    time.sleep(1.5)
    mouse.position = (round(1215 * x_conversion_factor, 4), round(765 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(5)
    mouse.scroll(round(16000 * x_conversion_factor, 4), round(-9000 * y_conversion_factor, 4))
    time.sleep(1.5)
    mouse.position = (round(1125 * x_conversion_factor, 4), round(765 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(5)
    mouse.position = (round(1400 * x_conversion_factor, 4), round(400 * y_conversion_factor, 4))
    mouse.scroll(round(16000 * x_conversion_factor, 4), round(-9000 * y_conversion_factor, 4))
    time.sleep(1.5)
    mouse.position = (round(327 * x_conversion_factor, 4), round(703 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    mouse.position = (round(1230 * x_conversion_factor, 4), round(765 * y_conversion_factor, 4))
    mouse.click(Button.left, 1)
    time.sleep(5)

    # Check For SAT
    time.sleep(3)
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
    mouse.position = (round(410 * x_conversion_factor, 4), round(433 * y_conversion_factor, 4))
    mouse.click(Button.left, 3)
    time.sleep(1.5)
    keyboard.press(Key.ctrl)
    keyboard.press("c")
    time.sleep(1.5)
    keyboard.release(Key.ctrl)
    keyboard.release("c")
    win32clipboard.OpenClipboard()
    my_text = str(win32clipboard.GetClipboardData(win32clipboard.CF_TEXT))
    win32clipboard.CloseClipboard()
    if "There are no available registration dates for the current test year." in my_text:
        print("Future SAT NOT Available!")
        mouse.position = (round(1230 * x_conversion_factor, 4), round(500 * y_conversion_factor, 4))
        mouse.click(Button.left, 1)
        time.sleep(5)
        mouse.position = (round(1070 * x_conversion_factor, 4), round(125 * y_conversion_factor, 4))
        mouse.click(Button.left, 1)
        time.sleep(1.5)
        mouse.position = (round(555 * x_conversion_factor, 4), round(290 * y_conversion_factor, 4))
        mouse.click(Button.left, 1)
        time.sleep(5)
        mouse.position = (round(1575 * x_conversion_factor, 4), round(15 * y_conversion_factor, 4))
        mouse.click(Button.left, 1)
    else:
        n = 1
        while n == 1:
            playsound("Alarm01.wav")


print("Program Will Run Automatically!")
schedule.every().day.at("22:30").do(sat_main_cracker)
schedule.every().day.at("23:00").do(sat_main_cracker)
schedule.every().day.at("23:30").do(sat_main_cracker)
schedule.every().day.at("00:30").do(sat_main_cracker)
schedule.every().day.at("01:00").do(sat_main_cracker)
schedule.every().day.at("01:30").do(sat_main_cracker)
schedule.every().day.at("02:00").do(sat_main_cracker)
schedule.every().day.at("02:30").do(sat_main_cracker)
schedule.every().day.at("03:00").do(sat_main_cracker)
schedule.every().day.at("03:30").do(sat_main_cracker)
schedule.every().day.at("04:00").do(sat_main_cracker)
schedule.every().day.at("04:30").do(sat_main_cracker)
schedule.every().day.at("05:00").do(sat_main_cracker)
schedule.every().day.at("05:30").do(sat_main_cracker)
schedule.every().day.at("06:00").do(sat_main_cracker)
schedule.every().day.at("06:30").do(sat_main_cracker)

while True:
    schedule.run_pending()
    time.sleep(1)
