from _pytest import config
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, NoSuchElementException
from Services.ErrorService import ErrorsHandler
from Services.utils import ProjectUtils
import logging
from Services.SmsServices import *
from pytest_testconfig import config


class Connect(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def register():

        Connect.login()

        EnterEmailPage.enterUnExistEmail()

        EnterEmailPage.submitEmail()

        FormPage.enterFullName()

        FormPage.enterPin()

        FormPage.enterDate()

        FormPage.chooseOptinTrue()

        FormPage.submitForm()

    @staticmethod
    def login():

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber(phone_number=SmsService.getFirstAvailableNumber())

        EnterPhonePage.submitPhoneNumber()

        EnterPhonePage.enterSmsCode()

        EnterPhonePage.submitSmsCode()

    @staticmethod
    def logout():

        Account.clickOnLogOut()

        Account.logOutYes()


class HomePage(GenericPO):


    @staticmethod
    def openSut(env):

        if env == 'test':
            GenericPO.webDriver.openSut(config['SUT']['TEST'])

        if env == 'prod':
            GenericPO.webDriver.openSut(config['SUT']['PROD'])

    @staticmethod
    def getSutUrl():
        text = GenericPO.webDriver.getCurrentUrl()

        return text

    @staticmethod
    def clickOnCookPolicyBtn():
        GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['COOKIES_POLICY_BTN'],
                                          By.XPATH).click()

    @staticmethod
    def getCookPolicyTxt():
        txt = GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['COOKIES_POLICY_BTN'],
                                                By.XPATH).text
        return txt

    @staticmethod
    def goToAppSite_header():
        GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'],
                                          By.XPATH).click()

    @staticmethod
    def getAppLinkText():
        app_link_text = GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'],
                                                          By.XPATH).text
        return app_link_text

    @staticmethod
    def clickOnConnect():
        GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['CONNECT_BTN'],
                                          By.ID).click()

    @staticmethod
    def getLoginConnectedButtonText():
        time.sleep(3)
        text = GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'],
                                                 By.XPATH).text
        return text

    @staticmethod
    def getLoginUnConectedButtonText():
        time.sleep(3)
        text = GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['CONNECT_BTN'],
                                          By.ID).text
        return text

    @staticmethod
    def getInputsPlaceHolder():
        place_holders = [
            GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_PLACE_HOLDER'],
                                              By.XPATH).text,
            GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['SELECT_DATE_PLACE_HOLDER'],
                                              By.XPATH).text,
            GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['SELECT_TIME_PLACE_HOLDER'],
                                              By.XPATH).text]
        return place_holders

    @staticmethod
    def chooseLocation():
        GenericPO.webDriver.selectFromDropDown(config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
                                               config['HOME_PAGE']['DATA']['SECOND_LOCATION'])

        time.sleep(2)

    @staticmethod
    def getLocationsList():
        locations_list = GenericPO.webDriver.getDropDownOptionsList(config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'])

        return locations_list

    @staticmethod
    def getTestLocation(locations_list, location_to_find):
        time.sleep(2)

        test_location = ''

        counter = 0

        for location in locations_list:

            if location.text == location_to_find:

                test_location = location.text

                break

                counter += 1

            elif location.text != location_to_find and counter == len(locations_list) - 1:

                assert False, ErrorsHandler.TEST_LOCATION_DOES_PNOT_EXIST + location_to_find + " " + location.text

        return test_location

    @staticmethod
    def chooseDate():
        GenericPO.webDriver.selectFromDropDown(config['HOME_PAGE']['LOCATORS']['SELECT_DATE_DROP_DOWN'],
                                               config['HOME_PAGE']['DATA']['TOMORROW'])

    @staticmethod
    def chooseTime():
        GenericPO.webDriver.selectFromDropDown(config['HOME_PAGE']['LOCATORS']['SELECT_TIME_DROP_DOWN'],

                                               config['HOME_PAGE']['DATA']['TIME'])

    # @staticmethod
    # def startOrder(test_location_number):
    #     if test_location_number == 1:
    #             GenericPO.webDriver.selectFromDropDown(config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
    #                                                    config['HOME_PAGE']['DATA']['FIRST_LOCATION_NOT_WORKING'])
    #
    #     if test_location_number == 2:
    #             time.sleep(1)
    #             GenericPO.webDriver.selectFromDropDown(config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
    #                                                    config['HOME_PAGE']['DATA']['SECOND_LOCATION'])
    #
    #
    #     time.sleep(2)
    #     GenericPO.webDriver.waitForElemToBeClickable(config['HOME_PAGE']['LOCATORS']['START_ORDER_BUTTON'])
    #
    #     time.sleep(3)
    #     if GenericPO.webDriver.getCurrentUrl() == config['MENU']['LOCATORS']['MENU_URL']:
    #                 pass
    #
    #
    #     elif HomePage.getStartOrderPopup() is not None:
    #
    #             if HomePage.getStartOrderPopup().text == config['HOME_PAGE']['TEXTS']['START_ORDER_CHOOSE_LOCATION_POPUP_TEXT']:
    #
    #                     HomePage.clickOnStartOrderPopupButton()
    #
    #                     HomePage.chooseLocation()
    #
    #                     HomePage.startOrder(1)
    #
    #             elif HomePage.getStartOrderPopup().text == config['HOME_PAGE']['TEXTS']['START_ORDER_TIME_EXCEEDED_POPUP_TEXT']:
    #
    #                     HomePage.clickOnStartOrderPopupButton()
    #
    #                     HomePage.startOrder(2)
    #
    #             elif HomePage.getStartOrderPopup().text == config['HOME_PAGE']['TEXTS']['START_ORDER_NOT_ACCEPTING_POPUP_TEXT']:
    #
    #                     HomePage.clickOnStartOrderPopupButton()
    #
    #                     HomePage.startOrder(2)
    #
    #             elif HomePage.getStartOrderPopup().text == config['HOME_PAGE']['TEXTS']['START_ORDER_SELECT_TIME_POPUP_TEXT']:
    #
    #                     HomePage.clickOnStartOrderPopupButton()
    #
    #                     HomePage.chooseLocation()
    #
    #                     HomePage.startOrder(2)
    @staticmethod
    def startOrder(location_to_order_from):
        time.sleep(1)
        founded_location = HomePage.getTestLocation(locations_list=HomePage.getLocationsList(), location_to_find=location_to_order_from)

        GenericPO.webDriver.selectFromDropDown(config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
                                               founded_location)

        time.sleep(2)
        GenericPO.webDriver.waitForElemToBeClickable(config['HOME_PAGE']['LOCATORS']['START_ORDER_BUTTON'])
        time.sleep(5)

    @staticmethod
    def startOrderWithErrors(location_to_order_from):
        time.sleep(1)
        founded_location = HomePage.getTestLocation(locations_list=HomePage.getLocationsList(),
                                                    location_to_find=location_to_order_from)

        GenericPO.webDriver.selectFromDropDown(config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
                                               founded_location)

        time.sleep(2)
        GenericPO.webDriver.waitForElemToBeClickable(config['HOME_PAGE']['LOCATORS']['START_ORDER_BUTTON'])


    @staticmethod
    def getStartOrderPopup():
        element = GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['START_ORDER_POPUP_TEXT_AREA'],
                                                    By.XPATH)
        return element

    @staticmethod
    def clickOnStartOrderPopupButton():
        GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['START_ORDER_POPUP_BUTTON'],
                                          By.XPATH).click()

    @staticmethod
    def clickOnTermsAndConditions():
        GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['TERMS_AND_COND_BUTTON'],
                                          By.XPATH).click()

    @staticmethod
    def ClIckOnPrivacyPolicy():
        GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['PRIVACY_POLICY'],
                                          By.XPATH).click()

    @staticmethod
    def getFooterTxt():

        footerTxts = [GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['FOOTER_FIRST_PART'],
                                                        By.XPATH).text,
                      GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['FOOTER_SECOND_PART'],
                                                        By.XPATH).text,
                      GenericPO.webDriver.findElementBy(config['HOME_PAGE']['LOCATORS']['FOOTER_THIRD_PART'],
                                                        By.XPATH).text]
        return footerTxts



