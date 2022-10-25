import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout
    while time.time() < mustend:
        if somepredicate(*args, **kwargs):
            return True
        time.sleep(period)
    return False


def s(driver):
    return len(driver.window_handles) == 2


def scroll(driver, item):
    x = item.location['x']
    y = item.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (x, y)
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    driver.execute_script(scroll_by_coord)
    driver.execute_script(scroll_nav_out_of_way)


def scroller(driver, item):
    try:
        scroll(driver, item)
        actions = ActionChains(driver)
        actions.move_to_element(item)
        actions.click()
        return True
    except:
        return False


def setup(driverLocation, m, p, u=True):
    print("setup")
    driver = webdriver.Chrome(driverLocation)
    if (u):
        driver.get(
            "https://chrome.google.com/webstore/detail/ultrasurf-security-privac/mjnbclmflcpookeapghfhapeffmpodij?hl=en-US")
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'g-c-Hf'))).click()
        print("add extension")
        wait_until(lambda: s(driver), 25)
    driver.get("https://www.tumblr.com/login")
    print("login")
    i = driver.find_elements(By.CLASS_NAME, "gj_Aq")
    i[0].send_keys(m)
    i[1].send_keys(p)
    driver.find_element(By.XPATH, "//span[text()='Log in']").click()
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'wl0Ka')))
    driver.get("https://www.tumblr.com/likes")
    return driver


def setBorder(driver, e):
    js = f"arguments[0].style = 'border: solid yellow 3px' "
    driver.execute_script(js, e)
    return e


def cleaner(driver):
    try:
        js = "arguments[0].remove()"
        e = driver.find_element(
            By.CLASS_NAME, "Lq1wm")
        print("found element to delete")
        driver.execute_script(js, e)
    except:
        print("pass")


def unliker(driver):
    try:
        e = driver.find_element(
            By.XPATH, "//*[local-name()='svg']//*[local-name()='use' and @href='#managed-icon__like-filled']")
        scroller(driver, e)
        e.click()
        print("unliked")
        return True
    except:
        print("no item found to unlike")
        return False


def runner(driver):

    return unliker(driver)


def runnerLoop(driver):
    c = 0
    z = 0
    while z != 5:
        try:
            a = runner(driver)
            if a == False:
                driver.get("https://www.tumblr.com/likes")
                z += 1
            else:
                z = 0
        except:
            c += 1
            print("c :", c)
            if c == 10:
                driver.get("https://www.tumblr.com/likes")
                driver.find_element(By.TAG_NAME, 'body').send_keys(
                    Keys.CONTROL + Keys.HOME)
                c = 0
            else:
                pass


driverLocation = ""
mail = ""
password = ""
vpn = False
driver = setup(driverLocation, mail, password, vpn)
runnerLoop(driver)
