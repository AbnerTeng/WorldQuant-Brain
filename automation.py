# %%
from curses import KEY_BACKSPACE
import email
from email import header
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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import argparse
import csv
from generate_commands import stage2_test

# %%
def hover(driver, element):
    hov = ActionChains(driver).move_to_element(element).perform()

# %%
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--driver_path', required=True, type=str)
    parser.add_argument('-u', '--url', default='https://platform.worldquantbrain.com/sign-in', type=str)
    parser.add_argument('-n', '--neutralizations', required=True, type=str, nargs='+')
    parser.add_argument('--decays', required=True, type=int, nargs='+')
    parser.add_argument('-t', '--truncations', required=True, type=float, nargs='+')
    parser.add_argument('--your_email', required = True, type = str)
    parser.add_argument('--your_password', required = True, type = str)
    parser.add_argument('-c', '--csv', required=True, type=str)
    args = parser.parse_args()
    return args 

# %%

def to_simulate(driver, url, your_email, your_password):
    driver.get(url)

    Accept = driver.find_element(By.CLASS_NAME, 'button--primary')
    Accept.click()

    ## login

    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )

    email.send_keys(your_email)
    password.send_keys(your_password)
    password.submit()

    time.sleep(6)

    # Skip = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "introjs-skipbutton"))
    # )
    Skip = driver.find_element(By.CLASS_NAME, "introjs-skipbutton")
    Skip.click()

    ## go to the simulate page
    Simulate = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "header__img--simulate"))
    )
    Simulate.click()

    time.sleep(5)
    Skip = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "introjs-skipbutton"))
    )
    Skips = driver.find_elements(By.CLASS_NAME, "introjs-skipbutton")
    assert(len(Skips) == 1)
    Skip = Skips[0]
    Skip.click()

# %%
def get_commands() -> list:
    commands = stage2_test()a
    return commands

# %%
def simulate(driver, command, neu, decay, trunc):
    '''
    return sharpe, turnover, etc...
    '''

    # %%
    settings = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "editor-top-bar-left__settings-btn"))
    )
    settings = driver.find_elements(By.CLASS_NAME, "editor-top-bar-left__settings-btn")[1]
    settings.click()

    neutralization = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "neutralization"))
    )
    neutralization.click()

    neu_types = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "select-portal__item"))
    )
    neu_types = driver.find_elements(By.CLASS_NAME, "select-portal__item")

    for neu_type in neu_types:
        if neu_type.text == neu:
            neu_type.click()
            break

    decay_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "decay"))
    )

    for _ in range(3):
        decay_element.send_keys(Keys.BACK_SPACE)
    decay_element.send_keys(f'{decay}')

    trunc_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "truncation"))
    )
    for _ in range(5):
        trunc_element.send_keys(Keys.BACK_SPACE)
    trunc_element.send_keys(f'{trunc}')

    apply = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button--lg"))
    )
    apply.click()

    # click simulate & save results
    alpha = driver.find_element(By.CLASS_NAME, "inputarea")
    alpha.send_keys(command)

    simulate_buttons = driver.find_elements(By.CLASS_NAME, "editor-simulate-button-text--is-code")
    assert(len(simulate_buttons) == 1)
    simulate_button = simulate_buttons[0]

    while True:
        try:
            simulate_button.click()
            break
        except:
            continue

    #progress = driver.find_element(By.CLASS_NAME, "progress")
    progress = WebDriverWait(driver, 30).until(
       EC.presence_of_element_located((By.CLASS_NAME, 'progress'))
    )

    while progress.text != '100%':
        ##time.sleep(1)
        print(progress.text)
        progress = driver.find_element(By.CLASS_NAME, 'progress')

    for _ in range(len(command)):
       alpha.send_keys(Keys.BACK_SPACE)

    return

    ## "editor-tabs__tab-dot--completed"
    ## "editor-tabs__tab-dot--new"
