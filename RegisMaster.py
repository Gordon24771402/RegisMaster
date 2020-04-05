from selenium import webdriver
import time
from playsound import playsound
import schedule
import os



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
        print("XPath: collegeboard_log_in001")
    except:
        try:
            sign_in = driver.find_element_by_id("cb-atlas-header-1")
            sign_in.clcik()
            print("ID: collegeboard_log_in001")
        except:
            try:
                driver.refresh()
                sign_in = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/a[1]/span[1]")
                sign_in.click()
                print("Refresh & XPath: collegeboard_log_in001")
            except:
                driver.refresh()
                sign_in = driver.find_element_by_id("cb-atlas-header-1")
                sign_in.clcik()
                print("Refresh & ID: collegeboard_log_in001")


# noinspection PyBroadException
def collegeboard_log_in002(driver):
    try:
        user_name = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[1]/input")
        user_name.send_keys("USERNAME")
        print("XPath: collegeboard_log_in002")
    except:
        try:
            user_name = driver.find_element_by_id("userName")
            user_name.send_keys("USERNAME")
            print("ID: collegeboard_log_in002")
        except:
            try:
                driver.refresh()
                user_name = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[1]/input")
                user_name.send_keys("USERNAME")
                print("Refresh & XPath: collegeboard_log_in002")
            except:
                driver.refresh()
                user_name = driver.find_element_by_id("userName")
                user_name.send_keys("USERNAME")
                print("Refresh & ID: collegeboard_log_in002")


