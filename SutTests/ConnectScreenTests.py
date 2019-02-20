import unittest
from App import PageObjects
from App.PageObjects import *
from Services.ErrorService import ErrorsHandler
from Infrastructure.BasicTest import BasicTestClass


class ConnectTests(BasicTestClass, unittest.TestCase):

    def test_100_registration(self):

        Connect.register()

        current_login_button_text = HomePage.getLoginButtonText()

        before_login_button_text = config['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        assert current_login_button_text != before_login_button_text

    def test_101_login(self):

        # login
        Connect.login()

        current_login_button_text = HomePage.getLoginButtonText()

        before_login_button_text = config['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        assert current_login_button_text != before_login_button_text

    def test_102_logout(self):

        # login
        Connect.login()

        current_login_button_text = HomePage.getLoginButtonText()

        before_login_button_text = config['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        assert current_login_button_text != before_login_button_text

        # logout
        Connect.logout()

        current_login_button_text = HomePage.getLoginButtonText()

        assert current_login_button_text == before_login_button_text

    def test_103_checkMigration(self):
        pass
