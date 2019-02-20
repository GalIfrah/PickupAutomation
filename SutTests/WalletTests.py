import unittest
from App import PageObjects
from App.PageObjects import *
from Services.ErrorService import ErrorsHandler


class WalletTestsClass(BasicTestClass, unittest.TestCase):


    def test_100_openWallet(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        walletSection = GenericPO.webDriver.waitForVisibilityOfElem(params['WALLET']['LOCATORS']['CARDS_SECTION'])

        self.assertIsNotNone(walletSection, ErrorsHandler.ELEMENT_IS_NONE)

    def test_101_addPaymentMethod_first(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        # add first card
        Wallet.addCreditCard()

        numberOfCards = Wallet.getUserCardsNumber()

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
            self.assertEqual(numberOfCards, 1, str(1 - numberOfCards) + ErrorsHandler.MISSING_CARDS)

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0:
            self.assertEqual(numberOfCards, 1, str(1 - numberOfCards) + ErrorsHandler.MISSING_CARDS)

    def test_102_getUserPayments(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        # validation for card
        currentDefaultCardText = Wallet.getUserCardsList()[0].text

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
            currentDefaultCardText = Wallet.getUserCardsList()[1].text

        expectedDefaultCardText = params['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']

        self.assertEqual(currentDefaultCardText, expectedDefaultCardText, ErrorsHandler.TEXT_IS_WRONG)

    def test_103_validateDefaultCard(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        numberOfCards = Wallet.getUserCardsList()

        defaultCardVmark = None

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0 and len(numberOfCards) > 1:

            try:
                defaultCardVmark = Wallet.getUserCardsList()[1].find_element_by_xpath(params['WALLET']['LOCATORS']
                                                                                      ['DEFAULT_CARD_V_MARK'])
            except NoSuchElementException:
                self.fail(ErrorsHandler.ELEMENT_NOT_VISIBLE)

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0 and numberOfCards[0].text == \
                params['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']:

            try:
                defaultCardVmark = Wallet.getUserCardsList()[0].find_element_by_xpath(params['WALLET']['LOCATORS']
                                                                                      ['DEFAULT_CARD_V_MARK'])
            except NoSuchElementException:
                self.fail(ErrorsHandler.ELEMENT_NOT_VISIBLE)

        else:
            print('USER_HAS_NO_CARDS')

        self.assertIsNotNone(defaultCardVmark, ErrorsHandler.CARD_IS_NOT_DEFAULT)


    def test_104_CheckInputsValidation(self):
        # ask for value attributes
        pass

    def test_105_checkUnsupportedCard(self):
        pass

    def test_106_checkCancelCcEntering(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        Wallet.clickOnCcCancelButton()

        self.assertFalse(Wallet.clickOnCcCancelButton(), "CANCEL_BUTTON_ISN'T_CLICKED")

    def test_107_checkCancelApplyButtonsText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        applyButtonText = Wallet.getCcApplyButtonText()

        self.assertEqual(applyButtonText, params['WALLET']['TEXTS']['APPLY_BUTTON_TEXT'], "BUTTON_TEXT_IS_WRONG")

        cancelButtonText = Wallet.getCcCancelButtonText()

        self.assertEqual(cancelButtonText, params['WALLET']['TEXTS']['CANCEL_BUTTON_TEXT'], "BUTTON_TEXT_IS_WRONG")

    def test_108_deleteCard(self):

        HomePage.openSut()

        Connect.login()

        Wallet.addCreditCard()

        numOfCardsBeforeDelete = Wallet.getUserCardsNumber()

        Wallet.clickOnDeleteCardButton()

        Wallet.clickOnDeleteYes()

        time.sleep(1)
        numOfCardsAfterDelete = Wallet.getUserCardsNumber()

        self.assertGreater(numOfCardsBeforeDelete, numOfCardsAfterDelete, 'CARD_NOT_DELETED')

        # add validation for success popup text & view

    def test_109_checkWalletHeader(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        walletHeader = Wallet.getWalletHeader()

        self.assertEqual(walletHeader, params['WALLET']['TEXTS']['WALLET_HEADER_TEXT'], "WALLET_HEADERS_NOT_EQUALS")

    def test_110_checkWeAcceptText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        weAcceptedCardText = Wallet.getWeAcceptCardsText()

        self.assertEqual(weAcceptedCardText, params['WALLET']['TEXTS']['ACCEPTED_CARDS_TEXT'],
                         "WE_ACCEPT_TEXT_IS_WRONG")

    def test_111_checkSupportedCardsImages(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        acceptedCards = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(
            params['WALLET']['LOCATORS']['WALLET_ACCEPTED_CARDS_AREA'])

        acceptedCardsLen = len(acceptedCards)

        self.assertEqual(acceptedCardsLen, 4, ErrorsHandler.MISSING_SUPPORTED_CARDS)

        acceptedCardsUrl = []

        words = ["visa", "amex", "maestro", "mastercard"]

        for card in acceptedCards:
            acceptedCardsUrl.append(card.get_attribute('src'))

        i = 0

        for word in words:
            print(acceptedCardsUrl[i])
            self.assertTrue(word in acceptedCardsUrl[i], 'word not exist')
            i += 1

    def test_112_checkFooterText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        pciFooterText = Wallet.getPciFooterText()

        self.assertEqual(pciFooterText, params['WALLET']['TEXTS']['PCI_FOOTER_TEXT'], ErrorsHandler.TEXT_IS_WRONG)

    def test_113_checkAddCardInputsHeaders(self):
        pass

    def test_114_openWalletFromCheckout(self):
        pass
