#!/usr/bin/env python
# coding: utf-8

# # Philippines' Freedom of Information website scraper and analysis
# 
# **(Data from September 2016-January 19 and ongoing)**
# 
# Below scrapes and processes requests data from the Philippines' Freedom of Information website **(www.foi.gov.ph)** and combining the same with an **existing file** of **older FOI requests from 2016.** 
# 
# The goal is to create a single database of these requests (which we will do in a separate notebook) and analyze them such as:
# 
# Which agency received the most number of requests?
# 
# How many requests had been denied/approved?
# 
# What type of requests are most common?
# 
# Some background: The FOI website is in compliance with Executive Order No. 2, Series of 2016 by President Rodrigo Duterte that institutionalized freedom of information in the Executive branch of government.

# ## Do your imports

# In[1]:


import pandas as pd

import time
import requests
import re
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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

from bs4 import BeautifulSoup


# In[2]:


driver.get("https://www.foi.gov.ph/requests")


# Note: That is the part of the website supposedly containing all FOI requests.

# ## Start locating and isolating elements
# 
# Some methods are:
# 
# By.TAG
# 
# By.CLASS_NAME
# 
# By.ID
# 
# By.XPATH
# 
# By.CSS_SELECTOR

# In[3]:


tabs = driver.find_elements(By.CLASS_NAME, "col-xxs-12 col-xs-12 col-sm-8")


# Used **BeautifulSoup** on this part just because I want to clearly see the elements I need to **isolate**.

# In[4]:


my_url = "https://www.foi.gov.ph/requests"
foi_html = requests.get(my_url).content
#print(type(foi_html))
#print(foi_html)

#foi_list = BeautifulSoup(foi_html, "html.parser")
#print(type(foi_list))
#print(foi_list.prettify())


# ## Actual scraping

# Now comes the main part: interacting with the pages and setting Selenium to scrape each page. We then put scraped information in a **list of dictionaries** and then into a **single data frame.** 
# 
# Kudos to my friend, Vincent, for some help in using **CSS_SELECTOR** as a locator since I'm not familiar with it.

# In[5]:


dataset = []
while True:
    try:
        print('Reading a page')
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".col-xxs-12.col-xs-12.col-sm-8"))
        )
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


# ## Generate your (first) data frame
# 
# This is now all pandas.

# So, some caveats:
# 
# First, the **ALL REQUESTS** tab apparently only contains data for about the past 40 or so days (in this case from **December 7, 2021**). Hence, we can only scrape until that level-- that represent only or **about 6%** of what the website says as **"93,373 requests"**.

# In[6]:


df = pd.DataFrame(dataset)
df


# In[7]:


df.to_csv("foi2.csv", index=False)
pd.read_csv("foi2.csv")

