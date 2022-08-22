# %%
import email
from wsgiref.util import setup_testing_defaults
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## go to brain website
#options = Options()
#options.add_argument('--disable-notifications')
#op = webdriver.ChromeOptions()
#op.add_argument('headless')

# %%
driver = webdriver.Chrome('/Users/abnerteng/GitHub/WorldQuant-Brain/chromeDriver')#, options = op) # without browser
driver.get('https://platform.worldquantbrain.com/sign-in')

Accept = driver.find_element(By.CLASS_NAME, 'button--primary')
Accept.click()

time.sleep(1)
## driver.close()

## login

email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'password')

your_email = 'abnerteng16@gmail.com'
your_password = 'teng1234'

email.send_keys(your_email)
password.send_keys(your_password)
password.submit()

# %%
Skip = driver.find_element(By.CLASS_NAME, 'introjs-skipbutton')
Skip.click()
time.sleep(2)


## go to the simulate page
Simulate = driver.find_element(By.CLASS_NAME, 'header__img--simulate')
Simulate.click()

time.sleep(2)
Skip = driver.find_element(By.CLASS_NAME, 'introjs-skipbutton')
Skip.click()

# %%
TODO
## crawl Universe, delay, neutralization, decay, truncation
## simulation part
# %%
types = ['None', 'Market', 'Sector', 'Industry', 'Subindustry']
decays = range(1, 11, 1)
truncations = np.arange(0.01, 0.11, 0.01)

for type in types:
    for decay in decays:
        for truncation in truncations:
            # try:
            print(type, decay, truncation)
            # print("test")
            settings = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "editor-top-bar-left__settings-btn"))
                )
            # finally:
                # driver.quit()
            settings.click()
            time.sleep(1)
            # try:
            neutralization = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "neutralization"))
                )

            # finally:
                # driver.quit()
            neutralization.click()
            time.sleep(1)

            # try:
            neu_types = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "select-portal__item"))
                )
            # finally:
                # driver.quit()

            neu_types = driver.find_elements(By.CLASS_NAME, "select-portal__item")

            for neu_type in neu_types:
                print(neu_type.text)
                if neu_type.text == type:
                    neu_type.click()
                    break

            # try:
            decay_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "decay"))
                )
            # finally:
                # driver.quit()

            decay_element.clear()
            decay_element.send_keys(decay)
            time.sleep(1)
            # try:
            truncation_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "truncation"))
                )
            # finally:
                # driver.quit()
            truncation_element.clear()
            truncation_element.send_keys(truncation)
            time.sleep(1)

            apply = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "button--lg"))
                )
            # driver.quit()
            apply.click()
            time.sleep(1)

            # simulate = driver.find_element(By.CLASS_NAME, 'editor-simulate-button-text--is-code')
            # simulate.click()

# %%
alpha = driver.find_element(By.CLASS_NAME, 'contentWidgets')
cmd = 'ts_mean(close, 5)'
alpha.send_keys(cmd)
# %%
# switch_to.active_element