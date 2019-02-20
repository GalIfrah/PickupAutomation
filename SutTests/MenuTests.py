import unittest
# from SutTests.TestsClassesInit import *
# from builtins import print
from App import PageObjects
from App.PageObjects import *
from Services.ErrorService import ErrorsHandler


class MenuTestsClass(BasicTestClass, unittest.TestCase):

    def test_100_chooseCategory(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseSecondCategory()

        self.assertTrue(Menu.checkIfCategoryChosen() is True, ErrorsHandler.ELEMENT_NOT_VISIBLE)

    @unittest.skipIf(params['MENU']['DATA']['AGE_LIMIT'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_101_checkAgeRestriction(self):

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

    @unittest.skipIf(params['MENU']['DATA']['AMOUNT_LIMIT'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_102_checkOrderItemLimit(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        for i in range(params['MENU']['DATA']['AMOUNT_LIMIT_NUMBER'] + 1):
                Menu.chooseSecondItem()

        moreThenSixText = Menu.getPopupText()

        self.assertEqual(moreThenSixText, params['MENU']['TEXTS']['MORE_THEN_6_POP_UP_TEXT'], ErrorsHandler.TEXT_IS_WRONG)


    @unittest.skipIf(params['MENU']['LOCATORS']['UP_SALE_ITEM'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_103_checkUpsSales(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseUpSaleItem()

        upSaleText = Menu.getUpSalePopupText()

        self.assertEqual(upSaleText, params['MENU']['TEXTS']['UP_SALE_POPUP_TEXT'], ErrorsHandler.TEXT_IS_WRONG)

    def test_104_openAndCloseModifiersModal(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseSecondItem()

        # open modal
        Menu.clickOnEditItem()

        self.assertIsNotNone(Menu.getModifiersModal(), ErrorsHandler.ELEMENT_NOT_VISIBLE)

        # close modal
        Menu.closeModifiersWindow()

        self.assertIsNone(Menu.getModifiersModal(), ErrorsHandler.ELEMENT_EXIST)

    @unittest.skipIf(params['MENU']['DATA']['MODIFIERS'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_105_checkModifiersSelection(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.clickOnEditItem()

        list = Menu.getModifiersBySection()

        for modifier in list:

            modifier.click()

            self.assertTrue(Menu.checkModifierActivity(modifier), ErrorsHandler.ELEMENT_NOT_VISIBLE)

            if list.index(modifier) == (params['MENU']['DATA']['SECOND_CATEGORY_MODIFIERS_LIMIT'] - 1):
                break

    def test_106_addItemToCart(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        cartItemsNumberBeforeAdding = len(Menu.getCartItemsList())

        # assert cart items list size before & after adding the item
        self.assertTrue(cartItemsNumberBeforeAdding == 0, ErrorsHandler.CART_DOES_NOT_EMPTY)

        Menu.chooseSecondItem()

        cartItemsNumberAfterAdding = len(Menu.getCartItemsList())

        self.assertTrue(cartItemsNumberAfterAdding == 1, ErrorsHandler.CART_EMPTY)

        # assert items name
        itemName = Menu.getSecondItemText()

        cartItemName = str.upper(Menu.getCartSecondItemText())

        self.assertEqual(itemName, cartItemName, ErrorsHandler.TEXT_IS_WRONG)

    def test_107_deleteItemFromCart(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseSecondItem()

        cartItemsNumberBeforeDelete = len(Menu.getCartItemsList())

        # assert cart items list size before & after deleting the item
        self.assertTrue(cartItemsNumberBeforeDelete == 1, ErrorsHandler.CART_EMPTY)

        Menu.deleteItemFromCart()

        cartItemsNumberAfterADelete = len(Menu.getCartItemsList())

        self.assertTrue(cartItemsNumberAfterADelete == 0, ErrorsHandler.CART_DOES_NOT_EMPTY)

