import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class UrbanRoutes:

    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_A_TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    SUPPORTIVE_ICON_LOCATOR =(By.XPATH, '//img[@src="/static/media/kids.27f92282.svg"]')
    ACTIVE_PLAN_TITLE_LOCATOR=(By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    CLICK_PHONE_LOCATOR = (By.CLASS_NAME, 'np-button')
    ENTER_PHONE_NUMBER = (By.XPATH, '//*[@id="phone"]' )
    CLICK_NEXT_BUTTON = (By.CSS_SELECTOR,'.full')
    ENTER_PHONE_CODE = (By.XPATH, '//*[@id="code"]')
    CLICK_PHONE_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')
    CLICK_PAYMENT_METHOD = (By.CLASS_NAME, 'pp-value')
    CLICK_ADD_CARD=(By.XPATH, '//div[contains(text(), "Add card")]')
    ENTER_CARD_NUMBER=(By.XPATH, '//*[@id="number"]')
    CLICK_CARD_CODE=(By.CLASS_NAME, 'card-code-input')
    ENTER_CARD_CODE=(By.CSS_SELECTOR, 'input#code.card-input')
    CLICK_LINK_BUTTON=(By.XPATH,'//button[text()="Link"]')
    ENTER_MESSAGE_FOR_DRIVER=(By.ID, 'comment')
    CLICK_FOR_BLANKETS = (By.CSS_SELECTOR, 'span.slider.round')
    CHECK_FOR_BLANKETS = (By.CLASS_NAME, 'switch-input')
    CLICK_ICE_CREAM_PLUS=(By.CLASS_NAME, 'counter-plus')
    ICE_CREAM_COUNT=(By.CLASS_NAME, 'counter-value')
    CLICK_SMART_BUTTON=(By.CLASS_NAME, 'smart-button-wrapper')
    CAR_SEARCH_MODAL = (By.CLASS_NAME, 'order-body')

    def __init__(self, driver):
            self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
            # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
            # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from_location(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property('value')

    def get_to_location(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property('value')

    def click_call_taxi(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON).click()

    def supportive_icon_click(self):
        self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR).click()

    def get_active_plan_title(self):
        return self.driver.find_element(*self.ACTIVE_PLAN_TITLE_LOCATOR).text

    def click_phone_number(self, PHONE_LOCATOR):
        self.driver.find_element(*self.CLICK_PHONE_LOCATOR).click()

    def enter_in_phone_number(self, ENTER_PHONE_NUMBER):
        self.driver.find_element(*self.ENTER_PHONE_NUMBER).send_keys(ENTER_PHONE_NUMBER)

    def clicking_next(self):
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()

    def clicking_phone_number_confirm(self):
        self.driver.find_element(*self.CLICK_PHONE_CONFIRM_BUTTON).click()

    def entering_phone_code(self, ENTER_PHONE_CODE):
        self.driver.find_element(*self.ENTER_PHONE_CODE).send_keys(ENTER_PHONE_CODE)

    def get_phone_number(self):
        return self.driver.find_element(*self.CLICK_PHONE_LOCATOR).text

    def click_payment_method(self):
        self.driver.find_element(*self.CLICK_PAYMENT_METHOD).click()

    def get_payment_method(self):
        return self.driver.find_element(*self.CLICK_PAYMENT_METHOD).text

    def click_add_card(self):
        self.driver.find_element(*self.CLICK_ADD_CARD).click()

    def entering_card_number(self, ENTER_CARD_NUMBER):
        self.driver.find_element(*self.ENTER_CARD_NUMBER).send_keys(ENTER_CARD_NUMBER)

    def clicking_card_code(self):
        self.driver.find_element(*self.CLICK_CARD_CODE).click()

    def entering_card_code(self, ENTER_CARD_CODE):
        self.driver.find_element(*self.ENTER_CARD_CODE).send_keys(ENTER_CARD_CODE)

    def clicking_link_button(self):
        self.driver.find_element(*self.CLICK_LINK_BUTTON).click()

    def get_card_number(self):
        return self.driver.find_element(*self.ENTER_CARD_NUMBER).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.ENTER_CARD_CODE).get_property('value')

    def entering_message(self, ENTER_MESSAGE_FOR_DRIVER):
        self.driver.find_element(*self.ENTER_MESSAGE_FOR_DRIVER).send_keys(ENTER_MESSAGE_FOR_DRIVER)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.ENTER_MESSAGE_FOR_DRIVER).get_property('value')

    def click_to_add_ice_creams(self):
        self.driver.find_element(*self.CLICK_ICE_CREAM_PLUS).click()

    def check_ice_creams_count(self, ICE_CREAM_COUNT):
        return self.driver.find_element(*self.ICE_CREAM_COUNT).get_property('counter value')

    def smart_button_click(self):
        self.driver.find_element(*self.CLICK_SMART_BUTTON).click()

    def car_search_modal(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()

    def clicking_blanket_button(self):
        self.driver.find_element(*self.CLICK_FOR_BLANKETS).click()
    def get_blanket_button(self):
        return self.driver.find_element(*self.CHECK_FOR_BLANKETS).get_property('checked')









