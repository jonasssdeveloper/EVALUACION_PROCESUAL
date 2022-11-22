from ui.login_ui import LoginUi
from actions.display import Display
from actions.get import Get
from actions.send_keys import SendKeys
from selenium import webdriver
from actions.click import Click


class LoginPage:

    def inicio_pagina(self, driver: webdriver):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            return Display().view_element(driver, LoginUi().xpath_image_login)
        except Exception as inst:
            print("Error: To init the request", inst)

    def enter_credential(self, driver: webdriver, user, password):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            SendKeys().send_text(driver, LoginUi().input_user, user)
            SendKeys().send_text(driver, LoginUi().input_password, password)
        except Exception as inst:
            print("Error: insert credential", inst)

    def enter_login(self, driver: webdriver, user, password):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            SendKeys().send_text(driver, LoginUi().input_user, user)
            SendKeys().send_text(driver, LoginUi().input_password, password)
            Click().click_element(driver, LoginUi().button)
            Display().view_element(driver, LoginUi().xpath_error)
        except Exception as inst:
            print("Error: insert credential", inst)

    def enter_lista_reservas(self, driver: webdriver, user, password):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            SendKeys().send_text(driver, LoginUi().input_user, user)
            SendKeys().send_text(driver, LoginUi().input_password, password)
            Click().click_element(driver, LoginUi().button)
            Click().click_element(driver, LoginUi().burger_menu)
            Click().click_element(driver, LoginUi().about)
            Display().view_element(driver, LoginUi().xpath_images)
        except Exception as inst:
            print("Error: insert credential", inst)

