

class ErrorsHandler(object):


    # GENERAL ERRORS
    SUCCESS = 'success'
    TIMEOUT_ERROR = 'time out error'
    FEATURE_NOT_EXIST_ON_APP = "the specific feature doesn't exist on current app"
    WRONG_ENVIRONMENT = "the url doesnt belong to environment - "


    # TEXT ERRORS
    TEXT_IS_WRONG = 'text is wrong & not equals to the expected one... please check the screen shot for that test & the error msg text on the html report'


    # CONNECT ERRORS
    LOGIN_ERROR = 'there was problem with the user login'
    LOGOUT_ERROR = 'there was logout error'


    # CHOOSE LOCATION ERRORS
    TEST_LOCATION_DOES_PNOT_EXIST = "test business doesn't exist on locations list"
    LOCATION_CHOOSING_ERRORS = 'there was an error with choosing the location...please see the error msg text on the html reporting'
    START_ORDER_WITH_NO_TIMES = "manage to start order with no times"
    CAN_NOT_START_ORDER = "failed to start order with valid location - menu url not found",
    ABOVE_DATES_LIMIT = "there is to many dates on drop down for that client"
    DATE_ON_LIST_IS_WRONG = "the date you are looking for isn't exist on list or not in the right index."

    # WALLET ERRORS
    ADD_PAYMENT_ERROR = 'error while adding the credit card'
    MISSING_CARDS = ' cards are missing'
    CARD_IS_NOT_DEFAULT = 'this card doesnt contain the "V" mark or the locator on config was changed, please check the screen shot for that test'
    MISSING_SUPPORTED_CARDS = 'number of card is lower then the on expected... please check to screen shot for that issue'
    WALLET_IS_NOT_VISIBLE = "wallet doesn't open "

    # MENU ERRORS
    CART_DOES_NOT_EMPTY = "the cart item list doesn't empty"
    CART_EMPTY = "the cart item list empty"

    # CHECKOUT ERRORS

    # VALIDATION POPUPS ERRORS
    MISSING_POPUP = "popup is missing"
    WRONG_POPUP_TEXT = TEXT_IS_WRONG

    # ELEMENTS ERRORS
    NO_SUCH_ELEMENT = 'no such element... the element you was trying to reach is ether missing or the locator on config is wrong, please check the screen shot for that test'
    ELEMENT_NOT_VISIBLE = 'element is not visible... the element you was trying to assert is ether missing or the locator on config is wrong, please check the screen shot for that test'
    ELEMENT_EXIST = "the element is exist... it shouldn't not be"
    ELEMENT_IS_NONE = 'element is none... or that it not exist or the config locator is wrong'
    ELEMENT_NOT_ASSIGNED_YET = 'the element you trying to get access to is not assign to any value yet, probably locator on config is wrong, please check the screen shot for that test '

    # CHECKOUT ERRORS
    GENERAL_CHECKOUT_ERROR = 'there was an error during checkout, please see the error msg text on the html reporting'
    TOTAL_PRICE_ERROR = 'the cart total not equal to the one on confirmation'

    # HISTORY ERRORS
    WRONG_HISTORY_TOTAL = 'history payment value is wrong'

    # CONFIRMATION SCREEN
    CONFIRMATION_MISSING = 'confirmation screen is missing check the screen shot for that test please'
