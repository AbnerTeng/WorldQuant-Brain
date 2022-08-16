# %%
import email
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--disable-notifications')

driver = webdriver.Chrome('/Users/abnerteng/GitHub/WorldQuant-Brain/chromeDriver', chrome_options = options)
driver.get('https://platform.worldquantbrain.com/sign-in')
## driver.close()

# %%
from selenium.webdriver.common.by import By

email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'password')

your_email = 'abnerteng16@gmail.com'
your_password = 'teng1234'

email.send_keys(your_email)
password.send_keys(your_password)
password.submit()


# %%
Simulate = driver.find_element(By.CLASS_NAME, 'header__img--simulate')
Simulate.click()
# %%
