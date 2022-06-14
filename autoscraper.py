#!/usr/bin/env python
# coding: utf-8

# In[3]:


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

#chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

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

#driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# In[2]:


driver.get("https://www.foi.gov.ph/requests")


# In[3]:


dataset = []
while True:
    all_div = driver.find_elements(By.CSS_SELECTOR, ".mb10")
    if len(dataset) >= 3000:
        break
    for div in all_div:
        data={}
        data ['agency'] = div.find_element(By.TAG_NAME, 'span').text
        data ['date'] = div.find_element(By.TAG_NAME, 'p').get_attribute('title')
        data ['title'] = div.find_element(By.TAG_NAME, 'h4').text
        data ['status'] = div.find_element(By.TAG_NAME, 'label').text
        data ['purpose'] = div.find_elements(By.TAG_NAME, 'span')[2].text
        data ['period_covered'] = div.find_elements(By.TAG_NAME, 'span')[3].text
        data ['link'] = div.find_element(By.TAG_NAME, 'a').get_attribute('href')
        dataset.append(data)
    
    driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[2]/div/div/div/a").click()


# In[ ]:


df = pd.DataFrame(dataset)


# In[ ]:


timestr = time.strftime("%Y%m%d-%H%M%S")
datamatrix= [[1,2,3],[1,2,3],[1,2,3]]
x=pd.DataFrame(datamatrix)  
df.to_csv(fr'output/foi{timestr}.csv',encoding="utf-8", index=False, header=True)

