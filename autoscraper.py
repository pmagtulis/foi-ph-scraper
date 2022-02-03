#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

import time
import re

import warnings
warnings.filterwarnings("ignore")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# In[2]:


driver.get("https://www.foi.gov.ph/requests")


# In[3]:


dataset = []
while True:
    try:
        tabs = driver.find_elements(By.CSS_SELECTOR, ".col-xxs-12.col-xs-12.col-sm-8")
        for tab in tabs:
            try:
                all_div = tab.find_elements(By.CSS_SELECTOR, '.component-panel')
            except:
                break
            for div in all_div[1:]:
                data={}
                data ['agency'] = div.find_element(By.TAG_NAME, 'span').text
                data ['date'] = div.find_element(By.TAG_NAME, 'p').get_attribute('title')
                data ['title'] = div.find_element(By.TAG_NAME, 'h4').text
                data ['status'] = div.find_element(By.TAG_NAME, 'label').text
                data ['purpose'] = div.find_elements(By.TAG_NAME, 'span')[2].text
                data ['period_covered'] = div.find_elements(By.TAG_NAME, 'span')[3].text
                data ['link'] = div.find_element(By.TAG_NAME, 'a').get_attribute('href')
                dataset.append(data)
    except:
        break

    try:
        driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/div/div/a").click()
    except:
        print("Nothing more.")
        break


# In[4]:


df = pd.DataFrame(dataset)
df


# In[5]:


timestr = time.strftime("%Y%m%d-%H%M%S")
datamatrix= [[1,2,3],[1,2,3],[1,2,3]]
x=pd.DataFrame(datamatrix)  
df.to_csv(output/fr'foi{timestr}.csv',encoding="utf-8", index=False, header=True)

