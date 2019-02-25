# from SutTests.TestsClassesInit import *
import unittest
from App import PageObjects
from App.PageObjects import *
from Infrastructure.BasicTest import BasicTestClass
from Services.ErrorService import ErrorsHandler


class EnterPhoneTestsClass(BasicTestClass, unittest.TestCase):


    def test_100_wrongSmsCode(self):

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()

        EnterPhonePage.submitPhoneNumber()

        EnterPhonePage.enterWrongSmsCode()

        EnterPhonePage.submitSmsCode()

        wrong_sms_pop_up = EnterPhonePage.getPopup()

        assert wrong_sms_pop_up is not None, ErrorsHandler.MISSING_POPUP

        popup_text = EnterPhonePage.getPopupText()

        assert popup_text == config['ENTER_PHONE_PAGE']['TEXTS']['WRONG_SMS_POPUP_TEXT'], ErrorsHandler.WRONG_POPUP_TEXT

    def test_101_resendCode(self):

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber(phone_number=SmsService.getFirstAvailableNumber())

        EnterPhonePage.submitPhoneNumber()

        EnterPhonePage.clickOnResendCode()

        resend_sms_pop_up = EnterPhonePage.getPopup()

        assert resend_sms_pop_up is not None, ErrorsHandler.MISSING_POPUP

        resend_sms_pop_up_text = EnterPhonePage.getPopupText()

        assert resend_sms_pop_up_text == config['ENTER_PHONE_PAGE']['TEXTS']['RESEND_CODE_POPUP_TEXT'], ErrorsHandler.WRONG_POPUP_TEXT


