# from SutTests.TestsClassesInit import *
import unittest
from builtins import print
from App import PageObjects
from App.PageObjects import *
from Infrastructure.BasicTest import BasicTestClass
from Services.ErrorService import ErrorsHandler
from pytest_testconfig import config


class MenuTestsClass(BasicTestClass, unittest.TestCase):

    def test_100_chooseCategory(self):

        HomePage.startOrder(2)

        Menu.chooseSecondCategory()

        self.assertTrue(Menu.checkIfCategoryChosen() is True, ErrorsHandler.ELEMENT_NOT_VISIBLE)

    @unittest.skipIf(config['MENU']['DATA']['AGE_LIMIT'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_101_checkAgeRestriction(self):

        HomePage.startOrder(2)

        Menu.chooseRestrictedAgeCategory()

        popup_header_text = Menu.getPopupHeaderText()

        assert popup_header_text == config['MENU']['TEXTS']['ALCOHOL_RESTRICTION_HEADER_TEXT']

        popup_body_text = Menu.getPopupText()

        assert popup_body_text == config['MENU']['TEXTS']['ALCOHOL_RESTRICTION_BODY_TEXT']

        Menu.clickOnPopupOkBtn()

        assert GenericPO.webDriver.remoteWebDriver.find_element_by_xpath(
            config['MENU']['DATA']['AGE_PASSING_INDICATOR']).is_displayed() is True

    @unittest.skipIf(config['MENU']['DATA']['AMOUNT_LIMIT'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_102_checkOrderItemLimit(self):

        HomePage.startOrder(2)

        for i in range(config['MENU']['DATA']['AMOUNT_LIMIT_NUMBER'] + 1):
                Menu.chooseSecondItem()

        more_then_six_text = Menu.getPopupText()

        assert more_then_six_text == config['MENU']['TEXTS']['MORE_THEN_6_POP_UP_TEXT']

    @unittest.skipIf(config['MENU']['LOCATORS']['UP_SALE_ITEM'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_103_checkUpsSales(self):

        HomePage.startOrder(2)

        Menu.chooseUpSaleItem()

        up_sale_text = Menu.getUpSalePopupText()

        assert up_sale_text == config['MENU']['TEXTS']['UP_SALE_POPUP_TEXT']

    def test_104_openAndCloseModifiersModal(self):

        HomePage.startOrder(2)

        Menu.chooseSecondItem()

        # open modal
        Menu.clickOnEditItem()

        assert Menu.getModifiersModal() is not None

        # close modal
        Menu.closeModifiersWindow()

        assert Menu.getModifiersModal() is not None

    @unittest.skipIf(config['MENU']['DATA']['MODIFIERS'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    def test_105_checkModifiersSelection(self):

        HomePage.startOrder(2)

        Menu.clickOnEditItem()

        list = Menu.getModifiersBySection()

        for modifier in list:

            modifier.click()

            assert Menu.checkModifierActivity(modifier) is True

            if list.index(modifier) == (config['MENU']['DATA']['SECOND_CATEGORY_MODIFIERS_LIMIT'] - 1):
                break

    def test_106_addItemToCart(self):

        HomePage.startOrder(2)

        cart_items_number_before_adding = len(Menu.getCartItemsList())

        # assert cart items list size before & after adding the item
        self.assertTrue(cart_items_number_before_adding == 0, ErrorsHandler.CART_DOES_NOT_EMPTY)

        Menu.chooseSecondItem()

        cart_items_number_after_adding = len(Menu.getCartItemsList())

        assert cart_items_number_after_adding == 1 is True

        # assert items name
        item_name = Menu.getSecondItemText()

        cart_item_name = str.upper(Menu.getCartSecondItemText())

        assert item_name == cart_item_name

    def test_107_deleteItemFromCart(self):

        HomePage.startOrder(2)

        Menu.chooseSecondItem()

        cart_items_number_before_delete = len(Menu.getCartItemsList())

        # assert cart items list size before & after deleting the item
        assert cart_items_number_before_delete == 1 is True

        Menu.deleteItemFromCart()

        cart_items_number_after_a_delete = len(Menu.getCartItemsList())

        assert cart_items_number_after_a_delete == 0 is True

