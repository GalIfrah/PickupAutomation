import time
from builtins import print

from selenium.webdriver.common.by import By

from Infrastructure.GenericPageObject import GenericPO


# SMS_PROVIDER_SITE = "http://receive-smss.com/"
# PHONE_NUMBER_LOCATOR = "//*[@id='content']/div[1]/div/div/div/div[1]/div[2]/div/h4"
# PHONE_NUMBER_BUTTON = "//*[@id='content']/div[1]/div/div/div/div[1]/div[3]/div/a"
# SMS_TEXT_LOCATOR_LIST = "//*[@id='content']/div/div/div/div/div/div/div/div/table/tbody/tr/td[2]"

SMS_PROVIDER_SITE = "https://receive-sms.com/"
PHONE_NUMBER_LOCATOR = "/html/body/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/b/a"
PHONE_NUMBER_BUTTON = "/html/body/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/b/a"
SMS_TEXT_LOCATOR_LIST = "//*[@id='messages-table']/tbody/tr/td[4]"


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

        return "+" + phone_number

    @staticmethod
    def getSmsCode():

        time.sleep(6)

        GenericPO.webDriver.findElementBy(PHONE_NUMBER_BUTTON, By.XPATH).click()

        time.sleep(2)

        received_sms_list = GenericPO.webDriver.findElementsBy(SMS_TEXT_LOCATOR_LIST, By.XPATH)

        received_sms_text = received_sms_list[0].text

        sms_code = received_sms_text[received_sms_text.index(": ") + 2:received_sms_text.index(" t")]

        GenericPO.webDriver.switchToWindow(0)

        return sms_code

