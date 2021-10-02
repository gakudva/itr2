import pytest

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from time import sleep
import sys
import csv

def test_automate_112a():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://eportal.incometax.gov.in/iec/foservices/#/login')
    sleep(15)

    #Enter User ID
    chrome_driver.find_element_by_id("panAdhaarUserId").click()
    chrome_driver.find_element_by_id("panAdhaarUserId").send_keys("<YOURPAN>")
    chrome_driver.find_element_by_id("panAdhaarUserId").send_keys(Keys.ENTER)
    sleep(5)

    #select the Checkbox "Please confirm your secure access message"
    chrome_driver.find_element_by_css_selector(".mat-checkbox-inner-container").click()

    #select Password field, and wait for user input to be supplied by 15 seconds and then press enter
    chrome_driver.find_element_by_id("loginPasswordField").click()
    sleep(15)
    chrome_driver.find_element_by_id("loginPasswordField").send_keys("")
    chrome_driver.find_element_by_id("loginPasswordField").send_keys(Keys.ENTER)
    sleep(5)


    #Click on generate OTP, press Continue
    chrome_driver.find_element_by_css_selector("#mat-radio-3 .mat-radio-label-content").click()
    chrome_driver.find_element_by_css_selector(".large-button-primary > .marRight4").click()

    #agree to use Aadhar, and click on requesting OTP
    chrome_driver.find_element_by_css_selector(".mat-checkbox-inner-container").click()
    chrome_driver.find_element_by_css_selector(".large-button-primary").click()
    #insert OTP -> manual input
    sleep(25)
    chrome_driver.find_element_by_css_selector(".large-button-primary").click()
    sleep(10)

    #click on "File Now"
    chrome_driver.find_element_by_css_selector(".defaultButton").click()
    sleep(5)

    #Select Assessment year as 2021-2022
    chrome_driver.find_element_by_css_selector("#filterStyleForChip\\ myPanelClassItr .mat-select-value").click()
    chrome_driver.find_element_by_xpath("//span[contains(text(),'(Current A.Y.)')]").click()
    #click on "Select mode of filing as online"
    chrome_driver.find_element_by_css_selector("#mat-radio-5 .A-Gross-Total-Income").click()
    #click on Continue
    chrome_driver.find_element_by_css_selector(".large-button-primary > span:nth-child(1)").click()
    sleep(3)

    #click on Resume Filing
    chrome_driver.find_element_by_css_selector(".col-md-3:nth-child(4) .primaryButton").click()
    sleep(3)

    #click on Continue
    chrome_driver.find_element_by_css_selector("#uniservenxtcmp_button_152 > span").click()
    sleep(3)

    #click on Continue on Note pop-up
    chrome_driver.find_element_by_id("uniservenxtcmp_button_373").click()

    #click "Skip the questions" on proceed to scheduled questions
    chrome_driver.find_element_by_id("uniservenxtcmp_hyper_12").click()
    sleep(3)

    #click OK on pop-up box
    chrome_driver.find_element_by_id("uniservenxtcmp_button_246").click()

    #click on 112A
    chrome_driver.find_element_by_css_selector("#uniservenxtcmp_list_111 .bluebrbg").click()
    sleep(3)

    #open CSV vile
    with open('112a.csv', mode='r')as file:
        csvFile = csv.reader(file)

        for lines in csvFile:
            #click +Add Another button
            chrome_driver.find_element_by_id("uniservenxtcmp_button_23").click()
            sleep(3)
            #Add a transaction
            chrome_driver.find_element_by_id("select2-uniservenxtcmp_dropdown_41-container").click()
            chrome_driver.find_element_by_xpath("//body[1]/span[1]/span[1]/span[2]/ul[1]/li[2]").click()
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_10").clear()
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_10").send_keys(lines[1])
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_11").clear()
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_11").send_keys(lines[2])
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_12").clear()
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_12").send_keys(lines[3])
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_13").clear()
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_13").send_keys(lines[4])
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_14").clear()
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_14").send_keys(lines[5])
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_15").clear()
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_15").send_keys(lines[6])
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_17").clear()
            chrome_driver.find_element_by_id("uniservenxtcmp_textbox_17").send_keys(lines[7])
            chrome_driver.find_element_by_id("uniservenxtcmp_button_19").click()
            sleep(3)
            #end loop

    sys.stderr.write("Success")
    #wait for manual save, confirm and logoff
    sleep(250)

    chrome_driver.close()
