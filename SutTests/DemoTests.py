import unittest
from Services.BrowserStackService import browserStack
from App import PageObjects
from App.PageObjects import *
from Services.ErrorService import ErrorsHandler
from Services.SmsServices import *


class DemoTestsClass(BasicTestClass, unittest.TestCase):


        def test_100_sanity(self):

            Connect.login()

            HomePage.startOrder(2)

            GenericPO.webDriver.saveScreenShot(1, self.testName)

            Menu.chooseFirstCategory()


"""
    @unittest.skipIf(params['MENU']['DATA']['AMOUNT_LIMIT'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_101_checkOrderItemLimit(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseFirstCategory()

        for i in range(params['MENU']['DATA']['AMOUNT_LIMIT_NUMBER'] + 1):

            Menu.chooseSecondItem()

            if i <= params['MENU']['DATA']['AMOUNT_LIMIT_NUMBER'] - 1:
             Menu.clickOnMenuToast()

        moreThenSixPopUpText = Menu.getPopupText()

        self.assertEqual(moreThenSixPopUpText, params['MENU']['TEXTS']['MORE_THEN_6_POP_UP_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)



    @unittest.skipIf(params['MENU']['DATA']['AGE_LIMIT'] == 0,
                     reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP + ' ' + BasicTestClass.appName)
    def test_102_checkAgeRestriction(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseRestrictedAgeCategory()

        popupHeaderText = Menu.getPopupHeaderText()

        self.assertEqual(popupHeaderText, params['MENU']['TEXTS']['ALCOHOL_RESTRICTION_HEADER_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)

        popupBodyText = Menu.getPopupText()

        self.assertEqual(popupBodyText, params['MENU']['TEXTS']['ALCOHOL_RESTRICTION_BODY_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)

        Menu.clickOnPopupOkBtn()

        self.assertTrue(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath(
            params['MENU']['DATA']['AGE_PASSING_INDICATOR']).is_displayed(), ErrorsHandler.ELEMENT_NOT_VISIBLE)


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



class DemoTestsClass2(BasicTestClass, unittest.TestCase):


    def test_100_sanity(self):

            Connect.login()

            # Wallet.addCreditCard()
            #
            # Wallet.closeWallet()

            HomePage.startOrder(2)

            GenericPO.webDriver.saveScreenShot(1, self.testName)

            Menu.chooseFirstCategory()

            Menu.chooseSecondItem()

            Menu.moveToCart()

            cartTotal = Menu.getTotalPrice()

            Menu.clickOnProceedToCheckout()


            if Checkout.getErrorPopup() is not None:

                   errorPopUpText = Checkout.getErrorPopupText()

                   if params['CHECKOUT_SCREEN']['TEXTS']['EXCEEDED_PICKUP_TIME_TEXT'] in errorPopUpText:

                          Checkout.clickOnPopUpOkBtn()


            Checkout.clickOnSubmitOrder()

            Checkout.Pass4DigitsPin()

            confirmationHeaderText = ConfirmationScreen.getConfirmationText()

            self.assertEqual(confirmationHeaderText, params['CONFIRMATION_SCREEN']['TEXTS']['CONFIRMATION_TEXT'])


            confirmationTotalPrice = ConfirmationScreen.getTotalPrice()

            self.assertEqual(cartTotal, confirmationTotalPrice, ErrorsHandler.TOTAL_PRICE_ERROR)

            ConfirmationScreen.clickOnDone()

            GenericPO.webDriver.remoteWebDriver.back()

            Account.clickOnHistory()

            historyOrderPrice = History.getHistoryFirstOrderPrice()

            self.assertEqual(historyOrderPrice, confirmationTotalPrice, ErrorsHandler.WRONG_HISTORY_TOTAL)

            # try:
            #     self.assertEqual(historyOrderPrice, confirmationTotalPrice, ErrorsHandler.WRONG_HISTORY_TOTAL)
            #
            # except AssertionError:
            #     browserStack.changeTestStatus(self, "Error", ErrorsHandler.WRONG_HISTORY_TOTAL)
            """

