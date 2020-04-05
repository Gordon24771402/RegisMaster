from selenium import webdriver
import time
import winsound


def browser_open(driver):
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
                password.send_keys("PASSWORD")
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
        print("Get: college_board_sat_home")
    except:
        driver.refresh()
        driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
        print("Refresh & Get: college_board_sat_home")


def sat_main(driver):
    browser_open(driver)
    collegeboard_website(driver)
    collegeboard_log_in001(driver)
    time.sleep(3)
    collegeboard_log_in002(driver)
    collegeboard_log_in003(driver)
    collegeboard_log_in004(driver)
    time.sleep(3)
    collegeboard_sat_home(driver)


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
sat_main(driver)
