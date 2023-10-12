# pylint: disable=bare-except
# pylint: disable=wildcard-import
# pylint: disable=unspecified-encoding
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=global-statement
from time import ctime, time, sleep
import traceback
from selenium import webdriver as WD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    NoSuchWindowException,
)
from multiprocessing import Process

from tgmessage import notify, cberror, logs
import schoolcount
# from xvfbwrapper import Xvfb

# x = Xvfb()
# x.start()

cberror(f"{ctime(time())}, Bot started")

bycss = By.CSS_SELECTOR
byxpath = By.XPATH


# Initiate Chrome Browser
def loginMySAT(driver: WD.Chrome, email, password, wdw: WebDriverWait):
    driver.get("https://mysat.collegeboard.org/")  # Login to website
    driver.refresh()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/div/div/div/div/div/a'))).click() # Click the first continue button
    sleep(2)
    elementIdpUsername = driver.find_element(By.XPATH, '//*[@id="idp-discovery-username"]') # Identify username inout field
    elementIdpUsername.clear()
    elementIdpUsername.send_keys("mehdievjamil@gmail.com") # Enter required email, to be prompted in next update if required
    
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idp-discovery-submit"]'))).click() # Trigger click event on Next "submit" type button after entering email
    except ElementClickInterceptedException:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idp-discovery-submit"]'))).click() # Trigger click event on Next "submit" type button after entering email
    else:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="okta-signin-password"]')))
        elementIdpPasswd = driver.find_element(By.XPATH, '//*[@id="okta-signin-password"]') # Identify Password input field
        elementIdpPasswd.clear()
        elementIdpPasswd.send_keys("Zz123456!") # Enter required password TODO: remove password before pushing to GitHub!!!!!!
        driver.find_element(By.XPATH, '//*[@id="okta-signin-submit"]').click() # Trigger click event to submit password and email
        #print(driver.title)


def satreg():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-id-header-register-button"]'))).click()
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div/div[2]/div[2]/button'))).click()
    except TimeoutException:
        print("reloading")
        driver.get("https://mysat.collegeboard.org/dashboard")
        satreg()
    except ElementClickInterceptedException:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div/div[2]/div[2]/button'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-id-personalinfo-button-graddateconfirm"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-id-personalinfo-button-gradeconfirm"]'))).click()
    sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue-to-demographics-btn"]'))).click()
    sleep(5)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save-exit-demographics-btn"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div[2]/div[2]/button[1]'))).click() # SAT Registration. Get Started Button
    driver.find_element(By.XPATH, '//*[@id="qc-id-termsconditions-scrollbox-termsconditions"]').send_keys(Keys.END)
    sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/label/span').click() # Click the checkbox
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="forward-btn"]'))).click() # Continue
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-id-selectdatecenter-testlocation-button-next"]'))).click()


def refreshTestCenter():
    sleep(2)
    if driver.title == "SAT Registration":
        driver.refresh()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div[2]/div[2]/button[1]'))).click() # SAT Registration. Get Started Button
    findtestcenter()


def chooseTestDate():
    driver.execute_script("window.scrollTo(0,600)")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "qc-id-selectdatecenter-testdate-button-DEC-2"))).click() # No need for May 6, deadline passed
    print("Dec 2 checked: ", driver.find_element(By.ID, 'qc-id-selectdatecenter-testdate-button-DEC-2').get_attribute('aria-current'))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="testdate-continue-button"]'))).click()


def findtestcenter():
    global jun_3
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'qc-id-selectdatecenter-testcenter-international-button-search'))).click() # Find a test center
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'toggle-btn').click()
    jun_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[4]/div[2]/div[1]').text # Save text
    print("Dec 2: {0}, Checked: {1}".format(jun_3, ctime(time())))

