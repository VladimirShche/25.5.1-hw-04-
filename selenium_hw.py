from selenium import webdriver
driver = webdriver.Chrome()

import time

def test_show_my_pets():
    # вводим почту
    pytest.driver.find_element(By.ID, "email").send_keys("dark.second@yandex.ru")
    # вводим пароль
    pytest.driver.find_element(By.ID, "pass").send_keys("retro125")
    # нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # проверяем , что мы оказались на главной странице пользователя
    # time.sleep(3)
    element = WebDriveWait(driver, 10).untill(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    # нажимаем на кнопку "Мои питомцы"
    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    #проверяем, что мы оказались на главной странице пользователя
    # assert pytest.driver.find_element(By.TAG_NAME. 'h2').text != ""