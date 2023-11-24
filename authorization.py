import pytest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import Select


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://149.255.118.78:7080")

    # открываю окно браузера на максимум, чтобы было видно кнопку "Добавить"
    # в форме добавления пользователя без вручную прописанного скролла вниз
    driver.maximize_window()
    yield driver
    driver.close()


def test_auth(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.is_displayed()
    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"


def test_navigation_tab_variants(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_variants = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuMore")))

    tab_variants.click()

    variants_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert variants_title.is_displayed()
    assert variants_title.get_attribute("class") == "uk-card-title"
    assert variants_title.text == "НТЦ ПРОТЕЙ"


def test_navigation_tab_users(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()
    tab_users.click()

    users_table = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "usersPage")))

    assert users_table.is_displayed()
    assert users_table.get_attribute("class") == "uk-panel-scrollable"


def test_navigation_dropdown_users(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsers")))
    dropdown_users.click()

    users_table = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "usersPage")))

    assert users_table.is_displayed()
    assert users_table.get_attribute("class") == "uk-panel-scrollable"


def test_navigation_tab_add_user(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()
    tab_users.click()

    button_add_user = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "addUser")))

    button_add_user.click()

    user_fieldset = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "fieldset")))

    assert user_fieldset.is_displayed()
    assert user_fieldset.get_attribute("class") == "uk-fieldset"


def test_navigation_dropdown_add_user(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    user_fieldset = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "fieldset")))

    assert user_fieldset.is_displayed()
    assert user_fieldset.get_attribute("class") == "uk-fieldset"


