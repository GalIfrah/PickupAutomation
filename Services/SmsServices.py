import time

from selenium.webdriver.common.by import By

from Infrastructure.GenericPageObject import GenericPO


SMS_PROVIDER_SITE = "http://receive-smss.com/"
PHONE_NUMBER_LOCATOR = "//*[@id='content']/div[1]/div/div/div/div[1]/div[2]/div/h4"
PHONE_NUMBER_BUTTON = "//*[@id='content']/div[1]/div/div/div/div[1]/div[3]/div/a"
SMS_TEXT_LOCATOR_LIST = "//*[@id='content']/div/div/div/div/div/div/div/div/table/tbody/tr/td[2]"


class SmsService(GenericPO):


    def __init__(self):
        pass

    @staticmethod
    def getFirstAvailableNumber():

        GenericPO.webDriver.executeScript("window.open('');")

        GenericPO.webDriver.switchToWindow(1)

        GenericPO.webDriver.openSut(SMS_PROVIDER_SITE)

        phone_number = GenericPO.webDriver.findElementBy(PHONE_NUMBER_LOCATOR, By.XPATH).text

        GenericPO.webDriver.switchToWindow(0)

        return phone_number

    @staticmethod
    def getSmsCode():

        time.sleep(3)

        GenericPO.webDriver.findElementBy(PHONE_NUMBER_BUTTON, By.XPATH).click()

        received_sms_list = GenericPO.webDriver.findELementsBy(SMS_TEXT_LOCATOR_LIST, By.XPATH)

        received_sms_text = received_sms_list[0].text

        sms_code = received_sms_text[received_sms_text.index(": ") + 2:received_sms_text.index(" t")]

        GenericPO.webDriver.switchToWindow(0)

        return sms_code



