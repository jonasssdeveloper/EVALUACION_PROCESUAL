"""
Locators login page.
"""


class LoginUi:
    base_url = "https://www.reservas.com/"
    xpath_image_login = '//*[@id="root"]/div/div[2]/div[1]/div[2]'
    input_user = 'user-name'
    input_password = 'password'
    button = 'login-button'
    button2 = '//*[@id="login-button"]'
    xpath_page_init = '//*[@id="header_container"]/div[2]/span'
    burger_menu = 'react-burger-menu-btn'
    about = 'about_sidebar_link'
    xpath_images = '//*[@id="entry-3qDFahnypj1KkiORyU1Zyh"]/div/div/div/div[2]/div/picture/img'
    xpath_error = '//*[@id="login_button_container"]/div/form/div[3]/h3'
