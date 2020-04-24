from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

DATA = {
    'username': 'username',
    'password': 'password',
}

URL = "https://sdo.g177.ru/mod/bigbluebuttonbn/view.php?id=4701"

MSG = "Добрый день!"

driver_PATH = 'chromedriver.exe'
# Используем Chrome
driver = webdriver.Chrome(driver_PATH)
# Открываем web-site
driver.get(URL)
# Ищем форму ввода логина
id_box = driver.find_element_by_name('username')
# Вводим пароль
id_box.send_keys(DATA['username'])
# Ищем форму ввода пароля
pass_box = driver.find_element_by_name('password')
# Вводим логин
pass_box.send_keys(DATA['password'])
# Ищем кнопку авторизации
login_button = driver.find_element_by_id('loginbtn')
# Авторизуемся
login_button.click()
# Ждём 2 секунды
sleep(2)
info = driver.find_element_by_id('join_button_input').get_attribute("onclick")
CONF = info.split("'")[1]

driver.get(CONF)
# Ждём 2 секунды
sleep(2)
XPath = '/html/body/div[2]/div/div/div[1]/div/div/span/button[2]'
# Ищем кнопку "Только слушать"
microphone = driver.find_element_by_xpath(XPath)
# Нажимаем на кнопку
microphone.click()
# Ждём 2 секунды
sleep(2)
# Ищем поле сообщений
message = driver.find_element_by_id('message-input')
# Пишем сообщение
message.send_keys(MSG)
# Отправляем
message.send_keys(Keys.RETURN)