class Account(GenericPO):



    @staticmethod
    def clickOnAccountInformation():
        GenericPO.webDriver.hoverAndClick(config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          config['HOME_PAGE']['LOCATORS']['ACCOUNT']['PERSONAL_INFO_BUTTON'])

    @staticmethod
    def clickOnPaymentMethods():
        time.sleep(3)
        # GenericPO.webDriver.waitForVisibilityOfElem(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])

        try:

            GenericPO.webDriver.hoverAndClick(config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                              config['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])
            time.sleep(1)

            wallet_section = GenericPO.webDriver.waitForVisibilityOfElem(config['WALLET']['LOCATORS']['CARDS_SECTION'])


            if wallet_section is None:
                GenericPO.webDriver.hoverAndClick(config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                                  config['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])
                time.sleep(1)

        except NoSuchElementException:
            logging.error(ErrorsHandler.WALLET_IS_NOT_VISIBLE)

    @staticmethod
    def clickOnGiftCards():
        GenericPO.webDriver.hoverAndClick(config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          config['HOME_PAGE']['LOCATORS']['ACCOUNT']['GIFT_CARDS'])

    @staticmethod
    def clickOnHistory():
        time.sleep(2)
        GenericPO.webDriver.hoverAndClick(config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          config['HOME_PAGE']['LOCATORS']['ACCOUNT']['HISTORY'])
        time.sleep(2)


    @staticmethod
    def clickOnLogOut():
        GenericPO.webDriver.hoverAndClick(config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          config['HOME_PAGE']['LOCATORS']['ACCOUNT']['LOG_OUT'])

    @staticmethod
    def logOutYes():
        GenericPO.webDriver.findElementBy(config['LOGOUT_SCREEN']['YES_BTN'], By.XPATH).click()

    @staticmethod
    def logOutNo():
        GenericPO.webDriver.findElementBy(config['LOGOUT_SCREEN']['NO_BTN']).click()



class AccountInformation(GenericPO):

    @staticmethod
    def getNameText():
        name_text = GenericPO.webDriver.findElementBy("//*[@id='modal-body']/div/div[1]/div/input",
                                                      By.XPATH).text
        return name_text



class History(GenericPO):

    @staticmethod
    def getHistoryList():

        history_list = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(config['HISTORY_SCREEN']['LOCATORS']['HISTORY_ORDERS_LIST'],
                                                                                  By.XPATH)
        return history_list


    @staticmethod
    def getHistoryFirstOrderPrice():

        history_list = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(
                                config['HISTORY_SCREEN']['LOCATORS']['HISTORY_ORDERS_LIST'])

        first_order_price = history_list[0].find_element_by_xpath(config['HISTORY_SCREEN']['LOCATORS']
                                                                    ['FIRST_ORDER_PRICE']).text

        return first_order_price



class EnterPhonePage(GenericPO):


    @staticmethod
    def getPhoneFieldElement():
        element = GenericPO.webDriver.findElementBy(config['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_FIELD'], By.XPATH)
        return element

    @staticmethod
    def enterValidPhoneNumber(phone_number):
        GenericPO.webDriver.findElementBy(config['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_FIELD'], By.XPATH).send_keys(phone_number)
        time.sleep(3)

    @staticmethod
    def submitPhoneNumber():
        GenericPO.webDriver.findElementBy(config['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_BUTTON'], By.XPATH).click()

        GenericPO.webDriver.switchToWindow(1)

    @staticmethod
    def getPopup():
        screen_popup = GenericPO.webDriver.waitForVisibilityOfElem(
            config['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP'])

        return screen_popup

    @staticmethod
    def getPopupText():
        screen_popup_text = GenericPO.webDriver.waitForVisibilityOfElem(
            config['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP_BODY']).text

        return screen_popup_text

    @staticmethod
    def clickOnPopupOkBtn():
        GenericPO.webDriver.waitForVisibilityOfElem(
            config['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP_OK']).click

    @staticmethod
    def enterSmsCode():
        # time.sleep(180)
        code = SmsService.getSmsCode()

        GenericPO.webDriver.switchToWindow(0)

        time.sleep(1)

        GenericPO.webDriver.findElementBy(config['ENTER_PHONE_PAGE']['LOCATORS']['ENTER_SMS_CODE'],
                                          By.XPATH).send_keys(code)

    @staticmethod
    def enterWrongSmsCode():

        rand_sms_code = ProjectUtils.createRandomSmsCode()

        GenericPO.webDriver.waitForVisibilityOfElem(config['ENTER_PHONE_PAGE']['LOCATORS']['ENTER_SMS_CODE']).send_keys(rand_sms_code)

    @staticmethod
    def submitSmsCode():
        GenericPO.webDriver.findElementBy(config['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_SMS_CODE'],
                                          By.XPATH).click()

        GenericPO.webDriver.waitForVisibilityOfElem(config['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'])

        #time.sleep(3)

    @staticmethod
    def clickOnResendCode():
        GenericPO.webDriver.findElementBy(config['ENTER_PHONE_PAGE']['LOCATORS']['RESEND_CODE'],
                                          By.XPATH).click()

    @staticmethod
    def getPhoneUsagesText():
        GenericPO.webDriver.findElementBy(config['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_USAGES_TEXT_AREA'],
                                          By.XPATH).text


class EnterEmailPage(GenericPO):

    @staticmethod
    def enterUnExistEmail():
        un_exist_email = ProjectUtils.createRandomMail()
        GenericPO.webDriver.findElementBy(config['ENTER_EMAIL_PAGE']['LOCATORS']['ENTER_EMAIL_FIELD'],
                                          By.XPATH).send_keys(un_exist_email)

    @staticmethod
    def submitEmail():
        GenericPO.webDriver.findElementBy(config['ENTER_EMAIL_PAGE']['LOCATORS']['SUBMIT_EMAIL_BUTTON'],
                                          By.XPATH).click()




class FormPage(GenericPO):


    @staticmethod
    def enterFullName():
        GenericPO.webDriver.findElementBy(config['FORM_PAGE']['LOCATORS']['FORM_FULL_NAME_FIELD'],
                                          By.XPATH).send_keys(
            config['FORM_PAGE']['DATA']['NAME'])

    @staticmethod
    def enterPin():
        GenericPO.webDriver.findElementBy(config['FORM_PAGE']['LOCATORS']['FORM_PIN_FIELD'],
                                          By.XPATH).send_keys(
            config['FORM_PAGE']['DATA']['PIN'])

    @staticmethod
    def enterDate():
        GenericPO.webDriver.findElementBy(config['FORM_PAGE']['LOCATORS']['FORM_DATE_FIELD'],
                                          By.XPATH).send_keys(
            config['FORM_PAGE']['DATA']['DATE'])

    @staticmethod
    def chooseOptinTrue():
        GenericPO.webDriver.findElementBy(config['FORM_PAGE']['LOCATORS']['FORM_OPTIN_TRUE'],
                                          By.XPATH).click()

    @staticmethod
    def submitForm():
        GenericPO.webDriver.findElementBy(config['FORM_PAGE']['LOCATORS']['FORM_SUBMIT_BUTTON'],
                                          By.XPATH).click()

        GenericPO.webDriver.waitForVisibilityOfElem(config['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'])
        # time.sleep(3)


class Wallet(GenericPO):

    @staticmethod
    def clickOnAddNewCard():
        if len(Wallet.getUserCardsList()) >= 1 and Wallet.getUserCardsList()[0].text == config['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

                    GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON'],
                                                      By.XPATH).click()

        if config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0 and Wallet.getUserCardsList()[0].text != config['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

                    GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'],
                                                      By.XPATH).click()

        # GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
        #                                  (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

    @staticmethod
    def getWalletHeader():
        wallet_header = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['WALLET_HEADER'],
                                                        config.XPATH).text
        return wallet_header

    @staticmethod
    def enterCcNumber():
        try:
            GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                               (config['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

            GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['CC_NUMBER_INPUT'],
                                              By.ID).send_keys(
                config['WALLET']['DATA']['FIRST_CARD_DETAILS']['VALID_CC_NUMBER'])

        except StaleElementReferenceException:
            print('stale element')

    @staticmethod
    def enterExpDate():
        GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['EXP_DATE_INPUT'],
                                          By.ID).send_keys(config['WALLET']['DATA']['FIRST_CARD_DETAILS']['EXP_DATE'])

    @staticmethod
    def enterCvc():
        GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['CVC_INPUT'],
                                          By.ID).send_keys(config['WALLET']['DATA']['FIRST_CARD_DETAILS']['CVC'])

    @staticmethod
    def enterPostalCode():
        GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['POSTCODE_INPUT'],
                                          By.ID).send_keys(config['WALLET']['DATA']['FIRST_CARD_DETAILS']['POSTCODE'])

    @staticmethod
    def clickOnCcApplyButton():
        GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['APPLY_BUTTON'],
                                          By.ID).click()
        GenericPO.webDriver.remoteWebDriver.switch_to.default_content()

        time.sleep(6)

    @staticmethod
    def getCcApplyButtonText():
        GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                           (config['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

        apply_button_text = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['APPLY_BUTTON'],
                                                            By.ID).text
        return apply_button_text

    @staticmethod
    def clickOnCcCancelButton():


        try:
            GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                               (config['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

            GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['CANCEL_BUTTON'],
                                              By.ID).click()
            GenericPO.webDriver.remoteWebDriver.switch_to.default_content()

        except WebDriverException:
            return False

    @staticmethod
    def getCcCancelButtonText():
        # GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
        #                                  (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

        cancel_button_text = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['CANCEL_BUTTON'],
                                                             By.ID).text
        return cancel_button_text

    @staticmethod
    def getUserCardsList():

        cardListElement = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['CARDS_SECTION'],
                                                            By.XPATH)

        cards = cardListElement.find_elements_by_tag_name(config['WALLET']['LOCATORS']['USER_CARDS'])

        return cards

    @staticmethod
    def getUserCardsNumber():

        card_list_element = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['CARDS_SECTION'],
                                                            By.XPATH)

        cards = card_list_element.find_elements_by_tag_name(config['WALLET']['LOCATORS']['USER_CARDS'])

        if cards[0].text == config['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

            del cards[0:1]

        return len(cards)

    @staticmethod
    def clickOnDeleteCardButton():
        GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['DELETE_CARD_BUTTON'],
                                          By.XPATH).click()

    @staticmethod
    def getDeletePopupText():
        text = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['DELETE_CARD_POPUP'],
                                          By.XPATH).text
        return text

    @staticmethod
    def clickOnDeleteYes():
        GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['DELETE_CARD_YES_BUTTON'],
                                          By.XPATH).click()

    @staticmethod
    def getDeleteYesButtonText():
        text = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['DELETE_CARD_YES_BUTTON'],
                                                 By.XPATH).text
        return text

    @staticmethod
    def clickOnDeleteNo():
        GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['DELETE_CARD_NO_BUTTON'],
                                          By.XPATH).click()

    @staticmethod
    def getDeleteNoButtonText():
        text = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['DELETE_CARD_NO_BUTTON'],
                                                 By.XPATH).text
        return text

    @staticmethod
    def getDefaultCardVmark():
        element = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['DEFAULT_CARD_V_MARK'],
                                                    By.XPATH)
        return element

    @staticmethod
    def getWeAcceptCardsText():
        we_accept_cards_text = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['ACCEPTED_CARDS_TEXT_AREA'],
                                                                 By.XPATH).text
        return we_accept_cards_text

    @staticmethod
    def getWeAcceptCardsIcons():
        GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(config['WALLET']['LOCATORS']['WALLET_ACCEPTED_CARDS_AREA'])

    @staticmethod
    def getPciFooterText():
        pci_footer_text = GenericPO.webDriver.findElementBy(config['WALLET']['LOCATORS']['PCI_FOOTER_TEXT_AREA'],
                                                            By.XPATH).text
        return pci_footer_text

    @staticmethod
    def getWalletModal():
        wallet_modal = GenericPO.webDriver.waitForVisibilityOfElem(config['WALLET']['LOCATORS']['CARDS_SECTION'])

        return wallet_modal

    @staticmethod
    def closeWallet():
        GenericPO.webDriver.waitForElemToBeClickable(config['WALLET']['LOCATORS']['WALLET_X_BUTTON'])

    @staticmethod
    def addCreditCard():

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        Wallet.enterCcNumber()

        Wallet.enterExpDate()

        Wallet.enterCvc()

        Wallet.enterPostalCode()

        Wallet.clickOnCcApplyButton()


    @staticmethod
    def addCreditCardFromCheckout():

        Wallet.clickOnAddNewCard()

        Wallet.enterCcNumber()

        Wallet.enterExpDate()

        Wallet.enterCvc()

        Wallet.enterPostalCode()

        Wallet.clickOnCcApplyButton()


