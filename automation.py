# %%
import email
from enum import auto
from wsgiref.util import setup_testing_defaults
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse

# %%
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--driver_path', required=True, type=str)
    parser.add_argument('-u', '--url', required=True, type=str)
    parser.add_argument('-n', '--neutralizations', required=True, type=str, nargs='+')
    parser.add_argument('--decays', required=True, type=int, nargs='+')
    parser.add_argument('-t', '--truncations', required=True, type=float, nargs='+')
    parser.add_argument('--your_email', required = True, type = str)
    parser.add_argument('--your_password', required = True, type = str)
    args = parser.parse_args()
    return args

# %%

def to_simulate(driver, url, your_email, your_password):
    driver.get(url)

    Accept = driver.find_element(By.CLASS_NAME, 'button--primary')
    Accept.click()

    time.sleep(1)

    ## login

    email = driver.find_element(By.ID, 'email')
    password = driver.find_element(By.ID, 'password')

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
def get_commands() -> list:
    pass

# %%
def simulate(driver, command, neu, decay, trunc):
    '''
    return sharpe, turnover, etc...
    '''
    pass

    type_strategy = driver.find_element(By.CLASS_NAME, "inputarea")
    type_strategy.send_keys(command)
    type_strategy.clean()

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

    for neu_type in neu_types:
        print(neu_type.text)
        if neu_type.text == neu:
            neu_type.click()
            break

    decay_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "decay"))
        )

    decay_element.clear()
    decay_element.send_keys(decay)
    time.sleep(1)

    trunc_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "truncation"))
        )
    trunc_element.clear()
    trunc_element.send_keys(trunc)
    time.sleep(1)

    apply = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button--lg"))
        )
    apply.click()
    time.sleep(1)

# %%
def search_settings(command, neutralizations, decays, truncations):
    '''
    Returns:
        results[(command, neu, decay, trunc)] = {'sharpe': 1.27, ...}
    '''

    pass

# %%
def dump_to_csv(results):
    pass

# %%
def automation(args):

    driver_path = args.driver_path
    url = args.url
    neutralizations = args.neutralizations
    decays = args.decays
    truncations = args.truncations

    driver = webdriver.Chrome(driver_path)
    to_simulate(driver, url)

    commands = get_commands()
    results = {}
    for command in commands:
        ret = search_settings(command, neutralizations, decays, truncations)
        results.update(ret)
    
    dump_to_csv(results)

# %%
if __name__ == '__main__':
    args = get_args()
    automation(args)