# %%
    # %%
    # time.sleep(30)
    try:
        Pass = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sumary__testing-checks-PASS-list"))
        )
        Pass = driver.find_element(By.CLASS_NAME, "sumary__testing-checks-PASS-list")

        pass_toggle = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sumary__testing-checks-icon--PASS-down"))
        )
        pass_toggle = driver.find_element(By.CLASS_NAME, 'sumary__testing-checks-icon--PASS-down')
        
        pass_toggle.click()
        pass_lines = []
        pass_text = Pass.text
        pass_lines += pass_text.split('\n')
        print(pass_lines)

    except:
        print('Pass fail')

    time.sleep(0.1)
    try:
        # Fail = WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "sumary__testing-checks-Fail-list"))
        # )
        Fail = driver.find_element(By.CLASS_NAME, 'sumary__testing-checks-FAIL-list')
        
        # fail_toggle = WebDriverWait(driver, 60).until(
            # EC.presence_of_element_located((By.CLASS_NAME, "sumary__testing-checks-icon--FAIL-down"))
        # )
        fail_toggle = driver.find_element(By.CLASS_NAME, 'sumary__testing-checks-icon--FAIL-down')
        fail_toggle.click()
        # print('wait list')
        
        fail_lines = []
        fail_text = Fail.text
        fail_lines += fail_text.split('\n')
        print(fail_lines)

    except:
        print('Fail fail')
    # %%

    if len(pass_lines) == 6:
        # check = driver.find_element(By.CLASS_NAME, 'editor-button__text')
        check = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "editor-button__text"))
        )
        check.click()

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

        information = {
            'sharpe': float(sharpe),
            'turnover': float(turnover[:-1]),
            'subsharpe': float(subsharpe),
            'fitness': float(fitness),
            'weight': weight,
            'corr': float(corr)
        }

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

        information = {
            'sharpe': float(sharpe),
            'turnover': float(turnover[:-1]),
            'subsharpe': float(subsharpe),
            'fitness': float(fitness),
            'weight': weight,
            'corr': -1
        }

    for _ in range(len(command)):
        alpha.send_keys(Keys.BACK_SPACE)
    
    return information

def stop_criterion(information):
    if information['sharpe'] < 1:
        return False
    if information['fitness'] < 0.8:
        return False
    return True

# %%
def search_settings(driver, command, neutralizations, decays, truncations):
    '''
    Returns:
        results[(command, neu, decay, trunc)] = {'sharpe': 1.27, ...}
    '''

    results = {}
    run_neu = [True for _ in range(len(neutralizations))]
    for decay in decays:
        for trunc in truncations:
            for i, neu in enumerate(neutralizations):
                # if run_neu[i]:
                simulate(driver, command, neu, decay, trunc)
                    # information = simulate(driver, command, neu, decay, trunc)
                    # results[(command, neu, decay, trunc)] = information
                    # run_neu[i] = stop_criterion(information)

    # return results
    return

# %%
def dump_to_csv(results, csv_file):
    with open(csv_file, 'a') as f:
        writer = csv.writer(f)
        print(results)
        for key, values in results.items():
            command, neu, decay, trunc = key
            sharpe    = values['sharpe']
            fitness   = values['fitness']
            turnover  = values['turnover']
            weight    = values['weight']
            subsharpe = values['subsharpe']
            corr      = values['corr']

            row = [
                command, neu, decay, trunc, sharpe,
                fitness, turnover, weight, subsharpe, corr
            ]
            writer.writerow(row)

# %%
def automation(args):

    driver_path = args.driver_path
    url = args.url
    neutralizations = args.neutralizations
    decays = args.decays
    truncations = args.truncations
    csv_file = args.csv

    driver = webdriver.Chrome(driver_path)
    to_simulate(driver, url, args.your_email, args.your_password)

    commands = get_commands()
    results = {}

    # write header
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        header = [
            'command', 'neutralization', 'decay', 'truncation',
            'sharpe', 'fitness', 'turnover', 'weight',
            'subsharpe', 'correlation'
        ]
        writer.writerow(header)

    for command in commands:
        # ret = search_settings(driver, command, neutralizations, decays, truncations)
        search_settings(driver, command, neutralizations, decays, truncations)
        # dump_to_csv(ret, csv_file)
        # results.update(ret)
    
    # print(results)

# %%
if __name__ == '__main__':
    args = get_args()
    automation(args)