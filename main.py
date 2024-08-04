from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import helper

try:
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options = options)
    while(1==1):
        driver.get("https://theamericapac.org/voter-registration/")
        year = helper.get_random_year()
        name = helper.get_name()
        surname = helper.get_surname()
        email = helper.get_email(name,surname,year)
        address = helper.get_address()
        phone = helper.get_phone(address)


        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        driver.switch_to.frame(iframe)

        email_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(email)

        zipcode_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "postal"))
        )
        zipcode_input.send_keys(address['postalCode'])

        button = driver.find_element(By.CLASS_NAME, "formbold-btn")

        zipcode_input.click() #the site is so buggy i have to click twice to remove popup
        button.click() # because it briefly reappers after going away and mess with button clicking

        button = driver.find_element(By.CLASS_NAME, "formbold-btn")
        button.click() # finally we can proceed to next page of the form :)



        name_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "firstname"))
        )
        name_input.send_keys(name)

        surname_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "lastname"))
        )
        surname_input.send_keys(surname)

        phone_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "phone"))
        )
        phone_input.send_keys(phone)

        address_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ship-address"))
        )
        address_input.send_keys(address['address1'])

        city_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        city_input.send_keys(address['city'])

        driver.switch_to.default_content()
        driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.CONTROL + Keys.END)
        driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.CONTROL + Keys.END)

        driver.switch_to.frame(iframe)

        month_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "dob_month"))
        )
        month = helper.get_random_month()
        month_input.send_keys(month)

        day_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "dob_day"))
        )
        day = helper.get_random_day()
        day_input.send_keys(day)

        year_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "dob_year"))
        )
        year_input.send_keys(year)


        chkbox_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "supportCheckbox"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", chkbox_input)
        driver.execute_script("arguments[0].click();", chkbox_input)

        button = driver.find_element(By.CLASS_NAME, "formbold-btn")
        button.click()
finally:
    driver.quit()
