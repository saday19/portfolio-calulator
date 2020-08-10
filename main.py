from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import robinhood_login_api as rai
import time

def main():
    attempts = 0
    driver = setup_driver()
    successful_login = rai.login(driver, "samuel_adam_day@yahoo.com", "Cd77889900!!")
    wait_for_login(driver, successful_login)
    wait_for_verification(driver)
    locate_stocks(driver, attempts)
    driver.close()

def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://robinhood.com/login")
    return driver

def wait_for_login(driver, login_successful):
    logged_in = False
    if not login_successful:
        print("Please log in...")
    while not logged_in:
        try:
            driver.find_element_by_class_name("css-wcapli")
            time.sleep(1)
        except Exception:
            logged_in = True
            print("logged-in")

        print("waiting for login")

def wait_for_verification(driver):
    verifying = True
    print("Please verify your identity...")
    while verifying:
        try:
            driver.find_element_by_class_name("_1zexMpwTfW5iM-hLKSX9WX")
            time.sleep(1)
        except Exception:
            verifying = False
    time.sleep(1)

def locate_stocks(driver, attempts):
    elem = find_element(driver, "_3HLJ3tNpwWnaSGO61Xz-VA", attempts)
    if len(elem) == 0:
        time.sleep(1)
        locate_stocks(driver,attempts)
        return
    print(str(type(elem)) + " type")
    for something in elem:
        text = something.text
        if "Shares" not in text:
            index = elem.index(something) + 1
            if len(elem) > index:
                share = elem[index]
                print(text, share)

def find_element(driver, class_name, attempts):
    try:
        elem = driver.find_elements_by_class_name(class_name)
        return elem
    except Exception:
        attempts = attempts + 1
        if(attempts < 20):
            print("Unable to locate element, attempting again in 3s")
            time.sleep(3)
            return find_element(driver, class_name, attempts + 1)
        else:
            print("Giving up after 10 attmpts...")

if __name__ == "__main__":
    main()

# NOTE:
# This script is currently a work in progress!
# Currently it opens chrome and requires login and verification to RobinhHood
# Once it it lists your stock holdings along with how much you hold.
# It will soon calculate your total holdings along with dividends and graph your passive income.