class Menu(GenericPO):


    @staticmethod
    def chooseFirstCategory():
        time.sleep(1)
        GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['FIRST_CATEGORY'],
                                          By.XPATH).click()

    @staticmethod
    def chooseSecondCategory():
        GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['SECOND_CATEGORY'],
                                          By.XPATH).click()

    @staticmethod
    def checkIfCategoryChosen():
        is_chosen = False

        if GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['SECOND_CATEGORY_ACTIVE'], By.XPATH) is not None:
            is_chosen = True

        return is_chosen

    @staticmethod
    def chooseRestrictedAgeCategory():
        time.sleep(1)
        GenericPO.webDriver.findElementBy(config['MENU']['DATA']['AGE_RESTRICTED_CATEGORY'], By.XPATH).click()

    @staticmethod
    def chooseUpSaleItem():
        GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['UP_SALE_ITEM'], By.XPATH).click()

    @staticmethod
    def firstCategoryText():
        first_category_pname = GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['FIRST_CATEGORY'], By.XPATH).text
        return first_category_pname

    @staticmethod
    def chooseSecondItem():
        time.sleep(1)
        GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['SECOND_ITEM'],
                                          By.XPATH).click()


    @staticmethod
    def clickOnMenuToast(platform):
        if platform == 'mobile':
            time.sleep(1)
            GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['MENU_TOAST'],
                                              By.XPATH).click()
            time.sleep(1)

    @staticmethod
    def getSecondItemText():
        text = GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['SECOND_ITEM'],
                                                 By.XPATH).text
        return text

    @staticmethod
    def getCartSecondItemText():
        text = GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['CART_SECOND_ITEM_TEXT'],
                                                 By.XPATH).text
        return text

    @staticmethod
    def getTotalPrice():

        price = GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['CART_TOTAL'],
                                                  By.XPATH).text

        return price

    @staticmethod
    def clickOnEditItem():
        GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['EDIT_ITEM_BUTTON'],
                                          By.XPATH).click()

    @staticmethod
    def clickOnEditItemFromCart():
        GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['EDIT_ITEM_FROM_CART'],
                                          By.XPATH).click()

    @staticmethod
    def getModifiersModal():
        modifier_modal = GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['MODIFIER_MODAL'],
                                                           By.XPATH)
        return modifier_modal

    @staticmethod
    def getModifiersModalHeaderText():
        header_text = GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['MODIFIER_MODAL_HEADER'],
                                                        By.XPATH).text
        return header_text

    @staticmethod
    def closeModifiersWindow():
        time.sleep(1)
        GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['CLOSE_MODIFIER_X_BUTTON'],
                                          By.XPATH).click()

    @staticmethod
    def deleteItemFromCart():
        GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['DELETE_ITEM_FROM_CART'],
                                          By.XPATH).click()

    @staticmethod
    def getCartItemsList():
        cart_items_list = GenericPO.webDriver.findElementsBy(config['MENU']['LOCATORS']['CART_ITEMS_CONTAINER'], By.XPATH)

        return cart_items_list

    @staticmethod
    def getModifiersBySection():
        time.sleep(1)

        modifiers_list = GenericPO.webDriver.findElementsBy(config['MENU']['LOCATORS']['SECOND_CATEGORY_MODIFIERS'], By.XPATH)

        return modifiers_list

    @staticmethod
    def checkModifierActivity(element):
        is_active = False

        if element.find_element_by_xpath(By['MENU']['LOCATORS']['ACTIVE_MODIFIER']) is not None:
            is_active = True

        return is_active

    @staticmethod
    def moveToCart(platform):

        if platform == 'mobile':
            time.sleep(1)
            GenericPO.webDriver.findElementBy("//div[@id='toast-container']",
                                              By.XPATH).click()
            time.sleep(1)

            GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['MOBILE_CART_ICON'],
                                              By.XPATH).click()


    @staticmethod
    def clickOnProceedToCheckout():

                GenericPO.webDriver.findElementBy(config['MENU']['LOCATORS']['PROCEED_TO_CHECKOUT_BUTTON'],
                                                  By.XPATH).click()

    @staticmethod
    def getPopup():
        screen_popup = GenericPO.webDriver.waitForVisibilityOfElem(
            config['MENU']['LOCATORS']['SCREEN_POPUP'])

        return screen_popup

    @staticmethod
    def getPopupHeaderText():
        screen_popup_header_text = GenericPO.webDriver.waitForVisibilityOfElem(
            config['MENU']['LOCATORS']['SCREEN_POPUP_HEADER']).text

        return screen_popup_header_text

    @staticmethod
    def getPopupText():
        screen_popup_text = GenericPO.webDriver.waitForVisibilityOfElem(
            config['MENU']['LOCATORS']['SCREEN_POPUP_BODY']).text

        return screen_popup_text

    @staticmethod
    def getUpSalePopupText():
        up_sale_popup_text = GenericPO.webDriver.waitForVisibilityOfElem(
            config['MENU']['LOCATORS']['UP_SALE_POPUP_BODY']).text

        return up_sale_popup_text

    @staticmethod
    def clickOnPopupOkBtn():
        GenericPO.webDriver.findElementBy(
            config['MENU']['LOCATORS']['SCREEN_POPUP_OK'], By.XPATH).click()


