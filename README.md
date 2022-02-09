# foi-ph-scraper
An automatic scraper for the Freedom of Information portal of the Philippine government.

# Recent updates
|column name|definition|
|---|---|
|*Feb 8*|linked this repositoryto directly push newly scraped information into [foi-analysis](https://github.com/pmagtulis/foi-analysis) repository for analysis|
|*Feb 4*|latest amendments scrape first 3,000 entries from the FOI website to avoid overloading. This was after the FOI website put back up older requests that date back to 2016, which were already removed from the site before.|
|*Jan 24*|resolved issues on scraper through the help of [jsoma's code](https://github.com/jsoma/selenium-github-actions). New CSV generated as of January 25 containing files from January 20 onwards.|
|*Jan 20*|overhauled the file to upload a Python file for auto scraping purposes; removed the analysis part and activated an auto-scraper every Sunday| 

# How to use this?

Follow the steps below. Each run of the autoscraper saves a new CSV file that contains 3,000 new entries from the FOI website. Since the website arranges requests
by latest date, it essentially scrapes new requests everytime it runs, with some allowance for older ones for merging purposes.

Download each CSV file from the **output** directory, and combine them with the larger dataset found at [foi-analysis](https://github.com/pmagtulis/foi-analysis) 
repository for processing. 

# What is this?

This code scrapes requests data from the Philippines' [Freedom of Information website](www.foi.gov.ph). We use a Python code as well to automatically scrape the
website for new information **every Sunday**.

The goal is to create a single database of these requests in a data frame and make some analysis out of them such as:

Which agency received the most number of requests?

How many requests had been denied/approved?

What type of requests are most common?

# FOI background

Launched in 2016, the FOI website is in compliance with Executive Order No. 2, Series of 2016 by President Rodrigo Duterte that institutionalized 
freedom of information in the Executive branch of government.

The portal is meant to be a one-stop shop where filers can file a request to all National Government agencies, government-owned and -controlled corporations,
as well state schools and colleges. The website allows the user to track developments of their request, chat with an **FOI officer** who handles the request,
and get feedback from them.

The legislative and judiciary branches of government, as well as the central bank, do not participate on the FOI portal, and have their own mechanisms for
public disclosures.

# The process

1. Using Selenium, we scrape 3,000 requests from the FOI website which contains a live list of [requests](www.foi.gov.ph/requests). We specifically scrape 
the contents of the tab labeled "ALL REQUESTS." Below is a screenshot of that page and an example of how each requests data is structured:

<center><img width="681" alt="Screen Shot 2022-01-15 at 6 31 50 PM" src="https://user-images.githubusercontent.com/87161563/149641061-726ec0c6-1f68-4ddc-b4a5-ad01f4e132f5.png"></center>

2. We put all scraped information in a single data frame for processing through pandas.

3. Raw scraped files are then saved into CSV format with a unique file name every Sunday.

4. The .yml file contains an automated push of the scraped file to the **foi-analysis** repository under the **output** directory. For that part of the code to
work, you would need to create a similar repository and directory, or you can just simply delete that part and just clone my [repository](https://github.com/pmagtulis/foi-analysis) analyzing the FOI requests data. Everything should be in there.

# Definition of terms

The following information were scraped from the website:

|column name|definition|
|---|---|
|**agency**|the name of the government agency where the request was submitted| 
|**date**|date when request was made through the FOI portal|
|**status**|shows at which stage of the FOI process is the file request in. Examples are "SUCCESSFUL", "PARTIALLY SUCCESSFUL", "DENIED", etc.|
|**date**|date when request was made through the FOI portal|  
|**period_covered**|a required information when filing a request meant to serve as filter for the extent of period covered by each request|
|**purpose**|the purpose why the request is being made, typically indicating how the data will be used. This is required when filing an FOI request|     
|**link**|hyperlink to each FOI request, containing details and direct messages between the filer and agency concerned. Only available for data from December 7, 2021|
|**reasons_denial**|a brief reason cited for a denial of request. Only available for data from 2016-December 31, 2021|

# Next steps

1. After running this code and getting the latest requests information from the FOI website, they are stored in a single file, CSV format. 

2. Proceed to the next notebook titled **"foi-analysis"** for next steps: including merging and cleaning the data with older ones from another CSV file, courtesy of 
the PCOO, which manages the website. The PCOO said they sometimes older remove requests data from the FOI website at the request of the filer. **It was not clear 
however if the agency also conducts regular cleaning of the portal to remove aging files.**

# Contact

Prinz Magtulis, [ppm2130@columbia.edu](mailto:ppm2130@columbia.edu)

**Comments and suggestions are always welcome! All rights reserved.**
