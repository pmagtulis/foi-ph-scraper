# foi-ph-scraper
An automatic scraper for the Freedom of Information portal of the Philippine government.

**Data from publicly available records from December 7, 2021 onwards**

# Recent updates
|column name|definition|
|---|---|
|*Jan 20*|overhauled the file to upload only a Python file (not Jupyter Notebook); removed the analysis part and activated an auto-scraper every Sunday| 

# What is this?

This code scrapes requests data from the Philippines' [Freedom of Information website](www.foi.gov.ph). We use a Python code as well to automatically scrape the
website for new information **every Sunday** and saves that new file into a CSV **(this component currently being polished)**.

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

1. Using Selenium, we scraped one part of the FOI website which contains a live list of [requests](www.foi.gov.ph/requests). We specifically scraped 
the contents of the tab labeled "ALL REQUESTS." Below is a screenshot of that page and an example of how each requests data is structured:

<center><img width="681" alt="Screen Shot 2022-01-15 at 6 31 50 PM" src="https://user-images.githubusercontent.com/87161563/149641061-726ec0c6-1f68-4ddc-b4a5-ad01f4e132f5.png"></center>

2. We put all scraped information in a single data frame for processing through pandas.

3. We made some initial analysis while the project is constantly **evolving and being developed.**

4. Raw scraped files are then saved into CSV format.

# Definition of terms

The following information were scraped from the website (labeled as in the **df**)

|column name|definition|
|---|---|
|**agency**|the name of the government agency where the request was submitted| 
|**date**|date when request was made through the FOI portal|
|**status**|shows at which stage of the FOI process is the file request in. Examples are "SUCCESSFUL", "PARTIALLY SUCCESSFUL", "DENIED", etc.|
|**date**|date when request was made through the FOI portal|  
|**period_covered**|a required information when filing a request meant to serve as filter for the extent of period covered by each request|
|**purpose**|the purpose why the request is being made, typically indicating how the data will be used. This is required when filing an FOI request|     
|**link**|hyperlink to each FOI request, containing details and direct messages between the filer and agency concerned|

# Next steps

1. After running this code and getting the latest requests information from the FOI website, the entire file is saved into a CSV format. 

2. Proceed to the next notebook titled "foi-analysis" for next steps: including merging the data with older ones from another CSV file, courtesy of the PCOO,
which manages the website. The PCOO said they sometimes older remove requests data from the FOI website at the request of the filer. **It was not clear however
if the agency also conducts regular cleaning of the portal to remove aging files.**

3. As a result of limited data in the website, the message below appears upon reaching the end of the **"ALL REQUESTS"** tab which is the portion of the 
site scraped. The code is designed not to break even after this.

<img width="1200" alt="Screen Shot 2022-01-13 at 4 51 14 PM" src="https://user-images.githubusercontent.com/87161563/149607477-4a973191-86a5-4e68-8dfa-737bb1993697.png">

# Contact

Prinz Magtulis, [ppm2130@columbia.edu](mailto:ppm2130@columbia.edu)

**Comments and suggestions are always welcome! All rights reserved.**
