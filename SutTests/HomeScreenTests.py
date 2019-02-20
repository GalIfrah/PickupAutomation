# from SutTests.TestsClassesInit import *
import unittest
from App import PageObjects
from App.PageObjects import *
from Services.ErrorService import ErrorsHandler
from Infrastructure.BasicTest import BasicTestClass
from pytest_testconfig import config


class HomeScreenTestsClass(BasicTestClass, unittest.TestCase):

        def test_100_openSut(self):

            current_app_link = HomePage.getSutUrl()

            if BasicTestClass.env == 'test':

                expected_app_url = config['SUT']['TEST']

            elif BasicTestClass.env == 'prod':

                expected_app_url = config['SUT']['PROD']
            HomePage.clickOnCookPolicyBtn()
            assert current_app_link == expected_app_url

        @unittest.skipIf(config['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'] == 0,
                         reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
        def test_101_checkBusinessLink(self):

            HomePage.clickOnCookPolicyBtn()

            current_app_link_text = HomePage.getAppLinkText()

            expected_app_link_text = config['HOME_PAGE']['TEXTS']['BACK_TO_APP_HEADER_LINK_TEXT']

            self.assertEqual(current_app_link_text, expected_app_link_text, 'not match')

        def test_102_getInputsPlaceHolders(self):

            inputs_place_holders = HomePage.getInputsPlaceHolder()

            self.assertEqual(inputs_place_holders[0], config['HOME_PAGE']['TEXTS']['SELECT_LOCATION_PLACE_HOLDER_TEXT'],
                             'LOCATION_PLACE_HOLDERS_NOT_EQUALS')
            self.assertEqual(inputs_place_holders[1], config['HOME_PAGE']['TEXTS']['SELECT_DATE_PLACE_HOLDER_TEXT'],
                             'DATE_PLACE_HOLDERS_NOT_EQUALS')
            self.assertEqual(inputs_place_holders[2], config['HOME_PAGE']['TEXTS']['SELECT_TIME_PLACE_HOLDER_TEXT'],
                             'TIME_PLACE_HOLDERS_NOT_EQUALS')

        def test_103_CheckInputsWithData(self):

            HomePage.clickOnCookPolicyBtn()

            HomePage.chooseLocation()

        def test_104_checkLocationList(self):

            Connect.login()

            locations_list = HomePage.getLocationsList()

            expected_location_number = 0

            for location in locations_list:
                assert location.text == config['HOME_PAGE']['DATA']['FULL_LOCATIONS_NAMES'][expected_location_number]

                expected_location_number += 1

        def test_105_connectButton(self):

            HomePage.clickOnCookPolicyBtn()

            HomePage.clickOnConnect()

            assert EnterPhonePage.getPhoneFieldElement().is_displayed() is True

        def test_106_footerText(self):

            HomePage.clickOnCookPolicyBtn()

            current_footer_text = HomePage.getFooterTxt()[0]

            expected_footer_text = config['HOME_PAGE']['TEXTS']['FOOTER_FIRST_PART_TEXT']

            self.assertEqual(current_footer_text, expected_footer_text, ErrorsHandler.TEXT_IS_WRONG)
