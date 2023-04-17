from selenium import webdriver as WD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = WD.Chrome() # Initiate Chrome Browser
def loginMySAT():
    driver.get("https://mysat.collegeboard.org/") # Login to website
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div/div/div/div/div/div/div/a'))).click() # Click the first continue button
    elementIdpUsername = driver.find_element(By.XPATH, '//*[@id="idp-discovery-username"]') # Identify username inout field
    elementIdpUsername.clear()
    elementIdpUsername.send_keys("alibbas177@gmail.com") # Enter required email, to be prompted in next update if required
    driver.find_element(By.XPATH, '//*[@id="idp-discovery-submit"]').click() # Trigger click event on Next "submit" type button after entering email
    elementIdpPasswd = driver.find_element(By.XPATH, '//*[@id="okta-signin-password"]') # Identify Password input field
    elementIdpPasswd.clear()
    elementIdpPasswd.send_keys("Bb(123456)") # Enter required password TODO: remove password before pushing to GitHub!!!!!!
    driver.find_element(By.XPATH, '//*[@id="okta-signin-submit"]') # Trigger click event to submit password and email
    print(driver.title)

def satreg():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-id-header-register-button"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div/div[2]/div[2]/button'))).click()
    driver.find_element(By.XPATH, '//*[@id="graddate-save-button"]').click()
    driver.find_element(By.XPATH, '//*[@id="grade-save-button"]').click()
    driver.find_element(By.XPATH, '//*[@id="continue-to-demographics-btn"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save-exit-demographics-btn"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div[2]/div[2]/button[1]'))).click()
    driver.find_element(By.XPATH, '//*[@id="terms-desc"]').send_keys(Keys.END)
    tos_checkbox = driver.find_element(By.ID, 'terms-acceptance-checkbox')
    if tos_checkbox.get_attribute('unchecked'):
        tos_checkbox.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="testlocation-continue-button"]'))).click()


def chooseTestDateMay6():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'test-center-date-button-MAY-6'))).click()
    driver.find_element(By.XPATH, '//*[@id="testdate-continue-button"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/button'))).click()
    driver.find_element(By.XPATH, '//*[@id="apricot_switch_1352"]').click()
    print(driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[4]/div[2]/div[1]'))

if ("Sign in" in driver.title):
    pass # TODO: Call loginMySAT function, needs fix and testing