previous = 0
def checkSchools(counter: str):
    global previous
    Message = [f"December 2\nLast update: {ctime(time())}\n\n"]
    if ((int)(counter) > 0):
        print(driver.find_element(By.ID, 'undefined_next').get_attribute("aria-disabled"))
        while (driver.find_element(By.ID,'undefined_next').get_attribute("aria-disabled") != "true"):
            table = driver.find_element(By.CLASS_NAME, 'cb-table').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
            for tr in table:
                school_name = tr.find_element(By.CLASS_NAME, 'test-center-name').text
                seat_available = tr.find_element(By.CLASS_NAME, 'seat-label').text
                Message.append("{0} : {1}\n".format(school_name, seat_available))
            driver.find_element(By.CLASS_NAME, 'cb-right').click()
        table = driver.find_element(By.CLASS_NAME, 'cb-table').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for tr in table:
            school_name = tr.find_element(By.CLASS_NAME, 'test-center-name').text
            seat_available = tr.find_element(By.CLASS_NAME, 'seat-label').text
            Message.append("{0} : {1}\n".format(school_name, seat_available))
        print(previous)
        Message = "\n".join(Message)
        print(Message)
        if previous == 0:
            print(tgmessage.telegram_sendmessage(976908358, Message))
            print(tgmessage.telegram_sendmessage(5670908383, Message))
            print(tgmessage.telegram_sendmessage(584098198, Message))
            print(tgmessage.telegram_sendmessage(853226047, Message))
            print(tgmessage.telegram_sendmessage(1278150481, Message))
            print(tgmessage.telegram_sendmessage(809899348, Message))
            print(tgmessage.telegram_sendmessage(853226047, Message))
            print(tgmessage.telegram_sendmessage(716930078, Message))
            print("Email sent, sleeping...")
    previous = (int)(schoolcount.stripresult(jun_3))
    


op = Options()
service = Service("/usr/bin/chromedriver")
# op.add_argument("--headless")
op.add_argument("--disable-browser-side-navigation")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")
op.add_argument("--start-maximized")
# PROXY="socks5://localhost:9050"
# op.add_argument(f"--proxy-server={PROXY}")
# op.add_argument("--user-data-dir='/root/.config/google-chrome/Profile 1'")
# logincreds = [[]] # logincreds[iterator][0] - email; logincreds[iterator][1]
iterator = 0


def main(test_date: str, email: str, password: str):
    print(f"Starting {test_date}")
    while 1:
        try:
            driver = WD.Chrome(service=service, options=op)
            print(111111)
            wdw = WebDriverWait(driver, 60)
            print(f"{test_date} Logging in")
            loginMySAT(driver=driver, email=email, password=password, wdw=wdw)
            cberror(f"{ctime(time())}, Logged IN")
            print(f"{test_date} Entering registration")
            satreg(driver=driver, wdw=wdw)
            print(f"{test_date} Choosing test date:")
            chooseTestDate(test_date, driver=driver, wdw=wdw)
            print(f"{test_date} Finding test centers")
            findtestcenter(test_date=test_date, driver=driver, wdw=wdw)
            checkSchools(schoolcount.stripresult(jun_3), test_date=test_date, driver=driver)
            while 1:  # Infinite loop which breaks if an exception appears
                try:
                    refreshTestCenter(test_date=test_date, driver=driver, wdw=wdw)
                except:
                    traceback.print_exc()
                    break
                else:
                    checkSchools(counter=schoolcount.stripresult(jun_3),test_date=test_date,driver=driver)
            # sleep(60)
            print(f"{test_date} Restarting the loop")
        except TimeoutException:
            print(TimeoutException)
            print(cberror(f"{ctime(time())}, {TimeoutException}{test_date}"))
            open("timeout.log", "w").write(traceback.format_exc())
            logs('timeout.log')
            driver.quit()
            continue
        except NoSuchWindowException:
            print("Killing application")
            return 1
        except KeyboardInterrupt:
            print("Killing application")
            return 0
        except:
            print(f"{test_date} Unknown error")
            print(cberror(f"{ctime(time())}, {test_date} Error! Check server!"))
            print(traceback.format_exc())
            open("./error.log", "w").write(traceback.format_exc())
            logs('./error.log')
            driver.quit()
            return -1


main("NOV-4", "fabbasov693@gmail.com", "Zz123456!")
# x.stop()
