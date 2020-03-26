from selenium import webdriver
from time import sleep

# enter creds here
EMAIL = ''
PASSWORD = ''

driver = webdriver.Firefox()
driver.get('https://vk.com')

# loginning
driver.find_element_by_id('index_email').send_keys(EMAIL)
driver.find_element_by_id('index_pass').send_keys(PASSWORD)
driver.find_element_by_id('index_login_button').click()
sleep(6)

# enter to message with friend
driver.find_element_by_id('l_fr').click()
sleep(8)
driver.find_element_by_id('friends_user_row38309949').find_element_by_class_name('friends_field_act').click()
sleep(2)

# send message
driver.find_element_by_id('mail_box_editable').send_keys('Тест')
driver.find_element_by_id('mail_box_send').click()

# exit from account
driver.find_element_by_id('top_profile_link').click()
driver.find_element_by_id('top_logout_link').click()

driver.quit()