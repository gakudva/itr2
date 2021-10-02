# Indian Income tax - online ITR 2 form Section 112A update script 
## Background
Filing Indian Income tax returns for Assessment year 2021-2022 has to be with new web portal https://www.incometax.gov.in/iec/foportal.  The portal is refurbished new, very user friendly.  However had many teething problems.  

One of the challenge is to update section 112A.  In 112A, you have to include Captial Gains transactions.  This data entry gets very complicated when there are grand fathered captital gains. To make life easy, most of the brokerages provide Excel files that contain all necessary information.  Usually, you will have hundred or more lines of data.  Manual entry into the portal is very cumbersom.  The portal provides a CSV upload option - however, its buggy and throws out random errors for when CSV file has more than 5 lines.

This repository contains a pytest script that updates the section 112A using a data from CSV. 

*Note:* the script only covers dealing with equity shares that were acquired "On or before 31st January 2018"; as they are the most cumbersom for data entry. 

## Pre-requisites
- Python 3 
  - Check if your PC has python 3 by entering command "python3 --version" 
  - if you do not have it already, download and install it from https://www.python.org/downloads/
- pytest
  - Check if your PC has pytest by entering command "pytest --version"
  - if you do not have it already, install it using instructions here: https://docs.pytest.org/en/6.2.x/getting-started.html
- Selenium
  - if you do not have it already, install selenium web driver and chrome driver using instructions here: https://pypi.org/project/selenium/

## Preparation
- Download the script itr2-112a.py into a directory on your PC
- Download the example CSV file 112a.csv into the same directory.  The CSV contains the following columns and are in the specific order:
  - Share/Unit acquired (1a)
  - ISIN Code(2)
  - Name of the Share/Unit(3)
  - No. of Shares/Units(4)
  - Sale-price per Share/Unit(5)
  - Cost of acquisition(8)
  - Fair Market Value per share/unit as on 31st January 2018(10)
  - Expenditure wholly and exclusively in connection with transfer(12)
- the CSV is just example content, change the content as per your personal data. Save the CSV with your data. 
- Prepare your tax returns
  -  Login to https://www.incometax.gov.in/iec/foportal
  -  Prepare your tax returns for Assessment year 2021 - 2022 -> Enter basic data and save draft.
## Executing the script
- edit the script itr2-112a.py
  - In line 20, replace USERNAME with your user name to the portal 
  - In line 30, replace PASSWORD with your passwork to the portal
  - If you dont updates the script; thats fine too.  But, when the test script is executing - you must quickly enter credentials in the browser.
  - the sleep timers in the scripts have been optimized as per the broadband internet speeds.  You may want to increase it if you have slow internet.
- execute the script usign command "pytest --verbose --capture=no itr2-112a.py
  - as soon as the script starts, a browser window is launched
  - Aadhar SMS OTP needs to be provided as asked by the browser
  - Rest of the data entry is automated
  - Once all the data is inserted, the script waits for 25 seconds -> in this time, click on Confirm Button and save the section 112A.  The Confirm step is not automated for safety reasons.
   