# noinspection PyBroadException
def collegeboard_log_in003(driver):
    try:
        password = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[2]/input")
        password.send_keys("PASSWORD")
        print("XPath: collegeboard_log_in003")
    except:
        try:
            password = driver.find_element_by_id("password")
            password.send_keys("PASSWORD")
            print("ID: collegeboard_log_in003")
        except:
            try:
                driver.refresh()
                password = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[2]/input")
                password.send_keys("PASSWORD)
                print("Refresh & XPath: collegeboard_log_in003")
            except:
                driver.refresh()
                password = driver.find_element_by_id("password")
                password.send_keys("PASSWORD")
                print("Refresh & ID: collegeboard_log_in003")


# noinspection PyBroadException
def collegeboard_log_in004(driver):
    try:
        submit = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/button")
        submit.click()
        print("XPath: collegeboard_log_in004")
    except:
        try:
            submit = driver.find_element_by_id("cb-atlas-identity-2")
            submit.click()
            print("ID: collegeboard_log_in004")
        except:
            try:
                driver.refresh()
                submit = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/button")
                submit.click()
                print("Refresh & XPath: collegeboard_log_in004")
            except:
                driver.refresh()
                submit = driver.find_element_by_id("cb-atlas-identity-2")
                submit.click()
                print("Refresh & ID: collegeboard_log_in004")


# noinspection PyBroadException
def collegeboard_sat_home(driver):
    try:
        driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
        print("Get: collegeboard_sat_home")
    except:
        driver.refresh()
        driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
        print("Refresh & Get: collegeboard_sat_home")


# noinspection PyBroadException
def sat_register_another(driver):
    try:
        register_another = driver.find_element_by_xpath(
            "/html/body/div[11]/div/div/div/div/div/div[2]/button")
        register_another.click()
        print("Xpath: sat_register_another")
    except:
        register_another = driver.find_element_by_id("actionRegisterAnother")
        register_another.click()
        print("ID: sat_register_another")
        try:
            driver.refresh()
            time.sleep(5)
            register_another = driver.find_element_by_xpath(
                "/html/body/div[11]/div/div/div/div/div/div[2]/button")
            register_another.click()
            print("Refresh & Xpath: sat_register_another")
        except:
            driver.refresh()
            time.sleep(5)
            register_another = driver.find_element_by_id("actionRegisterAnother")
            register_another.click()
            print("Refresh & ID: sat_register_another")
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
        print("Xpath: sat_authenticate_page")
    except:
        authenticate_page = driver.find_element_by_id("authenticatePage")
        authenticate_page.click()
        print("ID: sat_authenticate_page")
        try:
            driver.refresh()
            time.sleep(5)
            authenticate_page = driver.find_element_by_xpath(
                "/html/body/div[4]/div/div/div/footer/button")
            authenticate_page.click()
            print("Refresh & Xpath: sat_authenticate_page")
        except:
            driver.refresh()
            time.sleep(5)
            authenticate_page = driver.find_element_by_id("authenticatePage")
            authenticate_page.click()
            print("Refresh & ID: sat_authenticate_page")


# noinspection PyBroadException
def sat_register_continue001(driver):
    try:
        register_continue001 = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div/main/form/div[6]/div/input[2]")
        register_continue001.click()
        print("Xpath: sat_register_continue001")
    except:
        register_continue001 = driver.find_element_by_id("continue")
        register_continue001.click()
        print("ID: sat_register_continue001")
        try:
            driver.refresh()
            time.sleep(5)
            register_continue001 = driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div/main/form/div[6]/div/input[2]")
            register_continue001.click()
            print("Refresh & Xpath: sat_register_continue001")
        except:
            driver.refresh()
            time.sleep(5)
            register_continue001 = driver.find_element_by_id("continue")
            register_continue001.click()
            print("Refresh & ID: sat_register_continue001")


# noinspection PyBroadException
def sat_update_later(driver):
    try:
        update_later = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div/main/form/div[6]/div/button[2]")
        update_later.click()
        print("Xpath: sat_update_later")
    except:
        update_later = driver.find_element_by_id("updateLater")
        update_later.click()
        print("ID: sat_update_later")
        try:
            driver.refresh()
            time.sleep(5)
            update_later = driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div/main/form/div[6]/div/button[2]")
            update_later.click()
            print("Refresh & Xpath: sat_update_later")
        except:
            driver.refresh()
            time.sleep(5)
            update_later = driver.find_element_by_id("updateLater")
            update_later.click()
            print("Refresh & ID: sat_update_later")


# noinspection PyBroadException
def sat_agree_terms(driver):
    try:
        agree_terms = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[1]/main/form/fieldset/div/label/input")
        agree_terms.click()
        print("Xpath: sat_agree_terms")
    except:
        agree_terms = driver.find_element_by_id("agreeTerms")
        agree_terms.click()
        print("ID: sat_agree_terms")
        try:
            driver.refresh()
            time.sleep(5)
            agree_terms = driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div[1]/main/form/fieldset/div/label/input")
            agree_terms.click()
            print("Refresh & Xpath: sat_agree_terms")
        except:
            driver.refresh()
            time.sleep(5)
            agree_terms = driver.find_element_by_id("agreeTerms")
            agree_terms.click()
            print("Refresh & ID: sat_agree_terms")


# noinspection PyBroadException
def sat_register_continue002(driver):
    try:
        register_continue002 = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[2]/div/input[2]")
        register_continue002.click()
        print("Xpath: sat_register_continue002")
    except:
        register_continue002 = driver.find_element_by_id("continue")
        register_continue002.click()
        print("ID: sat_register_continue002")
        try:
            driver.refresh()
            time.sleep(5)
            register_continue002 = driver.find_element_by_xpath(
                "/html/body/div[3]/div[3]/div[2]/div/input[2]")
            register_continue002.click()
            print("Refresh & Xpath: sat_register_continue002")
        except:
            driver.refresh()
            time.sleep(5)
            register_continue002 = driver.find_element_by_id("continue")
            register_continue002.click()
            print("Refresh & ID: sat_register_continue002")


def browser_close(driver):
    driver.close()


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


def sat_schedule():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    sat_main(driver)
    html = str(driver.execute_script("return document.documentElement.outerHTML"))
    if "There are no available registration dates for the current test year. Please check back later to register for " \
       "future tests." in html:
        browser_close(driver)
        print("")
        print("Future SAT Registration Not Available!")
    else:
        n = 1
        while n == 1:
            playsound("Alarm01.wav")


schedule.every().day.at("21:00").do(sat_schedule)
schedule.every().day.at("22:00").do(sat_schedule)
schedule.every().day.at("23:00").do(sat_schedule)
schedule.every().day.at("00:00").do(sat_schedule)
schedule.every().day.at("01:00").do(sat_schedule)
schedule.every().day.at("02:00").do(sat_schedule)
schedule.every().day.at("03:00").do(sat_schedule)
schedule.every().day.at("04:00").do(sat_schedule)
schedule.every().day.at("05:00").do(sat_schedule)
schedule.every().day.at("06:00").do(sat_schedule)
schedule.every().day.at("07:00").do(sat_schedule)

while True:
    schedule.run_pending()
    time.sleep(1)
