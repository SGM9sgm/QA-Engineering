import selenium

import data
import helpers
from helpers import is_url_reachable
from helpers import retrieve_phone_code
from selenium import webdriver
from pages import UrbanRoutes
import time
from selenium.webdriver.common.keys import Keys

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Not connected to the Urban Routes server")




    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutes(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        assert data.ADDRESS_FROM == page.get_from_location()
        assert data.ADDRESS_TO == page.get_to_location()


    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page=UrbanRoutes(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi()
        time.sleep(1)
        page.supportive_icon_click()
        time.sleep(1)
        assert page.get_active_plan_title() == "Supportive"


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutes(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi()
        time.sleep(1)
        page.supportive_icon_click()
        time.sleep(1)
        page.click_phone_number(data.PHONE_NUMBER)
        time.sleep(1)
        page.enter_in_phone_number(data.PHONE_NUMBER)
        time.sleep(1)
        page.clicking_next()
        time.sleep(1)
        code=helpers.retrieve_phone_code(self.driver)
        page.entering_phone_code(code)
        time.sleep(2)
        page.clicking_phone_number_confirm()
        time.sleep(2)
        assert data.PHONE_NUMBER == page.get_phone_number()

    def test_fill_card_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutes(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi()
        time.sleep(1)
        page.supportive_icon_click()
        time.sleep(1)
        page.click_payment_method()
        time.sleep(1)
        page.click_add_card()
        time.sleep(1)
        page.entering_card_number(data.CARD_NUMBER)
        time.sleep(1)
        page.clicking_card_code()
        time.sleep(1)
        page.entering_card_code(data.CARD_CODE)
        time.sleep(1)
        page.clicking_link_button()
        time.sleep(1)
        assert data.CARD_NUMBER == page.get_card_number()
        assert data.CARD_CODE == page.get_card_code()
        assert "Card" == page.get_payment_method()

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutes(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi()
        time.sleep(1)
        page.supportive_icon_click()
        time.sleep(1)
        page.entering_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)
        assert data.MESSAGE_FOR_DRIVER == page.get_message_for_driver()


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutes(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi()
        time.sleep(1)
        page.supportive_icon_click()
        time.sleep(1)
        page.clicking_blanket_button()
        time.sleep(1)
        assert page.get_blanket_button()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutes(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi()
        time.sleep(1)
        page.supportive_icon_click()
        time.sleep(1)
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            page.click_to_add_ice_creams()
        assert number_of_ice_creams == 2



    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutes(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        time.sleep(1)
        page.click_call_taxi()
        time.sleep(1)
        page.supportive_icon_click()
        time.sleep(1)
        page.entering_message(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)
        page.smart_button_click()
        time.sleep(1)
        assert page.car_search_modal()





    @classmethod
    def teardown_class(cls):
        cls.driver.quit()