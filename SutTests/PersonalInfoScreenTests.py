import unittest
from App import PageObjects
from App.PageObjects import *
from Infrastructure.BasicTest import BasicTestClass
from Services.ErrorService import ErrorsHandler


class PersonalInformationTestsClass(BasicTestClass, unittest.TestCase):

    def test_100_openPersonalInformationScreen(self):

        Connect.login()

        Account.clickOnAccountInformation()

        assert AccountInformation.getPersonalInfoModal() is not None, ErrorsHandler.ELEMENT_IS_NONE
