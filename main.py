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
    elementIdpPasswd.send_keys("") # Enter required password TODO: remove password before pushing to GitHub!!!!!!
    driver.find_element(By.XPATH, '//*[@id="okta-signin-submit"]') # Trigger click event to submit password and email
    print(driver.title)
    
if ("Sign in" in driver.title):
    pass # TODO: Call loginMySAT function, needs fix and testing


def __main__():
    pass

if __name__ == "__main__":
    __main__()