class Checkout(GenericPO):


    @staticmethod
    def addPaymentFromCheckout():
        GenericPO.webDriver.findElementBy("//div[@class='add-payment-method ng-binding ng-scope']",
                                          By.XPATH)

    @staticmethod
    def clickOnSubmitOrder():
        if GenericPO.webDriver.waitForInvisibilityOfElem("//div[@class='loading']") is True:
                GenericPO.webDriver.waitForElemToBeClickable(config['CHECKOUT_SCREEN']['LOCATORS']['SUBMIT_ORDER_BUTTON'])


    @staticmethod
    def enter4DigitsCode():
        GenericPO.webDriver.findElementBy(config['CHECKOUT_SCREEN']['LOCATORS']['ENTER_PIN_INPUT'],
                                          By.XPATH).send_keys(
            config['FORM_PAGE']['DATA']['PIN'])

    @staticmethod
    def submit4digitsCode():
        GenericPO.webDriver.findElementBy(config['CHECKOUT_SCREEN']['LOCATORS']['POPUP_OK_BTN'],
                                          By.XPATH).click()
        time.sleep(2)

    @staticmethod
    def Pass4DigitsPin():
        if config['CHECKOUT_SCREEN']['DATA']['4_DIGIT_EXIST'] == 1:

            Checkout.enter4DigitsCode()

            Checkout.submit4digitsCode()

        else:
            pass

    @staticmethod
    def getErrorPopup():
        pop_up_element = GenericPO.webDriver.waitForVisibilityOfElem(config['CHECKOUT_SCREEN']['LOCATORS']['CHECKOUT_POPUP'])
        return pop_up_element

    @staticmethod
    def clickOnPopUpOkBtn():
        GenericPO.webDriver.findElementBy(config['CHECKOUT_SCREEN']['LOCATORS']['POPUP_OK_BTN'], By.XPATH).click()
        time.sleep(1)

    @staticmethod
    def getErrorPopupText():
        pop_up_text = GenericPO.webDriver.waitForVisibilityOfElem(config['CHECKOUT_SCREEN']['LOCATORS']['CHECKOUT_POPUP']).text

        return pop_up_text

    @staticmethod
    def clickOnManagePaymentMethod():
        GenericPO.webDriver.findElementBy(config['CHECKOUT_SCREEN']['LOCATORS']['MANAGE_PAYMENT_METHOD'], By.XPATH).click()



class ConfirmationScreen(GenericPO):

    @staticmethod
    def getConfirmationText():
        try:
            element = GenericPO.webDriver.findElementBy(config['CONFIRMATION_SCREEN']['LOCATORS']['CONFIRMATION_TEXT_AREA'],
                                                                 By.XPATH)

            return element.text

        except AttributeError:
            logging.error(ErrorsHandler.CONFIRMATION_MISSING)


    @staticmethod
    def clickOnDone():
        GenericPO.webDriver.findElementBy(config['CONFIRMATION_SCREEN']['LOCATORS']['DONE_BUTTON'],
                                          By.XPATH).click()
        time.sleep(4)
        # remove the sleep

    @staticmethod
    def getTotalPrice():
        price = GenericPO.webDriver.findElementBy(config['CONFIRMATION_SCREEN']['LOCATORS']['TOTAL'],
                                                  By.XPATH).text

        return price


