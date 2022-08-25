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


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--driver_path', required=True, type=str)
    parser.add_argument('-u', '--url', required=True, type=str)
    parser.add_argument('-n', '--neutralizations', required=True, type=str, nargs='+')
    parser.add_argument('--decays', required=True, type=int, nargs='+')
    parser.add_argument('-t', '--truncations', required=True, type=float, nargs='+')
    args = parser.parse_args()
    return args


def to_simulate(driver, url):
    pass


def get_commands() -> list:
    pass


def search_settings(command, neutralizations, decays, truncations):
    '''
    Returns:
        results[(command, neu, decay, trunc)] = {'sharpe': 1.27, ...}
    '''
    pass


def dump_to_csv(results):
    pass


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


if __name__ == '__main__':
    args = get_args()
    automation(args)