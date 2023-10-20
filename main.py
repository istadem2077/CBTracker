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
    WebDriverException
)
from tgmessage import notify, cberror, logs
import schoolcount
from elements_paths import *

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
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((bycss, sign_in_btn_id))
    ).click()  # Click the first continue button
    sleep(2)
    elementIdpUsername = driver.find_element(
        bycss, sign_in_email_id
    )  # Identify username inout field
    elementIdpUsername.clear()
    elementIdpUsername.send_keys(
        email
    )  # Enter required email, to be prompted in next update if required
    sleep(2)
    try:
        wdw.until(
            EC.element_to_be_clickable((bycss, sign_in_email_submit_id))
        ).click()  # Trigger click event on Next "submit" type button after entering email
    except ElementClickInterceptedException:
        wdw.until(
            EC.element_to_be_clickable((bycss, "#onetrust-accept-btn-handler"))
        ).click()
        wdw.until(
            EC.element_to_be_clickable((bycss, sign_in_email_submit_id))
        ).click()  # Trigger click event on Next "submit" type button after entering email
    wdw.until(EC.presence_of_element_located((bycss, sign_in_password_id)))
    driver.find_element(bycss, sign_in_password_id).clear()
    driver.find_element(bycss, sign_in_password_id).send_keys(
        password
    )  # Enter required password TODO: remove password before pushing to GitHub!!!!!!
    driver.find_element(
        bycss, sign_in_password_submit_id
    ).click()  # Trigger click event to submit password and email
    # print(driver.title)


def satreg(driver: WD.Chrome, wdw: WebDriverWait):
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((bycss, satreg_btn_id))).click()
    try:
        wdw.until(EC.element_to_be_clickable((bycss, get_started_btn_id))).click()
    except TimeoutException:
        print("reloading")
        driver.get("https://mysat.collegeboard.org/dashboard")
        satreg(driver, wdw)
    except ElementClickInterceptedException:
        wdw.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
        wdw.until(EC.element_to_be_clickable((bycss, get_started_btn_id))).click()
    wdw.until(EC.element_to_be_clickable((bycss, grade_date_confirm_id))).click()
    wdw.until(EC.element_to_be_clickable((bycss, grade_confirm_id))).click()
    sleep(5)
    wdw.until(EC.element_to_be_clickable((bycss, continue_to_demos_id))).click()
    sleep(5)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((bycss, save_demos_continue_id))).click()
    wdw.until(EC.element_to_be_clickable((bycss, get_started_btn_scroll_id))).click()  # SAT Registration. Get Started Button
    driver.find_element(bycss, tos_scrollbox_id).send_keys(Keys.END)
    sleep(5)
    driver.find_element(bycss, tos_accept_css).click()  # Click the checkbox
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((bycss, tos_continue_id))).click()  # Continue
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((bycss, select_location_next_id))).click()


def refreshTestCenter(test_date, driver: WD.Chrome, wdw: WebDriverWait):
    sleep(2)
    if driver.title == "SAT Registration":
        driver.refresh()
    wdw.until(EC.element_to_be_clickable((bycss, get_started_btn_scroll_id))).click()  # Passes the scrollbox after a refresh
    findtestcenter(test_date=test_date, driver=driver, wdw=wdw)


def chooseTestDate(test_date: str, driver: WD.Chrome, wdw: WebDriverWait):
    driver.execute_script("window.scrollTo(0,600)")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((bycss, test_date_button_id.format(test_date)))).click()
    print(f"{test_date} clicked: ",driver.find_element(bycss, test_date_button_id.format(test_date)).get_attribute("aria-current"),)
    wdw.until(EC.element_to_be_clickable((bycss, test_date_continue_id))).click()


jun_3 = ""


def findtestcenter(test_date: str, driver: WD.Chrome, wdw: WebDriverWait):
    global jun_3
    wdw.until(EC.element_to_be_clickable((bycss, select_diff_center_id))).click()
    wdw.until(EC.element_to_be_clickable((bycss, find_centers_id))).click()  # Find a test center
    sleep(2)
    wdw.until(EC.element_to_be_clickable((bycss, toggle_button_id))).click()
    jun_3 = driver.find_element(bycss, avail_schools_count_css).text  # Save text
    print(f"{test_date}: {jun_3}, Checked: {ctime(time())}")


previous = 0


def checkSchools(counter: str, test_date: str, driver: WD.Chrome):
    global previous
    Message = [f"{test_date}\nLast update: {ctime(time())}\n\n"]
    if (int)(counter) > 0:
        print(driver.find_element(By.ID, "undefined_next").get_attribute("aria-disabled"))
        while driver.find_element(By.ID, "undefined_next").get_attribute("aria-disabled") != "true":
            table = (driver.find_element(By.CLASS_NAME, "cb-table").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"))
            for tr in table:
                school_name = tr.find_element(By.CLASS_NAME, "test-center-name").text
                seat_available = tr.find_element(By.CLASS_NAME, "seat-label").text
                Message.append(f"{school_name} : {seat_available}\n")
            driver.find_element(By.CLASS_NAME, "cb-right").click()
        table = (driver.find_element(By.CLASS_NAME, "cb-table").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"))
        for tr in table:
            school_name = tr.find_element(By.CLASS_NAME, "test-center-name").text
            seat_available = tr.find_element(By.CLASS_NAME, "seat-label").text
            Message.append(f"{school_name} : {seat_available}\n")
        print(previous)
        Message = "\n".join(Message)
        print(Message)
        if previous == 0:
            print(notify(976908358, Message))  # Arif
            print(notify(5670908383, Message))  # My chat
            print(notify(584098198, Message))  # Mansur
            print(notify(912056633, Message))  # Abdulaziz
            print(notify(1278150481, Message))  # Rafail
            # print(notify(809899348, Message))
            # print(notify(853226047, Message))
            # print(notify(716930078, Message))
            print("Email sent, sleeping...")
    previous = (int)(schoolcount.stripresult(jun_3))


op = Options()
service = Service("/usr/bin/chromedriver")
# op.add_argument("--headless")
op.add_argument("--disable-browser-side-navigation")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")
# op.add_argument("--start-maximized")
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
                    cberror('Exited nested loop')
                    open('nested.log', 'w').write(traceback.format_exc)
                    logs('nested.log')
                    break
                else:
                    checkSchools(counter=schoolcount.stripresult(jun_3),test_date=test_date,driver=driver)
            # sleep(60)
            driver.quit()
            cberror(f"{test_date} Restarting the loop")
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
        except WebDriverException:
            cberror(f"{ctime(time())}, {test_date} WebDriverException! Check server!")
            open("./wdexc.log", "w").write(traceback.format_exc())
            logs('./wdexc.log')
            continue
        except:
            print(f"{test_date} Unknown error")
            print(cberror(f"{ctime(time())}, {test_date} Error! Check server!"))
            print(traceback.format_exc())
            open("./error.log", "w").write(traceback.format_exc())
            logs('./error.log')
            driver.quit()
            return -1


main("DEC-2", "clickclick0063@gmail.com", "Zz123456!")
# x.stop()
