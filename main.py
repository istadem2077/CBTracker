from selenium import webdriver as WD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException as TE
from time import ctime, time, sleep
import emailer
 # Initiate Chrome Browser
def loginMySAT():
    driver.get("https://mysat.collegeboard.org/") # Login to website
    driver.refresh()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/div/div/div/div/div/a'))).click() # Click the first continue button
    elementIdpUsername = driver.find_element(By.XPATH, '//*[@id="idp-discovery-username"]') # Identify username inout field
    elementIdpUsername.clear()
    elementIdpUsername.send_keys("alibbas177@gmail.com") # Enter required email, to be prompted in next update if required
    driver.find_element(By.XPATH, '//*[@id="idp-discovery-submit"]').click() # Trigger click event on Next "submit" type button after entering email
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="okta-signin-password"]')))
    elementIdpPasswd = driver.find_element(By.XPATH, '//*[@id="okta-signin-password"]') # Identify Password input field
    elementIdpPasswd.clear()
    elementIdpPasswd.send_keys("Bb(123456)") # Enter required password TODO: remove password before pushing to GitHub!!!!!!
    driver.find_element(By.XPATH, '//*[@id="okta-signin-submit"]').click() # Trigger click event to submit password and email
    #print(driver.title)


def satreg():
    sleep(10)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-id-header-register-button"]'))).click()
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div/div[2]/div[2]/button'))).click()
    except TE:
        print("reloading")
        driver.get("https://mysat.collegeboard.org/dashboard")
        satreg()
    else:
        driver.find_element(By.XPATH, '//*[@id="graddate-save-button"]').click()
        driver.find_element(By.XPATH, '//*[@id="grade-save-button"]').click()
        sleep(5)
        driver.find_element(By.XPATH, '//*[@id="continue-to-demographics-btn"]').click()
        sleep(5)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save-exit-demographics-btn"]'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div[2]/div[2]/button[1]'))).click()
        driver.find_element(By.XPATH, '//*[@id="terms-desc"]').send_keys(Keys.END)
        sleep(5)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/label/span').click() # Click the checkbox
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="forward-btn"]'))).click() # Continue
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="testlocation-continue-button"]'))).click()


def chooseTestDate():
    global may_6
    global jun_3
    driver.execute_script("window.scrollTo(0,600)")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'test-center-date-button-MAY-6'))).click()
    print("May 6 checked: ", driver.find_element(By.ID, 'test-center-date-button-MAY-6').get_attribute('aria-current'))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="testdate-continue-button"]'))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/button'))).click() # Find a test center
    sleep(5)
    driver.find_element(By.CLASS_NAME, 'toggle-btn').click()
    may_6 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[4]/div[2]/div[1]').text # Save text
    print("May 6: ", may_6)
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[2]/div/div[1]/div/a').click() # Go back to choosing test date
    driver.execute_script("window.scrollTo(0,600)")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "test-center-date-button-JUN-3"))).click()
    print("Jun 3 checked: ", driver.find_element(By.ID, 'test-center-date-button-JUN-3').get_attribute('aria-current'))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="testdate-continue-button"]'))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/button'))).click() # Find a test center
    sleep(5)
    driver.find_element(By.CLASS_NAME, 'toggle-btn').click()
    jun_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[4]/div[2]/div[1]').text # Save text
    print("June 3: ", jun_3)
    

while(1):
    try:
        driver = WD.Chrome()
        print("Logging in")
        loginMySAT()
        print("Entering registration")
        satreg()
        print("Choosing test date:")
        chooseTestDate()
        driver.quit()
        emailer.sendmail("itagizade@yahoo.com", f"Last update: {ctime(time())}", f"May 6: {may_6}\n June 3: {jun_3}")
        print("Email sent, sleeping...")
        sleep(60)
        print("Restarting the loop")
    except:
        print("Browser dead <3 starting all over")
        continue



