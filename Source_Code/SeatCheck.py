from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from playsound import playsound
from datetime import datetime

def reboot_main_program(driver):
    driver.close()
    time.sleep(60)
    main_program()

def get_collegeboard_website(driver):
    driver.get('https://collegereadiness.collegeboard.org/')
    time.sleep(5)

def login(driver):
    sign_in = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/a[1]")))
    sign_in.click()
    user_name = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[1]/input")))
    user_name.send_keys("USERNAME")
    password = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/div[2]/input")))
    password.send_keys("PASSWORD")
    submit = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/form/button")))
    submit.click()
    time.sleep(5)

def get_registration_website(driver):
    driver.get("https://nsat.collegeboard.org/satweb/satHomeAction.action")
    time.sleep(5)

def change_registration(driver):
    change = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div/div[2]/div/div/div/div/div[2]/button[3]')))
    change.click()
    time.sleep(5)
    change_test_date = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/main/form/div[2]/div[3]/div/div[4]/div[1]/div[1]/div[3]/a')))
    change_test_date.click()
    time.sleep(5)
    change_continue = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/main/form/div[6]/div/input')))
    change_continue.click()
    time.sleep(5)
    select_sat = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/main/form/div[4]/div/fieldset/div/div[1]/label/input')))
    select_sat.click()
    time.sleep(3)
    essay = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/main/form/div[6]/fieldset/div[2]/label/input')))
    essay.click()
    time.sleep(1)
    fee_waiver_no = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/main/form/div[8]/div/fieldset/div[1]/div[4]/label/input')))
    fee_waiver_no.click()
    time.sleep(1)
    answer_service_no = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/main/form/div[9]/div[2]/fieldset/div[2]/div[2]/input')))
    answer_service_no.click()
    time.sleep(1)
    change_continue_002 = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/main/form/div[10]/div/input')))
    change_continue_002.click()
    time.sleep(3)
    ok = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/main/div[3]/div/div/div[3]/input[2]')))
    ok.click()
    time.sleep(5)

def get_available_seats(driver):
    select_country_name = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/main/form/div[3]/fieldset/div/div[1]/div/select')))
    select_country_name.click()
    time.sleep(3)
    select_country_name.send_keys('Hong')
    time.sleep(3)
    search_by_country_or_region = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/main/form/div[3]/fieldset/div/div[1]/div/button')))
    search_by_country_or_region.click()
    time.sleep(5)
    show_available = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/main/form/div[3]/div[1]/div[1]/div[2]/label/input')))
    show_available.click()
    time.sleep(3)

def check_available_seats(driver):
    html = str(driver.execute_script("return document.documentElement.outerHTML"))
    if 'No matching records found' in html:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "Seats Not Available!")
        time.sleep(45)
        search_by_country_or_region = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/main/form/div[3]/fieldset/div/div[1]/div/button')))
        search_by_country_or_region.click()
        time.sleep(5)
        show_available = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/main/form/div[3]/div[1]/div[1]/div[2]/label/input')))
        show_available.click()
        time.sleep(3)
        check_available_seats(driver)
    elif 'No matching records found' not in html:
        while True:
            playsound("Alarm01.wav")

def main_program():
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    try:
        get_collegeboard_website(driver)
        login(driver)
        get_registration_website(driver)
        change_registration(driver)
        get_available_seats(driver)
        check_available_seats(driver)
    except:
        reboot_main_program(driver)


main_program()
