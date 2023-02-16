from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(autouse=True)
def testing():
   driver = webdriver.Chrome('chromedriver/chromedriver.exe')
   pytest.driver = driver
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)

    yield browser


    if request.node.rep_call.failed:

        try:
            browser.execute_script("document.body.bgColor = 'white';")


            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')


            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass

def test_petfriends(web_browser):
   # Открываем сайт петфрендс
   web_browser.get("https://petfriends.skillfactory.ru/")

   # Жмем на кнопку "зарегистрироваться"
   btn_newuser = web_browser.find_element(by=By.XPATH, value="//button[@onclick=\"document.location='/new_user';\"]")
   btn_newuser.click()

   # Клацаем на кнопку "у меня есть аккаунт"
   btn_exist_acc = web_browser.find_element(by=By.LINK_TEXT, value="У меня уже есть аккаунт")
   btn_exist_acc.click()

   # Вводим почту
   field_email = web_browser.find_element(by=By.ID, value="email")
   field_email.clear()
   field_email.send_keys("dark.second@yandex.ru")

   # Добавляем пароль
   field_pass = web_browser.find_element(by=By.ID, value="pass")
   field_pass.clear()
   field_pass.send_keys("retro125")

   # Жмем на кнопку
   WebDriverWait(pytest.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
   btn_submit = web_browser.find_element(by=By.XPATH, value="//button[@type='submit']")
   btn_submit.click()

   assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"
