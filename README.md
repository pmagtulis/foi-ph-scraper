# foi-ph-scraper
A scraper for the Freedom of Information portal of the Philippine government.

**Data from publicly available records from December 7, 2021 onwards**

# What is this?

This code scrapes and processes requests data from the Philippines' [Freedom of Information website](www.foi.gov.ph). The goal is to create a single 
database of these requests in a data frame and make some analysis out of them such as:

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
the tab labeled "ALL REQUESTS."

2. The following information were scraped from the website:

      a. The filer's name
      
      b. The name of the agency where the request was submitted
      
      c. Date of request
      
      d. Title of the request (usually providing a brief indication of what type of information is being requested)

      e. Purpose of the request
      
      f. Link to each request (which contains details and direct messages between the filer and agency concerned).

3. 
