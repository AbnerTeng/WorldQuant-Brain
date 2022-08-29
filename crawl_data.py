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
import csv


def to_alpha(driver, url, your_email, your_password):
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

    ## go to the alpha page
    Alpha = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "header__img--alpha"))
    )
    Alpha.click()

    time.sleep(5)
    Skip = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "introjs-skipbutton"))
    )
    Skips = driver.find_elements(By.CLASS_NAME, "introjs-skipbutton")
    assert(len(Skips) == 1)
    Skip = Skips[0]
    Skip.click()

def select_columns(driver):
    select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'table__select-columns '))
    )
    select.click()

    _ = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'checkbox'))
    )

    checkbox = driver.find_elements(By.CLASS_NAME, 'checkbox')
    for checkboxes in checkbox:
        if checkboxes.text in ['Decay', 'Neutralization', 'Truncation', 'Fitness']:
            checkboxes.click()
    
    apply = driver.find_elements(By.CLASS_NAME, 'button--primary')[1]
    apply.click()


def crawl_data():

    url = 'https://platform.worldquantbrain.com/sign-in'
    driver_path = './chromeDriver'
    email = 'your_email'
    password = 'your_password'
    csv_file = './test.csv'

    driver = webdriver.Chrome(driver_path)
    to_alpha(driver, url, email, password)

    date = '08/27/2022 EDT'

    '''
    * alphas-list-table__cell-content--dateCreated
    * alphas-list-table__cell-content--decay
    * alphas-list-table__cell-content--neutralization
    * alphas-list-table__cell-content--truncation
    * alphas-list-table__cell-content--sharpe
    * alphas-list-table__cell-content--returns
    * alphas-list-table__cell-content--turnover
    * alphas-list-table__cell-content--fitness
    '''

    crawl_terms = [
        'alphas-list-table__cell-content--dateCreated',
        'alphas-list-table__cell-content--decay',
        'alphas-list-table__cell-content--neutralization',
        'alphas-list-table__cell-content--truncation',
        'alphas-list-table__cell-content--sharpe',
        'alphas-list-table__cell-content--returns',
        'alphas-list-table__cell-content--turnover',
        'alphas-list-table__cell-content--fitness'
    ]

    select_columns(driver)

    information = {}

    # find the first page containing {date}
    while True:
        page_information = {}
        for crawl_term in crawl_terms:
            _ = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, crawl_term))
            )
            elements =  driver.find_elements(By.CLASS_NAME, crawl_term)
            page_information[crawl_term] = [element.text for element in elements]
        
        # print(page_information)
        print('first loop')
        # footer__buttons footer__buttons-next footer__buttons-active
        # Next = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div/div/div[1]/div/div[2]/div/div[2]/button[2]")
        Next = driver.find_element(By.CLASS_NAME, 'footer__buttons-next')
        print('[Next]', Next.text)
        Next.click()
        time.sleep(5)
        print(page_information['alphas-list-table__cell-content--dateCreated'][-1])
        if page_information['alphas-list-table__cell-content--dateCreated'][-1] == date:
            information = page_information
            break

    print(information)

    while True:
        page_information = {}
        for crawl_term in crawl_terms:
            _ = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, crawl_term))
            )
            elements =  driver.find_elements(By.CLASS_NAME, crawl_term)
            page_information[crawl_term] = [element.text for element in elements]
        for key in page_information:
            information[key] += page_information[key]
        
        print('second loop')
        Next = driver.find_element(By.CLASS_NAME, 'footer__buttons-next')
        Next.click()
        time.sleep(5)
        if page_information['alphas-list-table__cell-content--dateCreated'][-1] != date:
            break

    print(information)

    # write header
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        header = [
            'date', 'decay', 'neutralization', 'truncation',
            'sharpe', 'returns', 'turnover', 'fitness'
        ]
        writer.writerow(header)

        num_rows = len(information['alphas-list-table__cell-content--dateCreated'])
        for i in range(num_rows):
            date = information['alphas-list-table__cell-content--dateCreated'][i]
            decay = information['alphas-list-table__cell-content--decay'][i]
            neutralization = information['alphas-list-table__cell-content--neutralization'][i]
            truncation = information['alphas-list-table__cell-content--truncation'][i]
            sharpe = information['alphas-list-table__cell-content--sharpe'][i]
            returns = information['alphas-list-table__cell-content--returns'][i]
            turnover = information['alphas-list-table__cell-content--turnover'][i]
            fitness = information['alphas-list-table__cell-content--fitness'][i]

            row = [
                date, decay, neutralization, truncation,
                sharpe, returns, turnover, fitness
            ]
            writer.writerow(row)


if __name__ == '__main__':
    crawl_data()