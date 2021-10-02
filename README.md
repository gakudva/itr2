# Indian Income tax - online ITR 2 form section 112 update script 
##Background
Filing Indian Income tax returns for Assessment year 2021-2022 has to be done using the new portal https://www.incometax.gov.in/iec/foportal.  The portal is refurbished new, very usefriendly.  However had many teething problems.  One of the issues you will find is to update section 112A information.  In Section 112A, you have to submit Captial Gains related transactions.  This data entry can get very complicated if you have grand fathered captital gains.  

To make life easy, most of the brokerages provide you their own Excel files that contain all necessary information that can be used for data entry.  Usually, you will have hundred or more lines of data.  Manual entry of this data into the portal is cumbersom, and also can lead to many errors.  The portal does provide a CSV upload option - however, as of today its buggy and throws random errors for any CSV file that has more than 5 lines.

In this repository, you will find a pytest script that makes use of Selenium to update the section 112A from CSV.  This script has been tested on my own personal data.  Hope you will find it useful.

##Pre-requisites
- Python 3 
-- Check if your PC has python 3 by entering command "python3 --version" 
-- if you do not have it already, download and install it from https://www.python.org/downloads/
- pytest
-- Check if your PC has pytest by entering command "pytest --version"
-- if you do not have it already, install it using instructions here: https://docs.pytest.org/en/6.2.x/getting-started.html
- Selenium
- if you do not have it already, install selenium web driver and chrome driver using instructions here: https://pypi.org/project/selenium/
