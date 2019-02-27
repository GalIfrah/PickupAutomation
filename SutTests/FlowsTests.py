import unittest
from builtins import print

from App import PageObjects
from App.PageObjects import *
from Infrastructure.BasicTest import BasicTestClass
from Services.ErrorService import ErrorsHandler


class FlowsTestsClass(BasicTestClass, unittest.TestCase):

    def test_100_sanity(self):

            Connect.login()

            Wallet.addCreditCard()

            Wallet.closeWallet()

            HomePage.startOrder(config['HOME_PAGE']['DATA']['TEST_BUSINESS'])

            GenericPO.webDriver.saveScreenShot(1, self.testName)

            Menu.chooseFirstCategory()

            Menu.chooseSecondItem()

            Menu.moveToCart()

            cart_total = Menu.getTotalPrice()

            Menu.clickOnProceedToCheckout()

            if Checkout.getErrorPopup() is not None:

                if config['CHECKOUT_SCREEN']['TEXTS']['EXCEEDED_PICKUP_TIME_TEXT'] in Checkout.getErrorPopupText():

                                Checkout.clickOnPopUpOkBtn()

            Checkout.clickOnSubmitOrder()

            Checkout.Pass4DigitsPin()

            confirmation_header_text = ConfirmationScreen.getConfirmationText()

            assert confirmation_header_text == config['CONFIRMATION_SCREEN']['TEXTS']['CONFIRMATION_TEXT']

            confirmation_total_price = ConfirmationScreen.getTotalPrice()

            assert cart_total == confirmation_total_price, ErrorsHandler.TOTAL_PRICE_ERROR

            ConfirmationScreen.clickOnDone()

            GenericPO.webDriver.remoteWebDriver.back()

            Account.clickOnHistory()

            history_order_price = History.getHistoryOrderPriceByIndex(order_index=0)

            assert history_order_price == confirmation_total_price, ErrorsHandler.WRONG_HISTORY_TOTAL

# cards list locator is different
    def test_100_sanity_with_missing_card(self):

            Connect.login()

            HomePage.startOrder(config['HOME_PAGE']['DATA']['TEST_BUSINESS'])

            Menu.chooseFirstCategory()

            Menu.chooseSecondItem()

            Menu.moveToCart()

            cart_total = Menu.getTotalPrice()

            Menu.clickOnProceedToCheckout()

            if Checkout.getErrorPopup() is not None:

                        if config['CHECKOUT_SCREEN']['TEXTS']['EXCEEDED_PICKUP_TIME_TEXT'] in Checkout.getErrorPopupText():

                                Checkout.clickOnPopUpOkBtn()

            Checkout.clickOnSubmitOrder()


            if Checkout.getErrorPopup() is not None:
                        if config['CHECKOUT_SCREEN']['TEXTS']['PROVIDE_PAYMENT_FOR_CHECKOUT_TEXT'] in Checkout.getErrorPopupText():

                                Checkout.clickOnPopUpOkBtn()

                                Checkout.clickOnManagePaymentMethod()

                                Wallet.addCreditCardFromCheckout()

                                Wallet.closeWallet()

                                if Checkout.getErrorPopup() is not None:

                                        if config['CHECKOUT_SCREEN']['TEXTS']['EXCEEDED_PICKUP_TIME_TEXT'] in Checkout.getErrorPopupText():

                                                Checkout.clickOnPopUpOkBtn()

            Checkout.clickOnSubmitOrder()

            Checkout.Pass4DigitsPin()

            confirmation_header_text = ConfirmationScreen.getConfirmationText()

            assert confirmation_header_text == config['CONFIRMATION_SCREEN']['TEXTS']['CONFIRMATION_TEXT']

            confirmation_total_price = ConfirmationScreen.getTotalPrice()

            assert cart_total == confirmation_total_price, ErrorsHandler.TOTAL_PRICE_ERROR

            ConfirmationScreen.clickOnDone()

            GenericPO.webDriver.back()

            Account.clickOnHistory()

            history_order_price = History.getHistoryOrderPriceByIndex(order_index=0)

            assert history_order_price == confirmation_total_price, ErrorsHandler.WRONG_HISTORY_TOTAL