def test_pairwase_1(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("example@mail.com")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("qwerty12345")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("Иванушка")

    select_male = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_male.select_by_index(0)

    add_user_variant_1_1 = driver.find_element(by=By.ID, value="dataSelect11")
    add_user_variant_1_1.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_success = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_success.is_displayed()
    assert add_user_success.get_attribute("class") == "uk-modal-dialog"

    # XPATH ниже работает, но плох для потенциального расширения проекта,
    # так как текст 'Ok' может встречается на многих других кнопоках
    # add_user_success_button = driver.find_element(by=By.XPATH, value="//*[text()='Ok']")

    add_user_success_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_success_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_success_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("example@mail.com")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("qwerty12345")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"


def test_pairwase_2(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("EXAmPlE@YAndEx.Ru")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("f#db96l%4~boA@")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("Екатерина 2 Великая")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_1 = driver.find_element(by=By.ID, value="dataSelect21")
    add_user_variant_2_1.click()

    add_user_variant_2_2 = driver.find_element(by=By.ID, value="dataSelect22")
    add_user_variant_2_2.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_success = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_success.is_displayed()
    assert add_user_success.get_attribute("class") == "uk-modal-dialog"

    add_user_success_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_success_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_success_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("EXAmPlE@YAndEx.Ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("f#db96l%4~boA@")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"

def test_pairwase_3(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("8888@88.com")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("надёжныйпароль")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("Владимир Владимирович Путин")

    select_male = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_male.select_by_index(0)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_1 = driver.find_element(by=By.ID, value="dataSelect21")
    add_user_variant_2_1.click()

    add_user_variant_2_3 = driver.find_element(by=By.ID, value="dataSelect23")
    add_user_variant_2_3.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_success = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_success.is_displayed()
    assert add_user_success.get_attribute("class") == "uk-modal-dialog"

    add_user_success_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_success_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_success_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("8888@88.com")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("надёжныйпароль")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"

def test_pairwase_4(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("москва@москва.рф")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("港口で難船")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("اردشیر")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_2 = driver.find_element(by=By.ID, value="dataSelect22")
    add_user_variant_2_2.click()

    add_user_variant_2_3 = driver.find_element(by=By.ID, value="dataSelect23")
    add_user_variant_2_3.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_success = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_success.is_displayed()
    assert add_user_success.get_attribute("class") == "uk-modal-dialog"

    add_user_success_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_success_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_success_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("москва@москва.рф")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("港口で難船")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"

def test_pairwase_5(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("admin@example")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("Q")

    select_male = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_male.select_by_index(0)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_1 = driver.find_element(by=By.ID, value="dataSelect21")
    add_user_variant_2_1.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_success = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_success.is_displayed()
    assert add_user_success.get_attribute("class") == "uk-modal-dialog"

    add_user_success_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_success_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_success_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("admin@example")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"

def test_pairwase_6(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("postmaster@[123.123.123.123]")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("п")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("123456789012345678901234567890")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_1 = driver.find_element(by=By.ID, value="dataSelect11")
    add_user_variant_1_1.click()

    add_user_variant_2_2 = driver.find_element(by=By.ID, value="dataSelect22")
    add_user_variant_2_2.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_success = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_success.is_displayed()
    assert add_user_success.get_attribute("class") == "uk-modal-dialog"

    add_user_success_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_success_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_success_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("postmaster@[123.123.123.123]")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("п")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"

def test_pairwase_7(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("emailaddresss@example.com")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("latineca")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("あんな")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_3 = driver.find_element(by=By.ID, value="dataSelect23")
    add_user_variant_2_3.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_success = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_success.is_displayed()
    assert add_user_success.get_attribute("class") == "uk-modal-dialog"

    add_user_success_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_success_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_success_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("emailaddresss@example.com")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("latineca")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"

def test_pairwase_8(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("ivanov322gamer1@mail.ru")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("СВЕТЛАНА")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("СВЕТЛАНА")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_1 = driver.find_element(by=By.ID, value="dataSelect11")
    add_user_variant_1_1.click()

    add_user_variant_2_1 = driver.find_element(by=By.ID, value="dataSelect21")
    add_user_variant_2_1.click()

    add_user_variant_2_2 = driver.find_element(by=By.ID, value="dataSelect22")
    add_user_variant_2_2.click()

    add_user_variant_2_3 = driver.find_element(by=By.ID, value="dataSelect23")
    add_user_variant_2_3.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_success = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_success.is_displayed()
    assert add_user_success.get_attribute("class") == "uk-modal-dialog"

    add_user_success_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_success_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_success_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("ivanov322gamer1@mail.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("СВЕТЛАНА")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"


def test_pairwase_9_negative_empty_email(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("7d F5v")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("Tom Marvolo Riddle")

    select_male = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_male.select_by_index(0)

    add_user_variant_1_1 = driver.find_element(by=By.ID, value="dataSelect11")
    add_user_variant_1_1.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_fail_alert_email = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert add_user_fail_alert_email.is_displayed()
    assert add_user_fail_alert_email.get_attribute("class") == "uk-alert uk-alert-danger"

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("7d F5v")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    auth_error = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert auth_error.get_attribute("class") == "uk-alert uk-alert-danger"

def test_pairwase_10_negative_empty_password(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("name@and.subdomains.example.com")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("Иван")

    select_male = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_male.select_by_index(0)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_1 = driver.find_element(by=By.ID, value="dataSelect21")
    add_user_variant_2_1.click()

    add_user_variant_2_2 = driver.find_element(by=By.ID, value="dataSelect22")
    add_user_variant_2_2.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_fail_alert_password = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "blankPasswordError")))

    assert add_user_fail_alert_password.is_displayed()
    assert add_user_fail_alert_password.get_attribute("class") == "uk-alert uk-alert-danger"

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("name@and.subdomains.example.com")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    auth_error = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))

    assert auth_error.get_attribute("class") == "uk-alert uk-alert-danger"


def test_pairwase_11_negative_long_password(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("e.x.a.m.p.l.e@sub_domain.example.com")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("Ра")

    select_male = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_male.select_by_index(0)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_1 = driver.find_element(by=By.ID, value="dataSelect21")
    add_user_variant_2_1.click()

    add_user_variant_2_3 = driver.find_element(by=By.ID, value="dataSelect23")
    add_user_variant_2_3.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_fail = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_fail.is_displayed()

    add_user_fail_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_fail_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_fail_button.click()


    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("e.x.a.m.p.l.e@sub_domain.example.com")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    auth_error = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))

    assert auth_error.get_attribute("class") == "uk-alert uk-alert-danger"

def test_pairwase_12_negative_invalid_email(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("elki-palki@best-server-ever.com")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("па")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("12345678901234567890123456789")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_2 = driver.find_element(by=By.ID, value="dataSelect22")
    add_user_variant_2_2.click()

    add_user_variant_2_3 = driver.find_element(by=By.ID, value="dataSelect23")
    add_user_variant_2_3.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_fail_alert_email = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert add_user_fail_alert_email.is_displayed()
    assert add_user_fail_alert_email.get_attribute("class") == "uk-alert uk-alert-danger"

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("elki-palki@best-server-ever.com")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("па")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    auth_error = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert auth_error.get_attribute("class") == "uk-alert uk-alert-danger"

def test_pairwase_13_negative_empty_name(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("e@9.is")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("QwErTy")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("")

    select_male = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_male.select_by_index(0)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_1 = driver.find_element(by=By.ID, value="dataSelect21")
    add_user_variant_2_1.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_fail_alert_name = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "blankNameError")))

    assert add_user_fail_alert_name.is_displayed()
    assert add_user_fail_alert_name.get_attribute("class") == "uk-alert uk-alert-danger"

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("e@9.is")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("QwErTy")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    auth_error = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))

    assert auth_error.get_attribute("class") == "uk-alert uk-alert-danger"

def test_pairwase_14_negative_long_email(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("long.email-addresss@example.com")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("حرف حرف میاره")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("Aрtёm")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_1 = driver.find_element(by=By.ID, value="dataSelect11")
    add_user_variant_1_1.click()

    add_user_variant_2_2 = driver.find_element(by=By.ID, value="dataSelect22")
    add_user_variant_2_2.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_fail_alert_email = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert add_user_fail_alert_email.is_displayed()
    assert add_user_fail_alert_email.get_attribute("class") == "uk-alert uk-alert-danger"

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("long.email-addresss@example.com")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("حرف حرف میاره")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    auth_error = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert auth_error.get_attribute("class") == "uk-alert uk-alert-danger"

def test_pairwase_15_negative_long_name(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("abc@example.com")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("ABCDE")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("1234567890123456789012345678901")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_2 = driver.find_element(by=By.ID, value="dataSelect12")
    add_user_variant_1_2.click()

    add_user_variant_2_3 = driver.find_element(by=By.ID, value="dataSelect23")
    add_user_variant_2_3.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_fail = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "uk-modal-dialog")))

    assert add_user_fail.is_displayed()

    add_user_fail_button = driver.find_element(by=By.XPATH, value="//div/div/div/button")
    assert add_user_fail_button.get_attribute("class") == "uk-button uk-button-primary uk-modal-close"
    add_user_fail_button.click()

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("abc@example.com")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("ABCDE")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    auth_error = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))

    assert auth_error.get_attribute("class") == "uk-alert uk-alert-danger"

