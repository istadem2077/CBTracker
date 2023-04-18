from selenium import webdriver as WD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException as TE
import time


driver = WD.Chrome() # Initiate Chrome Browser
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
    time.sleep(10)
    try: # Sometimes a popup appears, wait until exception is thrown and reload MySAT Dashboard page, and try clicking agian.
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-id-header-register-button"]'))).click()
    except TE:
        driver.get("https://mysat.collegeboard.org/dashboard")
        satreg()
    else:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div/div[2]/div[2]/button'))).click()
        driver.find_element(By.XPATH, '//*[@id="graddate-save-button"]').click()
        driver.find_element(By.XPATH, '//*[@id="grade-save-button"]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="continue-to-demographics-btn"]').click()
        time.sleep(5)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save-exit-demographics-btn"]'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div[2]/div[2]/button[1]'))).click()
        driver.find_element(By.XPATH, '//*[@id="terms-desc"]').send_keys(Keys.END)
        time.sleep(5)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/label/span').click() # Click the checkbox
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="forward-btn"]'))).click() # Continue
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="testlocation-continue-button"]'))).click()


def chooseTestDateMay6():
    driver.execute_script("window.scrollTo(0,600)")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'test-center-date-button-MAY-6'))).click()
    print(driver.find_element(By.ID, 'test-center-date-button-MAY-6').get_attribute('aria-current'))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="testdate-continue-button"]'))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/button'))).click() # Find a test center
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, 'toggle-btn').click()
    print("Aria Checked:", driver.find_element(By.CLASS_NAME, 'toggle-btn').find_element(By.TAG_NAME, 'input').get_attribute('aria-checked'))
    print(driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[4]/div[2]/div[1]').text)

loginMySAT()
satreg()
chooseTestDateMay6()