# %%
from ast import Pass
import email
from wsgiref.util import setup_testing_defaults
from xml.etree import ElementInclude
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import pandas as pd
from pandas import DataFrame, Series
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

time.sleep(5)

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
types = ['None', 'Market', 'Sector', 'Industry', 'Subindustry']
decays = range(1, 11, 1)
truncations = np.arange(0.01, 0.11, 0.01)  

for type in types:
    for decay in decays:
        for truncation in truncations:
            
            print(type, decay, truncation)

            settings = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "editor-top-bar-left__settings-btn"))
                )
            settings.click()
            time.sleep(1)
            neutralization = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "neutralization"))
                )
            neutralization.click()
            time.sleep(1)

            neu_types = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "select-portal__item"))
                )

            neu_types = driver.find_elements(By.CLASS_NAME, "select-portal__item")

            for neu_type in neu_types:
                print(neu_type.text)
                if neu_type.text == type:
                    neu_type.click()
                    break

            decay_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "decay"))
                )

            decay_element.clear()
            decay_element.send_keys(decay)
            time.sleep(1)
            truncation_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "truncation"))
                )
            truncation_element.clear()
            truncation_element.send_keys(truncation)
            time.sleep(1)

            apply = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "button--lg"))
                )
            apply.click()
            time.sleep(1)

# %%
alpha = driver.find_element(By.CLASS_NAME, "inputarea")
cmd = 'ts_mean(close, 5)'
alpha.click()
alpha.clear()
alpha.send_keys(cmd)


# %%
try:
    Pass = driver.find_element(By.CLASS_NAME, "sumary__testing-checks-PASS-list")
    pass_toggle = driver.find_element(By.CLASS_NAME, 'sumary__testing-checks-icon--PASS-down')
    pass_toggle.click()
    pass_lines = []
    pass_text = Pass.text
    pass_lines += pass_text.split('\n')
    print('{}{}'.format(Pass.text, pass_lines))

except:
    print('pass fail')
    # pass

try:
    Fail = driver.find_element(By.CLASS_NAME, 'sumary__testing-checks-FAIL-list')
    fail_toggle = driver.find_element(By.CLASS_NAME, 'sumary__testing-checks-icon--FAIL-down')
    fail_toggle.click()
    fail_lines = []
    fail_text = Fail.text
    fail_lines += fail_text.split('\n')
    print('{}{}'.format(Fail.text, fail_lines))

except:
    print('fail fail')
    # pass
# %%

if len(pass_lines) == 6:
    check = driver.find_element(By.CLASS_NAME, 'editor-button__text')
    check.click()
    time.sleep(5)

    for line in pass_lines:
        elements = line.split(' ')

        if elements[0] == 'Sharpe':
            sharpe = elements[2]
        if elements[0] == 'Turnover':
            turnover = elements[2]
        if elements[0] == 'Sub-universe':
            subsharpe = elements[3]
        if elements[0] == 'Fitness':
            fitness = elements[2]
        if elements[0] == 'Weight':
            weight = 'Weight is well distributed over instruments.'
        if elements[0] == 'Self-correlation':
            corr = elements[1]

    pass_information = {
        'sharpe': sharpe,
        'turnover': turnover,
        'subsharpe': subsharpe,
        'fitness': fitness,
        'weight': 'Weight is well distributed over instruments.',
        'corr': corr
    }
    print(pass_information)

else:
    for line in pass_lines:
        elements = line.split(' ')
        if elements[0] == 'Sharpe':
            sharpe = elements[2]
        if elements[0] == 'Turnover':
            turnover = elements[2]
        if elements[0] == 'Sub-universe':
            subsharpe = elements[3]
        if elements[0] == 'Fitness':
            fitness = elements[2]
        if elements[0] == 'Weight':
            weight = 'Weight is well distributed over instruments.'

    for line in fail_lines:
        elements = line.split(' ')
        if elements[0] == 'Sharpe':
            sharpe = elements[2]
        if elements[0] == 'Turnover':
            turnover = elements[2]
        if elements[0] == 'Sub-universe':
            subsharpe = elements[3]
        if elements[0] == 'Fitness':
            fitness = elements[2]
        if elements[0] == 'Weight':
            weight = 'Weight is too strongly concentrated or too few instruments are assigned weight.'

    retry_information = {
        'sharpe': sharpe,
        'turnover': turnover,
        'subsharpe': subsharpe,
        'fitness': fitness,
        'weight': weight,
        'corr': -1
    }
    print(retry_information)


# %%
## Weight is too strongly concentrated or too few instruments are assigned weight.