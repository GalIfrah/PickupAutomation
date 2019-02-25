# from SutTests.TestsClassesInit import *
import unittest

import pytest

from App import PageObjects
from App.PageObjects import *
from Infrastructure.BasicTest import BasicTestClass
from Services.ErrorService import ErrorsHandler
from pytest_testconfig import config


class WalletTestsClass(BasicTestClass, unittest.TestCase):


    def test_100_openWallet(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        wallet_section = GenericPO.webDriver.waitForVisibilityOfElem(config['WALLET']['LOCATORS']['CARDS_SECTION'])

        assert wallet_section is not None , "sdas"

    def test_101_addPaymentMethod_first(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        # add first card
        Wallet.addCreditCard()

        number_of_cards = Wallet.getUserCardsNumber()

        if config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
            assert number_of_cards == 1

        if config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0:
            assert number_of_cards == 1

    def test_102_getUserPayments(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        # validation for card
        current_default_card_text = Wallet.getUserCardsList()[0].text

        if config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
            current_default_card_text = Wallet.getUserCardsList()[1].text

        expected_default_card_text = config['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']

        assert current_default_card_text == expected_default_card_text

    def test_103_validateDefaultCard(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        number_of_cards = Wallet.getUserCardsList()

        default_card_vmark = None

        if config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0 and len(number_of_cards) > 1:

            try:
                default_card_vmark = Wallet.getUserCardsList()[1].find_element_by_xpath(config['WALLET']['LOCATORS']
                                                                                      ['DEFAULT_CARD_V_MARK'])
            except NoSuchElementException as e:
                pytest.fail(e.msg)
                # self.fail(ErrorsHandler.ELEMENT_NOT_VISIBLE)

        if config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0 and number_of_cards[0].text == \
                config['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']:

            try:
                default_card_vmark = Wallet.getUserCardsList()[0].find_element_by_xpath(config['WALLET']['LOCATORS']
                                                                                      ['DEFAULT_CARD_V_MARK'])
            except NoSuchElementException:
                pytest.fail(e.msg)
                # self.fail(ErrorsHandler.ELEMENT_NOT_VISIBLE)

        else:
            print('USER_HAS_NO_CARDS')

        assert default_card_vmark is not None

    def test_104_CheckInputsValidation(self):
        # ask for value attributes
        pass

    def test_105_checkUnsupportedCard(self):
        pass

    def test_106_checkCancelCcEntering(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        Wallet.clickOnCcCancelButton()

        assert Wallet.clickOnCcCancelButton() is False

    def test_107_checkCancelApplyButtonsText(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        apply_button_text = Wallet.getCcApplyButtonText()

        assert apply_button_text == config['WALLET']['TEXTS']['APPLY_BUTTON_TEXT']

        cancel_button_text = Wallet.getCcCancelButtonText()

        assert cancel_button_text, config['WALLET']['TEXTS']['CANCEL_BUTTON_TEXT']

    def test_108_deleteCard(self):

        Connect.login()

        Wallet.addCreditCard()

        num_of_cards_before_delete = Wallet.getUserCardsNumber()

        Wallet.clickOnDeleteCardButton()

        Wallet.clickOnDeleteYes()

        time.sleep(1)

        num_of_cards_after_delete = Wallet.getUserCardsNumber()

        assert num_of_cards_before_delete > num_of_cards_after_delete

        # add validation for success popup text & view

    def test_109_checkWalletHeader(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        wallet_header = Wallet.getWalletHeader()

        assert wallet_header == config['WALLET']['TEXTS']['WALLET_HEADER_TEXT'], "WALLET_HEADERS_NOT_EQUALS"

    def test_110_checkWeAcceptText(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        we_accepted_card_text = Wallet.getWeAcceptCardsText()

        assert we_accepted_card_text == config['WALLET']['TEXTS']['ACCEPTED_CARDS_TEXT'], "WE_ACCEPT_TEXT_IS_WRONG"

    def test_111_checkSupportedCardsImages(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        accepted_cards = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(
            config['WALLET']['LOCATORS']['WALLET_ACCEPTED_CARDS_AREA'])

        accepted_cards_len = len(accepted_cards)

        assert accepted_cards_len == 4, ErrorsHandler.MISSING_SUPPORTED_CARDS

        accepted_cards_url = []

        cards_name = ["visa", "amex", "maestro", "mastercard"]

        for card in accepted_cards:
            accepted_cards_url.append(card.get_attribute('src'))

        i = 0

        for word in cards_name:
            print(accepted_cards_url[i])
            assert word in accepted_cards_url[i] is True, 'word not exist'
            i += 1

    def test_112_checkFooterText(self):

        Connect.login()

        Account.clickOnPaymentMethods()

        pci_footer_text = Wallet.getPciFooterText()

        assert pci_footer_text == config['WALLET']['TEXTS']['PCI_FOOTER_TEXT'], ErrorsHandler.TEXT_IS_WRONG

    def test_113_checkAddCardInputsHeaders(self):
        pass

    def test_114_openWalletFromCheckout(self):
        pass
