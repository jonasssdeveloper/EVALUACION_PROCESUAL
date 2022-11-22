import unittest
from selenium import webdriver
from tasks.login_page import LoginPage



class Test_Login(unittest.TestCase):

    driver = webdriver.Chrome(executable_path="chromedriver.exe")

    __user = 'juanp@gmail.com'
    __password = '12345'

    __usuario = 'pedrito'
    __contraseña = 'perez'

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test3_pantalla(self):
        page_login = LoginPage().inicio_pagina(self.driver)
        self.assertTrue(page_login)

    def test1_insert_credential(self):
        driver = self.driver
        LoginPage().enter_credential(driver, self.__user, self.__password)

    def test2_login(self):
        driver = self.driver
        pagina_inicio_pasajero = LoginPage().enter_login(driver, self.__usuario, self.__contraseña)
        self.assertTrue(pagina_inicio_pasajero)

    def test4_lista_reservas(self):
        driver = self.driver
        pagina_pasajero = LoginPage().enter_lista_reservas(driver, self.__user, self.__password)
        self.assertTrue(pagina_pasajero)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
