from selenium.webdriver.common.keys import Keys

def login(driver, username, password):
    try:
        sendElementInfo(driver, "username", username)
        sendElementInfo(driver, "password", password)
        elem = driver.find_element_by_class_name("_1OsoaRGpMCXh9KT8s7wtwm")
        elem.send_keys(Keys.RETURN)
        return True
    except Exception:
        return False

def sendElementInfo(driver, element_name, info):
    username_element = driver.find_element_by_name(element_name)
    username_element.send_keys(info)
