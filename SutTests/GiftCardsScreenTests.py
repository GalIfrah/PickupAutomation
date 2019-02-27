import unittest
from App import PageObjects
from App.PageObjects import *
from Infrastructure.BasicTest import BasicTestClass
from Services.ErrorService import ErrorsHandler


class GiftCardsTestsClass(BasicTestClass, unittest.TestCase):

    def test_100_openGiftCardsScreen(self):

        Connect.login()

        Account.clickOnGiftCards()

        time.sleep(3)