def test_pairwase_16_negative_email_without_at(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("test")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    tab_users = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUsersOpener")))

    tab_users.click()

    dropdown_user_add = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuUserAdd")))
    dropdown_user_add.click()

    add_user_login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "dataEmail")))

    add_user_login.send_keys("example")

    add_user_password = driver.find_element(by=By.ID, value="dataPassword")
    add_user_password.send_keys("P@ssword")

    add_user_name = driver.find_element(by=By.ID, value="dataName")
    add_user_name.send_keys("S1mple_fan")

    select_female = Select(driver.find_element(by=By.TAG_NAME, value="select"))
    select_female.select_by_index(1)

    add_user_variant_1_1 = driver.find_element(by=By.ID, value="dataSelect11")
    add_user_variant_1_1.click()

    add_user_variant_2_1 = driver.find_element(by=By.ID, value="dataSelect21")
    add_user_variant_2_1.click()

    add_user_variant_2_2 = driver.find_element(by=By.ID, value="dataSelect22")
    add_user_variant_2_2.click()

    add_user_variant_2_3 = driver.find_element(by=By.ID, value="dataSelect23")
    add_user_variant_2_3.click()

    add_user_button = driver.find_element(by=By.ID, value="dataSend")
    add_user_button.click()

    add_user_fail_alert_email = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert add_user_fail_alert_email.is_displayed()
    assert add_user_fail_alert_email.get_attribute("class") == "uk-alert uk-alert-danger"

    tab_auth = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "menuAuth")))

    tab_auth.click()

    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("example")

    password = driver.find_element(by=By.ID, value="loginPassword")
    password.send_keys("P@ssword")

    enter = driver.find_element(by=By.ID, value="authButton")
    enter.click()

    auth_error = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert auth_error.get_attribute("class") == "uk-alert uk-alert-danger"

