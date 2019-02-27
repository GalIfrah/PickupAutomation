import unittest
from builtins import print

import pytest

from App import PageObjects
from App.PageObjects import *
from Infrastructure.BasicTest import BasicTestClass
from Services.ErrorService import ErrorsHandler


class DemoTestsClass(BasicTestClass, unittest.TestCase):

    # def test_109_logoOrderText(self):
    #     logo_order_text = HomePage.getLogoOrderText()
    #
    #     assert logo_order_text == config['HOME_PAGE']['TEXTS']['LOGO_TEXT_ORDER_TEXT'], ErrorsHandler.TEXT_IS_WRONG

    @pytest.mark.skipif(condition=config['HOME_PAGE']['DATA']['HAS_DATES_LIMIT'] is not True, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_109_supportText(self):

        HomePage.chooseLocation(config['HOME_PAGE']['DATA']['TEST_BUSINESS'])

        dates_list = HomePage.getDatesList()

        dates_values = []

        for date in dates_list:
            dates_values.append(date.text)

        if config['HOME_PAGE']['DATA']['HAS_DATES_LIMIT'] == 1:
            assert len(dates_values) == config['HOME_PAGE']['DATA'][
                'DATES_LIMIT_NUMBER'], ErrorsHandler.ABOVE_DATES_LIMIT

            assert dates_values[0] == config['HOME_PAGE']['DATA'][
                'DATES_LIMIT_VALUE'], ErrorsHandler.DATE_ON_LIST_IS_WRONG