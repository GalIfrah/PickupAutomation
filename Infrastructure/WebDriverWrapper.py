import logging
import time
from selenium.common.exceptions import (NoSuchElementException, TimeoutException)
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Services.ErrorService import ErrorsHandler


class Wrapper:
    global driver

    driver = None

    def openSut(self, url):
        self.driver.get(url)

    def closeCurrent(self):
        self.driver.close()

    def closeAll(self):
        self.driver.quit()

    def findElementBy(self, value, locator_type):
        element_assigned = False

        try:
            if locator_type == By.XPATH:

                element = WebDriverWait(self.driver, 20).until(
                    ec.visibility_of_element_located((By.XPATH, value)))

            elif locator_type == By.ID:

                element = WebDriverWait(self.driver, 20).until(
                    ec.visibility_of_element_located((By.ID, value)))

            if element is not None:
                element_assigned = True

        except TimeoutException as E:
            logging.error(ErrorsHandler.TIMEOUT_ERROR)

        except TimeoutError as E:
            logging.error(ErrorsHandler.TIMEOUT_ERROR)

        except NoSuchElementException as E:
            logging.error(ErrorsHandler.NO_SUCH_ELEMENT)

        except UnboundLocalError as E:
            E.with_traceback(E.__context__)

        if element_assigned is True:
            return element
        else:
            print(ErrorsHandler.ELEMENT_NOT_ASSIGNED_YET)

    def findElementsBy(self, value, locator_type):

        elemnts = self.driver.find_elements(value=value, by=locator_type)

        return elemnts

    def hoverAndClick(self, first_element_locator, second_element_locator):
        action = ActionChains(self.driver)

        action.move_to_element(self.driver.find_element_by_xpath(first_element_locator)).move_to_element(
            (self.driver.find_element_by_xpath(second_element_locator))).double_click((
                self.driver.find_element_by_xpath(second_element_locator))).perform()

    def selectFromDropDown(self, drop_down_locator, option_text):
        time.sleep(1)
        selector = Select(self.driver.find_element_by_id(drop_down_locator))
        selector.select_by_visible_text(option_text)

    def getDropDownOptionsList(self, drop_down_locator):
        selector = Select(self.driver.find_element_by_id(drop_down_locator))

        return selector.options

    def waitForElemToBeClickable(self, element_locator):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, element_locator))).click()

        except TimeoutException:
            print(ErrorsHandler.TIMEOUT_ERROR + " " + ErrorsHandler.ELEMENT_NOT_VISIBLE)

    def waitForInvisibilityOfElem(self, element_locator):
        is_visible = WebDriverWait(self.driver, 5).until(
            ec.invisibility_of_element_located((By.XPATH, element_locator)))

        return is_visible

    def waitForVisibilityOfElem(self, element_locator):
        try:
            element = WebDriverWait(self.driver, 7).until(
                ec.visibility_of_element_located((By.XPATH, element_locator)))

            return element

        except TimeoutException:
            print(ErrorsHandler.TIMEOUT_ERROR + " " + ErrorsHandler.ELEMENT_NOT_VISIBLE)

    def switchToIframe(self, element):
        self.driver.switch_to.frame(element)

    def switchToWindow(self, window_number):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def getCurrentUrl(self):
        current_url = self.driver.current_url

        return current_url

    def executeScript(self, script_to_execute):
        self.driver.execute_script(script_to_execute)

    def refreshPage(self):
        self.driver.refresh()

    def saveScreenShot(self, i, test_name):
        time.sleep(1)

        if i == 0:

            filename = test_name + '_screenShot.png'

            self.driver.save_screenshot(

                'Wallet/ScreenShots' + filename)

        elif i != 0:

            filename = test_name + '_screenShot' + str(i) + '.png'

            self.remoteWebDriver.save_screenshot(

                'Wallet/ScreenShots' + filename)

        return test_name

    def back(self):
        self.driver.back()
