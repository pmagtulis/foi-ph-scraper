# foi-ph-scraper
A scraper for the Freedom of Information portal of the Philippine government.

**Data from publicly available records from December 7, 2021 onwards**

# What is this?

This code scrapes and processes requests data from the Philippines' [Freedom of Information website](www.foi.gov.ph). The goal is to create a single database of 
these requests in a data frame and make some analysis out of them such as:

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
|**filer**|the name of the filer of FOI request. Most often containing only the initials of the first name and entire last name|
|**agency**|the name of the government agency where the request was submitted| 
|**date**|date when request was made through the FOI portal|  
|**title**|title of the request (usually providing a brief indication of what type of information is being requested)|
|**purpose**|the purpose why the request is being made, typically indicating how the data will be used. This is required when filing an FOI request|     
|**link**|hyperlink to each FOI request, containing details and direct messages between the filer and agency concerned|

# Some caveats

1. While the primary intention on scraping the FOI website was to get as much information from it worthy of historical analysis, the ALL REQUESTS tab
however appeared to contain only data from **December 7, 2021** onwards. The website shows the photo below after reaching a certain page.

<img width="1200" alt="Screen Shot 2022-01-13 at 4 51 14 PM" src="https://user-images.githubusercontent.com/87161563/149607477-4a973191-86a5-4e68-8dfa-737bb1993697.png">

2. That said, there are three more tabs that filter according to **successful, pending and denied requests** which appear to have older data. Future project
may focus on scraping these tabs as well, and merging with the current data, while discounting potential duplicates.

# Contact

Prinz Magtulis, [ppm2130@columbia.edu](mailto:ppm2130@columbia.edu)

**Comments and suggestions are always welcome! All rights reserved.**
