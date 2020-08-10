from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    attempts = 0
    driver = setup_driver()
    wait_for_login()
    wait_for_verification()
    locate_stocks()
    print("execution over")
    driver.close()

def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://robinhood.com/login")
    return driver

def wait_for_login():
    logged_in = False
    while not logged_in:
        try:
            driver.find_element_by_class_name("css-wcapli")
            print("Not logged in...")
            time.sleep(1)
        except Exception:
            logged_in = True

def wait_for_verification():
    verifying = True
    while verifying:
        try:
            driver.find_element_by_class_name("_1zexMpwTfW5iM-hLKSX9WX")
            print("Verifying")
            time.sleep(1)
        except Exception:
            verifying = False
    time.sleep(1)

def locate_stocks():
    elem = find_element(driver, "_3HLJ3tNpwWnaSGO61Xz-VA", attempts)
    print(type(elem))
    for something in elem:
        print(str(something.text))

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
