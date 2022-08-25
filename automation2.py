import email
from enum import auto
from unittest import result
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
import csv


HEDAERS = ['command', '']

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--driver_path', required=True, type=str)
    parser.add_argument('-u', '--url', required=True, type=str)
    parser.add_argument('-n', '--neutralizations', required=True, type=str, nargs='+')
    parser.add_argument('--decays', required=True, type=int, nargs='+')
    parser.add_argument('-t', '--truncations', required=True, type=float, nargs='+')
    parser.add_argument('-c', '--csv', required=True, type=str)
    args = parser.parse_args()
    return args


def to_simulate(driver, url):
    pass


def get_commands() -> list:
    pass


def simulate(driver, command, neu, decay, trunc):
    '''
    return sharpe, turnover, etc.
    '''


    pass


def search_settings(driver, command, neutralizations, decays, truncations):
    '''
    Returns:
        results[(command, neu, decay, trunc)] = {'sharpe': 1.27, ...}
    '''

    results = {}
    for neu in neutralizations:
        for decay in decays:
            for trunc in truncations:
                results[(command, neu, decay, trunc)] = simulate(driver, command, neu, decay, trunc)
    
    return results


def dump_to_csv(results, csv_file):
    with open(csv_file, 'a') as f:
        writer = csv.writer(f)
        for key, values in results:
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


def automation(args):

    driver_path = args.driver_path
    url = args.url
    neutralizations = args.neutralizations
    decays = args.decays
    truncations = args.truncations
    csv_file = args.csv

    driver = webdriver.Chrome(driver_path)

    # %%
    to_simulate(driver, url)

    commands = get_commands()
    # [ts_mean(close, 5), ts_mean(close, 6), ...]
    results = {}

    # %%
    for command in commands:
        ret = search_settings(command, neutralizations, decays, truncations)
        results.update(ret)
    
    # %%
    dump_to_csv(results, csv_file)


if __name__ == '__main__':
    args = get_args()
    automation(args)